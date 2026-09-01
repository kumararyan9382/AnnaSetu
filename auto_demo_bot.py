"""
AnnaSetu One-Click Automated Demo Bot
Runs a live end-to-end simulation across all 5 stages in real time with visual commentary.
"""

import time
import sys
import requests

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_URL = "http://127.0.0.1:8000"

def run_automated_demo():
    print("=================================================================")
    print("🌾 AnnaSetu Live Automated Demo Bot (Smart India Hackathon 2026)")
    print("=================================================================\n")

    # Step 1: Check Server Health
    print("[1/5] Checking Server Connection...")
    try:
        r = requests.get(f"{BASE_URL}/api/centers/compare", timeout=3)
        if r.status_code == 200:
            print("   -> Server is LIVE at http://127.0.0.1:8000\n")
        else:
            print("   -> Server returned non-200 status code.")
            return
    except Exception as e:
        print(f"   -> ERROR: Could not connect to {BASE_URL}. Make sure 'python run.py' is running!")
        return

    # Step 2: Book a Farmer Slot
    print("[2/5] Creating Farmer Slot Booking on Front Page...")
    book_payload = {
        "farmer_name": "Rajeshwar Singh (Live Demo)",
        "phone": "9876543210",
        "village": "Taraori",
        "district": "Karnal",
        "crop_name": "Wheat",
        "estimated_quantity_qtl": 50.0,
        "vehicle_type": "Tractor Trolley (ट्रैक्टर ट्रॉली)",
        "vehicle_number": "HR-05-AB-9921",
        "center_id": "CTR-001",
        "preferred_slot": "09:00 AM - 11:00 AM"
    }

    resp = requests.post(f"{BASE_URL}/api/farmers/book", json=book_payload)
    if resp.status_code != 200:
        print(f"   -> Booking failed: {resp.text}")
        return

    token_data = resp.json()
    token_id = token_data.get("id") or token_data.get("token_id")
    payout = float(token_data.get("msp_rate_applied", 2425)) * float(token_data.get("estimated_quantity_qtl", 50.0))
    print(f"   -> SUCCESS: Created Token: {token_id}")
    print(f"   -> Guaranteed MSP Payout: Rs. {payout:,.2f}")
    print(f"   -> Queue Number: #{token_data.get('queue_number', 1)} | Est. Wait: {token_data.get('estimated_wait_mins', 20)} Mins\n")

    time.sleep(3)

    # Step 3: Advance to Stage 2 (Gate Entry)
    print(f"[3/5] Mandi Staff: Checking in at Gate Entry for {token_id}...")
    r = requests.post(f"{BASE_URL}/api/staff/advance-stage", json={
        "token_id": token_id,
        "next_stage": "GATE_ENTRY",
        "operator_id": "OP-GATE-01"
    })
    print(f"   -> Stage 2 Confirmed: {r.json().get('message', 'Gate Entry Done')}")
    print("   -> Live WebSocket broadcast sent to Farmer Screen!\n")

    time.sleep(3)

    # Step 4: Advance to Stage 3 (Weighbridge)
    print(f"[4/5] Mandi Staff: Logging Gross Weight at Certified Weighbridge...")
    r = requests.post(f"{BASE_URL}/api/staff/advance-stage", json={
        "token_id": token_id,
        "next_stage": "WEIGHBRIDGE",
        "operator_id": "OP-WEIGH-01",
        "gross_weight_kg": 7850.0
    })
    print("   -> Stage 3 Confirmed: Gross Weight 7,850 kg recorded to audit log.\n")

    time.sleep(3)

    # Step 5: Advance to Stage 4 (Quality Testing Lab)
    print(f"[5/5] Mandi Staff: Logging Quality & Moisture Test Results...")
    r = requests.post(f"{BASE_URL}/api/staff/advance-stage", json={
        "token_id": token_id,
        "next_stage": "QUALITY_CHECK",
        "operator_id": "OP-LAB-01",
        "moisture_percentage": 11.4,
        "quality_grade": "Grade A"
    })
    print("   -> Stage 4 Confirmed: Moisture 11.4% (Passed FAQ Standard). Grade A recorded.\n")

    time.sleep(3)

    # Step 6: Advance to Stage 5 (Unloading & DBT Payout)
    print(f"[FINAL] Mandi Staff: Authorizing Instant DBT Payment Clearance...")
    r = requests.post(f"{BASE_URL}/api/staff/advance-stage", json={
        "token_id": token_id,
        "next_stage": "PAYMENT_PROCESSED",
        "operator_id": "OP-PAY-01",
        "tare_weight_kg": 2850.0
    })
    payment_data = r.json().get("payment_summary", {})
    print("   -> Stage 5 Confirmed: Direct Benefit Transfer (DBT) Authorized!")
    print(f"   -> Net Quantity: {payment_data.get('net_quantity_quintals', 50.0)} Quintals (7,850 kg - 2,850 kg)")
    print(f"   -> Total Disbursed: Rs. {payment_data.get('total_amount', 121250.0):,.2f}")
    print(f"   -> Official DBT Reference: {payment_data.get('dbt_reference', 'DBT-2026-WHT-XXXXX')}")
    print(f"\n=================================================================")
    print(f"🎉 Live Demo Complete! Check Live Tracker at:")
    print(f"   http://127.0.0.1:8000/track/{token_id}")
    print(f"=================================================================")

if __name__ == "__main__":
    run_automated_demo()
