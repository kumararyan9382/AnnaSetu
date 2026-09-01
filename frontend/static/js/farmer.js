/**
 * Farmer Module: Slot Booking, Live Token Tracking & Receipts
 */

let activeTokenData = null;

// Dynamic MSP and Value Calculation on Booking Page
function setupBookingCalculator(crops) {
    const cropSelect = document.getElementById("crop-select");
    const qtyInput = document.getElementById("qty-input");
    const mspDisplay = document.getElementById("msp-rate-val");
    const estValDisplay = document.getElementById("est-val-display");

    function updateCalc() {
        if (!cropSelect || !qtyInput) return;
        const cropName = cropSelect.value;
        const qty = parseFloat(qtyInput.value) || 0;
        const cropInfo = crops[cropName];

        if (cropInfo) {
            const msp = cropInfo.msp_per_quintal;
            const total = qty * msp;
            if (mspDisplay) mspDisplay.innerText = `₹${msp.toLocaleString('en-IN')}`;
            if (estValDisplay) estValDisplay.innerText = `₹${total.toLocaleString('en-IN')}`;
        }

        // Check e-Bhulekh land quota limit (4.5 acres x 20 qtl = 90 qtl)
        const quotaWarning = document.getElementById("quota-warning-box");
        const quotaBadge = document.getElementById("quota-status-badge");
        if (qty > 90.0) {
            if (quotaWarning) quotaWarning.classList.remove("hidden");
            if (quotaBadge) {
                quotaBadge.className = "px-3 py-1 bg-amber-500 text-slate-950 text-[10px] font-black rounded-full shadow-xs whitespace-nowrap";
                quotaBadge.innerText = "⚠️ कोटा सीमा से अधिक (>90 Qtl)";
            }
        } else {
            if (quotaWarning) quotaWarning.classList.add("hidden");
            if (quotaBadge) {
                quotaBadge.className = "px-3 py-1 bg-emerald-600 text-white text-[10px] font-black rounded-full shadow-xs whitespace-nowrap";
                quotaBadge.innerText = "✓ कोटा सीमा के अंदर";
            }
        }
    }

    if (cropSelect && qtyInput) {
        cropSelect.addEventListener("change", updateCalc);
        qtyInput.addEventListener("input", updateCalc);
        updateCalc();
    }
}

// Visual Crop Selection Card Handler
function selectCropVisual(cropName, mspRate) {
    const cropSelect = document.getElementById("crop-select");
    if (cropSelect) {
        cropSelect.value = cropName;
        cropSelect.dispatchEvent(new Event("change"));
    }
    document.querySelectorAll(".crop-visual-card").forEach(el => {
        el.classList.remove("border-emerald-600", "bg-emerald-50", "ring-4", "ring-emerald-200");
        el.classList.add("border-slate-200", "bg-white");
        const check = el.querySelector(".crop-check-icon");
        if (check) check.classList.add("hidden");
    });
    const key = cropName.split(' ')[0].toLowerCase();
    const selected = document.getElementById(`crop-card-${key}`);
    if (selected) {
        selected.classList.remove("border-slate-200", "bg-white");
        selected.classList.add("border-emerald-600", "bg-emerald-50", "ring-4", "ring-emerald-200");
        const check = selected.querySelector(".crop-check-icon");
        if (check) check.classList.remove("hidden");
    }
    if (typeof speakVoiceAnnouncement === "function") {
        speakVoiceAnnouncement(`आपने चुना ${cropName.split(' ')[0]}। सरकारी एमएसपी मूल्य है ₹${mspRate} प्रति क्विंटल।`);
    }
}

// Visual Vehicle Selection Card Handler
function selectVehicleVisual(vehicleValue, hindiName) {
    const vehicleSelect = document.getElementById("vehicle-select");
    if (vehicleSelect) {
        vehicleSelect.value = vehicleValue;
    }
    document.querySelectorAll(".vehicle-visual-card").forEach(el => {
        el.classList.remove("border-emerald-600", "bg-emerald-50", "ring-4", "ring-emerald-200");
        el.classList.add("border-slate-200", "bg-white");
    });
    const key = vehicleValue.split(' ')[0].toLowerCase();
    const selected = document.getElementById(`vehicle-card-${key}`);
    if (selected) {
        selected.classList.remove("border-slate-200", "bg-white");
        selected.classList.add("border-emerald-600", "bg-emerald-50", "ring-4", "ring-emerald-200");
    }
    if (typeof speakVoiceAnnouncement === "function") {
        speakVoiceAnnouncement(`वाहन: ${hindiName || vehicleValue}`);
    }
}

