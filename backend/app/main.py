"""
Main Application Entry Point for AnnaSetu (अन्नसेतु)
FastAPI Full-Stack Platform with WebSockets & Jinja2 Templates
"""

import json
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from backend.app.database import init_db, fetch_all, fetch_one
from backend.app.websocket_manager import ws_manager
from backend.app.routers import farmers, staff, centers, admin, voice_ivr, earnings, ai_advisor
from backend.app.config import BASE_DIR, MSP_RATES, STAGES


# ============================================================
# FRONTEND PATHS
# ============================================================

FRONTEND_DIR = BASE_DIR / "frontend"
TEMPLATES_DIR = FRONTEND_DIR / "templates"
STATIC_DIR = FRONTEND_DIR / "static"


# ============================================================
# APPLICATION LIFESPAN
# ============================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database tables and sample data
    init_db()
    yield


# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="AnnaSetu | Smart Farmer Procurement Tracking & Scheduling Platform",
    description=(
        "SIH 2026 Problem Statement SIH26032 | "
        "Ministry of Consumer Affairs, Food & Public Distribution"
    ),
    version="1.0.0",
    lifespan=lifespan
)


# ============================================================
# CORS MIDDLEWARE
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# STATIC FILES & JINJA2 TEMPLATES
# ============================================================

app.mount(
    "/static",
    StaticFiles(directory=str(STATIC_DIR)),
    name="static"
)

templates = Jinja2Templates(
    directory=str(TEMPLATES_DIR)
)


# ============================================================
# API ROUTERS
# ============================================================

app.include_router(farmers.router)
app.include_router(staff.router)
app.include_router(centers.router)
app.include_router(admin.router)
app.include_router(voice_ivr.router)
app.include_router(earnings.router)
app.include_router(ai_advisor.router)


# ============================================================
# WEBSOCKET ENDPOINT
# ============================================================

@app.websocket("/ws/queue")
async def websocket_queue_endpoint(websocket: WebSocket):
    await ws_manager.connect(websocket)

    try:
        while True:
            data_text = await websocket.receive_text()

            try:
                msg = json.loads(data_text)
                action = msg.get("action")

                if action == "subscribe_token":
                    ws_manager.subscribe_token(
                        msg.get("token_id"),
                        websocket
                    )

                elif action == "subscribe_center":
                    ws_manager.subscribe_center(
                        msg.get("center_id"),
                        websocket
                    )

            except Exception:
                pass

    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)


# ============================================================
# UI / TEMPLATE ROUTES
# ============================================================


# -------------------------
# HOME PAGE
# -------------------------

@app.get("/", response_class=HTMLResponse)
async def index_page(request: Request):

    centers_list = fetch_all(
        "SELECT * FROM centers WHERE is_active = 1"
    )

    recent_tokens = fetch_all("""
        SELECT
            t.*,
            f.name AS farmer_name,
            c.name AS center_name
        FROM tokens t
        JOIN farmers f ON t.farmer_id = f.id
        JOIN centers c ON t.center_id = c.id
        ORDER BY t.booking_time DESC
        LIMIT 6
    """)

    featured_token = fetch_one("""
        SELECT t.*, f.name AS farmer_name, f.phone AS farmer_phone, c.name AS center_name
        FROM tokens t
        JOIN farmers f ON t.farmer_id = f.id
        JOIN centers c ON t.center_id = c.id
        WHERE t.stage != 'PAYMENT_PROCESSED'
        ORDER BY t.queue_number ASC
        LIMIT 1
    """) or (recent_tokens[0] if recent_tokens else None)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "centers": centers_list,
            "recent_tokens": recent_tokens,
            "featured_token": featured_token,
            "stages": STAGES,
            "msp_rates": MSP_RATES,
            "crops": MSP_RATES
        }
    )


# -------------------------
# FARMER BOOKING PAGE
# -------------------------

@app.get("/book", response_class=HTMLResponse)
async def book_page(request: Request):

    centers_list = fetch_all(
        "SELECT * FROM centers WHERE is_active = 1"
    )

    return templates.TemplateResponse(
        request=request,
        name="farmer_book.html",
        context={
            "request": request,
            "centers": centers_list,
            "crops": MSP_RATES
        }
    )


# -------------------------
# FARMER TRACKER
# -------------------------

@app.get("/track", response_class=HTMLResponse)
@app.get("/track/{token_id}", response_class=HTMLResponse)
async def track_page(
    request: Request,
    token_id: str = None
):

    # If no token is provided,
    # use the first active token.
    if not token_id:

        active = fetch_one(
            """
            SELECT id
            FROM tokens
            WHERE stage != 'PAYMENT_PROCESSED'
            ORDER BY queue_number ASC
            LIMIT 1
            """
        )

        token_id = (
            active["id"]
            if active
            else "AS-26-WHT-101"
        )

    return templates.TemplateResponse(
        request=request,
        name="farmer_track.html",
        context={
            "request": request,
            "initial_token_id": token_id,
            "stages": STAGES
        }
    )


# -------------------------
# MANDI CENTERS
# -------------------------

@app.get("/centers", response_class=HTMLResponse)
async def centers_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="centers_compare.html",
        context={
            "request": request
        }
    )


# -------------------------
# STAFF DASHBOARD
# -------------------------

@app.get("/staff", response_class=HTMLResponse)
@app.get("/staf", response_class=HTMLResponse)
async def staff_page(request: Request):

    centers_list = fetch_all(
        "SELECT * FROM centers WHERE is_active = 1"
    )

    return templates.TemplateResponse(
        request=request,
        name="staff_dashboard.html",
        context={
            "request": request,
            "centers": centers_list,
            "stages": STAGES
        }
    )


# -------------------------
# ADMIN DASHBOARD
# -------------------------

@app.get("/admin", response_class=HTMLResponse)
async def admin_page(request: Request):

    centers_list = fetch_all(
        "SELECT * FROM centers WHERE is_active = 1"
    )

    return templates.TemplateResponse(
        request=request,
        name="admin_dashboard.html",
        context={
            "request": request,
            "centers": centers_list
        }
    )


# -------------------------
# VOICE / IVR PAGE
# -------------------------

@app.get("/ivr", response_class=HTMLResponse)
async def ivr_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="ivr_demo.html",
        context={
            "request": request
        }
    )


# -------------------------
# FARMER EARNINGS & SALES PASSBOOK
# -------------------------

@app.get("/earnings", response_class=HTMLResponse)
@app.get("/sales", response_class=HTMLResponse)
async def earnings_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="farmer_earnings.html",
        context={
            "request": request,
            "crops": MSP_RATES,
            "msp_rates": MSP_RATES
        }
    )


# -------------------------
# FREE KISAN AI MANDI PRICE ADVISOR
# -------------------------

@app.get("/ai-advisor", response_class=HTMLResponse)
async def ai_advisor_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="ai_advisor.html",
        context={
            "request": request,
            "crops": MSP_RATES,
            "msp_rates": MSP_RATES
        }
    )