"""
Free Kisan AI Mandi Price & Profit Advisor Router for AnnaSetu
Uses heuristics & market spot pricing to calculate net in-hand profits, fuel costs, and optimal mandi recommendations.
"""

import math
from typing import Optional
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, Query
from backend.app.database import fetch_all
from backend.app.services.queue_service import get_center_live_metrics
from backend.app.config import MSP_RATES, VEHICLE_FACTORS

router = APIRouter(prefix="/api/ai", tags=["Kisan AI Advisor"])

class AIRecommendationRequest(BaseModel):
    crop_name: str = "Wheat (गेहूं)"
    quantity_qtl: float = 50.0
    village: Optional[str] = "Nilokheri"
    district: Optional[str] = "Karnal"
    vehicle_type: Optional[str] = "Tractor Trolley (ट्रैक्टर ट्रॉली)"

class AIQueryRequest(BaseModel):
    query: str
    language: Optional[str] = "hi"

@router.post("/recommend-mandi")
async def get_ai_mandi_recommendation(req: AIRecommendationRequest):
    """
    AI Algorithm that evaluates all Government APMC and Private Mandis,
    calculates diesel transport cost, queue wait time, and net in-hand profit.
    """
    crop = req.crop_name
    qty = max(1.0, req.quantity_qtl)
    v_type = req.vehicle_type or "Tractor Trolley (ट्रैक्टर ट्रॉली)"

    # Fuel cost rate per km based on vehicle
    fuel_rates = {
        "Tractor Trolley (ट्रैक्टर ट्रॉली)": 14.0,  # ₹14/km diesel
        "Large Tractor (बड़ा ट्रैक्टर - 2 ट्रॉली)": 20.0,
        "Mini Truck / Pickup (छोटा हाथी / पिकअप)": 9.5,
        "Commercial Truck (बड़ा ट्रक)": 24.0,
        "Bullock Cart / Jugad (बैलगाड़ी / जुगाड़)": 2.0,
    }
    fuel_cost_per_km = fuel_rates.get(v_type, 14.0)

    centers = fetch_all("SELECT * FROM centers WHERE is_active = 1")
    crop_info = MSP_RATES.get(crop, MSP_RATES.get("Wheat (गेहूं)"))
    base_msp = crop_info["msp_per_quintal"] if crop_info else 2425

    ranked_mandis = []

    for c in centers:
        metrics = get_center_live_metrics(c["id"])
        
        # Spot buying price
        if "Mustard" in crop or "सरसों" in crop:
            price_qtl = c.get("mustard_price_qtl") or 5950
        elif "Paddy" in crop or "धान" in crop:
            price_qtl = c.get("paddy_price_qtl") or 2320
        elif "Soybean" in crop or "सोयाबीन" in crop:
            price_qtl = c.get("soybean_price_qtl") or 4892
        else:
            price_qtl = c.get("wheat_price_qtl") or 2425

        dist_km = c.get("distance_km") or 5.0
        travel_time_mins = int(math.ceil((dist_km / 30.0) * 60))
        
        # Round trip transport cost
        transport_cost = round(dist_km * 2.0 * fuel_cost_per_km, 2)
        
        gross_payout = round(price_qtl * qty, 2)
        base_msp_gross = round(base_msp * qty, 2)
        
        # Net In-Hand Take-Home Profit (Gross - Fuel)
        net_in_hand_profit = round(gross_payout - transport_cost, 2)
        base_apmc_net = round(base_msp_gross - (4.5 * 2.0 * fuel_cost_per_km), 2)
        net_advantage_over_apmc = round(net_in_hand_profit - base_apmc_net, 2)

        is_pvt = c.get("mandi_type") == "PRIVATE_CORPORATE"

        # AI Composite Score: 70% Net Profit, 20% Distance/Wait time, 10% Rating
        profit_score = net_in_hand_profit / 1000.0
        convenience_score = max(0, 50 - dist_km - metrics["avg_wait_mins"])
        rating_score = (c.get("rating") or 4.5) * 10.0
        ai_score = round(profit_score * 0.7 + convenience_score * 0.2 + rating_score * 0.1, 2)

        ranked_mandis.append({
            "center_id": c["id"],
            "center_name": c["name"],
            "operator_name": c.get("operator_name", "Mandi Board"),
            "mandi_type": c.get("mandi_type", "GOVERNMENT_APMC"),
            "location": c["location"],
            "district": c["district"],
            "distance_km": dist_km,
            "travel_time_mins": travel_time_mins,
            "avg_wait_mins": metrics["avg_wait_mins"],
            "congestion_status": metrics["congestion_status"],
            "buying_price_per_qtl": price_qtl,
            "price_delta_per_qtl": round(price_qtl - base_msp, 2),
            "gross_payout_inr": gross_payout,
            "transport_fuel_cost_inr": transport_cost,
            "net_in_hand_profit_inr": net_in_hand_profit,
            "net_advantage_over_apmc_inr": net_advantage_over_apmc,
            "payment_speed": c.get("payment_speed", "Direct Bank Transfer"),
            "rating": c.get("rating", 4.7),
            "facilities": c.get("facilities", "Standard Scales"),
            "ai_score": ai_score
        })

    # Sort by Net In-Hand Profit
    ranked_mandis.sort(key=lambda x: x["net_in_hand_profit_inr"], reverse=True)

    top_pick = ranked_mandis[0]
    runner_up = ranked_mandis[1] if len(ranked_mandis) > 1 else None

    # Generate Natural Language AI Guidance in Hindi & English
    hindi_speech = (
        f"किसान भाई, आपकी {qty} क्विंटल {crop} के लिए एआई की सबसे बेहतरीन सिफारिश {top_pick['center_name']} है। "
        f"यहाँ आपको ₹{top_pick['buying_price_per_qtl']} प्रति क्विंटल का भाव मिलेगा। "
        f"डीजल खर्च घटाने के बाद भी आपको कुल ₹{top_pick['net_in_hand_profit_inr']:,.0f} का शुद्ध मुनाफा होगा, "
        f"जो सामान्य सरकारी मंडी से ₹{top_pick['net_advantage_over_apmc_inr']:,.0f} रुपये ज्यादा है!"
    )

    english_speech = (
        f"For your {qty} Quintals of {crop}, Kisan AI strongly recommends {top_pick['center_name']}. "
        f"At ₹{top_pick['buying_price_per_qtl']}/Qtl, your net in-hand profit after fuel deduction is ₹{top_pick['net_in_hand_profit_inr']:,.0f}, "
        f"giving you ₹{top_pick['net_advantage_over_apmc_inr']:,.0f} extra profit over standard APMC mandi."
    )

    quality_tips = [
        f"Ensure grain moisture is below {crop_info.get('standard_moisture_max', 12.0)}% to get Grade A+ premium.",
        "Private hubs (like ITC & Adani) offer direct pit unloading, saving 2-3 hours of manual bagging.",
        "Payments at private corporate hubs are disbursed via Instant RTGS/UPI within 30-60 minutes."
    ]

    return {
        "success": True,
        "crop": crop,
        "quantity_qtl": qty,
        "base_msp_rate": base_msp,
        "top_ai_pick": top_pick,
        "runner_up": runner_up,
        "all_ranked_mandis": ranked_mandis,
        "ai_speech_hi": hindi_speech,
        "ai_speech_en": english_speech,
        "quality_tips": quality_tips
    }