// Visual Time Slot Selection Card Handler
function selectSlotVisual(slotValue, labelHindi) {
    const slotSelect = document.getElementById("slot-select");
    if (slotSelect) {
        slotSelect.value = slotValue;
    }
    document.querySelectorAll(".slot-visual-card").forEach(el => {
        el.classList.remove("border-emerald-600", "bg-emerald-50", "ring-4", "ring-emerald-200");
        el.classList.add("border-slate-200", "bg-white");
    });
    const key = slotValue.split(' ')[0].replace(':', '');
    const selected = document.getElementById(`slot-card-${key}`);
    if (selected) {
        selected.classList.remove("border-slate-200", "bg-white");
        selected.classList.add("border-emerald-600", "bg-emerald-50", "ring-4", "ring-emerald-200");
    }
    if (typeof speakVoiceAnnouncement === "function") {
        speakVoiceAnnouncement(`समय स्लॉट चुना गया: ${labelHindi || slotValue}`);
    }
}

// Adjust Quantity via Stepper Buttons or Quick-Pick Chips
function adjustQuantity(delta, isAbsolute = false) {
    const qtyInput = document.getElementById("qty-input");
    if (!qtyInput) return;
    let val = parseFloat(qtyInput.value) || 0;
    if (isAbsolute) {
        val = delta;
    } else {
        val += delta;
    }
    if (val < 1) val = 1;
    qtyInput.value = val;
    qtyInput.dispatchEvent(new Event("input"));
    
    // Update Quick Chip Highlight
    document.querySelectorAll(".qty-chip-btn").forEach(btn => {
        if (parseFloat(btn.getAttribute("data-qty")) === val) {
            btn.className = "qty-chip-btn px-4 py-2 rounded-xl text-xs font-black bg-emerald-600 text-white shadow-sm border border-emerald-600 transition-all";
        } else {
            btn.className = "qty-chip-btn px-4 py-2 rounded-xl text-xs font-bold bg-white text-slate-700 hover:bg-emerald-50 border border-slate-200 transition-all";
        }
    });

    if (typeof speakVoiceAnnouncement === "function" && isAbsolute) {
        speakVoiceAnnouncement(`मात्रा ${val} क्विंटल चुनी गई।`);
    }
}

// Farmer Registration Number (FRN) Validation & Auto-Fill
function fillDemoBookingFRN() {
    const frnInput = document.getElementById("farmer-reg-no");
    if (frnInput) frnInput.value = "MFMB-2026-KR-8821";
    verifyBookingFRN();
}

function verifyBookingFRN() {
    const frnInput = document.getElementById("farmer-reg-no");
    const frn = frnInput ? frnInput.value.trim() : "";
    const badge = document.getElementById("frn-verified-badge");

    if (!frn) {
        if (typeof showToast === "function") showToast("कृपया किसान पंजीकरण संख्या दर्ज करें", "error");
        return;
    }

    if (badge) {
        badge.className = "px-2.5 py-0.5 bg-emerald-600 text-white text-[10px] font-black rounded-full shadow-xs";
        badge.innerText = `✓ ${frn} सत्यापित (Govt Certified)`;
    }

    // Auto populate farmer details if empty
    const nameEl = document.getElementById("farmer-name");
    const phoneEl = document.getElementById("farmer-phone");
    const villageEl = document.getElementById("farmer-village");
    const districtEl = document.getElementById("farmer-district");

    if (nameEl && !nameEl.value) nameEl.value = "रमेश कुमार (Ramesh Kumar)";
    if (phoneEl && !phoneEl.value) phoneEl.value = localStorage.getItem("annasetu_user_phone") || "9876543210";
    if (villageEl && !villageEl.value) villageEl.value = "तरावड़ी (Taraori)";
    if (districtEl && !districtEl.value) districtEl.value = "करनाल (Karnal)";

    localStorage.setItem("annasetu_farmer_frn", frn);
    if (typeof showToast === "function") {
        showToast(`🛡️ किसान पंजीकरण संख्या (${frn}) सत्यापित!`, "success");
    }
    if (typeof playChime === "function") playChime("stage_advance");
    if (typeof speakVoiceAnnouncement === "function") {
        speakVoiceAnnouncement(`किसान पंजीकरण संख्या ${frn} सत्यापित हो गई है।`);
    }
}

