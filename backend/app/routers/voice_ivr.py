"""
Voice Assistant & Simulated IVR Router for Low-Literacy / Non-Smartphone Farmers
"""

import re
from fastapi import APIRouter, HTTPException
from backend.app.database import fetch_all, fetch_one
from backend.app.models import VoiceQueryRequest
from backend.app.services.queue_service import calculate_token_wait_time

router = APIRouter(prefix="/api/voice", tags=["Voice & IVR"])

@router.post("/lookup")
def voice_lookup_token(req: VoiceQueryRequest):
    """
    Simulates a toll-free IVR call or voice search query (e.g. Kisan Call Center 1800-XXX-XXXX).
    Input can be a 10-digit phone number, token ID, or spoken sentence.
    """
    raw_query = req.query.strip()
    digits = "".join(re.findall(r'\d+', raw_query))
    
    token = None
    # 1. Search by token ID
    if "AS-" in raw_query.upper():
        token_match = re.search(r'AS-[\w-]+', raw_query.upper())
        if token_match:
            token = fetch_one("""
                SELECT t.*, f.name as farmer_name, f.phone as farmer_phone, c.name as center_name
                FROM tokens t
                JOIN farmers f ON t.farmer_id = f.id
                JOIN centers c ON t.center_id = c.id
                WHERE t.id = ?
            """, (token_match.group(0),))

    # 2. Search by phone number (at least last 4-10 digits)
    if not token and len(digits) >= 4:
        token = fetch_one("""
            SELECT t.*, f.name as farmer_name, f.phone as farmer_phone, c.name as center_name
            FROM tokens t
            JOIN farmers f ON t.farmer_id = f.id
            JOIN centers c ON t.center_id = c.id
            WHERE f.phone LIKE ? OR t.id LIKE ?
            ORDER BY t.booking_time DESC LIMIT 1
        """, (f"%{digits}%", f"%{digits}%"))

    if not token:
        # Fallback to the latest active token for demonstration
        token = fetch_one("""
            SELECT t.*, f.name as farmer_name, f.phone as farmer_phone, c.name as center_name
            FROM tokens t
            JOIN farmers f ON t.farmer_id = f.id
            JOIN centers c ON t.center_id = c.id
            WHERE t.stage != 'PAYMENT_PROCESSED'
            ORDER BY t.booking_time DESC LIMIT 1
        """)

    if not token:
        return {
            "found": False,
            "speech_hi": "क्षमा करें, आपका कोई सक्रिय उपार्जन टोकन नहीं मिला। कृपया अपना पंजीकृत मोबाइल नंबर दोबारा बताएं।",
            "speech_en": "Sorry, no active procurement token found. Please repeat your registered mobile number.",
            "token": None
        }

    # Format speech readout
    stage_text_hi = {
        "REGISTERED": "आपका स्लॉट सफलतापूर्वक बुक है। कृपया निर्धारित समय पर मंडी पहुंचें।",
        "GATE_ENTRY": "आपकी गाड़ी मंडी के मुख्य द्वार में प्रवेश कर चुकी है। आप वर्तमान में तौल कतार में हैं।",
        "WEIGHBRIDGE": "आपका सकल वजन दर्ज हो चुका है। अब आपकी फसल की गुणवत्ता और नमी की जांच हो रही है।",
        "QUALITY_CHECK": "गुणवत्ता जांच पूरी हो चुकी है। उपार्जन स्वीकृति की प्रक्रिया चल रही है।",
        "PAYMENT_PROCESSED": f"उपार्जन सफलतापूर्वक पूरा हो चुका है। कुल राशि ₹{token.get('total_amount_inr', 0):,} का डायरेक्ट बैंक ट्रांसफर (DBT) भेज दिया गया है।"
    }.get(token["stage"], "आपकी स्थिति प्रक्रियाधीन है।")

    speech_hi = (
        f"नमस्ते {token['farmer_name']} जी। "
        f"आपका टोकन नंबर {token['id']} है। "
        f"केंद्र: {token['center_name']}। "
        f"फसल: {token['crop_name']}। "
        f"वर्तमान स्थिति: {stage_text_hi} "
        f"अनुमानित प्रतीक्षा समय लगभग {token.get('estimated_wait_mins', 15)} मिनट है।"
    )

    speech_en = (
        f"Hello {token['farmer_name']}. "
        f"Your Token ID is {token['id']} at {token['center_name']}. "
        f"Crop: {token['crop_name']}. "
        f"Current stage: {token['stage'].replace('_', ' ')}. "
        f"Estimated wait time is approximately {token.get('estimated_wait_mins', 15)} minutes."
    )

    return {
        "found": True,
        "token_id": token["id"],
        "farmer_name": token["farmer_name"],
        "stage": token["stage"],
        "speech_hi": speech_hi,
        "speech_en": speech_en,
        "token": token
    }