@router.post("/ask-query")
async def ask_ai_query(req: AIQueryRequest):
    """
    Conversational AI answers for farmer queries on mandi prices and advisories.
    """
    q = req.query.lower()
    
    if "wheat" in q or "गेहूं" in q:
        reply_hi = "वर्तमान में गेहूं का सबसे अधिक भाव 'ITC e-Choupal' (करनाल) में ₹2,510/क्विंटल है, जो सरकारी MSP (₹2,425) से ₹85 ज्यादा है। भुगतान 30 मिनट में यूपीआई/बैंक से होता है।"
        reply_en = "Currently, ITC e-Choupal offers the highest Wheat price at ₹2,510/Qtl (+₹85 bonus over Govt MSP ₹2,425). Instant UPI/Bank settlement within 30 minutes."
    elif "mustard" in q or "सरसों" in q:
        reply_hi = "सरसों का सबसे बेहतरीन भाव ₹6,120/क्विंटल है। अगर तेल की मात्रा अच्छी है तो नमी 8% से कम रखें ताकि अधिकतम भाव मिले।"
        reply_en = "Top Mustard rate is ₹6,120/Qtl (+₹170 bonus over MSP ₹5,950). Keep moisture below 8% for maximum rate."
    elif "distance" in q or "दूरी" in q or "नज़दीक" in q or "near" in q:
        reply_hi = "आपके गाँव से सबसे नज़दीकी केंद्र ITC e-Choupal (3.8 किमी) और करनाल सरकारी मंडी (4.5 किमी) हैं। दोनों में ट्रैक्टर से 8 से 10 मिनट का समय लगता है।"
        reply_en = "Nearest centers to your village are ITC e-Choupal (3.8 km) and Karnal Main APMC (4.5 km), taking under 10 minutes by tractor."
    elif "payment" in q or "भुगतान" in q or "dbt" in q:
        reply_hi = "सरकारी मंडियों में भुगतान सीधे आधार से जुड़े बैंक खाते में DBT के माध्यम से 2-4 घंटे में आता है, जबकि ITC और Reliance में 30 मिनट में डायरेक्ट ट्रांसफर मिलता है।"
        reply_en = "APMC Mandis clear payments directly into your Aadhaar-linked account via DBT within 2-4 hours, while private corporate hubs disburse within 30 minutes."
    else:
        reply_hi = f"नमस्ते किसान भाई! हमारे AI विश्लेषण के अनुसार, अपनी उपज को सीधे ITC e-Choupal या अदाणी साइलो में बेचने पर आपको सरकारी MSP से ₹65 से ₹85 प्रति क्विंटल अधिक मुनाफा मिलता है।"
        reply_en = f"Hello Farmer! According to our AI market analysis, selling directly to corporate hubs like ITC e-Choupal or Adani Silos yields ₹65 to ₹85/Qtl higher profit than standard APMC rates."

    return {
        "success": True,
        "reply_hi": reply_hi,
        "reply_en": reply_en
    }