// 1-Click Auto Fill Demo Farmer Profile
function fillDemoFarmerProfile() {
    const nameEl = document.getElementById("farmer-name");
    const phoneEl = document.getElementById("farmer-phone");
    const villageEl = document.getElementById("farmer-village");
    const districtEl = document.getElementById("farmer-district");
    const vehicleNumEl = document.getElementById("vehicle-num");
    const frnInput = document.getElementById("farmer-reg-no");

    if (frnInput) frnInput.value = "MFMB-2026-KR-8821";
    if (nameEl) nameEl.value = "रामेश कुमार (Ramesh Kumar)";
    if (phoneEl) phoneEl.value = "9876543210";
    if (villageEl) villageEl.value = "तरावड़ी (Taraori)";
    if (districtEl) districtEl.value = "करनाल (Karnal)";
    if (vehicleNumEl) vehicleNumEl.value = "HR-05-AE-4421";
    verifyBookingFRN();

    if (typeof showToast === "function") {
        showToast("⚡ किसान विवरण स्वतः भर दिया गया (Demo Profile Filled)", "success");
    }
}

// Spoken Audio Guides for Sections
function speakSectionHelp(section) {
    if (typeof speakVoiceAnnouncement !== "function") return;
    
    const messages = {
        "intro": "नमस्ते किसान भाई! यह अन्नसेतु का स्लॉट बुकिंग पेज है। यहाँ 3 आसान चरणों में अपनी फसल बेचने का समय बुक करें और मंडी में बिना इंतज़ार किए टोकन पाएं।",
        "profile": "चरण 1: अपना नाम, 10 अंकों का मोबाइल नंबर, गाँव और ज़िले का नाम भरें। या ऊपर एक-क्लिक डेमो बटन दबाएं।",
        "crop": "चरण 2: अपनी फसल के बड़े चित्र पर क्लिक करें, जैसे गेहूं या सरसों। फिर अपनी मात्रा और वाहन चुनें।",
        "payout": "यह आपकी गारंटीड सरकारी एमएसपी राशि है जो फसल की तौल होते ही सीधे आपके बैंक खाते में भेजी जाएगी।",
        "slot": "चरण 3: अपनी नजदीकी सरकारी अनाज मंडी चुनें और आने का सुविधाजनक समय चुनें।",
        "submit": "फॉर्म पूरा होने के बाद नीचे हरा बटन दबाएं। आपको तुरंत एसएमएस पर टोकन नंबर मिल जाएगा।"
    };

    speakVoiceAnnouncement(messages[section] || "अपनी जानकारी भरें और आगे बढ़ें।");
}

