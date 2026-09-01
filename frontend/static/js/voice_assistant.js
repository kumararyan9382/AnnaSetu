/**
 * Voice Assistant & Simulated IVR Phone Interface
 * Allows speech recognition queries and audio spoken responses in Hindi and English
 */

let recognition = null;
let isListening = false;

function initVoiceAssistant() {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (SpeechRecognition) {
        recognition = new SpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = currentLang === "hi" ? "hi-IN" : "en-IN";

        recognition.onstart = () => {
            isListening = true;
            updateVoiceMicUI(true);
            showToast("🎙️ Listening... Please speak your mobile or token number", "info");
        };

        recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript;
            const inputField = document.getElementById("voice-search-input") || document.getElementById("ivr-phone-input");
            if (inputField) inputField.value = transcript;
            lookupVoiceQuery(transcript);
        };

        recognition.onerror = (event) => {
            isListening = false;
            updateVoiceMicUI(false);
            showToast("Voice recognition error: " + event.error, "error");
        };

        recognition.onend = () => {
            isListening = false;
            updateVoiceMicUI(false);
        };
    }
}

function toggleVoiceListen() {
    if (!recognition) {
        initVoiceAssistant();
    }
    if (!recognition) {
        showToast("Speech recognition is not supported in this browser. Please type number.", "warning");
        return;
    }

    if (isListening) {
        recognition.stop();
    } else {
        recognition.lang = currentLang === "hi" ? "hi-IN" : "en-IN";
        recognition.start();
    }
}

function updateVoiceMicUI(active) {
    const micBtn = document.getElementById("voice-mic-btn");
    const micIcon = document.getElementById("voice-mic-icon");
    if (micBtn) {
        if (active) {
            micBtn.classList.add("bg-rose-600", "animate-pulse", "ring-4", "ring-rose-200");
            micBtn.classList.remove("bg-emerald-600");
        } else {
            micBtn.classList.remove("bg-rose-600", "animate-pulse", "ring-4", "ring-rose-200");
            micBtn.classList.add("bg-emerald-600");
        }
    }
}

async function lookupVoiceQuery(queryText) {
    if (!queryText) return;

    const speechResultBox = document.getElementById("ivr-speech-box");
    const speechTextEl = document.getElementById("ivr-speech-text");
    const tokenCard = document.getElementById("ivr-token-card");

    try {
        const res = await fetch("/api/voice/lookup", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query: queryText, language: currentLang })
        });

        const data = await res.json();

        const spokenMessage = (currentLang === "hi" || currentLang === "mr" || currentLang === "pa") ? data.speech_hi : data.speech_en;

        if (speechTextEl) speechTextEl.innerText = spokenMessage;
        if (speechResultBox) speechResultBox.classList.remove("hidden");

        // Speak aloud
        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel();
            const utterance = new SpeechSynthesisUtterance(spokenMessage);
            utterance.lang = (currentLang === "hi" || currentLang === "mr" || currentLang === "pa") ? "hi-IN" : "en-IN";
            utterance.rate = 0.95;
            window.speechSynthesis.speak(utterance);
        }

        // Render token card if found
        if (data.found && data.token && tokenCard) {
            tokenCard.classList.remove("hidden");
            const t = data.token;
            tokenCard.innerHTML = `
                <div class="p-4 bg-emerald-50 border border-emerald-200 rounded-xl space-y-2 text-xs">
                    <div class="flex justify-between items-center">
                        <span class="font-mono font-bold text-emerald-800">${t.id}</span>
                        <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 font-bold">${t.stage.replace('_', ' ')}</span>
                    </div>
                    <p class="font-bold text-slate-800 text-sm">${t.farmer_name} (${t.phone || t.farmer_phone})</p>
                    <p class="text-slate-600">${t.crop_name} • ${t.center_name}</p>
                    <div class="pt-2 flex justify-between items-center border-t border-emerald-200">
                        <span class="text-slate-500">Wait Time: <b>${t.estimated_wait_mins} Mins</b></span>
                        <a href="/track/${t.id}" class="text-emerald-700 font-bold underline">Open Live Tracker &rarr;</a>
                    </div>
                </div>
            `;
        }

    } catch (err) {
        showToast("Voice query error: " + err.message, "error");
    }
}

// IVR Keypad Simulation Helper
function pressKeypad(digit) {
    const input = document.getElementById("ivr-phone-input");
    if (input) {
        input.value += digit;
        playChime("stage_advance");
    }
}

function clearKeypad() {
    const input = document.getElementById("ivr-phone-input");
    if (input) input.value = "";
}
