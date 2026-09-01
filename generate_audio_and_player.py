"""
Generate High-Quality Hindi Voiceover Audio Files & HTML Video Presentation Player
for AnnaSetu Hackathon Day Playbook
"""

import os
import sys
from gtts import gTTS

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

OUTPUT_DIR = r"C:\Users\kumar\OneDrive\Documents\Aryan\Hackathon"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Scene Narrations in High-Quality Spoken Hindi
SCENES = [
    {
        "id": "scene1",
        "title": "Scene 1: Morning Setup (सुबह की तैयारी)",
        "duration_est": "35s",
        "audio_file": "Scene1_Morning_Setup.mp3",
        "text": (
            "नमस्ते दोस्तों! आज हम देखेंगे कि स्मार्ट इंडिया हैकाथॉन वाले दिन अन्नसेतु प्रोजेक्ट का लाइव डेमो जजेस के सामने कैसे प्रस्तुत करना है। "
            "सबसे पहले, जजेस के आने से 5 मिनट पहले आपको टर्मिनल में python run.py कमांड चलानी है। "
            "हमारा सिस्टम पूरी तरह से लोकल सर्वर 127.0.0.1:8000 पर चलता है, यानी अगर वेन्यू पर वाई-फाई न भी हो, तब भी आपका पूरा प्रोजेक्ट बिना किसी रुकावट के चलेगा! "
            "सर्वर स्टार्ट होने के बाद अपने ब्राउज़र में होम पेज, मंडी ट्रैकर, लाइव ट्रैकर, स्टाफ बोर्ड, मिनिस्ट्री एनालिटिक्स और वॉइस IVR डेमो के टैब्स पहले से खोलकर रख लें।"
        ),
        "visual_desc": "Terminal running 'python run.py' and Google Chrome browser with 6 pre-arranged tabs.",
        "badge": "Setup Phase"
    },
    {
        "id": "scene2",
        "title": "Scene 2: Problem & Farmer Booking (समस्या और किसान स्लॉट बुकिंग)",
        "duration_est": "45s",
        "audio_file": "Scene2_Farmer_Booking.mp3",
        "text": (
            "जैसे ही जजेस आपके पास आएं, सबसे पहले होम पेज दिखाते हुए समस्या समझाएं: "
            "आदरणीय जजेस, हर साल फसल कटाई के बाद किसानों को सरकारी मंडियों में 18 से 48 घंटे तक लंबी कतारों और जाम में खड़ा रहना पड़ता है। "
            "उन्हें यह पता नहीं होता कि उनका नंबर कब आएगा या भुगतान कब मिलेगा। इसी समस्या का समाधान है अन्नसेतु। "
            "यहाँ किसान सीधे होम पेज पर अपना नाम, मोबाइल नंबर, गाँव और फसल चुनता है। "
            "सिस्टम तुरंत सरकारी एमएसपी के आधार पर 1 लाख 21 हजार 250 रुपये का गारंटीड भुगतान दिखाता है। "
            "जैसे ही किसान कन्फर्म करता है, उसे एक टोकन नंबर और लाइव वेटिंग टाइम मिल जाता है।"
        ),
        "visual_desc": "Homepage farmer registration form filled with Wheat 50 Qtls, showing ₹1,21,250 guaranteed payout.",
        "badge": "Farmer Experience"
    },
    {
        "id": "scene3",
        "title": "Scene 3: Real-Time Two-Window Sync (लाइव टू-विंडो सिंक)",
        "duration_est": "55s",
        "audio_file": "Scene3_Realtime_Two_Window_Sync.mp3",
        "text": (
            "अब आता है प्रेजेंटेशन का सबसे बड़ा आकर्षण: लाइव टू-विंडो रियल-टाइम सिंक। "
            "बाईं तरफ किसान का मोबाइल स्क्रीन है और दाईं तरफ मंडी स्टाफ ऑपरेटर का बोर्ड है। "
            "स्टाफ बोर्ड पर जैसे ही हम चेक-इन गेट एंट्री क्लिक करते हैं, देखिए बिना पेज रिफ्रेश किए किसान की स्क्रीन पर तुरंत बीप साउंड के साथ स्टेज 2 अपडेट हो जाती है! "
            "इसके बाद धर्मकांटे पर 7850 किलो वजन दर्ज होता है, लैब में 11.4% नमी की जांच पास होती है, और अनलोडिंग के बाद 2850 किलो खाली वजन कटकर नेट 50 क्विंटल का हिसाब बनता है। "
            "सिस्टम तुरंत डीबीटी रेफरेंस नंबर जनरेट करता है और किसान के फोन पर सरकारी डिजिटल ई-रसीद वॉटरमार्क के साथ तैयार हो जाती है।"
        ),
        "visual_desc": "Split-screen with Farmer Live Tracker on left and Staff Operator Dashboard on right advancing through all 5 stages.",
        "badge": "Core Innovation"
    },
    {
        "id": "scene4",
        "title": "Scene 4: Mandi Tracker, Voice IVR & Ministry Hub (मंडी ट्रैकर व वॉइस असिस्टेंस)",
        "duration_est": "50s",
        "audio_file": "Scene4_Mandi_Tracker_Voice_IVR.mp3",
        "text": (
            "अन्नसेतु का अगला बड़ा फीचर है मंडी लोड बैलेंसर। घर से निकलने से पहले किसान देख सकता है कि किस मंडी में कितनी भीड़ है। "
            "हमारा एल्गोरिदम ट्रैक्टर का ट्रैवल टाइम और मंडी का वेटिंग टाइम जोड़कर सबसे तेज और खाली मंडी की सिफारिश करता है। "
            "जिन किसानों के पास स्मार्टफोन नहीं है, उनके लिए हमने टोल-फ्री वॉइस और आईवीआर असिस्टेंट बनाया है। "
            "किसान सिर्फ अपना मोबाइल नंबर बोलकर या डायल करके अपनी स्थिति हिंदी, पंजाबी, मराठी, तेलुगु या अंग्रेजी में सुन सकते हैं। "
            "और जिला अधिकारियों के लिए यह सेंट्रल एनालिटिक्स डैशबोर्ड है, जहाँ कुल उपार्जन और बजट का लाइव विश्लेषण देखा जा सकता है।"
        ),
        "visual_desc": "Mandi comparison matrix, simulated phone IVR dialer with speech synthesis, and Ministry Admin charts.",
        "badge": "Accessibility & Scale"
    },
    {
        "id": "scene5",
        "title": "Scene 5: Judge Q&A Defense & Outro (जज के सवाल और निष्कर्ष)",
        "duration_est": "35s",
        "audio_file": "Scene5_Judge_QA_Defense.mp3",
        "text": (
            "जजेस के संभावित सवालों के लिए तैयार रहें: "
            "यदि जज पूछें कि बिना स्मार्टफोन वाले किसान कैसे इस्तेमाल करेंगे, तो बताएं कि वे टोल-फ्री आईवीआर से सीधे कॉल करके सुन सकते हैं। "
            "यदि पूछें कि देरी होने पर क्या होगा, तो बताएं कि 2 घंटे का फ्लेक्सिबल स्लॉट विंडो है और टोकन कैंसिल नहीं होता। "
            "और तौल में धोखाधड़ी रोकने के लिए हर रीडिंग सुरक्षित ऑडिट लॉग में डिजिटल टाइमस्टैम्प के साथ दर्ज होती है। "
            "इस तरह अन्नसेतु किसानों के समय और फसल की सुरक्षा करता है। धन्यवाद जजेस!"
        ),
        "visual_desc": "Key Judge Q&A defense cheat sheet, offline resilience tips, and concluding team thank you slide.",
        "badge": "Winning Defense"
    }
]