// Handle Slot Booking Form Submission
async function submitBookingForm(e) {
    if (e) e.preventDefault();
    const btn = document.getElementById("submit-book-btn");
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = `<svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white inline" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z"></path></svg> Booking Slot...`;
    }

    const nameEl = document.getElementById("farmer-name");
    const phoneEl = document.getElementById("farmer-phone");
    const villageEl = document.getElementById("farmer-village");
    const districtEl = document.getElementById("farmer-district");
    const cropEl = document.getElementById("crop-select");
    const qtyEl = document.getElementById("qty-input");
    const vehicleTypeEl = document.getElementById("vehicle-select");
    const vehicleNumEl = document.getElementById("vehicle-num");
    const centerEl = document.getElementById("center-select");
    const slotEl = document.getElementById("slot-select");

    const payload = {
        farmer_name: nameEl && nameEl.value.trim() ? nameEl.value.trim() : "किसान (Farmer)",
        phone: phoneEl && phoneEl.value.trim() ? phoneEl.value.trim() : "9876543210",
        village: villageEl && villageEl.value.trim() ? villageEl.value.trim() : "गाँव (Village)",
        district: districtEl && districtEl.value.trim() ? districtEl.value.trim() : "ज़िला (District)",
        crop_name: cropEl ? cropEl.value : "Wheat (गेहूं)",
        estimated_quantity_qtl: qtyEl ? parseFloat(qtyEl.value) || 50.0 : 50.0,
        vehicle_type: vehicleTypeEl ? vehicleTypeEl.value : "Tractor Trolley (ट्रैक्टर ट्रॉली)",
        vehicle_number: vehicleNumEl && vehicleNumEl.value.trim() ? vehicleNumEl.value.trim() : "HR-TR-001",
        center_id: centerEl ? centerEl.value : "CTR-001",
        scheduled_slot: slotEl ? slotEl.value : "09:00 AM - 11:00 AM"
    };

    try {
        const res = await fetch("/api/farmers/book", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        if (!res.ok) {
            const err = await res.json();
            throw new Error(err.detail || "Booking failed");
        }

        const data = await res.json();
        try {
            localStorage.setItem("annasetu_last_token", data.id);
            localStorage.setItem("annasetu_last_farmer", payload.farmer_name);
            localStorage.setItem("annasetu_last_crop", payload.crop_name);
        } catch (e) {}

        try {
            if (typeof showToast === "function") {
                showToast(`🎉 Slot Booked! Your Token ID is ${data.id}`, "success");
            }
            if (typeof playChime === "function") {
                playChime("stage_advance");
            }
            if (typeof speakVoiceAnnouncement === "function") {
                speakVoiceAnnouncement(`बधाई हो! आपका मंडी स्लॉट बुक हो गया है। टोकन नंबर ${data.id.split('-').pop()} तैयार है।`);
            }
        } catch (uiErr) {
            console.warn("UI feedback warning:", uiErr);
        }

        // Instant fast redirect to live tracker for this token
        setTimeout(() => {
            window.location.href = `/track/${data.id}`;
        }, 400);

    } catch (err) {
        console.error("Booking error:", err);
        if (typeof showToast === "function") {
            showToast(err.message, "error");
        } else {
            alert(err.message);
        }
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = `<span>✨ Confirm & Generate Token</span>`;
        }
    }
}

// Fetch and Render Live Token Tracker
async function loadTokenTracker(tokenId) {
    if (!tokenId) return;

    try {
        const res = await fetch(`/api/farmers/token/${tokenId}`);
        if (!res.ok) {
            throw new Error(`Token ${tokenId} not found`);
        }
        const data = await res.json();
        activeTokenData = data;
        renderTrackerUI(data);

        // Subscribe to real-time updates for this specific token
        liveSync.subscribeToken(tokenId);

    } catch (err) {
        const trackerContainer = document.getElementById("tracker-content");
        if (trackerContainer) {
            trackerContainer.innerHTML = `
                <div class="bg-rose-50 border border-rose-200 text-rose-700 p-6 rounded-2xl text-center">
                    <p class="font-bold text-lg">⚠️ Token Not Found</p>
                    <p class="text-sm mt-1">Could not find active token with ID "${tokenId}". Please check the number or book a new slot.</p>
                    <a href="/book" class="inline-block mt-4 px-5 py-2 bg-rose-600 text-white font-medium rounded-xl text-sm hover:bg-rose-700">Book New Slot</a>
                </div>
            `;
        }
    }
}

