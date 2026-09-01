"""
AnnaSetu System Configuration & Constants
SIH 2026 Problem Statement: SIH26032
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "annasetu.db"

# Official 2025-2026 Minimum Support Price (MSP) Data (in INR per Quintal)
MSP_RATES = {
    "Wheat (गेहूं)": {
        "code": "WHT",
        "msp_per_quintal": 2425,
        "category": "Rabi",
        "standard_moisture_max": 12.0,
        "standard_foreign_matter_max": 1.5,
        "avg_weigh_time_mins": 6,
        "avg_quality_check_mins": 8,
    },
    "Paddy Common (धान सामान्य)": {
        "code": "PDY",
        "msp_per_quintal": 2300,
        "category": "Kharif",
        "standard_moisture_max": 17.0,
        "standard_foreign_matter_max": 2.0,
        "avg_weigh_time_mins": 7,
        "avg_quality_check_mins": 9,
    },
    "Paddy Grade A (धान ग्रेड-ए)": {
        "code": "PDYA",
        "msp_per_quintal": 2320,
        "category": "Kharif",
        "standard_moisture_max": 17.0,
        "standard_foreign_matter_max": 1.5,
        "avg_weigh_time_mins": 7,
        "avg_quality_check_mins": 9,
    },
    "Mustard / Rapeseed (सरसों)": {
        "code": "MST",
        "msp_per_quintal": 5950,
        "category": "Rabi",
        "standard_moisture_max": 8.0,
        "standard_foreign_matter_max": 1.0,
        "avg_weigh_time_mins": 5,
        "avg_quality_check_mins": 10,
    },
    "Gram / Chana (चना)": {
        "code": "CHN",
        "msp_per_quintal": 5650,
        "category": "Rabi",
        "standard_moisture_max": 10.0,
        "standard_foreign_matter_max": 1.5,
        "avg_weigh_time_mins": 6,
        "avg_quality_check_mins": 7,
    },
    "Maize (मक्का)": {
        "code": "MAZ",
        "msp_per_quintal": 2225,
        "category": "Kharif",
        "standard_moisture_max": 14.0,
        "standard_foreign_matter_max": 2.0,
        "avg_weigh_time_mins": 6,
        "avg_quality_check_mins": 7,
    },
    "Soybean (सोयाबीन)": {
        "code": "SOY",
        "msp_per_quintal": 4892,
        "category": "Kharif",
        "standard_moisture_max": 12.0,
        "standard_foreign_matter_max": 2.0,
        "avg_weigh_time_mins": 6,
        "avg_quality_check_mins": 8,
    },
}

# Vehicle Type Impact Factor on Unloading & Weighing Times
VEHICLE_FACTORS = {
    "Tractor Trolley (ट्रैक्टर ट्रॉली)": {"factor": 1.0, "base_mins": 15, "capacity_qtl": 40},
    "Large Tractor (बड़ा ट्रैक्टर - 2 ट्रॉली)": {"factor": 1.6, "base_mins": 25, "capacity_qtl": 80},
    "Mini Truck / Pickup (छोटा हाथी / पिकअप)": {"factor": 0.8, "base_mins": 12, "capacity_qtl": 25},
    "Commercial Truck (बड़ा ट्रक)": {"factor": 2.2, "base_mins": 35, "capacity_qtl": 150},
    "Bullock Cart / Jugad (बैलगाड़ी / जुगाड़)": {"factor": 0.6, "base_mins": 10, "capacity_qtl": 15},
}

# Default Pre-Configured Mandi Procurement Centers (Government APMC & Private Corporate Mandis)
DEFAULT_CENTERS = [
    # --- 🏛️ GOVERNMENT APMC MANDIS ---
    {
        "id": "CTR-001",
        "name": "Karnal Main Anaj Mandi (करनाल सरकारी अनाज मंडी)",
        "district": "Karnal",
        "state": "Haryana",
        "location": "Sector 38, GT Road, Karnal",
        "latitude": 29.6857,
        "longitude": 76.9905,
        "mandi_type": "GOVERNMENT_APMC",
        "operator_name": "Haryana State Agricultural Marketing Board (HSAMB)",
        "distance_km": 4.5,
        "wheat_price_qtl": 2425,
        "mustard_price_qtl": 5950,
        "paddy_price_qtl": 2320,
        "soybean_price_qtl": 4892,
        "payment_speed": "Direct DBT Bank Transfer (2-4 hrs)",
        "rating": 4.6,
        "active_weighbridges": 3,
        "active_quality_labs": 2,
        "daily_capacity_quintals": 5000,
        "operating_hours": "08:00 AM - 07:00 PM",
        "contact_phone": "+91-184-2254101",
        "is_active": True,
        "congestion_status": "Moderate",
        "facilities": "Government MSP Guarantee, FCI Procurement Hub, Official Gate Pass"
    },
    {
        "id": "CTR-002",
        "name": "Khanna Asia Largest Grain Market (खन्ना सरकारी मंडी)",
        "district": "Ludhiana",
        "state": "Punjab",
        "location": "GT Road, Khanna, Ludhiana",
        "latitude": 30.7071,
        "longitude": 76.2167,
        "mandi_type": "GOVERNMENT_APMC",
        "operator_name": "Punjab Mandi Board (PSAMB)",
        "distance_km": 18.2,
        "wheat_price_qtl": 2425,
        "mustard_price_qtl": 5950,
        "paddy_price_qtl": 2320,
        "soybean_price_qtl": 4892,
        "payment_speed": "Direct DBT Bank Transfer (2-4 hrs)",
        "rating": 4.5,
        "active_weighbridges": 5,
        "active_quality_labs": 3,
        "daily_capacity_quintals": 9000,
        "operating_hours": "07:30 AM - 08:00 PM",
        "contact_phone": "+91-1628-220045",
        "is_active": True,
        "congestion_status": "Busy",
        "facilities": "High Capacity Silos, 5 Weighbridges, Government MSP Portal Sync"
    },
    {
        "id": "CTR-003",
        "name": "Indore Krishi Upaj Mandi (इंदौर सरकारी कृषि उपज मंडी)",
        "district": "Indore",
        "state": "Madhya Pradesh",
        "location": "Chhavani Mandi Complex, Indore",
        "latitude": 22.7196,
        "longitude": 75.8577,
        "mandi_type": "GOVERNMENT_APMC",
        "operator_name": "MP State APMC Board",
        "distance_km": 12.0,
        "wheat_price_qtl": 2425,
        "mustard_price_qtl": 5950,
        "paddy_price_qtl": 2320,
        "soybean_price_qtl": 4892,
        "payment_speed": "Direct DBT Bank Transfer (2-4 hrs)",
        "rating": 4.7,
        "active_weighbridges": 4,
        "active_quality_labs": 2,
        "daily_capacity_quintals": 6500,
        "operating_hours": "08:30 AM - 06:30 PM",
        "contact_phone": "+91-731-2521990",
        "is_active": True,
        "congestion_status": "Smooth",
        "facilities": "E-Nam Integrated, Official Grade Certification, Covered Sheds"
    },
    
    # --- 🏢 TOP PRIVATE MANDIS & CORPORATE AGRI HUBS ---
    {
        "id": "CTR-PVT-001",
        "name": "ITC e-Choupal Rural Hub (आईटीसी ई-चौपाल प्राइवेट केंद्र)",
        "district": "Karnal",
        "state": "Haryana",
        "location": "Karnal-Kaithal Highway, Near Nilokheri",
        "latitude": 29.7420,
        "longitude": 76.9210,
        "mandi_type": "PRIVATE_CORPORATE",
        "operator_name": "ITC Limited Agri-Business",
        "distance_km": 3.8,
        "wheat_price_qtl": 2510,  # +₹85/Qtl Bonus over MSP!
        "mustard_price_qtl": 6120, # +₹170/Qtl Bonus!
        "paddy_price_qtl": 2410,
        "soybean_price_qtl": 5010,
        "payment_speed": "Instant Spot RTGS / UPI (30 mins)",
        "rating": 4.9,
        "active_weighbridges": 3,
        "active_quality_labs": 2,
        "daily_capacity_quintals": 4000,
        "operating_hours": "07:00 AM - 08:00 PM",
        "contact_phone": "+91-1800-419-0123",
        "is_active": True,
        "congestion_status": "Smooth",
        "facilities": "🌟 +₹85/Qtl Higher Price, 0% Commission, Instant UPI Payment, Free Soil Test"
    },
    {
        "id": "CTR-PVT-002",
        "name": "Adani Agri Logistics Silo (अदाणी मॉडर्न एग्री साइलो)",
        "district": "Karnal",
        "state": "Haryana",
        "location": "Industrial Corridor, Taraori",
        "latitude": 29.8010,
        "longitude": 76.9290,
        "mandi_type": "PRIVATE_CORPORATE",
        "operator_name": "Adani Agri Logistics Ltd.",
        "distance_km": 8.4,
        "wheat_price_qtl": 2490,  # +₹65/Qtl Bonus!
        "mustard_price_qtl": 6050,
        "paddy_price_qtl": 2390,
        "soybean_price_qtl": 4980,
        "payment_speed": "Direct Account Credit (1 hour)",
        "rating": 4.8,
        "active_weighbridges": 4,
        "active_quality_labs": 2,
        "daily_capacity_quintals": 7500,
        "operating_hours": "06:30 AM - 09:00 PM",
        "contact_phone": "+91-1800-233-5566",
        "is_active": True,
        "congestion_status": "Smooth",
        "facilities": "🌟 Direct Pit Unload (5 Mins), No Gunny Bagging Needed, Moisture Premium"
    },
    {
        "id": "CTR-PVT-003",
        "name": "Reliance Kisan Agro Hub (रिलायंस किसान एग्रो केंद्र)",
        "district": "Karnal",
        "state": "Haryana",
        "location": "Gharaunda Highway Hub, Karnal",
        "latitude": 29.5410,
        "longitude": 76.9710,
        "mandi_type": "PRIVATE_CORPORATE",
        "operator_name": "Reliance Retail Fresh Supply Chain",
        "distance_km": 6.2,
        "wheat_price_qtl": 2500,  # +₹75/Qtl Bonus!
        "mustard_price_qtl": 6080,
        "paddy_price_qtl": 2400,
        "soybean_price_qtl": 4995,
        "payment_speed": "Same-Day Instant NEFT",
        "rating": 4.8,
        "active_weighbridges": 3,
        "active_quality_labs": 2,
        "daily_capacity_quintals": 4500,
        "operating_hours": "07:30 AM - 07:30 PM",
        "contact_phone": "+91-1800-889-9999",
        "is_active": True,
        "congestion_status": "Smooth",
        "facilities": "🌟 +₹75/Qtl Premium, Digital Certified Weight, Farmer Air-Conditioned Lounge"
    },
    {
        "id": "CTR-PVT-004",
        "name": "Cargill Grain Hub (कारगिल ग्रेन टर्मिनल)",
        "district": "Indore",
        "state": "Madhya Pradesh",
        "location": "Pithampur Agro Cluster, Indore",
        "latitude": 22.6100,
        "longitude": 75.6800,
        "mandi_type": "PRIVATE_CORPORATE",
        "operator_name": "Cargill India Pvt. Ltd.",
        "distance_km": 14.5,
        "wheat_price_qtl": 2485,
        "mustard_price_qtl": 6060,
        "paddy_price_qtl": 2380,
        "soybean_price_qtl": 5040, # +₹148/Qtl on Soybean!
        "payment_speed": "Instant IMPS Bank Transfer",
        "rating": 4.7,
        "active_weighbridges": 3,
        "active_quality_labs": 2,
        "daily_capacity_quintals": 5500,
        "operating_hours": "08:00 AM - 07:00 PM",
        "contact_phone": "+91-1800-209-4455",
        "is_active": True,
        "congestion_status": "Smooth",
        "facilities": "🌟 High Quality Protein Premium, Electronic Payment Slip, Zero Deduction"
    }
]

# 5 Procurement Pipeline Stages
STAGES = [
    {
        "step": 1,
        "code": "REGISTERED",
        "title_en": "Slot Booked & Scheduled",
        "title_hi": "स्लॉट बुक और निर्धारित",
        "description": "Token generated. Farmer allocated expected arrival window.",
    },
    {
        "step": 2,
        "code": "GATE_ENTRY",
        "title_en": "Arrived & Gate Checked-In",
        "title_hi": "मंडी में प्रवेश व गेट एंट्री",
        "description": "Vehicle entered Mandi. In active physical queue.",
    },
    {
        "step": 3,
        "code": "WEIGHBRIDGE",
        "title_en": "Gross Weighing Completed",
        "title_hi": "सकल वजन (तौल) संपन्न",
        "description": "Vehicle weighed on certified electronic weighbridge.",
    },
    {
        "step": 4,
        "code": "QUALITY_CHECK",
        "title_en": "Quality & Moisture Tested",
        "title_hi": "गुणवत्ता व नमी जांच संपन्न",
        "description": "Lab tested moisture %, foreign matter, and assigned quality grade.",
    },
    {
        "step": 5,
        "code": "PAYMENT_PROCESSED",
        "title_en": "Procured & Payment Voucher Issued",
        "title_hi": "उपार्जन पूर्ण व भुगतान वाउचर जारी",
        "description": "Net weight calculated, tare weight deducted, DBT payment voucher generated.",
    },
]
