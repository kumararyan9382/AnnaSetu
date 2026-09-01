import sys
import os
import socket
import subprocess
import time

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def ensure_port_available(port=8000):
    """Auto-detects and frees port if occupied by previous python instance"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) == 0:
                print(f"⚠️ Port {port} is occupied by previous server. Freeing port...")
                if sys.platform == "win32":
                    subprocess.run([
                        "powershell", "-Command", 
                        f"Get-NetTCPConnection -LocalPort {port} -ErrorAction SilentlyContinue | ForEach-Object {{ Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }}"
                    ], capture_output=True)
                time.sleep(1.2)
    except Exception:
        pass

import uvicorn

if __name__ == "__main__":
    ensure_port_available(8000)

    print("=" * 65)
    print("🌾 Starting AnnaSetu (अन्नसेतु) Full-Stack Platform...")
    print("   SIH 2026 Problem Statement: SIH26032")
    print("   Ministry of Consumer Affairs, Food & Public Distribution")
    print("=" * 65)
    print("🚀 Server running at: http://127.0.0.1:8000")
    print("   - Farmer Portal:       http://127.0.0.1:8000/")
    print("   - Slot Booking:        http://127.0.0.1:8000/book")
    print("   - Live Token Tracker:  http://127.0.0.1:8000/track")
    print("   - Mandi Centers Map:   http://127.0.0.1:8000/centers")
    print("   - Staff Operator Board:http://127.0.0.1:8000/staff")
    print("   - Ministry Admin Hub:  http://127.0.0.1:8000/admin")
    print("   - Voice / IVR Sim:     http://127.0.0.1:8000/ivr")
    print("   - OpenAPI Docs:        http://127.0.0.1:8000/docs")
    print("=" * 65)

    uvicorn.run("backend.app.main:app", host="127.0.0.1", port=8000, reload=False)