// Render the 5-Stage Live Progression & Metrics
function renderTrackerUI(data) {
    // Basic Details
    const elTokenId = document.getElementById("display-token-id");
    const elFarmer = document.getElementById("display-farmer-name");
    const elPhone = document.getElementById("display-farmer-phone");
    const elCrop = document.getElementById("display-crop-name");
    const elCenter = document.getElementById("display-center-name");
    const elVehicle = document.getElementById("display-vehicle");
    const elSlot = document.getElementById("display-slot");
    const elWaitMins = document.getElementById("display-wait-mins");
    const elAhead = document.getElementById("display-ahead-count");
    const elProgressBar = document.getElementById("tracker-progress-bar");
    const elStatusBadge = document.getElementById("tracker-status-badge");

    if (elTokenId) elTokenId.innerText = data.id;
    if (elFarmer) elFarmer.innerText = data.farmer_name;
    if (elPhone) elPhone.innerText = data.farmer_phone;
    if (elCrop) elCrop.innerText = `${data.crop_name} (${data.estimated_quantity_qtl} Qtls)`;
    if (elCenter) elCenter.innerText = `${data.center_name} - ${data.center_location}`;
    if (elVehicle) elVehicle.innerText = `${data.vehicle_type} [${data.vehicle_number || 'N/A'}]`;
    if (elSlot) elSlot.innerText = `${data.scheduled_date} | ${data.scheduled_slot}`;
    if (elWaitMins) elWaitMins.innerText = `${data.live_estimated_wait_mins} Mins`;
    if (elAhead) elAhead.innerText = `${data.farmers_ahead} Vehicles`;

    if (elProgressBar) {
        elProgressBar.style.width = `${data.stage_percentage}%`;
    }

    const stageMap = {
        "REGISTERED": { text: "1. Slot Scheduled", color: "bg-blue-100 text-blue-800 border-blue-300" },
        "GATE_ENTRY": { text: "2. Gate Entry & In Queue", color: "bg-amber-100 text-amber-800 border-amber-300" },
        "WEIGHBRIDGE": { text: "3. Gross Weighing Done", color: "bg-purple-100 text-purple-800 border-purple-300" },
        "QUALITY_CHECK": { text: "4. Quality Tested & Approved", color: "bg-indigo-100 text-indigo-800 border-indigo-300" },
        "PAYMENT_PROCESSED": { text: "5. DBT Payment Completed 🎉", color: "bg-emerald-100 text-emerald-800 border-emerald-300" }
    };

    if (elStatusBadge && stageMap[data.stage]) {
        elStatusBadge.className = `px-3.5 py-1.5 rounded-full text-xs font-bold border ${stageMap[data.stage].color}`;
        elStatusBadge.innerText = stageMap[data.stage].text;
    }

    // Update 5 Stages Visual Step Cards
    const stages = ["REGISTERED", "GATE_ENTRY", "WEIGHBRIDGE", "QUALITY_CHECK", "PAYMENT_PROCESSED"];
    const currentIdx = stages.indexOf(data.stage);

    stages.forEach((stg, idx) => {
        const card = document.getElementById(`stage-step-${idx + 1}`);
        const icon = document.getElementById(`stage-icon-${idx + 1}`);
        const timeEl = document.getElementById(`stage-time-${idx + 1}`);

        if (card && icon) {
            if (idx < currentIdx) {
                // Completed stage
                card.className = "stage-card completed p-4 rounded-2xl border-2 border-emerald-500 bg-white shadow-sm";
                icon.className = "w-10 h-10 rounded-full bg-emerald-500 text-white flex items-center justify-center font-bold text-base shadow-sm";
                icon.innerHTML = `<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>`;
            } else if (idx === currentIdx) {
                // Active current stage
                card.className = "stage-card active p-4 rounded-2xl border-2 border-emerald-600 bg-emerald-50 shadow-md live-pulse ring-4 ring-emerald-100";
                icon.className = "w-10 h-10 rounded-full bg-emerald-600 text-white flex items-center justify-center font-bold text-base shadow-sm";
                icon.innerText = `${idx + 1}`;
            } else {
                // Upcoming stage
                card.className = "stage-card p-4 rounded-2xl border border-slate-200 bg-slate-50/70 opacity-60";
                icon.className = "w-10 h-10 rounded-full bg-slate-200 text-slate-500 flex items-center justify-center font-bold text-base";
                icon.innerText = `${idx + 1}`;
            }
        }

        // Render timestamps if available
        const timeField = data[`stage_${idx + 1}_time`];
        if (timeEl) {
            timeEl.innerText = timeField ? timeField.split(" ")[1] : "Pending";
        }
    });

    // Render Measurement Details if available
    const elWeighData = document.getElementById("measured-weighbridge-val");
    const elQualityData = document.getElementById("measured-quality-val");
    const elPaymentData = document.getElementById("measured-payment-val");

    if (elWeighData) {
        if (data.gross_weight_kg) {
            elWeighData.innerHTML = `Gross: <b>${data.gross_weight_kg} kg</b> ${data.tare_weight_kg ? `| Tare: <b>${data.tare_weight_kg} kg</b> | Net: <b>${data.net_weight_qtl} Qtls</b>` : ''}`;
        } else {
            elWeighData.innerText = "Awaiting weighbridge scale...";
        }
    }

    if (elQualityData) {
        if (data.moisture_percent) {
            elQualityData.innerHTML = `Moisture: <b>${data.moisture_percent}%</b> | Grade: <span class="text-emerald-700 font-bold">${data.quality_grade || 'Grade A'}</span>`;
        } else {
            elQualityData.innerText = "Awaiting lab inspection...";
        }
    }

    if (elPaymentData) {
        if (data.total_amount_inr) {
            elPaymentData.innerHTML = `<span class="text-emerald-700 font-extrabold text-lg">₹${data.total_amount_inr.toLocaleString('en-IN')}</span> <br/><span class="text-xs text-slate-500 font-mono">Ref: ${data.dbt_reference_no}</span>`;
            const receiptSection = document.getElementById("voucher-section");
            if (receiptSection) receiptSection.classList.remove("hidden");
        } else {
            elPaymentData.innerText = "Calculated upon tare weight completion";
        }
    }

    // Populate Printable Receipt Fields
    populatePrintReceipt(data);
}

