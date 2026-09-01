"""
Database Layer for AnnaSetu
SQLite with thread-safe connections, automated migrations & rich seed data.
"""

import sqlite3
import random
from datetime import datetime, timedelta
from backend.app.config import DB_PATH, DEFAULT_CENTERS, MSP_RATES, VEHICLE_FACTORS

def get_db():
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    # 1. Centers Table (Government APMC & Private Mandis)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS centers (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        district TEXT NOT NULL,
        state TEXT NOT NULL,
        location TEXT NOT NULL,
        latitude REAL,
        longitude REAL,
        mandi_type TEXT DEFAULT 'GOVERNMENT_APMC',
        operator_name TEXT,
        distance_km REAL DEFAULT 5.0,
        wheat_price_qtl REAL DEFAULT 2425,
        mustard_price_qtl REAL DEFAULT 5950,
        paddy_price_qtl REAL DEFAULT 2320,
        soybean_price_qtl REAL DEFAULT 4892,
        payment_speed TEXT DEFAULT 'Direct DBT Bank Transfer (2-4 hrs)',
        rating REAL DEFAULT 4.7,
        facilities TEXT,
        active_weighbridges INTEGER DEFAULT 2,
        active_quality_labs INTEGER DEFAULT 2,
        daily_capacity_quintals INTEGER DEFAULT 5000,
        operating_hours TEXT DEFAULT '08:00 AM - 07:00 PM',
        contact_phone TEXT,
        is_active INTEGER DEFAULT 1,
        congestion_status TEXT DEFAULT 'Smooth',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # 2. Farmers Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS farmers (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        aadhaar_mask TEXT,
        village TEXT NOT NULL,
        district TEXT NOT NULL,
        state TEXT NOT NULL,
        bank_name TEXT DEFAULT 'State Bank of India',
        bank_acc_mask TEXT DEFAULT 'XXXXXX4892',
        ifsc_code TEXT DEFAULT 'SBIN0001248',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # 3. Procurement Tokens Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tokens (
        id TEXT PRIMARY KEY,
        farmer_id TEXT NOT NULL,
        center_id TEXT NOT NULL,
        crop_name TEXT NOT NULL,
        crop_code TEXT NOT NULL,
        estimated_quantity_qtl REAL NOT NULL,
        vehicle_type TEXT NOT NULL,
        vehicle_number TEXT,
        booking_time TEXT DEFAULT CURRENT_TIMESTAMP,
        scheduled_date TEXT NOT NULL,
        scheduled_slot TEXT NOT NULL,
        stage TEXT DEFAULT 'REGISTERED',
        queue_number INTEGER,
        gross_weight_kg REAL,
        tare_weight_kg REAL,
        net_weight_qtl REAL,
        moisture_percent REAL,
        foreign_matter_percent REAL,
        quality_grade TEXT,
        msp_rate_applied REAL,
        total_amount_inr REAL,
        dbt_reference_no TEXT,
        stage_1_time TEXT,
        stage_2_time TEXT,
        stage_3_time TEXT,
        stage_4_time TEXT,
        stage_5_time TEXT,
        estimated_wait_mins INTEGER DEFAULT 30,
        priority_tag TEXT DEFAULT 'Normal',
        notes TEXT,
        FOREIGN KEY (farmer_id) REFERENCES farmers(id),
        FOREIGN KEY (center_id) REFERENCES centers(id)
    )
    """)

    # 4. Notifications Table (Simulated SMS / In-App / WhatsApp)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notifications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        token_id TEXT,
        farmer_phone TEXT NOT NULL,
        channel TEXT DEFAULT 'SMS',
        message TEXT NOT NULL,
        status TEXT DEFAULT 'DELIVERED',
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # 5. Stage Audit Trail Logs
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stage_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        token_id TEXT NOT NULL,
        from_stage TEXT,
        to_stage TEXT NOT NULL,
        operator_name TEXT DEFAULT 'Mandi Staff Operator',
        remarks TEXT,
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    seed_initial_data(conn)
    conn.close()

def seed_initial_data(conn):
    cursor = conn.cursor()

    # Always ensure centers table has all Government & Private Mandis
    cursor.execute("DELETE FROM centers")
    for c in DEFAULT_CENTERS:
        cursor.execute("""
        INSERT INTO centers (
            id, name, district, state, location, latitude, longitude,
            mandi_type, operator_name, distance_km, wheat_price_qtl, mustard_price_qtl,
            paddy_price_qtl, soybean_price_qtl, payment_speed, rating, facilities,
            active_weighbridges, active_quality_labs, daily_capacity_quintals, operating_hours,
            contact_phone, is_active, congestion_status
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            c["id"], c["name"], c["district"], c["state"], c["location"], c["latitude"], c["longitude"],
            c.get("mandi_type", "GOVERNMENT_APMC"), c.get("operator_name", "APMC Mandi Board"),
            c.get("distance_km", 5.0), c.get("wheat_price_qtl", 2425), c.get("mustard_price_qtl", 5950),
            c.get("paddy_price_qtl", 2320), c.get("soybean_price_qtl", 4892),
            c.get("payment_speed", "Direct DBT Bank Transfer"), c.get("rating", 4.7), c.get("facilities", "Certified Weights"),
            c["active_weighbridges"], c["active_quality_labs"], c["daily_capacity_quintals"], c["operating_hours"],
            c["contact_phone"], 1, c["congestion_status"]
        ))
    conn.commit()

    # Seed Sample Farmers & Live Tokens if empty
    cursor.execute("SELECT COUNT(*) FROM farmers")
    if cursor.fetchone()[0] == 0:
        sample_farmers = [
            ("FRM-101", "Rajeshwar Singh (राजेश्वर सिंह)", "9876543210", "XXXX-XXXX-8921", "Taraori", "Karnal", "Haryana", "SBI", "XXXXXX7812", "SBIN0001001"),
            ("FRM-102", "Gurpreet Singh Gill (गुरप्रीत सिंह)", "9812345678", "XXXX-XXXX-4512", "Samrala", "Ludhiana", "Punjab", "PNB", "XXXXXX9923", "PUNB0002144"),
            ("FRM-103", "Rameshwar Patel (रामेश्वर पटेल)", "9425112233", "XXXX-XXXX-6789", "Sanwer", "Indore", "Madhya Pradesh", "BOI", "XXXXXX3310", "BKID0008810"),
            ("FRM-104", "Suresh Reddy (सुरेश रेड्डी)", "9988776655", "XXXX-XXXX-1122", "Armoor", "Nizamabad", "Telangana", "Union Bank", "XXXXXX6641", "UBIN0009931"),
            ("FRM-105", "Manjit Kaur (मनजीत कौर)", "9872201199", "XXXX-XXXX-3344", "Doraha", "Ludhiana", "Punjab", "HDFC", "XXXXXX5520", "HDFC0004112"),
            ("FRM-106", "Dharmendra Yadav (धर्मेंद्र यादव)", "9711002233", "XXXX-XXXX-9900", "Gharaunda", "Karnal", "Haryana", "SBI", "XXXXXX4400", "SBIN0001001"),
            ("FRM-107", "Kailash Choudhary (कैलाश चौधरी)", "9414005566", "XXXX-XXXX-7788", "Depalpur", "Indore", "Madhya Pradesh", "CBI", "XXXXXX1190", "CBIN0003300"),
        ]

        for f in sample_farmers:
            cursor.execute("""
            INSERT INTO farmers (id, name, phone, aadhaar_mask, village, district, state, bank_name, bank_acc_mask, ifsc_code)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, f)

        today_str = datetime.now().strftime("%Y-%m-%d")
        now = datetime.now()

        # Seed sample tokens at various stages for instant demo richness
        sample_tokens = [
            # Token 1: Quality Check Stage at Karnal
            {
                "id": "AS-26-WHT-101",
                "farmer_id": "FRM-101",
                "center_id": "CTR-001",
                "crop_name": "Wheat (गेहूं)",
                "crop_code": "WHT",
                "estimated_quantity_qtl": 45.0,
                "vehicle_type": "Tractor Trolley (ट्रैक्टर ट्रॉली)",
                "vehicle_number": "HR-05-AB-4819",
                "booking_time": (now - timedelta(hours=3)).strftime("%Y-%m-%d %H:%M:%S"),
                "scheduled_date": today_str,
                "scheduled_slot": "09:00 AM - 11:00 AM",
                "stage": "QUALITY_CHECK",
                "queue_number": 1,
                "gross_weight_kg": 7250.0,
                "tare_weight_kg": None,
                "net_weight_qtl": None,
                "moisture_percent": 11.2,
                "foreign_matter_percent": 0.8,
                "quality_grade": "Grade A (FAQ Standard)",
                "msp_rate_applied": 2425.0,
                "total_amount_inr": None,
                "dbt_reference_no": None,
                "stage_1_time": (now - timedelta(hours=3)).strftime("%Y-%m-%d %H:%M:%S"),
                "stage_2_time": (now - timedelta(hours=1, minutes=45)).strftime("%Y-%m-%d %H:%M:%S"),
                "stage_3_time": (now - timedelta(minutes=50)).strftime("%Y-%m-%d %H:%M:%S"),
                "stage_4_time": (now - timedelta(minutes=15)).strftime("%Y-%m-%d %H:%M:%S"),
                "stage_5_time": None,
                "estimated_wait_mins": 10,
                "priority_tag": "Normal",
                "notes": "Moisture well within permissible limits (11.2%). High lustre grain.",
            },
            # Token 2: Weighbridge Stage at Karnal
            {
                "id": "AS-26-MST-102",
                "farmer_id": "FRM-106",
                "center_id": "CTR-001",
                "crop_name": "Mustard / Rapeseed (सरसों)",
                "crop_code": "MST",
                "estimated_quantity_qtl": 28.0,
                "vehicle_type": "Mini Truck / Pickup (छोटा हाथी / पिकअप)",
                "vehicle_number": "HR-05-CD-9912",
                "booking_time": (now - timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S"),
                "scheduled_date": today_str,
                "scheduled_slot": "10:00 AM - 12:00 PM",
                "stage": "WEIGHBRIDGE",
                "queue_number": 2,
                "gross_weight_kg": 4650.0,
                "tare_weight_kg": None,
                "net_weight_qtl": None,
                "moisture_percent": None,
                "foreign_matter_percent": None,
                "quality_grade": None,
                "msp_rate_applied": 5950.0,
                "total_amount_inr": None,
                "dbt_reference_no": None,
                "stage_1_time": (now - timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S"),
                "stage_2_time": (now - timedelta(minutes=40)).strftime("%Y-%m-%d %H:%M:%S"),
                "stage_3_time": (now - timedelta(minutes=8)).strftime("%Y-%m-%d %H:%M:%S"),
                "stage_4_time": None,
                "stage_5_time": None,
                "estimated_wait_mins": 18,
                "priority_tag": "Normal",
                "notes": "Weighbridge #1 Gross reading taken.",
            },
            # Token 3: Gate Entry (In Queue) at Khanna
            {
                "id": "AS-26-PDY-103",
                "farmer_id": "FRM-102",
                "center_id": "CTR-002",
                "crop_name": "Paddy Common (धान सामान्य)",
                "crop_code": "PDY",
                "estimated_quantity_qtl": 75.0,
                "vehicle_type": "Large Tractor (बड़ा ट्रैक्टर - 2 ट्रॉली)",
                "vehicle_number": "PB-10-XX-7810",
                "booking_time": (now - timedelta(hours=1, minutes=30)).strftime("%Y-%m-%d %H:%M:%S"),
                "scheduled_date": today_str,
                "scheduled_slot": "11:00 AM - 01:00 PM",
                "stage": "GATE_ENTRY",
                "queue_number": 3,
                "gross_weight_kg": None,
                "tare_weight_kg": None,
                "net_weight_qtl": None,
                "moisture_percent": None,
                "foreign_matter_percent": None,
                "quality_grade": None,
                "msp_rate_applied": 2300.0,
                "total_amount_inr": None,
                "dbt_reference_no": None,
                "stage_1_time": (now - timedelta(hours=1, minutes=30)).strftime("%Y-%m-%d %H:%M:%S"),
                "stage_2_time": (now - timedelta(minutes=25)).strftime("%Y-%m-%d %H:%M:%S"),
                "stage_3_time": None,
                "stage_4_time": None,
                "stage_5_time": None,
                "estimated_wait_mins": 25,
                "priority_tag": "Normal",
                "notes": "Gate 2 entry verified. Waiting for weighbridge lane call.",
            },
            # Token 4: Payment Processed (Completed) at Indore
            {
                "id": "AS-26-SOY-104",
                "farmer_id": "FRM-103",
                "center_id": "CTR-003",
                "crop_name": "Soybean (सोयाबीन)",
                "crop_code": "SOY",
                "estimated_quantity_qtl": 52.0,
                "vehicle_type": "Tractor Trolley (ट्रैक्टर ट्रॉली)",
                "vehicle_number": "MP-09-KA-5521",
                "booking_time": (now - timedelta(hours=5)).strftime("%Y-%m-%d %H:%M:%S"),
                "scheduled_date": today_str,
                "scheduled_slot": "08:30 AM - 10:30 AM",
                "stage": "PAYMENT_PROCESSED",
                "queue_number": 0,
                "gross_weight_kg": 8100.0,
                "tare_weight_kg": 2900.0,
                "net_weight_qtl": 52.0,
                "moisture_percent": 10.8,
                "foreign_matter_percent": 1.1,
                "quality_grade": "Grade A",
                "msp_rate_applied": 4892.0,
                "total_amount_inr": 254384.0,
                "dbt_reference_no": "DBT-2026-MP-9841284",
                "stage_1_time": (now - timedelta(hours=5)).strftime("%Y-%m-%d %H:%M:%S"),
                "stage_2_time": (now - timedelta(hours=4)).strftime("%Y-%m-%d %H:%M:%S"),
                "stage_3_time": (now - timedelta(hours=3, minutes=15)).strftime("%Y-%m-%d %H:%M:%S"),
                "stage_4_time": (now - timedelta(hours=2, minutes=30)).strftime("%Y-%m-%d %H:%M:%S"),
                "stage_5_time": (now - timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S"),
                "estimated_wait_mins": 0,
                "priority_tag": "Normal",
                "notes": "Procurement completed successfully. ₹2,54,384 DBT credited to bank account.",
            },
            # Token 5: Slot Booked / Scheduled at Nizamabad
            {
                "id": "AS-26-MAZ-105",
                "farmer_id": "FRM-104",
                "center_id": "CTR-004",
                "crop_name": "Maize (मक्का)",
                "crop_code": "MAZ",
                "estimated_quantity_qtl": 35.0,
                "vehicle_type": "Tractor Trolley (ट्रैक्टर ट्रॉली)",
                "vehicle_number": "TS-16-ZZ-2231",
                "booking_time": (now - timedelta(minutes=45)).strftime("%Y-%m-%d %H:%M:%S"),
                "scheduled_date": today_str,
                "scheduled_slot": "02:00 PM - 04:00 PM",
                "stage": "REGISTERED",
                "queue_number": 4,
                "gross_weight_kg": None,
                "tare_weight_kg": None,
                "net_weight_qtl": None,
                "moisture_percent": None,
                "foreign_matter_percent": None,
                "quality_grade": None,
                "msp_rate_applied": 2225.0,
                "total_amount_inr": None,
                "dbt_reference_no": None,
                "stage_1_time": (now - timedelta(minutes=45)).strftime("%Y-%m-%d %H:%M:%S"),
                "stage_2_time": None,
                "stage_3_time": None,
                "stage_4_time": None,
                "stage_5_time": None,
                "estimated_wait_mins": 35,
                "priority_tag": "Normal",
                "notes": "Scheduled for afternoon arrival. Recommended travel departure: 01:15 PM.",
            },
            # Token 6: Completed Past Sale at ITC e-Choupal (Private Mandi Bonus!)
            {
                "id": "AS-26-WHT-088",
                "farmer_id": "FRM-101",
                "center_id": "CTR-PVT-001",
                "crop_name": "Wheat (गेहूं)",
                "crop_code": "WHT",
                "estimated_quantity_qtl": 50.0,
                "vehicle_type": "Tractor Trolley (ट्रैक्टर ट्रॉली)",
                "vehicle_number": "HR-05-AE-4421",
                "booking_time": (now - timedelta(days=5)).strftime("%Y-%m-%d %H:%M:%S"),
                "scheduled_date": (now - timedelta(days=5)).strftime("%Y-%m-%d"),
                "scheduled_slot": "09:00 AM - 11:00 AM",
                "stage": "PAYMENT_PROCESSED",
                "queue_number": 0,
                "gross_weight_kg": 7450.0,
                "tare_weight_kg": 2450.0,
                "net_weight_qtl": 50.0,
                "moisture_percent": 11.4,
                "foreign_matter_percent": 0.6,
                "quality_grade": "Grade A+ (Premium Protein)",
                "msp_rate_applied": 2510.0, # Private Mandi Rate!
                "total_amount_inr": 125500.0, # ₹1,25,500 (+₹4,250 Bonus over MSP!)
                "dbt_reference_no": "DBT-2026-ITC-8812903",
                "stage_1_time": (now - timedelta(days=5, hours=4)).strftime("%Y-%m-%d %H:%M:%S"),
                "stage_2_time": (now - timedelta(days=5, hours=3)).strftime("%Y-%m-%d %H:%M:%S"),
                "stage_3_time": (now - timedelta(days=5, hours=2)).strftime("%Y-%m-%d %H:%M:%S"),
                "stage_4_time": (now - timedelta(days=5, hours=1)).strftime("%Y-%m-%d %H:%M:%S"),
                "stage_5_time": (now - timedelta(days=5)).strftime("%Y-%m-%d %H:%M:%S"),
                "estimated_wait_mins": 0,
                "priority_tag": "Normal",
                "notes": "Delivered to ITC e-Choupal Hub. Instant spot payment credited.",
            },
            # Token 7: Completed Past Sale at Karnal APMC (Mustard)
            {
                "id": "AS-26-MST-042",
                "farmer_id": "FRM-101",
                "center_id": "CTR-001",
                "crop_name": "Mustard / Rapeseed (सरसों)",
                "crop_code": "MST",
                "estimated_quantity_qtl": 30.0,
                "vehicle_type": "Tractor Trolley (ट्रैक्टर ट्रॉली)",
                "vehicle_number": "HR-05-AE-4421",
                "booking_time": (now - timedelta(days=14)).strftime("%Y-%m-%d %H:%M:%S"),
                "scheduled_date": (now - timedelta(days=14)).strftime("%Y-%m-%d"),
                "scheduled_slot": "10:00 AM - 12:00 PM",
                "stage": "PAYMENT_PROCESSED",
                "queue_number": 0,
                "gross_weight_kg": 5450.0,
                "tare_weight_kg": 2450.0,
                "net_weight_qtl": 30.0,
                "moisture_percent": 7.6,
                "foreign_matter_percent": 0.5,
                "quality_grade": "Grade A",
                "msp_rate_applied": 5950.0,
                "total_amount_inr": 178500.0,
                "dbt_reference_no": "DBT-2026-HR-7721849",
                "stage_1_time": (now - timedelta(days=14, hours=4)).strftime("%Y-%m-%d %H:%M:%S"),
                "stage_2_time": (now - timedelta(days=14, hours=3)).strftime("%Y-%m-%d %H:%M:%S"),
                "stage_3_time": (now - timedelta(days=14, hours=2)).strftime("%Y-%m-%d %H:%M:%S"),
                "stage_4_time": (now - timedelta(days=14, hours=1)).strftime("%Y-%m-%d %H:%M:%S"),
                "stage_5_time": (now - timedelta(days=14)).strftime("%Y-%m-%d %H:%M:%S"),
                "estimated_wait_mins": 0,
                "priority_tag": "Normal",
                "notes": "Official MSP procurement completed. ₹1,78,500 DBT cleared.",
            }
        ]

        for t in sample_tokens:
            cursor.execute("""
            INSERT INTO tokens (
                id, farmer_id, center_id, crop_name, crop_code, estimated_quantity_qtl,
                vehicle_type, vehicle_number, booking_time, scheduled_date, scheduled_slot,
                stage, queue_number, gross_weight_kg, tare_weight_kg, net_weight_qtl,
                moisture_percent, foreign_matter_percent, quality_grade, msp_rate_applied,
                total_amount_inr, dbt_reference_no, stage_1_time, stage_2_time, stage_3_time,
                stage_4_time, stage_5_time, estimated_wait_mins, priority_tag, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                t["id"], t["farmer_id"], t["center_id"], t["crop_name"], t["crop_code"], t["estimated_quantity_qtl"],
                t["vehicle_type"], t["vehicle_number"], t["booking_time"], t["scheduled_date"], t["scheduled_slot"],
                t["stage"], t["queue_number"], t["gross_weight_kg"], t["tare_weight_kg"], t["net_weight_qtl"],
                t["moisture_percent"], t["foreign_matter_percent"], t["quality_grade"], t["msp_rate_applied"],
                t["total_amount_inr"], t["dbt_reference_no"], t["stage_1_time"], t["stage_2_time"], t["stage_3_time"],
                t["stage_4_time"], t["stage_5_time"], t["estimated_wait_mins"], t["priority_tag"], t["notes"]
            ))

        # Sample notifications
        sample_notifs = [
            ("AS-26-WHT-101", "9876543210", "SMS", "AnnaSetu: Token AS-26-WHT-101 has entered Quality Testing at Karnal Mandi. Approx wait: 10 mins."),
            ("AS-26-SOY-104", "9425112233", "SMS", "AnnaSetu: Procurement of 52.0 Qtls Soybean completed. DBT ₹2,54,384 initiated to Bank A/c ending 4892. Ref: DBT-2026-MP-9841284"),
            ("AS-26-PDY-103", "9812345678", "SMS", "AnnaSetu: Gate entry confirmed at Khanna Mandi for Token AS-26-PDY-103. Current queue position: #3."),
        ]
        for n in sample_notifs:
            cursor.execute("INSERT INTO notifications (token_id, farmer_phone, channel, message) VALUES (?, ?, ?, ?)", n)

        conn.commit()

# Helper dict-fetch functions
def fetch_all(query, params=()):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def fetch_one(query, params=()):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(query, params)
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def execute_write(query, params=()):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(query, params)
    last_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return last_id
