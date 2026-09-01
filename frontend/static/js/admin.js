/**
 * Admin & Ministry Analytics Dashboard
 * Renders live Chart.js visualizations, bottleneck diagnoses, and demo simulation controls
 */

let arrivalChart = null;
let cropChart = null;
let centerLoadChart = null;

async function initAdminDashboard() {
    await loadAdminData();
    await loadNotificationAudit();

    // Auto-refresh summary every 15 seconds
    setInterval(loadAdminData, 15000);
}

async function loadAdminData() {
    try {
        const res = await fetch("/api/admin/overview");
        if (!res.ok) throw new Error("Failed to load admin analytics");
        const data = await res.json();

        renderSummaryKPIs(data.summary);
        renderBottlenecks(data.bottlenecks);
        renderArrivalChart(data.hourly_trends);
        renderCropChart(data.crop_stats);
        renderCenterLoadChart(data.centers);
    } catch (err) {
        console.error("Admin load error:", err);
    }
}

function renderSummaryKPIs(summary) {
    if (!summary) return;
    const elFarmers = document.getElementById("admin-kpi-farmers");
    const elTokens = document.getElementById("admin-kpi-tokens");
    const elTons = document.getElementById("admin-kpi-tons");
    const elDisbursed = document.getElementById("admin-kpi-disbursed");
    const elActive = document.getElementById("admin-kpi-active");

    if (elFarmers) elFarmers.innerText = summary.total_farmers.toLocaleString('en-IN');
    if (elTokens) elTokens.innerText = summary.total_tokens.toLocaleString('en-IN');
    if (elTons) elTons.innerText = `${summary.total_procured_metric_tons.toLocaleString('en-IN')} MT`;
    if (elDisbursed) elDisbursed.innerText = `₹${summary.total_msp_disbursed_crore} Cr`;
    if (elActive) elActive.innerText = summary.active_in_pipeline.toLocaleString('en-IN');
}

function renderBottlenecks(bottlenecks) {
    const container = document.getElementById("bottlenecks-table-body");
    if (!container || !bottlenecks) return;

    container.innerHTML = bottlenecks.map(b => {
        const statusBadge = b.status === "Optimal" 
            ? `<span class="px-2 py-0.5 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800">Optimal</span>`
            : b.status === "Normal"
            ? `<span class="px-2 py-0.5 rounded-full text-xs font-bold bg-blue-100 text-blue-800">Normal</span>`
            : `<span class="px-2 py-0.5 rounded-full text-xs font-bold bg-amber-100 text-amber-800">Needs Attention</span>`;

        return `
            <tr class="border-b border-slate-100 hover:bg-slate-50">
                <td class="py-3 px-4 text-sm font-semibold text-slate-800">${b.stage}</td>
                <td class="py-3 px-4 text-sm font-bold text-slate-900">${b.avg_duration_mins} mins</td>
                <td class="py-3 px-4 text-sm text-slate-500">${b.target_mins} mins</td>
                <td class="py-3 px-4 text-sm">${statusBadge}</td>
            </tr>
        `;
    }).join('');
}

function renderArrivalChart(hourlyData) {
    const ctx = document.getElementById("arrivalThroughputChart");
    if (!ctx || !hourlyData) return;

    const labels = hourlyData.map(h => h.hour);
    const arrivals = hourlyData.map(h => h.arrivals);
    const processed = hourlyData.map(h => h.processed);

    if (arrivalChart) {
        arrivalChart.data.labels = labels;
        arrivalChart.data.datasets[0].data = arrivals;
        arrivalChart.data.datasets[1].data = processed;
        arrivalChart.update();
        return;
    }

    arrivalChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Farmer Arrivals',
                    data: arrivals,
                    borderColor: '#f59e0b',
                    backgroundColor: 'rgba(245, 158, 11, 0.1)',
                    fill: true,
                    tension: 0.4
                },
                {
                    label: 'Procurements Processed',
                    data: processed,
                    borderColor: '#10b981',
                    backgroundColor: 'rgba(16, 185, 129, 0.1)',
                    fill: true,
                    tension: 0.4
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'top' } },
            scales: { y: { beginAtZero: true } }
        }
    });
}

function renderCropChart(cropStats) {
    const ctx = document.getElementById("cropDistributionChart");
    if (!ctx || !cropStats) return;

    const labels = cropStats.map(c => c.crop_name.split(' ')[0]);
    const values = cropStats.map(c => c.total_procured_qtl || c.total_estimated_qtl);

    if (cropChart) {
        cropChart.data.labels = labels;
        cropChart.data.datasets[0].data = values;
        cropChart.update();
        return;
    }

    cropChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                data: values,
                backgroundColor: ['#10b981', '#3b82f6', '#f59e0b', '#8b5cf6', '#ec4899', '#6366f1']
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'bottom' } }
        }
    });
}

function renderCenterLoadChart(centers) {
    const ctx = document.getElementById("centerLoadChart");
    if (!ctx || !centers) return;

    const labels = centers.map(c => c.center_name.split(' ')[0]);
    const waitTimes = centers.map(c => c.avg_wait_mins);

    if (centerLoadChart) {
        centerLoadChart.data.labels = labels;
        centerLoadChart.data.datasets[0].data = waitTimes;
        centerLoadChart.update();
        return;
    }

    centerLoadChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Avg Wait Time (Minutes)',
                data: waitTimes,
                backgroundColor: '#15803d'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: { y: { beginAtZero: true } }
        }
    });
}

async function loadNotificationAudit() {
    try {
        const res = await fetch("/api/admin/notifications");
        if (!res.ok) return;
        const data = await res.json();
        const container = document.getElementById("admin-notifications-stream");
        if (!container) return;

        container.innerHTML = (data.notifications || []).map(n => `
            <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl text-xs space-y-1">
                <div class="flex justify-between items-center text-slate-500">
                    <span class="font-bold text-slate-800">${n.token_id || 'SYSTEM'}</span>
                    <span class="px-1.5 py-0.5 rounded bg-emerald-100 text-emerald-800 font-semibold text-[10px]">${n.channel}</span>
                </div>
                <p class="text-slate-700">${n.message}</p>
                <div class="flex justify-between items-center text-[10px] text-slate-400">
                    <span>${n.farmer_phone}</span>
                    <span>${n.timestamp}</span>
                </div>
            </div>
        `).join('');
    } catch (e) {
        console.warn("Notification load error:", e);
    }
}

// Trigger Live Hackathon Demo Simulation Actions
async function triggerDemoSimulation(action) {
    try {
        showToast(`⚡ Running simulation: ${action}...`, "info");
        const res = await fetch(`/api/admin/simulate?action=${action}`, { method: "POST" });
        const result = await res.json();
        showToast("✅ Simulation event dispatched in real-time!", "success");
        playChime("stage_advance");
        await loadAdminData();
        await loadNotificationAudit();
    } catch (err) {
        showToast("Simulation error: " + err.message, "error");
    }
}

// WebSocket broadcast listener
liveSync.on("TOKEN_UPDATED", () => {
    loadAdminData();
    loadNotificationAudit();
});