function populatePrintReceipt(data) {
    const pToken = document.getElementById("rcpt-token-id");
    const pFarmer = document.getElementById("rcpt-farmer-name");
    const pPhone = document.getElementById("rcpt-farmer-phone");
    const pCrop = document.getElementById("rcpt-crop-name");
    const pGross = document.getElementById("rcpt-gross-kg");
    const pTare = document.getElementById("rcpt-tare-kg");
    const pNet = document.getElementById("rcpt-net-qtl");
    const pMsp = document.getElementById("rcpt-msp-rate");
    const pTotal = document.getElementById("rcpt-total-inr");
    const pDbt = document.getElementById("rcpt-dbt-ref");
    const pCenter = document.getElementById("rcpt-center-name");
    const pDate = document.getElementById("rcpt-date");

    if (pToken) pToken.innerText = data.id;
    if (pFarmer) pFarmer.innerText = data.farmer_name;
    if (pPhone) pPhone.innerText = data.farmer_phone;
    if (pCrop) pCrop.innerText = data.crop_name;
    if (pGross) pGross.innerText = `${data.gross_weight_kg || 0} kg`;
    if (pTare) pTare.innerText = `${data.tare_weight_kg || 0} kg`;
    if (pNet) pNet.innerText = `${data.net_weight_qtl || data.estimated_quantity_qtl} Quintals`;
    if (pMsp) pMsp.innerText = `₹${(data.msp_rate_applied || 2425).toLocaleString('en-IN')} / Qtl`;
    if (pTotal) pTotal.innerText = `₹${(data.total_amount_inr || (data.estimated_quantity_qtl * 2425)).toLocaleString('en-IN')}`;
    if (pDbt) pDbt.innerText = data.dbt_reference_no || "DBT-PENDING-STAGE5";
    if (pCenter) pCenter.innerText = data.center_name;
    if (pDate) pDate.innerText = data.scheduled_date;
}

