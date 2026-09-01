"""
Farmer Earnings & Sales Passbook Router for AnnaSetu
Tracks lifetime income, crop-wise revenue, APMC vs Private Mandi sales, and digital invoice vouchers.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from backend.app.database import fetch_all, fetch_one
from backend.app.config import MSP_RATES

router = APIRouter(prefix="/api/farmers/earnings", tags=["Farmer Earnings & Sales"])

@router.get("")
async def get_farmer_earnings(phone: Optional[str] = None):
    """
    Returns comprehensive lifetime earnings, crop-wise revenue, and transaction passbook.
    """
    # Fetch all tokens that have payments or active transactions
    if phone:
        farmer = fetch_one("SELECT * FROM farmers WHERE phone = ?", (phone,))
        farmer_id = farmer["id"] if farmer else None
        if farmer_id:
            tokens = fetch_all("""
                SELECT t.*, f.name AS farmer_name, f.phone AS farmer_phone, f.village, f.district AS farmer_district,
                       f.bank_name, f.bank_acc_mask, f.ifsc_code,
                       c.name AS center_name, c.district AS center_district, c.mandi_type, c.operator_name, c.distance_km
                FROM tokens t
                JOIN farmers f ON t.farmer_id = f.id
                JOIN centers c ON t.center_id = c.id
                WHERE t.farmer_id = ?
                ORDER BY t.booking_time DESC
            """, (farmer_id,))
        else:
            tokens = []
    else:
        # Default global/demo farmer transactions
        tokens = fetch_all("""
            SELECT t.*, f.name AS farmer_name, f.phone AS farmer_phone, f.village, f.district AS farmer_district,
                   f.bank_name, f.bank_acc_mask, f.ifsc_code,
                   c.name AS center_name, c.district AS center_district, c.mandi_type, c.operator_name, c.distance_km
            FROM tokens t
            JOIN farmers f ON t.farmer_id = f.id
            JOIN centers c ON t.center_id = c.id
            ORDER BY t.booking_time DESC
        """)

    # Compute Statistics
    completed_tokens = [t for t in tokens if t["stage"] == "PAYMENT_PROCESSED" and t.get("total_amount_inr")]
    active_tokens = [t for t in tokens if t["stage"] != "PAYMENT_PROCESSED"]

    total_earnings = sum(t["total_amount_inr"] for t in completed_tokens)
    total_qty_sold = sum(t.get("net_weight_qtl") or t.get("estimated_quantity_qtl") or 0.0 for t in completed_tokens)
    
    # Crop breakdown
    crop_stats = {}
    for t in completed_tokens:
        crop = t.get("crop_name", "Other")
        amt = t.get("total_amount_inr") or 0.0
        qty = t.get("net_weight_qtl") or t.get("estimated_quantity_qtl") or 0.0
        if crop not in crop_stats:
            crop_stats[crop] = {"crop_name": crop, "total_amount": 0.0, "total_quantity": 0.0, "count": 0}
        crop_stats[crop]["total_amount"] += amt
        crop_stats[crop]["total_quantity"] += qty
        crop_stats[crop]["count"] += 1

    # Mandi type breakdown (Govt APMC vs Private Mandi)
    govt_earnings = sum(t["total_amount_inr"] for t in completed_tokens if t.get("mandi_type") == "GOVERNMENT_APMC")
    pvt_earnings = sum(t["total_amount_inr"] for t in completed_tokens if t.get("mandi_type") == "PRIVATE_CORPORATE")
    
    # Calculate bonus earned over base MSP
    bonus_earned_over_msp = 0.0
    for t in completed_tokens:
        crop_info = MSP_RATES.get(t["crop_name"])
        base_msp = crop_info["msp_per_quintal"] if crop_info else 2425
        applied_rate = t.get("msp_rate_applied") or base_msp
        qty = t.get("net_weight_qtl") or t.get("estimated_quantity_qtl") or 0.0
        if applied_rate > base_msp:
            bonus_earned_over_msp += (applied_rate - base_msp) * qty

    avg_price_per_qtl = round(total_earnings / total_qty_sold, 2) if total_qty_sold > 0 else 2425.0

    return {
        "success": True,
        "farmer_name": tokens[0]["farmer_name"] if tokens else "Harishchandra Verma",
        "farmer_phone": tokens[0]["farmer_phone"] if tokens else "9876501234",
        "lifetime_earnings_inr": total_earnings,
        "total_quantity_sold_qtl": round(total_qty_sold, 1),
        "total_sales_count": len(completed_tokens),
        "active_deliveries_count": len(active_tokens),
        "avg_price_per_qtl": avg_price_per_qtl,
        "bonus_earned_over_msp": bonus_earned_over_msp,
        "govt_apmc_earnings": govt_earnings,
        "private_mandi_earnings": pvt_earnings,
        "crop_breakdown": list(crop_stats.values()),
        "transactions": tokens
    }
