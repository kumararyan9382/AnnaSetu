"""
WebSocket Connection Manager for Real-Time Queue & Stage Sync
"""

import json
from typing import List, Dict, Set
from fastapi import WebSocket

class WebSocketManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.token_subscribers: Dict[str, Set[WebSocket]] = {}
        self.center_subscribers: Dict[str, Set[WebSocket]] = {}

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
        
        # Clean up subscriptions
        for subscribers in self.token_subscribers.values():
            subscribers.discard(websocket)
        for subscribers in self.center_subscribers.values():
            subscribers.discard(websocket)

    def subscribe_token(self, token_id: str, websocket: WebSocket):
        if token_id not in self.token_subscribers:
            self.token_subscribers[token_id] = set()
        self.token_subscribers[token_id].add(websocket)

    def subscribe_center(self, center_id: str, websocket: WebSocket):
        if center_id not in self.center_subscribers:
            self.center_subscribers[center_id] = set()
        self.center_subscribers[center_id].add(websocket)

    async def broadcast_all(self, event_type: str, payload: dict):
        message = json.dumps({"event": event_type, "data": payload})
        dead_connections = []
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except Exception:
                dead_connections.append(connection)
        
        for dead in dead_connections:
            self.disconnect(dead)

    async def broadcast_token_update(self, token_id: str, payload: dict):
        # Broadcast globally to operator dashboards and specifically to token subscribers
        await self.broadcast_all("TOKEN_UPDATED", {"token_id": token_id, "token": payload})

    async def broadcast_center_update(self, center_id: str, payload: dict):
        await self.broadcast_all("CENTER_UPDATED", {"center_id": center_id, "center": payload})

ws_manager = WebSocketManager()