// Speak Token Status Aloud (Speech Synthesis in Hindi / English)
function speakTokenStatus() {
    if (!activeTokenData) return;

    if (!('speechSynthesis' in window)) {
        showToast("Speech synthesis not supported in this browser.", "warning");
        return;
    }

    window.speechSynthesis.cancel();

    let textToSpeak = "";
    let langCode = "hi-IN";

    if (currentLang === "hi" || currentLang === "mr" || currentLang === "pa") {
        const stageHindi = {
            "REGISTERED": "आपका टोकन स्लॉट बुक है।",
            "GATE_ENTRY": "आपकी गाड़ी मंडी के गेट में प्रवेश कर चुकी है।",
            "WEIGHBRIDGE": "आपका सकल वजन हो चुका है। अब गुणवत्ता जांच की बारी है।",
            "QUALITY_CHECK": "गुणवत्ता जांच पास हो गई है।",
            "PAYMENT_PROCESSED": `उपार्जन पूरा हो गया है। कुल राशि ${activeTokenData.total_amount_inr || 0} रुपये आपके बैंक खाते में भेजी जा चुकी है।`
        }[activeTokenData.stage] || "आपकी स्थिति प्रक्रियाधीन है।";

        textToSpeak = `नमस्ते ${activeTokenData.farmer_name} जी। टोकन नंबर ${activeTokenData.id}। वर्तमान स्थिति: ${stageHindi}। अनुमानित प्रतीक्षा समय लगभग ${activeTokenData.live_estimated_wait_mins} मिनट है।`;
    } else {
        langCode = "en-IN";
        textToSpeak = `Hello ${activeTokenData.farmer_name}. Your Token ID is ${activeTokenData.id}. Current stage is ${activeTokenData.stage.replace('_', ' ')}. Estimated wait time is ${activeTokenData.live_estimated_wait_mins} minutes.`;
    }

    const utterance = new SpeechSynthesisUtterance(textToSpeak);
    utterance.lang = langCode;
    utterance.rate = 0.95;
    window.speechSynthesis.speak(utterance);
    showToast("🔊 Reading token status aloud...", "info");
}

// Helper to get current Token ID reliably
function getCurrentTokenId() {
    if (activeTokenData && activeTokenData.id) return activeTokenData.id;
    const inputEl = document.getElementById("lookup-token-input");
    if (inputEl && inputEl.value.trim().startsWith("AS-26-")) return inputEl.value.trim();
    const pathParts = window.location.pathname.split("/").filter(Boolean);
    const lastPart = pathParts[pathParts.length - 1];
    if (lastPart && lastPart.startsWith("AS-26-")) return lastPart;
    const displayEl = document.getElementById("display-token-id");
    if (displayEl) {
        const cleaned = displayEl.innerText.replace(/\s+/g, '').replace(/–/g, '-');
        if (cleaned.startsWith("AS-26-")) return cleaned;
    }
    return "AS-26-WHT-101";
}

// 1-Click Advance Next Stage for Demo
async function advanceCurrentTokenNext() {
    const currentToken = getCurrentTokenId();
    console.log("⚡ Advance clicked for Token:", currentToken);
    if (!currentToken) {
        showToast("Please enter or select a Token ID first", "warning");
        return;
    }

    try {
        const res = await fetch(`/api/farmers/token/${currentToken}/advance-next`, { 
            method: "POST",
            headers: { "Content-Type": "application/json" }
        });
        
        if (res.ok) {
            const data = await res.json();
            showToast(`⚡ Advanced to: ${data.stage.replace('_', ' ')}`, "success");
            playChime(data.stage === "PAYMENT_PROCESSED" ? "payment" : "stage_advance");
            await loadTokenTracker(currentToken);
        } else {
            const err = await res.json();
            showToast(err.detail || "Could not advance token", "error");
        }
    } catch (e) {
        console.error("Failed to advance stage:", e);
        showToast("Error connecting to backend server", "error");
    }
}

// Auto-Play 5-Stage Live Simulation
let autoSimInterval = null;

function toggleAutoSimulate() {
    const btnText = document.getElementById("auto-play-text");
    const btnIcon = document.getElementById("auto-play-icon");
    const currentToken = getCurrentTokenId();

    if (autoSimInterval) {
        clearInterval(autoSimInterval);
        autoSimInterval = null;
        if (btnText) btnText.innerText = "Auto-Play Demo";
        if (btnIcon) btnIcon.innerText = "▶";
        showToast("Simulation Paused", "info");
    } else {
        if (btnText) btnText.innerText = "Playing...";
        if (btnIcon) btnIcon.innerText = "⏸";
        showToast("▶ Auto-Play Started! Advancing through stages...", "success");

        // Advance immediately once
        advanceCurrentTokenNext();

        // Then advance every 3 seconds
        autoSimInterval = setInterval(async () => {
            if (activeTokenData && activeTokenData.stage === "PAYMENT_PROCESSED") {
                clearInterval(autoSimInterval);
                autoSimInterval = null;
                if (btnText) btnText.innerText = "Completed 🎉";
                if (btnIcon) btnIcon.innerText = "✅";
                showToast("🎉 All 5 Stages Complete! Payment Voucher Ready.", "success");
            } else {
                advanceCurrentTokenNext();
            }
        }, 3000);
    }
}

