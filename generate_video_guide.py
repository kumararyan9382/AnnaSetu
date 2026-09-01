"""
Generate an Interactive Step-by-Step Animated Video Guide Player for AnnaSetu
Simulates animated screen recording, cursor clicks, split-screen sync, and plays synced Hindi audio.
"""

import os

OUTPUT_DIR = r"C:\Users\kumar\OneDrive\Documents\Aryan\Hackathon"
HTML_GUIDE_PATH = os.path.join(OUTPUT_DIR, "AnnaSetu_Step_by_Step_Video_Guide.html")

html_content = """<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AnnaSetu — Complete Step-by-Step Video Guide</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Noto+Sans+Devanagari:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Plus Jakarta Sans', 'Noto Sans Devanagari', sans-serif; }
        
        /* Simulated Animated Cursor */
        .cursor-pointer-sim {
            position: absolute;
            width: 24px;
            height: 24px;
            background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23ef4444' viewBox='0 0 24 24'%3E%3Cpath d='M3 3l7 18 3-7 7-3L3 3z' stroke='%23ffffff' stroke-width='1.5'/%3E%3C/svg%3E") no-repeat center;
            background-size: contain;
            pointer-events: none;
            z-index: 50;
            transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .click-pulse {
            position: absolute;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: rgba(239, 68, 68, 0.4);
            border: 2px solid #ef4444;
            transform: translate(-50%, -50%) scale(0);
            animation: pulse-click 0.6s ease-out;
            pointer-events: none;
            z-index: 49;
        }

        @keyframes pulse-click {
            0% { transform: translate(-50%, -50%) scale(0.2); opacity: 1; }
            100% { transform: translate(-50%, -50%) scale(1.5); opacity: 0; }
        }

        .active-tab {
            background-color: #ffffff !important;
            color: #0f172a !important;
            border-bottom: 2px solid #10b981;
        }

        .glow-box {
            box-shadow: 0 0 0 4px rgba(16, 185, 129, 0.4);
            border-color: #10b981 !important;
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col justify-between select-none">

    <!-- Top Navigation Header -->
    <header class="border-b border-slate-800 bg-slate-900 px-6 py-3 flex items-center justify-between sticky top-0 z-50">
        <div class="flex items-center space-x-3">
            <span class="text-2xl">🌾</span>
            <div>
                <h1 class="text-sm font-black text-white">AnnaSetu — Step-by-Step Visual Video Guide</h1>
                <p class="text-[11px] text-emerald-400">SIH 2026 Problem Statement SIH26032 • Animated Live Demonstration Walkthrough</p>
            </div>
        </div>

        <div class="flex items-center space-x-3">
            <span class="px-3 py-1 bg-emerald-900/60 border border-emerald-500/40 text-emerald-300 rounded-full text-xs font-bold flex items-center space-x-1.5">
                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                <span>ऑटोमैटिक हिंदी वॉइसओवर के साथ</span>
            </span>
        </div>
    </header>

    <!-- Main Content Area -->
    <main class="max-w-7xl mx-auto px-4 py-6 grid grid-cols-1 lg:grid-cols-4 gap-6 w-full flex-grow items-start">
        
        <!-- Video Screen Viewport (Left 3 Columns) -->
        <div class="lg:col-span-3 space-y-4">
            
            <!-- Simulated Browser Frame -->
            <div class="bg-slate-900 rounded-3xl border-2 border-slate-700 shadow-2xl overflow-hidden relative">
                
                <!-- Browser Titlebar & Tabs -->
                <div class="bg-slate-800 px-4 py-2 border-b border-slate-700 flex items-center justify-between">
                    <div class="flex items-center space-x-2">
                        <div class="w-3 h-3 rounded-full bg-rose-500"></div>
                        <div class="w-3 h-3 rounded-full bg-amber-500"></div>
                        <div class="w-3 h-3 rounded-full bg-emerald-500"></div>
                    </div>

                    <!-- Browser Tabs Simulation -->
                    <div class="flex space-x-1 overflow-x-auto text-[11px] font-bold">
                        <div id="sim-tab-1" class="px-3 py-1.5 rounded-t-lg bg-slate-700 text-slate-300 active-tab transition-all">1. Home & Booking</div>
                        <div id="sim-tab-2" class="px-3 py-1.5 rounded-t-lg bg-slate-700 text-slate-300 transition-all">2. Mandi Tracker</div>
                        <div id="sim-tab-3" class="px-3 py-1.5 rounded-t-lg bg-slate-700 text-slate-300 transition-all">3. Live Tracker</div>
                        <div id="sim-tab-4" class="px-3 py-1.5 rounded-t-lg bg-slate-700 text-slate-300 transition-all">4. Staff Board</div>
                        <div id="sim-tab-5" class="px-3 py-1.5 rounded-t-lg bg-slate-700 text-slate-300 transition-all">5. Ministry Admin</div>
                        <div id="sim-tab-6" class="px-3 py-1.5 rounded-t-lg bg-slate-700 text-slate-300 transition-all">6. Voice/IVR</div>
                    </div>

                    <div id="sim-url-bar" class="text-[10px] font-mono text-slate-400 bg-slate-900 px-3 py-1 rounded-md border border-slate-700">
                        http://127.0.0.1:8000/
                    </div>
                </div>

                <!-- Simulated Video Screen Canvas (Interactive Visual State) -->
                <div id="video-screen-canvas" class="relative min-h-[460px] bg-slate-100 text-slate-900 p-6 overflow-hidden flex flex-col justify-between">
                    
                    <!-- Simulated Cursor -->
                    <div id="sim-cursor" class="cursor-pointer-sim" style="top: 50%; left: 50%;"></div>
                    <div id="click-effect-container"></div>

                    <!-- Screen State 1: Terminal Startup -->
                    <div id="screen-state-1" class="space-y-4">
                        <div class="bg-slate-900 text-emerald-400 p-6 rounded-2xl font-mono text-xs shadow-inner space-y-2 border border-slate-800">
                            <p class="text-slate-500">Windows PowerShell - Step 1: Start Backend Server</p>
                            <p class="text-white">PS C:\Users\kumar> <span class="text-amber-400">cd C:\Users\kumar\.gemini\antigravity\scratch\annasetu</span></p>
                            <p class="text-white">PS C:\Users\kumar\...\annasetu> <span class="text-emerald-400 font-bold">python run.py</span></p>
                            <div class="pt-2 text-slate-300 border-t border-slate-800 space-y-1">
                                <p class="text-emerald-400 font-bold">🌾 Starting AnnaSetu (अन्नसेतु) Full-Stack Platform...</p>
                                <p>🚀 Server running at: http://127.0.0.1:8000</p>
                                <p class="text-slate-500">✅ 100% Localhost Execution (Works completely offline with 0% venue Wi-Fi lag)</p>
                            </div>
                        </div>
                        <div class="p-4 bg-emerald-50 border border-emerald-300 rounded-2xl text-emerald-900 text-xs">
                            💡 <b>निर्देश:</b> सबसे पहले अपने कंप्यूटर पर टर्मिनल खोलकर <code class="bg-emerald-200 px-1 py-0.5 rounded font-bold">python run.py</code> चलाएं।
                        </div>
                    </div>

                    <!-- Screen State 2: Front Page Farmer Booking Form -->
                    <div id="screen-state-2" class="space-y-4 hidden">
                        <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow space-y-4">
                            <div class="flex justify-between items-center border-b pb-2">
                                <h3 class="font-black text-sm text-slate-900">🌾 Fill Farmer Details & Schedule Slot</h3>
                                <span class="text-xs px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 font-bold">Live Booking</span>
                            </div>

                            <div class="grid grid-cols-2 gap-3 text-xs">
                                <div>
                                    <label class="font-bold text-slate-600 block mb-0.5">Farmer Name:</label>
                                    <input id="demo-name" type="text" class="w-full p-2 border rounded-lg bg-slate-50 font-bold" value="Harishchandra Verma" readonly />
                                </div>
                                <div>
                                    <label class="font-bold text-slate-600 block mb-0.5">Crop Produce:</label>
                                    <input id="demo-crop" type="text" class="w-full p-2 border rounded-lg bg-slate-50 font-bold text-emerald-800" value="Wheat (गेहूं) — ₹2,425/Qtl" readonly />
                                </div>
                                <div>
                                    <label class="font-bold text-slate-600 block mb-0.5">Quantity (Quintals):</label>
                                    <input id="demo-qty" type="text" class="w-full p-2 border rounded-lg bg-slate-50 font-bold" value="50.0 Qtls" readonly />
                                </div>
                                <div>
                                    <label class="font-bold text-slate-600 block mb-0.5">Procurement Mandi:</label>
                                    <input id="demo-mandi" type="text" class="w-full p-2 border rounded-lg bg-slate-50 font-bold" value="Karnal Main Anaj Mandi" readonly />
                                </div>
                            </div>

                            <!-- Live MSP calculation box -->
                            <div id="demo-payout-box" class="p-3 bg-emerald-50 border border-emerald-300 rounded-xl flex justify-between items-center">
                                <span class="text-xs text-emerald-900 font-bold">Guaranteed MSP Payout:</span>
                                <span class="text-xl font-black text-emerald-800">₹1,21,250</span>
                            </div>

                            <div class="text-right">
                                <button id="demo-book-btn" class="px-6 py-2.5 bg-emerald-600 text-white rounded-xl font-bold text-xs shadow">
                                    ✨ Confirm & Generate Token
                                </button>
                            </div>
                        </div>
                    </div>

                    <!-- Screen State 3: Side-by-Side Two-Window Live Sync -->
                    <div id="screen-state-3" class="space-y-4 hidden">
                        <div class="grid grid-cols-2 gap-4">
                            <!-- Left: Farmer Live Tracker -->
                            <div class="bg-white p-4 rounded-2xl border-2 border-emerald-500 shadow space-y-3">
                                <div class="flex justify-between items-center border-b pb-1.5 text-xs">
                                    <span class="font-mono font-bold text-emerald-800">Token: AS-26-WHT-101</span>
                                    <span id="demo-farmer-stage-badge" class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-bold text-[10px]">1. Scheduled</span>
                                </div>
                                <div class="text-xs space-y-1">
                                    <p class="font-bold text-slate-800">Farmer: Rajeshwar Singh</p>
                                    <p class="text-slate-500 text-[11px]">Wheat (50 Qtls) • Karnal Mandi</p>
                                </div>
                                <div class="bg-slate-50 p-2 rounded-xl text-center">
                                    <p class="text-[10px] text-slate-400 uppercase font-bold">Est. Wait Time</p>
                                    <p id="demo-wait-text" class="text-lg font-black text-emerald-700">18 Mins</p>
                                </div>
                                <div id="demo-receipt-box" class="p-2 bg-emerald-50 border border-dashed border-emerald-300 rounded-xl text-[10px] text-emerald-900 hidden space-y-0.5">
                                    <p class="font-bold">✅ Payment Voucher Generated</p>
                                    <p>Net: 50.0 Qtls | Payout: ₹1,21,250</p>
                                    <p class="font-mono text-[9px] text-slate-500">Ref: DBT-2026-WHT-984128</p>
                                </div>
                            </div>

                            <!-- Right: Staff Operator Board -->
                            <div class="bg-slate-900 text-white p-4 rounded-2xl border-2 border-slate-700 shadow space-y-3">
                                <div class="flex justify-between items-center border-b border-slate-700 pb-1.5 text-xs">
                                    <span class="font-bold text-amber-400">Mandi Operator Board</span>
                                    <span class="text-[10px] text-slate-400">Queue #1</span>
                                </div>
                                <div class="text-xs space-y-1">
                                    <p class="font-bold text-slate-200">Action Step:</p>
                                    <p id="demo-staff-instruction" class="text-emerald-400 font-semibold text-[11px]">Click 'Check-in Gate Entry'</p>
                                </div>
                                <button id="demo-staff-action-btn" class="w-full py-2 bg-emerald-600 hover:bg-emerald-500 text-white rounded-xl text-xs font-bold shadow">
                                    Advance Stage &rarr;
                                </button>
                            </div>
                        </div>
                    </div>

                    <!-- Screen State 4: Mandi Tracker & Voice / IVR -->
                    <div id="screen-state-4" class="space-y-4 hidden">
                        <div class="grid grid-cols-2 gap-4">
                            <!-- Mandi Comparison Card -->
                            <div class="bg-emerald-900 text-white p-4 rounded-2xl space-y-2">
                                <span class="px-2 py-0.5 rounded bg-amber-400 text-slate-950 font-bold text-[10px]">🌟 SYSTEM RECOMMENDED</span>
                                <h4 class="font-black text-xs">Karnal Main Anaj Mandi</h4>
                                <p class="text-[11px] text-emerald-200">Est. Wait: 12 Mins | Travel: 0 Mins (0 km)</p>
                                <p class="text-[10px] text-emerald-300">Heuristic calculates Travel + Queue delay to load-balance traffic.</p>
                            </div>

                            <!-- IVR Voice Phone Demo -->
                            <div class="bg-slate-900 text-white p-4 rounded-2xl space-y-2 border border-slate-700">
                                <div class="flex justify-between items-center text-[10px]">
                                    <span class="text-emerald-400">Toll-Free: 1800-180-2626</span>
                                    <span class="px-1.5 py-0.5 rounded bg-slate-800 text-slate-300">हिन्दी / English</span>
                                </div>
                                <div class="p-2 bg-slate-800 rounded-xl text-center">
                                    <span class="text-lg">🎙️ 📞</span>
                                    <p class="text-[11px] text-emerald-300 font-bold mt-1">"नमस्ते! आपका टोकन क्वालिटी टेस्टिंग स्टेज में है..."</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Screen State 5: Ministry Admin Hub -->
                    <div id="screen-state-5" class="space-y-4 hidden">
                        <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow space-y-3">
                            <div class="flex justify-between items-center border-b pb-2">
                                <h3 class="font-black text-xs text-slate-900">📊 District & Ministry Oversight Dashboard</h3>
                                <span class="text-xs text-purple-700 font-bold bg-purple-100 px-2 py-0.5 rounded-full">Live Analytics</span>
                            </div>
                            <div class="grid grid-cols-3 gap-2 text-center text-xs">
                                <div class="bg-slate-50 p-2.5 rounded-xl">
                                    <p class="text-slate-400 text-[10px]">Total Procured</p>
                                    <p class="text-base font-black text-emerald-700">20.2 MT</p>
                                </div>
                                <div class="bg-slate-50 p-2.5 rounded-xl">
                                    <p class="text-slate-400 text-[10px]">MSP Disbursed</p>
                                    <p class="text-base font-black text-purple-700">₹0.0618 Cr</p>
                                </div>
                                <div class="bg-slate-50 p-2.5 rounded-xl">
                                    <p class="text-slate-400 text-[10px]">Active in Pipeline</p>
                                    <p class="text-base font-black text-amber-600">6 Vehicles</p>
                                </div>
                            </div>
                            <div class="p-2 bg-slate-100 rounded-xl text-center text-xs text-slate-600 font-medium">
                                Bottleneck Diagnosis: Weighbridge (8m) | Quality Lab (14m) | DBT Clearance (4m)
                            </div>
                        </div>
                    </div>

                </div>

                <!-- Video Timeline Controls -->
                <div class="bg-slate-900 p-4 border-t border-slate-800 flex flex-col space-y-3">
                    
                    <!-- Progress Bar -->
                    <div class="w-full bg-slate-800 rounded-full h-2 cursor-pointer overflow-hidden">
                        <div id="video-progress-bar" class="bg-emerald-500 h-2 rounded-full transition-all duration-300" style="width: 20%;"></div>
                    </div>

                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-3">
                            <button id="play-pause-btn" onclick="toggleAutoPlay()" class="px-5 py-2 bg-emerald-600 hover:bg-emerald-500 text-white rounded-xl text-xs font-black shadow transition-all flex items-center space-x-1.5">
                                <span id="play-icon">▶</span>
                                <span id="play-label">Play Video Guide</span>
                            </button>
                            <button onclick="restartGuide()" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-xs font-bold">
                                ↺ Restart
                            </button>
                        </div>

                        <div class="flex items-center space-x-2 text-xs text-slate-400">
                            <span>Chapter:</span>
                            <span id="chapter-label" class="font-bold text-white">1. Server Setup</span>
                        </div>
                    </div>

                </div>
            </div>

            <!-- Spoken Hindi Subtitles Box -->
            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 space-y-1">
                <div class="flex justify-between items-center text-[10px] text-emerald-400 font-bold uppercase">
                    <span>🎙️ Spoken Hindi Narration (ऑडियो वॉइसओवर):</span>
                    <span id="audio-status-badge">Audio Synced</span>
                </div>
                <p id="spoken-subtitle-text" class="text-xs text-slate-200 font-medium leading-relaxed">
                    नमस्ते दोस्तों! आज हम देखेंगे कि स्मार्ट इंडिया हैकाथॉन वाले दिन अन्नसेतु प्रोजेक्ट का लाइव डेमो जजेस के सामने कैसे प्रस्तुत करना है...
                </p>
            </div>
        </div>

        <!-- Right Side: Chapter Playlist & Interactive Links -->
        <div class="space-y-4">
            <h3 class="text-xs font-black uppercase tracking-wider text-slate-400">Chapters & Walkthrough Steps</h3>

            <div class="space-y-2.5">
                <div onclick="jumpToChapter(1)" id="ch-card-1" class="p-3.5 rounded-2xl border border-emerald-500 bg-emerald-950/40 cursor-pointer hover:border-emerald-400 transition-all space-y-1">
                    <span class="text-[10px] font-bold text-emerald-400">STEP 1</span>
                    <h4 class="text-xs font-bold text-white">Morning Setup & Terminal Run</h4>
                    <p class="text-[10px] text-slate-400">python run.py & 100% offline localhost</p>
                </div>

                <div onclick="jumpToChapter(2)" id="ch-card-2" class="p-3.5 rounded-2xl border border-slate-800 bg-slate-900/60 cursor-pointer hover:border-emerald-400 transition-all space-y-1">
                    <span class="text-[10px] font-bold text-slate-400">STEP 2</span>
                    <h4 class="text-xs font-bold text-white">Front-Page Farmer Booking</h4>
                    <p class="text-[10px] text-slate-400">MSP payout calculator & token generation</p>
                </div>

                <div onclick="jumpToChapter(3)" id="ch-card-3" class="p-3.5 rounded-2xl border border-slate-800 bg-slate-900/60 cursor-pointer hover:border-emerald-400 transition-all space-y-1">
                    <span class="text-[10px] font-bold text-slate-400">STEP 3</span>
                    <h4 class="text-xs font-bold text-white">Two-Window Live WebSocket Sync</h4>
                    <p class="text-[10px] text-slate-400">Weighbridge, Lab & instant DBT voucher</p>
                </div>

                <div onclick="jumpToChapter(4)" id="ch-card-4" class="p-3.5 rounded-2xl border border-slate-800 bg-slate-900/60 cursor-pointer hover:border-emerald-400 transition-all space-y-1">
                    <span class="text-[10px] font-bold text-slate-400">STEP 4</span>
                    <h4 class="text-xs font-bold text-white">Mandi Load Balancer & Voice IVR</h4>
                    <p class="text-[10px] text-slate-400">Routing heuristic & 5 Indic languages</p>
                </div>

                <div onclick="jumpToChapter(5)" id="ch-card-5" class="p-3.5 rounded-2xl border border-slate-800 bg-slate-900/60 cursor-pointer hover:border-emerald-400 transition-all space-y-1">
                    <span class="text-[10px] font-bold text-slate-400">STEP 5</span>
                    <h4 class="text-xs font-bold text-white">Ministry Admin & Q&A Defense</h4>
                    <p class="text-[10px] text-slate-400">Macro metrics, SLA tables & answers</p>
                </div>
            </div>

            <!-- Direct Live Links Box -->
            <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 space-y-2">
                <p class="text-xs font-bold text-slate-200">🚀 Open Live Working Tabs:</p>
                <div class="grid grid-cols-2 gap-1.5 text-[10px]">
                    <a href="http://127.0.0.1:8000/" target="_blank" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-emerald-400 font-bold text-center">Home Page</a>
                    <a href="http://127.0.0.1:8000/centers" target="_blank" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-emerald-400 font-bold text-center">Mandi Tracker</a>
                    <a href="http://127.0.0.1:8000/track" target="_blank" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-emerald-400 font-bold text-center">Live Tracker</a>
                    <a href="http://127.0.0.1:8000/staff" target="_blank" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-emerald-400 font-bold text-center">Staff Board</a>
                </div>
            </div>

        </div>

    </main>

    <!-- Hidden Audio Elements -->
    <audio id="audio-ch-1" src="Scene1_Morning_Setup.mp3" preload="auto"></audio>
    <audio id="audio-ch-2" src="Scene2_Farmer_Booking.mp3" preload="auto"></audio>
    <audio id="audio-ch-3" src="Scene3_Realtime_Two_Window_Sync.mp3" preload="auto"></audio>
    <audio id="audio-ch-4" src="Scene4_Mandi_Tracker_Voice_IVR.mp3" preload="auto"></audio>
    <audio id="audio-ch-5" src="Scene5_Judge_QA_Defense.mp3" preload="auto"></audio>

    <script>
        let currentChapter = 1;
        let isPlaying = false;
        let activeAudio = document.getElementById("audio-ch-1");

        const chapters = [
            {
                num: 1,
                title: "1. Server Setup & Localhost Run",
                url: "http://127.0.0.1:8000/",
                tabId: "sim-tab-1",
                screenId: "screen-state-1",
                audioId: "audio-ch-1",
                text: "नमस्ते दोस्तों! आज हम देखेंगे कि स्मार्ट इंडिया हैकाथॉन वाले दिन अन्नसेतु प्रोजेक्ट का लाइव डेमो जजेस के सामने कैसे प्रस्तुत करना है। सबसे पहले टर्मिनल में python run.py चलाएं। हमारा प्रोजेक्ट पूरी तरह 100% लोकल सर्वर पर चलता है!",
                cursorX: "50%",
                cursorY: "30%"
            },
            {
                num: 2,
                title: "2. Front-Page Farmer Booking",
                url: "http://127.0.0.1:8000/",
                tabId: "sim-tab-1",
                screenId: "screen-state-2",
                audioId: "audio-ch-2",
                text: "जैसे ही जजेस आएं, होम पेज दिखाते हुए बताएं कि किसान सीधे फ्रंट पेज पर अपना नाम, फसल (गेहूं) और मात्रा भरता है। सिस्टम तुरंत 1 लाख 21 हजार 250 रुपये का गारंटीड भुगतान दिखाता है!",
                cursorX: "85%",
                cursorY: "75%"
            },
            {
                num: 3,
                title: "3. Side-by-Side Live WebSocket Sync",
                url: "http://127.0.0.1:8000/track",
                tabId: "sim-tab-3",
                screenId: "screen-state-3",
                audioId: "audio-ch-3",
                text: "अब स्क्रीन को दो हिस्सों में बांटें: बाईं तरफ किसान का फोन है और दाईं तरफ स्टाफ ऑपरेटर बोर्ड। स्टाफ बोर्ड पर बटन दबाते ही किसान की स्क्रीन पर बिना रिफ्रेश किए लाइव अपडेट होता है!",
                cursorX: "75%",
                cursorY: "50%"
            },
            {
                num: 4,
                title: "4. Mandi Load Balancer & Voice IVR",
                url: "http://127.0.0.1:8000/centers",
                tabId: "sim-tab-2",
                screenId: "screen-state-4",
                audioId: "audio-ch-4",
                text: "अन्नसेतु का मंडी लोड बैलेंसर यात्रा समय और कतार को देखकर सबसे खाली मंडी की सिफारिश करता है। और बिना स्मार्टफोन वाले किसानों के लिए टोल-फ्री IVR फोन सिस्टम हिंदी में लाइव स्टेटस सुनाता है!",
                cursorX: "30%",
                cursorY: "40%"
            },
            {
                num: 5,
                title: "5. Ministry Admin Hub & Q&A Defense",
                url: "http://127.0.0.1:8000/admin",
                tabId: "sim-tab-5",
                screenId: "screen-state-5",
                audioId: "audio-ch-5",
                text: "मंत्रालय डैशबोर्ड कुल उपार्जन और बॉटलनेक का विश्लेषण दिखाता है। अगर जज पूछें कि बिना स्मार्टफोन वाले कैसे इस्तेमाल करेंगे, तो बताएं कि टोल-फ्री IVR नंबर 1800-180-2626 से वे सीधे सुन सकते हैं। धन्यवाद!",
                cursorX: "50%",
                cursorY: "50%"
            }
        ];

        function jumpToChapter(chNum) {
            currentChapter = chNum;
            const ch = chapters[chNum - 1];

            // Stop any currently playing audio
            if (activeAudio) {
                activeAudio.pause();
                activeAudio.currentTime = 0;
            }

            // Switch Screen State
            for (let i = 1; i <= 5; i++) {
                const screen = document.getElementById("screen-state-" + i);
                if (screen) screen.classList.add("hidden");
                const card = document.getElementById("ch-card-" + i);
                if (card) {
                    card.className = (i === chNum) 
                        ? "p-3.5 rounded-2xl border border-emerald-500 bg-emerald-950/40 cursor-pointer shadow-lg transition-all space-y-1"
                        : "p-3.5 rounded-2xl border border-slate-800 bg-slate-900/60 cursor-pointer hover:border-emerald-400 transition-all space-y-1";
                }
                const tab = document.getElementById("sim-tab-" + i);
                if (tab) tab.className = (tab.id === ch.tabId) 
                    ? "px-3 py-1.5 rounded-t-lg bg-slate-700 text-slate-300 active-tab transition-all"
                    : "px-3 py-1.5 rounded-t-lg bg-slate-700 text-slate-300 transition-all";
            }

            const activeScreen = document.getElementById(ch.screenId);
            if (activeScreen) activeScreen.classList.remove("hidden");

            // Update URL & Labels
            document.getElementById("sim-url-bar").innerText = ch.url;
            document.getElementById("chapter-label").innerText = ch.title;
            document.getElementById("spoken-subtitle-text").innerText = ch.text;
            document.getElementById("video-progress-bar").style.width = (chNum * 20) + "%";

            // Move Animated Cursor
            const cursor = document.getElementById("sim-cursor");
            cursor.style.left = ch.cursorX;
            cursor.style.top = ch.cursorY;
            showClickEffect(ch.cursorX, ch.cursorY);

            // Audio Player
            activeAudio = document.getElementById(ch.audioId);
            if (isPlaying && activeAudio) {
                activeAudio.play().catch(e => console.log("Audio play blocked"));
            }

            // Attach auto-next on audio end
            activeAudio.onended = () => {
                if (isPlaying && currentChapter < 5) {
                    setTimeout(() => jumpToChapter(currentChapter + 1), 1200);
                } else if (currentChapter === 5) {
                    isPlaying = false;
                    updatePlayButtonUI();
                }
            };
        }

        function showClickEffect(x, y) {
            const container = document.getElementById("click-effect-container");
            const clickEl = document.createElement("div");
            clickEl.className = "click-pulse";
            clickEl.style.left = x;
            clickEl.style.top = y;
            container.appendChild(clickEl);
            setTimeout(() => clickEl.remove(), 600);
        }

        function toggleAutoPlay() {
            isPlaying = !isPlaying;
            updatePlayButtonUI();

            if (isPlaying) {
                if (activeAudio) activeAudio.play().catch(e => console.log("Audio start"));
            } else {
                if (activeAudio) activeAudio.pause();
            }
        }

        function updatePlayButtonUI() {
            const btnLabel = document.getElementById("play-label");
            const btnIcon = document.getElementById("play-icon");
            if (isPlaying) {
                btnLabel.innerText = "Pause Guide";
                btnIcon.innerText = "⏸";
            } else {
                btnLabel.innerText = "Play Video Guide";
                btnIcon.innerText = "▶";
            }
        }

        function restartGuide() {
            jumpToChapter(1);
            if (!isPlaying) toggleAutoPlay();
        }

        document.addEventListener("DOMContentLoaded", () => {
            jumpToChapter(1);
        });
    </script>
</body>
</html>
"""

with open(HTML_GUIDE_PATH, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[OK] Interactive Video Guide generated at: {HTML_GUIDE_PATH}")
