"""
Notification & Communication Dispatch Service (SMS / WhatsApp / In-App)
"""

from datetime import datetime
from backend.app.database import execute_write, fetch_all

def send_stage_notification(token_id: str, farmer_phone: str, farmer_name: str, stage_code: str, details: dict = None) -> dict:
    details = details or {}
    total_amt = details.get("total_amount_inr") or 0
    gross_wt = details.get("gross_weight_kg") or 0
    moisture = details.get("moisture_percent") or 0
    grade = details.get("quality_grade") or "Grade A"
    dbt_ref = details.get("dbt_reference_no") or "DBT-GOV-PRO"

    messages = {
        "REGISTERED": f"AnnaSetu: नमस्ते {farmer_name}, टोकन {token_id} सफलतापूर्वक बुक हुआ। कृपया निर्धारित समय पर मंडी पहुंचें।",
        "GATE_ENTRY": f"AnnaSetu: टोकन {token_id} की गेट एंट्री दर्ज हो गई है। आप कतार में हैं। अगला चरण: वे-ब्रिज तौल।",
        "WEIGHBRIDGE": f"AnnaSetu: टोकन {token_id} का सकल वजन (Gross Weight) {gross_wt} kg दर्ज किया गया। अगला चरण: गुणवत्ता व नमी जांच।",
        "QUALITY_CHECK": f"AnnaSetu: टोकन {token_id} गुणवत्ता जांच संपन्न। नमी: {moisture}%, ग्रेड: {grade}।",
        "PAYMENT_PROCESSED": f"AnnaSetu: बधाई! टोकन {token_id} उपार्जन पूर्ण। DBT राशि ₹{total_amt:,.2f} आपके बैंक खाते में भेजी जा रही है। Ref: {dbt_ref}"
    }

    message_text = messages.get(stage_code, f"AnnaSetu: टोकन {token_id} की स्थिति अपडेट की गई: {stage_code}")
    
    # Save to database notifications
    notif_id = execute_write("""
        INSERT INTO notifications (token_id, farmer_phone, channel, message, status, timestamp)
        VALUES (?, ?, 'SMS', ?, 'DELIVERED', ?)
    """, (token_id, farmer_phone, message_text, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    return {
        "id": notif_id,
        "token_id": token_id,
        "phone": farmer_phone,
        "message": message_text,
        "status": "DELIVERED",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def get_recent_notifications(limit: int = 15) -> list:
    return fetch_all("""
        SELECT n.*, t.crop_name, f.name as farmer_name 
        FROM notifications n
        LEFT JOIN tokens t ON n.token_id = t.id
        LEFT JOIN farmers f ON t.farmer_id = f.id
        ORDER BY n.id DESC LIMIT ?
    """, (limit,))
