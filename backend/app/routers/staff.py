"""
Mandi Staff Operator Router: Queue Management, Stage Transitions & Quality Logs
"""

import random
from datetime import datetime
from fastapi import APIRouter, HTTPException
from backend.app.config import MSP_RATES
from backend.app.database import get_db, fetch_all, fetch_one, execute_write
from backend.app.models import StageAdvanceRequest, CenterCapacityUpdateRequest
from backend.app.services.notification_service import send_stage_notification
from backend.app.websocket_manager import ws_manager
from backend.app.routers.farmers import get_token_details

router = APIRouter(prefix="/api/staff", tags=["Staff Operator"])

@router.get("/queue/{center_id}")
def get_center_queue(center_id: str):
    center = fetch_one("SELECT * FROM centers WHERE id = ?", (center_id,))
    if not center:
        raise HTTPException(status_code=404, detail="Procurement center not found.")

    all_tokens = fetch_all("""
        SELECT t.*, f.name as farmer_name, f.phone as farmer_phone, f.village, f.district as farmer_district
        FROM tokens t
        JOIN farmers f ON t.farmer_id = f.id
        WHERE t.center_id = ?
        ORDER BY t.queue_number ASC, t.booking_time ASC
    """, (center_id,))

    # Group tokens by stage
    stages_map = {
        "REGISTERED": [],
        "GATE_ENTRY": [],
        "WEIGHBRIDGE": [],
        "QUALITY_CHECK": [],
        "PAYMENT_PROCESSED": []
    }

    for t in all_tokens:
        s = t.get("stage", "REGISTERED")
        if s in stages_map:
            stages_map[s].append(t)

    return {
        "center": center,
        "queues": stages_map,
        "counts": {k: len(v) for k, v in stages_map.items()},
        "total_active": len(stages_map["REGISTERED"]) + len(stages_map["GATE_ENTRY"]) + len(stages_map["WEIGHBRIDGE"]) + len(stages_map["QUALITY_CHECK"])
    }

@router.post("/token/{token_id}/advance")
async def advance_token_stage(token_id: str, req: StageAdvanceRequest):
    token = fetch_one("""
        SELECT t.*, f.name as farmer_name, f.phone as farmer_phone, c.state as center_state
        FROM tokens t
        JOIN farmers f ON t.farmer_id = f.id
        JOIN centers c ON t.center_id = c.id
        WHERE t.id = ?
    """, (token_id,))

    if not token:
        raise HTTPException(status_code=404, detail=f"Token {token_id} not found.")

    from_stage = token["stage"]
    to_stage = req.to_stage.upper()
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = get_db()
    cursor = conn.cursor()

    # Track fields to update
    updates = ["stage = ?", "notes = ?"]
    params = [to_stage, req.notes or token["notes"]]

    # Stage specific timestamp and measurements
    if to_stage == "GATE_ENTRY":
        updates.append("stage_2_time = ?")
        params.append(now_str)

    elif to_stage == "WEIGHBRIDGE":
        updates.append("stage_3_time = ?")
        params.append(now_str)
        if req.gross_weight_kg is not None:
            updates.append("gross_weight_kg = ?")
            params.append(req.gross_weight_kg)

    elif to_stage == "QUALITY_CHECK":
        updates.append("stage_4_time = ?")
        params.append(now_str)
        if req.moisture_percent is not None:
            updates.append("moisture_percent = ?")
            params.append(req.moisture_percent)
        if req.foreign_matter_percent is not None:
            updates.append("foreign_matter_percent = ?")
            params.append(req.foreign_matter_percent)
        if req.quality_grade is not None:
            updates.append("quality_grade = ?")
            params.append(req.quality_grade)

    elif to_stage == "PAYMENT_PROCESSED":
        updates.append("stage_5_time = ?")
        params.append(now_str)
        updates.append("estimated_wait_mins = 0")

        gross = req.gross_weight_kg or token["gross_weight_kg"] or (token["estimated_quantity_qtl"] * 100 + 2500)
        tare = req.tare_weight_kg or token["tare_weight_kg"] or 2500.0  # Approx vehicle tare weight in kg
        net_kg = max(100.0, gross - tare)
        net_qtl = round(net_kg / 100.0, 2)

        msp_rate = token["msp_rate_applied"] or 2425.0
        total_payout = round(net_qtl * msp_rate, 2)
        dbt_ref = f"DBT-2026-{token['crop_code']}-{random.randint(1000000, 9999999)}"

        updates.extend([
            "gross_weight_kg = ?",
            "tare_weight_kg = ?",
            "net_weight_qtl = ?",
            "total_amount_inr = ?",
            "dbt_reference_no = ?"
        ])
        params.extend([gross, tare, net_qtl, total_payout, dbt_ref])

    params.append(token_id)
    query_str = f"UPDATE tokens SET {', '.join(updates)} WHERE id = ?"
    cursor.execute(query_str, params)

    # Insert audit trail log
    cursor.execute("""
        INSERT INTO stage_logs (token_id, from_stage, to_stage, operator_name, remarks, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (token_id, from_stage, to_stage, req.operator_name or 'Mandi Operator', req.notes or f'Transitioned to {to_stage}', now_str))

    conn.commit()
    conn.close()

    # Re-fetch rich updated token
    updated_token = await get_token_details(token_id)

    # Trigger SMS notification
    notif_details = {
        "gross_weight_kg": updated_token.get("gross_weight_kg"),
        "moisture_percent": updated_token.get("moisture_percent"),
        "quality_grade": updated_token.get("quality_grade"),
        "total_amount_inr": updated_token.get("total_amount_inr"),
        "dbt_reference_no": updated_token.get("dbt_reference_no"),
    }
    send_stage_notification(token_id, token["farmer_phone"], token["farmer_name"], to_stage, notif_details)

    # Real-time WebSocket broadcast to all connected farmer trackers & staff dashboards
    await ws_manager.broadcast_token_update(token_id, updated_token)

    return {
        "success": True,
        "message": f"Token {token_id} advanced from {from_stage} to {to_stage}",
        "token": updated_token
    }

@router.post("/center/{center_id}/capacity")
async def update_center_capacity(center_id: str, req: CenterCapacityUpdateRequest):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE centers 
        SET active_weighbridges = ?, active_quality_labs = ?, congestion_status = ?, is_active = ?
        WHERE id = ?
    """, (req.active_weighbridges, req.active_quality_labs, req.congestion_status, 1 if req.is_active else 0, center_id))
    conn.commit()
    conn.close()

    updated_center = fetch_one("SELECT * FROM centers WHERE id = ?", (center_id,))
    await ws_manager.broadcast_center_update(center_id, updated_center)

    return {"success": True, "center": updated_center}
