# AnnaSetu (अन्नसेतु) — Smart Farmer Procurement Tracking & Scheduling Platform

**Smart India Hackathon (SIH 2026)**  
**Problem Statement ID:** SIH26032  
**Theme:** Smart Automation | **Track:** Software  
**Sponsoring Ministry:** Ministry of Consumer Affairs, Food & Public Distribution  

---

## 🌟 Key Features

1. **Farmer Slot Booking**:
   - Crop selection with official 2025–26 MSP rates (Wheat, Paddy, Mustard, Chana, Maize, Soybean).
   - Dynamic payout calculation and vehicle selection.
   - Guaranteed arrival token generation with dynamic queue wait-time estimation.

2. **Live 5-Stage Procurement Tracker**:
   - Real-time pipeline: *1. Registered → 2. Gate Entry → 3. Weighbridge Scale → 4. Quality Lab Testing → 5. DBT Direct Payment*.
   - Live WebSocket sync without page reloads.
   - Verified digital DBT e-Receipt / Voucher with official watermark.

3. **Mandi Staff Operator Command Center**:
   - High-throughput Kanban queue board.
   - Weighbridge gross and tare weight entry with automatic net calculation.
   - Quality lab grading (moisture %, foreign matter %, Grade A/B/C).
   - Audio token call chimes and automated SMS dispatch simulation.

4. **Multi-Center Load Balancer**:
   - Live queue length and congestion indicators across neighboring mandis.
   - Recommends the optimal mandi based on shortest travel + processing time.

5. **District & Ministry Analytics Hub**:
   - Macro KPIs: Total farmers, metric tons procured, total MSP disbursed (in ₹ Crore).
   - Hourly arrival curve vs. processing throughput.
   - Stage bottleneck diagnosis against SLA targets.
   - Live hackathon demo simulation controller.

6. **Inclusive Accessibility**:
   - 5 Indic Languages: **Hindi (हिन्दी), English, Punjabi (ਪੰਜਾਬੀ), Marathi (मराठी), Telugu (తెలుగు)**.
   - Voice assistant with Web Speech recognition and text-to-speech spoken status.
   - Simulated toll-free phone IVR (1800-180-2626) with interactive dialpad.

---

## 🚀 Quick Start Guide

### 1. Requirements
- Python 3.10+ (Dependencies: `fastapi`, `uvicorn`, `websockets`, `jinja2`, `pydantic`)

### 2. Run the Platform
```bash
python run.py
```

### 3. Open in Browser
- **Portal Landing Page**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Farmer Slot Booking**: [http://127.0.0.1:8000/book](http://127.0.0.1:8000/book)
- **Live 5-Stage Tracker**: [http://127.0.0.1:8000/track](http://127.0.0.1:8000/track)
- **Multi-Mandi Comparison**: [http://127.0.0.1:8000/centers](http://127.0.0.1:8000/centers)
- **Mandi Staff Dashboard**: [http://127.0.0.1:8000/staff](http://127.0.0.1:8000/staff)
- **Ministry Admin Hub**: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
- **Voice & IVR Simulator**: [http://127.0.0.1:8000/ivr](http://127.0.0.1:8000/ivr)
- **Interactive Swagger API Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📂 Project Structure

```
annasetu/
├── backend/
│   ├── app/
│   │   ├── config.py             # MSP rates, centers, vehicle factors
│   │   ├── database.py           # SQLite schema, thread-safe session & seed data
│   │   ├── models.py             # Pydantic validation schemas
│   │   ├── websocket_manager.py  # Real-time WebSocket event broadcaster
│   │   ├── services/
│   │   │   ├── queue_service.py  # Wait-time estimation & load balancer
│   │   │   ├── notification_service.py # SMS / in-app dispatcher
│   │   │   └── analytics_service.py # District throughput & bottleneck stats
│   │   ├── routers/
│   │   │   ├── farmers.py        # Slot booking, token tracker, crop catalog
│   │   │   ├── staff.py          # Operator queue actions, weights, quality
│   │   │   ├── centers.py        # Multi-mandi live comparison
│   │   │   ├── admin.py          # Ministry analytics & simulation triggers
│   │   │   └── voice_ivr.py      # Spoken status & IVR lookups
│   │   └── main.py               # FastAPI application & static mounts
├── frontend/
│   ├── static/
│   │   ├── css/styles.css        # GovTech theme, stage pulses, print layouts
│   │   └── js/
│   │       ├── app.js            # i18n localization (5 languages) & audio synthesizers
│   │       ├── websocket.js      # Resilient WebSocket client
│   │       ├── farmer.js         # Booking calculations & live tracker
│   │       ├── staff.js          # Operator pipeline & stage modals
│   │       ├── admin.js          # Chart.js analytics & simulation handlers
│   │       └── voice_assistant.js # Web Speech recognition & TTS
│   └── templates/
│       ├── base.html             # Common navbar, language selector & indicator
│       ├── index.html            # Landing page & live ticker
│       ├── farmer_book.html      # Farmer booking wizard
│       ├── farmer_track.html     # Live 5-stage tracker & e-receipt
│       ├── centers_compare.html  # Multi-center load comparison
│       ├── staff_dashboard.html  # Mandi operator console
│       ├── admin_dashboard.html  # Ministry analytics dashboard
│       └── ivr_demo.html         # Voice / IVR phone simulator
├── docs/
│   ├── SIH_PRESENTATION_GUIDE.md # 3-minute pitch script, slide outline, judge Q&A
│   └── ARCHITECTURE.md           # Architecture diagrams & algorithmic formulations
├── run.py                        # One-click startup script
└── requirements.txt
```
