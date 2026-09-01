# AnnaSetu (अन्नसेतु) Technical Architecture

## 1. System Architecture Overview

```mermaid
graph TD
    subgraph Client Tier
        A1[Farmer Mobile Web App]
        A2[Mandi Staff Operator Command Board]
        A3[District / Ministry Analytics Dashboard]
        A4[Interactive Voice & IVR Console]
    end

    subgraph Transport & Real-Time Gateway
        B1[HTTP / REST Endpoints - JSON API]
        B2[WebSocket Stream /ws/queue - Bidirectional Event Bus]
    end

    subgraph Backend Services Fast-API
        C1[Queue & Wait Time Heuristic Engine]
        C2[Token & Stage State Machine]
        C3[Notification & SMS Simulator]
        C4[District Analytics & Bottleneck Analyzer]
        C5[Multi-Center Load Balancer]
    end

    subgraph Persistence & Audit
        D1[(SQLite Database)]
        D2[Stage Transition Audit Logs]
        D3[Outbound Notification Logs]
    end

    A1 <-->|REST & WS| B1 & B2
    A2 <-->|REST & WS| B1 & B2
    A3 <-->|REST & WS| B1 & B2
    A4 <-->|REST & Speech| B1

    B1 & B2 --> C1 & C2 & C3 & C4 & C5
    C1 & C2 & C3 & C4 & C5 --> D1 & D2 & D3
```

---

## 2. Queue Wait-Time Estimation Formulation

Given:
- $N_{ahead}$: Number of vehicles ahead in queue for the center.
- $W_{active}$: Number of active weighbridge lanes at the center.
- $L_{active}$: Number of active quality testing labs at the center.
- $T_{weigh}^{base}$: Base weigh time for the selected crop (minutes).
- $F_{vehicle}$: Vehicle impact multiplier (e.g. 1.0 for standard tractor, 1.6 for 2-trolley tractor, 2.2 for commercial truck).
- $T_{quality}^{base}$: Base quality inspection and moisture test duration (minutes).
- $B_{transit}$: Buffer time for vehicle maneuvering and repositioning ($\approx 3$ minutes).

The effective service rate per vehicle $\mu$ is constrained by the bottleneck stage:
$$\mu_{stage} = \max\left(\frac{T_{weigh}^{base} \times F_{vehicle}}{W_{active}}, \frac{T_{quality}^{base}}{L_{active}}\right)$$

The dynamic estimated wait time $T_{wait}$ is computed as:
$$T_{wait} = \lceil N_{ahead} \times (\mu_{stage} + B_{transit}) \rceil \text{ minutes}$$

---

## 3. Mandi Load-Balancing Optimization Formula

For a farmer located at coordinate $(Lat_f, Lon_f)$, candidate procurement centers $C_i$ are evaluated on total time investment:

$$T_{total}(C_i) = T_{travel}(C_i) + T_{wait}(C_i)$$

Where:
$$T_{travel}(C_i) = \frac{\text{HaversineDistance}((Lat_f, Lon_f), (Lat_{C_i}, Lon_{C_i}))}{V_{avg\_tractor}} \times 60$$

The center $C^*$ with $\min_{i} T_{total}(C_i)$ is recommended to the farmer, preventing localized traffic concentration and distributing harvest flow across the district.
