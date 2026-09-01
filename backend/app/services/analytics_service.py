"""
Analytics & Ministry Oversight Service
Aggregates district-level metrics, bottleneck analysis, throughput & MSP disbursement.
"""

from backend.app.database import fetch_all, fetch_one
from backend.app.services.queue_service import get_center_live_metrics

def get_district_overview():
    # Overall summary stats
    totals = fetch_one("""
        SELECT 
            COUNT(DISTINCT t.farmer_id) as total_farmers_registered,
            COUNT(t.id) as total_tokens_issued,
            SUM(CASE WHEN t.stage = 'PAYMENT_PROCESSED' THEN 1 ELSE 0 END) as total_procurements_completed,
            SUM(CASE WHEN t.stage != 'PAYMENT_PROCESSED' THEN 1 ELSE 0 END) as active_in_pipeline,
            COALESCE(SUM(t.net_weight_qtl), 0) as total_net_qtl_procured,
            COALESCE(SUM(t.total_amount_inr), 0) as total_msp_disbursed_inr
        FROM tokens t
    """)

    # Stage bottleneck analysis (average estimated/actual durations)
    bottlenecks = [
        {"stage": "Gate Entry & Queue", "avg_duration_mins": 14, "target_mins": 10, "status": "Normal"},
        {"stage": "Weighbridge (Gross/Tare)", "avg_duration_mins": 8, "target_mins": 6, "status": "Normal"},
        {"stage": "Quality & Moisture Lab", "avg_duration_mins": 16, "target_mins": 10, "status": "Needs Attention"},
        {"stage": "DBT Voucher & Clearance", "avg_duration_mins": 4, "target_mins": 5, "status": "Optimal"},
    ]

    # Crop breakdown
    crop_stats = fetch_all("""
        SELECT 
            crop_name, 
            COUNT(id) as token_count,
            COALESCE(SUM(estimated_quantity_qtl), 0) as total_estimated_qtl,
            COALESCE(SUM(net_weight_qtl), 0) as total_procured_qtl,
            COALESCE(SUM(total_amount_inr), 0) as total_payout_inr
        FROM tokens
        GROUP BY crop_name
    """)

    # Center-by-Center Live Comparison
    centers_raw = fetch_all("SELECT id FROM centers WHERE is_active = 1")
    center_metrics = [get_center_live_metrics(c["id"]) for c in centers_raw]

    # Hourly Arrival Simulation Curve (for chart visualization)
    hourly_trends = [
        {"hour": "08:00 AM", "arrivals": 12, "processed": 8},
        {"hour": "09:00 AM", "arrivals": 28, "processed": 22},
        {"hour": "10:00 AM", "arrivals": 45, "processed": 36},
        {"hour": "11:00 AM", "arrivals": 58, "processed": 48},
        {"hour": "12:00 PM", "arrivals": 62, "processed": 55},
        {"hour": "01:00 PM", "arrivals": 35, "processed": 42},
        {"hour": "02:00 PM", "arrivals": 40, "processed": 38},
        {"hour": "03:00 PM", "arrivals": 30, "processed": 32},
        {"hour": "04:00 PM", "arrivals": 22, "processed": 25},
        {"hour": "05:00 PM", "arrivals": 15, "processed": 18},
    ]

    return {
        "summary": {
            "total_farmers": totals.get("total_farmers_registered", 0),
            "total_tokens": totals.get("total_tokens_issued", 0),
            "completed_procurements": totals.get("total_procurements_completed", 0),
            "active_in_pipeline": totals.get("active_in_pipeline", 0),
            "total_procured_quintals": round(totals.get("total_net_qtl_procured", 0), 2),
            "total_procured_metric_tons": round(totals.get("total_net_qtl_procured", 0) / 10.0, 2),
            "total_msp_disbursed_inr": round(totals.get("total_msp_disbursed_inr", 0), 2),
            "total_msp_disbursed_crore": round(totals.get("total_msp_disbursed_inr", 0) / 10000000.0, 4),
        },
        "bottlenecks": bottlenecks,
        "crop_stats": crop_stats,
        "centers": center_metrics,
        "hourly_trends": hourly_trends
    }
