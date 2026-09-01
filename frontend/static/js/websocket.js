/**
 * AnnaSetu Real-Time WebSocket Client
 * Connects to ws://{host}/ws/queue with auto-reconnection and event dispatching
 */

class LiveSyncClient {
    constructor() {
        this.ws = null;
        this.reconnectAttempts = 0;
        this.maxReconnectAttempts = 20;
        this.reconnectInterval = 2000;
        this.listeners = new Map(); // event -> array of callbacks
        this.subscribedTokenId = null;
        this.subscribedCenterId = null;

        this.init();
    }

    init() {
        const protocol = window.location.protocol === "https:" ? "wss:" : "ws:";
        const wsUrl = `${protocol}//${window.location.host}/ws/queue`;

        try {
            this.ws = new WebSocket(wsUrl);

            this.ws.onopen = () => {
                this.reconnectAttempts = 0;
                this.updateConnectionIndicator(true);
                
                // Re-subscribe if we had previous subscriptions
                if (this.subscribedTokenId) {
                    this.subscribeToken(this.subscribedTokenId);
                }
                if (this.subscribedCenterId) {
                    this.subscribeCenter(this.subscribedCenterId);
                }
            };

            this.ws.onmessage = (event) => {
                try {
                    const message = JSON.parse(event.data);
                    const eventType = message.event;
                    const payload = message.data;

                    if (this.listeners.has(eventType)) {
                        this.listeners.get(eventType).forEach(callback => callback(payload));
                    }
                    if (this.listeners.has("*")) {
                        this.listeners.get("*").forEach(callback => callback(eventType, payload));
                    }
                } catch (err) {
                    console.error("Error parsing WebSocket payload:", err);
                }
            };

            this.ws.onclose = () => {
                this.updateConnectionIndicator(false);
                this.scheduleReconnect();
            };

            this.ws.onerror = (err) => {
                console.warn("WebSocket error:", err);
                this.ws.close();
            };
        } catch (e) {
            console.error("WebSocket init failed:", e);
            this.scheduleReconnect();
        }
    }

    scheduleReconnect() {
        if (this.reconnectAttempts < this.maxReconnectAttempts) {
            this.reconnectAttempts++;
            setTimeout(() => this.init(), this.reconnectInterval);
        }
    }

    subscribeToken(tokenId) {
        this.subscribedTokenId = tokenId;
        if (this.ws && this.ws.readyState === WebSocket.OPEN) {
            this.ws.send(JSON.stringify({ action: "subscribe_token", token_id: tokenId }));
        }
    }

    subscribeCenter(centerId) {
        this.subscribedCenterId = centerId;
        if (this.ws && this.ws.readyState === WebSocket.OPEN) {
            this.ws.send(JSON.stringify({ action: "subscribe_center", center_id: centerId }));
        }
    }

    on(eventType, callback) {
        if (!this.listeners.has(eventType)) {
            this.listeners.set(eventType, []);
        }
        this.listeners.get(eventType).push(callback);
    }

    updateConnectionIndicator(connected) {
        const dot = document.getElementById("ws-status-dot");
        const text = document.getElementById("ws-status-text");
        if (dot && text) {
            if (connected) {
                dot.className = "w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse";
                text.innerText = "Live";
                text.className = "text-xs font-semibold text-emerald-700";
            } else {
                dot.className = "w-2.5 h-2.5 rounded-full bg-amber-500";
                text.innerText = "Syncing...";
                text.className = "text-xs font-semibold text-amber-700";
            }
        }
    }
}

// Global live sync instance
const liveSync = new LiveSyncClient();
