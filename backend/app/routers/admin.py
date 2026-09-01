"""
Admin Router: District & Ministry Level Analytics, Reports & Simulation
"""

import random
from datetime import datetime
from fastapi import APIRouter
from backend.app.services.analytics_service import get_district_overview
from backend.app.services.notification_service import get_recent_notifications
from backend.app.database import get_db, fetch_all, execute_write
from backend.app.websocket_manager import ws_manager

router = APIRouter(prefix="/api/admin", tags=["Admin & Ministry"])

@router.get("/overview")
def get_analytics_overview():
    return get_district_overview()

@router.get("/notifications")
def get_audit_notifications():
    return {"notifications": get_recent_notifications(20)}

@router.post("/simulate")
async def trigger_simulation_action(action: str = "advance_sample"):
    """
    Hackathon Demo Trigger:
    Simulates rapid mandi operations (advances a waiting token or adds a live arrival)
    so judges can see the live real-time WebSocket sync in action.
    """
    conn = get_db()
    cursor = conn.cursor()

    if action == "advance_sample":
        # Find a token in REGISTERED or GATE_ENTRY and advance it
        token = conn.execute("""
            SELECT * FROM tokens 
            WHERE stage IN ('REGISTERED', 'GATE_ENTRY', 'WEIGHBRIDGE', 'QUALITY_CHECK')
            ORDER BY RANDOM() LIMIT 1
        """).fetchone()

        if token:
            t = dict(token)
            next_stages = {
                "REGISTERED": "GATE_ENTRY",
                "GATE_ENTRY": "WEIGHBRIDGE",
                "WEIGHBRIDGE": "QUALITY_CHECK",
                "QUALITY_CHECK": "PAYMENT_PROCESSED"
            }
            nxt = next_stages.get(t["stage"], "PAYMENT_PROCESSED")
            
            # Quick advance
            from backend.app.routers.staff import advance_token_stage
            from backend.app.models import StageAdvanceRequest
            req = StageAdvanceRequest(
                to_stage=nxt,
                operator_name="Auto-Simulation Bot",
                notes="Simulated step advancement for SIH Judge Demo"
            )
            res = await advance_token_stage(t["id"], req)
            return {"action": action, "result": res}

    elif action == "add_arrival":
        # Simulate an incoming farmer booking
        crops = ["Wheat (गेहूं)", "Mustard / Rapeseed (सरसों)", "Paddy Common (धान सामान्य)", "Gram / Chana (चना)"]
        farmers = [("Baldev Singh", "9814552233", "Pehowa"), ("Devendra Sharma", "9826011223", "Mhow"), ("Gopal Rao", "9949012345", "Bodhan")]
        c_choice = random.choice(farmers)
        crop_choice = random.choice(crops)
        
        from backend.app.routers.farmers import book_procurement_slot
        from backend.app.models import FarmerBookingRequest
        req = FarmerBookingRequest(
            farmer_name=f"{c_choice[0]} (Demo)",
            phone=c_choice[1],
            village=c_choice[2],
            district="Karnal",
            crop_name=crop_choice,
            estimated_quantity_qtl=round(random.uniform(20.0, 60.0), 1),
            center_id="CTR-001"
        )
        res = await book_procurement_slot(req)
        return {"action": action, "result": res}

    return {"action": action, "status": "No action executed"}