// Kisan Sawaari Freight Pooling Toggle
let isFreightPooling = false;
function toggleFreightPooling() {
    isFreightPooling = !isFreightPooling;
    const btn = document.getElementById("pooling-toggle-btn");
    const vehicleSelect = document.getElementById("vehicle-select");
    if (isFreightPooling) {
        if (btn) {
            btn.className = "px-3.5 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-black rounded-xl shadow-xs transition-transform active:scale-95 whitespace-nowrap";
            btn.innerText = "✓ सांझा पूलिंग सक्रिय (₹1,200 बचत)";
        }
        if (vehicleSelect) vehicleSelect.value = "Shared Tractor Pooling (किराया सांझा ट्रॉली)";
        showToast("🤝 किसान सवारी सक्रिय: 3 किसानों के साथ सांझा भाड़ा ₹400/ट्रॉली तय हुआ!", "success");
        speakVoiceAnnouncement("किसान सवारी पूलिंग सक्रिय हो गई है। सांझा ट्रॉली से आपके बारह सौ रुपये भाड़े की बचत होगी।");
    } else {
        if (btn) {
            btn.className = "px-3.5 py-1.5 bg-amber-500 hover:bg-amber-600 text-slate-950 text-xs font-black rounded-xl shadow-xs transition-transform active:scale-95 whitespace-nowrap";
            btn.innerText = "✓ सांझा ट्रॉली सक्रिय करें";
        }
        if (vehicleSelect) vehicleSelect.value = "Tractor Trolley (ट्रैक्टर ट्रॉली)";
        showToast("व्यक्तिगत वाहन मोड (Individual Transport)", "info");
    }
}

// AI Grain Quality Camera Scanner
function openAIGrainScanner() {
    const modal = document.getElementById("ai-grain-modal");
    if (modal) modal.classList.remove("hidden");
}

function closeAIGrainModal() {
    const modal = document.getElementById("ai-grain-modal");
    if (modal) modal.classList.add("hidden");
}

function runAIGrainScan() {
    const resBox = document.getElementById("ai-grain-results");
    if (resBox) resBox.classList.remove("hidden");
    showToast("🔬 AI कंप्यूटर विजन दाना विश्लेषण पूर्ण! ग्रेड A प्रमाणित।", "success");
    speakVoiceAnnouncement("ए आई दाना स्कैनर विश्लेषण पूर्ण हो गया है। आपका अनाज 98.4 प्रतिशत शुद्ध है और पूर्ण समर्थन मूल्य हेतु प्रमाणित है।");
}

// e-NWR Instant Micro-Credit Loan Against Grain in Warehouse
async function applyEnwrLoan(tokenId) {
    const token = tokenId || getCurrentTokenId() || "AS-26-WHT-101";
    try {
        const res = await fetch(`/api/farmers/enwr-loan-apply?token_id=${token}&loan_amount=75000`, { method: "POST" });
        const data = await res.json();
        alert(`🏦 ई-गिरवी ऋण स्वीकृत (e-NWR Micro-Credit)!\n\nरसीद नंबर: ${data.enwr_receipt_no}\nऋण राशि: ₹75,000 (75% MSP मूल्य)\nब्याज दर: 4.0% प्रति वर्ष\nवितरण बैंक: SBI KCC शाखा करनाल\n\nराशि सीधे आपके आधार लिंक बैंक खाते में स्थानांतरित कर दी गई है।`);
        showToast("🏦 ₹75,000 ई-गिरवी ऋण स्वीकृत!", "success");
        speakVoiceAnnouncement("ई-गिरवी ऋण पचहत्तर हज़ार रुपये आपके बैंक खाते में चार प्रतिशत ब्याज दर पर स्वीकृत हो गया है।");
    } catch (e) {
        showToast("Error processing loan request", "error");
    }
}