def generate_audio():
    print("🎙️ Generating Hindi Audio Voiceover Files...")
    
    full_narration_text = ""

    for scene in SCENES:
        print(f"   -> Generating: {scene['title']} ({scene['audio_file']})...")
        tts = gTTS(text=scene["text"], lang="hi", slow=False)
        scene_path = os.path.join(OUTPUT_DIR, scene["audio_file"])
        tts.save(scene_path)
        full_narration_text += " " + scene["text"]

    # Generate complete continuous audio file
    print("   -> Generating Full Combined Audio: AnnaSetu_Complete_Hindi_Explanation.mp3...")
    full_tts = gTTS(text=full_narration_text.strip(), lang="hi", slow=False)
    full_audio_path = os.path.join(OUTPUT_DIR, "AnnaSetu_Complete_Hindi_Explanation.mp3")
    full_tts.save(full_audio_path)

    print(f"✅ All Hindi MP3 voiceover files generated in: {OUTPUT_DIR}")

def generate_html_video_player():
    print("🎬 Generating Interactive HTML Video & Slide Player...")
    
    player_html = f"""<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AnnaSetu (अन्नसेतु) — Hindi Video Explanation & Demo Player</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Noto+Sans+Devanagari:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Plus Jakarta Sans', 'Noto Sans Devanagari', sans-serif; }}
        .scene-card.active {{ border-color: #10b981; background: #ecfdf5; transform: scale(1.02); }}
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col justify-between">

    <!-- Header -->
    <header class="border-b border-slate-800 bg-slate-900/80 backdrop-blur-md px-6 py-4 sticky top-0 z-50 flex items-center justify-between">
        <div class="flex items-center space-x-3">
            <span class="text-3xl">🌾</span>
            <div>
                <h1 class="text-lg font-black text-white">AnnaSetu (अन्नसेतु) — Hindi Video Explanation</h1>
                <p class="text-xs text-emerald-400">SIH 2026 Problem Statement SIH26032 • Video Presentation Player</p>
            </div>
        </div>
        <div class="flex items-center space-x-3">
            <span class="px-3 py-1 bg-emerald-950 text-emerald-300 border border-emerald-700/50 rounded-full text-xs font-bold">
                🇮🇳 स्पोकन हिंदी वॉइसओवर (HD Audio)
            </span>
        </div>
    </header>

    <!-- Main Player Area -->
    <main class="max-w-6xl mx-auto px-4 py-8 grid grid-cols-1 lg:grid-cols-3 gap-8 items-start w-full flex-grow">
        
        <!-- Video Screen / Presentation Viewport (Left 2 cols) -->
        <div class="lg:col-span-2 space-y-6">
            <div class="bg-slate-900 rounded-3xl border border-slate-800 p-6 sm:p-8 shadow-2xl space-y-6 relative overflow-hidden">
                <div class="flex items-center justify-between border-b border-slate-800 pb-4">
                    <span id="current-badge" class="px-3 py-1 rounded-full text-xs font-black uppercase bg-amber-500 text-slate-950">
                        {SCENES[0]['badge']}
                    </span>
                    <span id="current-duration" class="text-xs text-slate-400 font-mono">
                        {SCENES[0]['duration_est']}
                    </span>
                </div>

                <div class="space-y-3 min-h-[140px]">
                    <h2 id="current-title" class="text-2xl font-black text-white leading-tight">
                        {SCENES[0]['title']}
                    </h2>
                    <p id="current-visual" class="text-xs text-emerald-300 font-mono bg-slate-950/80 p-3 rounded-xl border border-emerald-900/50">
                        🖥️ <b>Visual:</b> {SCENES[0]['visual_desc']}
                    </p>
                </div>

                <!-- Hindi Spoken Transcript Box -->
                <div class="bg-slate-950/90 rounded-2xl p-5 border border-slate-800 space-y-2">
                    <p class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">🎙️ Spoken Hindi Narration (वॉइसओवर):</p>
                    <p id="current-text" class="text-sm font-medium text-slate-200 leading-relaxed">
                        {SCENES[0]['text']}
                    </p>
                </div>

                <!-- Audio Controller -->
                <div class="space-y-3 pt-2">
                    <audio id="main-audio-player" class="w-full rounded-xl" controls src="{SCENES[0]['audio_file']}"></audio>
                </div>

                <!-- Player Nav Buttons -->
                <div class="flex items-center justify-between pt-2">
                    <button onclick="prevScene()" class="px-5 py-2.5 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold rounded-xl transition-all">
                        &larr; Previous Scene
                    </button>
                    <button onclick="playCurrentScene()" class="px-6 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-extrabold rounded-xl shadow-lg transition-all">
                        ▶ Play Audio
                    </button>
                    <button onclick="nextScene()" class="px-5 py-2.5 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold rounded-xl transition-all">
                        Next Scene &rarr;
                    </button>
                </div>
            </div>
        </div>

        <!-- Scene Playlist Playlist (Right 1 col) -->
        <div class="space-y-4">
            <h3 class="text-sm font-black uppercase text-slate-400 tracking-wider">All Scenes ({len(SCENES)})</h3>
            <div class="space-y-3">
    """

    for idx, s in enumerate(SCENES):
        active_class = "active border-emerald-500 bg-emerald-950/30" if idx == 0 else "border-slate-800 bg-slate-900/60"
        player_html += f"""
                <div onclick="selectScene({idx})" id="playlist-card-{idx}" class="scene-card p-4 rounded-2xl border {active_class} cursor-pointer hover:border-emerald-500 transition-all space-y-1">
                    <div class="flex justify-between items-center text-[10px]">
                        <span class="text-emerald-400 font-bold">SCENE {idx + 1}</span>
                        <span class="text-slate-400 font-mono">{s['duration_est']}</span>
                    </div>
                    <h4 class="text-xs font-bold text-white leading-snug">{s['title']}</h4>
                    <p class="text-[11px] text-slate-400 truncate">{s['visual_desc']}</p>
                </div>
        """

    player_html += """
            </div>

            <!-- Full Audio Playback Card -->
            <div class="p-4 rounded-2xl bg-gradient-to-r from-emerald-900/40 to-slate-900 border border-emerald-800/40 space-y-2">
                <p class="text-xs font-black text-emerald-300">🎧 Complete Continuous Narration</p>
                <p class="text-[11px] text-slate-400">Play all 5 scenes combined in one full audio stream:</p>
                <audio class="w-full" controls src="AnnaSetu_Complete_Hindi_Explanation.mp3"></audio>
            </div>
        </div>

    </main>

    <!-- Footer -->
    <footer class="border-t border-slate-800 bg-slate-900/50 py-4 px-6 text-center text-xs text-slate-500">
        AnnaSetu Presentation Player • Smart India Hackathon 2026 • Ministry of Consumer Affairs, Food & Public Distribution
    </footer>

    <script>
        const scenesData = """ + str(SCENES).replace("True", "true").replace("False", "false") + """;
        let currentIndex = 0;
        const audioPlayer = document.getElementById("main-audio-player");

        function selectScene(index) {
            if (index < 0 || index >= scenesData.length) return;
            currentIndex = index;
            const scene = scenesData[index];

            document.getElementById("current-title").innerText = scene.title;
            document.getElementById("current-badge").innerText = scene.badge;
            document.getElementById("current-duration").innerText = scene.duration_est;
            document.getElementById("current-visual").innerHTML = "🖥️ <b>Visual:</b> " + scene.visual_desc;
            document.getElementById("current-text").innerText = scene.text;

            audioPlayer.src = scene.audio_file;
            audioPlayer.play().catch(e => console.log("Audio autoplay blocked by browser, click play"));

            // Update playlist styles
            scenesData.forEach((_, idx) => {
                const card = document.getElementById("playlist-card-" + idx);
                if (card) {
                    if (idx === index) {
                        card.className = "scene-card p-4 rounded-2xl border border-emerald-500 bg-emerald-950/40 cursor-pointer scale-[1.02] shadow-lg transition-all space-y-1";
                    } else {
                        card.className = "scene-card p-4 rounded-2xl border border-slate-800 bg-slate-900/60 cursor-pointer hover:border-emerald-500 transition-all space-y-1";
                    }
                }
            });
        }

        function playCurrentScene() {
            audioPlayer.play();
        }

        function nextScene() {
            if (currentIndex < scenesData.length - 1) {
                selectScene(currentIndex + 1);
            }
        }

        function prevScene() {
            if (currentIndex > 0) {
                selectScene(currentIndex - 1);
            }
        }

        // Auto-advance when scene audio finishes
        audioPlayer.addEventListener("ended", () => {
            if (currentIndex < scenesData.length - 1) {
                setTimeout(() => selectScene(currentIndex + 1), 1000);
            }
        });
    </script>
</body>
</html>
    """

    player_path = os.path.join(OUTPUT_DIR, "AnnaSetu_Hindi_Video_Player.html")
    with open(player_path, "w", encoding="utf-8") as f:
        f.write(player_html)

    print(f"✅ Interactive Presentation Player generated at: {player_path}")

if __name__ == "__main__":
    generate_audio()
    generate_html_video_player()
