"""
Queue Prediction & Wait-Time Estimation Heuristic Algorithm
SIH 2026 Innovation Component
"""

import math
from backend.app.config import MSP_RATES, VEHICLE_FACTORS
from backend.app.database import fetch_all, fetch_one

def calculate_token_wait_time(center_id: str, vehicle_type: str, crop_name: str, queue_pos: int) -> int:
    """
    Intelligent Queue Estimation Algorithm:
    Factors vehicle unloading capacity, crop inspection parameters,
    active electronic weighbridges, and lab throughput.
    """
    center = fetch_one("SELECT * FROM centers WHERE id = ?", (center_id,))
    if not center:
        return max(5, queue_pos * 15)

    weighbridges = max(1, center.get("active_weighbridges", 2))
    quality_labs = max(1, center.get("active_quality_labs", 2))

    crop_cfg = MSP_RATES.get(crop_name, {
        "avg_weigh_time_mins": 6,
        "avg_quality_check_mins": 8
    })
    vehicle_cfg = VEHICLE_FACTORS.get(vehicle_type, {
        "factor": 1.0,
        "base_mins": 15
    })

    t_weigh_per_vehicle = crop_cfg["avg_weigh_time_mins"] * vehicle_cfg["factor"]
    t_quality_per_sample = crop_cfg["avg_quality_check_mins"]

    effective_weighbridge_time = t_weigh_per_vehicle / weighbridges
    effective_lab_time = t_quality_per_sample / quality_labs

    bottleneck_time_per_token = max(effective_weighbridge_time, effective_lab_time) + 3.0  # 3 min buffer for movement

    # Total wait time for queue position ahead
    estimated_mins = int(math.ceil(queue_pos * bottleneck_time_per_token))
    return max(5, estimated_mins)

def get_center_live_metrics(center_id: str) -> dict:
    center = fetch_one("SELECT * FROM centers WHERE id = ?", (center_id,))
    if not center:
        return {}

    # Query active tokens in pipeline (excluding completed PAYMENT_PROCESSED)
    active_tokens = fetch_all("""
        SELECT stage, crop_name, vehicle_type, estimated_quantity_qtl 
        FROM tokens 
        WHERE center_id = ? AND stage != 'PAYMENT_PROCESSED'
        ORDER BY queue_number ASC
    """, (center_id,))

    stage_counts = {
        "REGISTERED": 0,
        "GATE_ENTRY": 0,
        "WEIGHBRIDGE": 0,
        "QUALITY_CHECK": 0,
        "TOTAL_IN_QUEUE": len(active_tokens)
    }

    total_procured_today = fetch_one("""
        SELECT COALESCE(SUM(net_weight_qtl), 0) as total_qtl,
               COALESCE(SUM(total_amount_inr), 0) as total_payout,
               COUNT(*) as completed_count
        FROM tokens
        WHERE center_id = ? AND stage = 'PAYMENT_PROCESSED'
    """, (center_id,))

    for t in active_tokens:
        s = t.get("stage", "REGISTERED")
        if s in stage_counts:
            stage_counts[s] += 1

    in_mandi_count = stage_counts["GATE_ENTRY"] + stage_counts["WEIGHBRIDGE"] + stage_counts["QUALITY_CHECK"]
    
    # Calculate average wait time for a newly arriving farmer
    weighbridges = center.get("active_weighbridges", 2)
    labs = center.get("active_quality_labs", 2)
    avg_mins_wait = int(math.ceil(in_mandi_count * (12.0 / max(1, weighbridges))))

    # Determine dynamic congestion label
    if in_mandi_count == 0:
        congestion = "Smooth"
    elif in_mandi_count <= 3:
        congestion = "Light"
    elif in_mandi_count <= 7:
        congestion = "Moderate"
    else:
        congestion = "Busy"

    return {
        "center_id": center_id,
        "center_name": center["name"],
        "district": center["district"],
        "state": center["state"],
        "location": center["location"],
        "mandi_type": center.get("mandi_type", "GOVERNMENT_APMC"),
        "operator_name": center.get("operator_name", "APMC Mandi Board"),
        "distance_km": center.get("distance_km", 5.0),
        "wheat_price_qtl": center.get("wheat_price_qtl", 2425),
        "mustard_price_qtl": center.get("mustard_price_qtl", 5950),
        "paddy_price_qtl": center.get("paddy_price_qtl", 2320),
        "soybean_price_qtl": center.get("soybean_price_qtl", 4892),
        "payment_speed": center.get("payment_speed", "Direct DBT Bank Transfer"),
        "rating": center.get("rating", 4.7),
        "facilities": center.get("facilities", "Certified Electronic Weighbridge"),
        "active_weighbridges": weighbridges,
        "active_quality_labs": labs,
        "daily_capacity_quintals": center["daily_capacity_quintals"],
        "stage_counts": stage_counts,
        "in_mandi_count": in_mandi_count,
        "avg_wait_mins": avg_mins_wait,
        "congestion_status": congestion,
        "total_procured_today_qtl": round(total_procured_today["total_qtl"], 2),
        "total_payout_today_inr": round(total_procured_today["total_payout"], 2),
        "completed_count_today": total_procured_today["completed_count"],
    }

def calculate_distance_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Haversine formula for distance between coordinates"""
    R = 6371.0
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(R * c, 1)

def get_multi_center_comparison(farmer_lat: float = 29.6857, farmer_lon: float = 76.9905) -> list:
    centers = fetch_all("SELECT * FROM centers WHERE is_active = 1")
    comparison = []

    for c in centers:
        metrics = get_center_live_metrics(c["id"])
        
        # Calculate distance
        c_lat = c.get("latitude") or 29.6857
        c_lon = c.get("longitude") or 76.9905
        dist_km = calculate_distance_km(farmer_lat, farmer_lon, c_lat, c_lon)
        
        # Est travel time by tractor (~30 km/h)
        travel_time_mins = int(math.ceil((dist_km / 30.0) * 60))
        total_time_investment_mins = travel_time_mins + metrics["avg_wait_mins"]

        comparison.append({
            **metrics,
            "latitude": c_lat,
            "longitude": c_lon,
            "distance_km": dist_km,
            "travel_time_mins": travel_time_mins,
            "total_time_investment_mins": total_time_investment_mins,
            "recommended": False
        })

    # Find the optimal center (minimal total time investment)
    if comparison:
        comparison.sort(key=lambda x: x["total_time_investment_mins"])
        comparison[0]["recommended"] = True

    return comparison
