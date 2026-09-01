/**
 * AnnaSetu Universal Client App & Dynamic Full-DOM i18n Localization Engine
 * Supports 5 Languages: English (en), Hindi (hi), Punjabi (pa), Marathi (mr), and Telugu (te)
 */

const I18N_DICTIONARY = {
    en: {
        "brand_name": "AnnaSetu",
        "brand_tagline": "“A bridge that connects farmers”",
        "portal_title": "AnnaSetu Portal",
        
        // Navigation & Header
        "nav_home": "Dashboard",
        "nav_book": "Sell Crop",
        "nav_ai": "AI Advisor",
        "nav_prices": "Market Prices",
        "nav_centers": "Nearby Mandis",
        "nav_track": "Mandi Token",
        "nav_sales": "My Sales & Earnings",
        "nav_staff": "Staff Board",
        "nav_admin": "Ministry Admin",
        "nav_ivr": "Voice / IVR Sim",
        "nav_offline": "Offline SMS / USSD",
        "nav_help": "Help & Support",
        "simple_mode": "Simple Kisan Mode",
        "role_farmer": "Farmer",
        "role_staff": "Mandi Staff",
        "live_status": "Live",
        "ask_voice": "Ask by Voice",
        
        // Portals & Login
        "farmer_portal_title": "Farmer Portal",
        "farmer_portal_desc": "Crop slot booking, live token queue tracking, nearby mandi MSP comparison & bank DBT earnings.",
        "btn_sell_crop": "🌾 Sell Crop →",
        "staff_portal_title": "Staff Operator Console",
        "staff_portal_desc": "Gate entry check-in, IoT digital weighbridge scale, quality moisture test & instant DBT approval.",
        "btn_staff_login": "🏛️ Staff Login →",
        
        // Step 1: Farmer Details
        "step_1_title": "1. Farmer Details",
        "step_1_sub": "Under whose name token will be issued",
        "farmer_name_label": "Farmer Full Name *",
        "farmer_phone_label": "Mobile Number (10-Digit) *",
        "farmer_village_label": "Village / Gram *",
        "farmer_district_label": "District *",
        "btn_listen_form": "📢 Listen to Form",
        "btn_demo_profile": "⚡ Auto-Fill Demo",
        "btn_listen": "🔊 Listen",
        "bhulekh_title": "e-Bhulekh Land Record Verified",
        "bhulekh_sub": "Land: 4.50 Acres (Khasra #214/12) • Max MSP Quota: 90.0 Qtl",
        "bhulekh_quota_ok": "✓ Quota within limit",
        "weather_title": "IMD Mandi Weather Guard",
        "weather_sub": "Karnal Center: 28.5°C • Clear Skies • Rain Risk: 8% (Safe)",
        "btn_listen_weather": "🔊 Listen Weather",
        
        // Step 2: Crop & Quantity
        "step_2_title": "2. Select Crop & Transport Vehicle",
        "step_2_sub": "Tap picture to select your produce",
        "tap_crop_label": "Tap your crop:",
        "crop_wheat": "Wheat (गेहूं)",
        "crop_mustard": "Mustard (सरसों)",
        "crop_paddy": "Paddy (धान)",
        "crop_soybean": "Soybean (सोयाबीन)",
        "crop_maize": "Maize (मक्का)",
        "qty_label": "Estimated Quantity in Quintals *",
        "qty_hint": "1 Quintal = 100 Kilograms",
        "quick_pick": "Quick Pick:",
        "qtl_suffix": "Quintals",
        "vehicle_label": "Choose Transport Vehicle *",
        "veh_tractor": "Tractor Trolley",
        "veh_large": "Large Tractor (2 Trolleys)",
        "veh_mini": "Mini Truck / Pickup",
        "veh_truck": "Commercial Truck",
        "veh_bullock": "Bullock Cart / Jugad",
        "veh_num_label": "Vehicle Number (Optional)",
        "kisan_sawaari_title": "Kisan Sawaari (Shared Trolley Pooling)",
        "kisan_sawaari_sub": "Pool with 2 neighboring farmers in Taraori & save ₹1,200 freight.",
        "btn_sawaari": "✓ Activate Shared Trolley",
        "payout_title": "Assured Govt MSP Payout",
        "payout_sub": "Quantity × 2026 MSP Rate • Direct to Bank Account (DBT)",
        "btn_listen_amount": "🔊 Listen Amount in Voice",
        "rate_label": "Govt Rate:",
        
        // Step 3: Mandi & Time Slot
        "step_3_title": "3. Select Mandi & Time Slot",
        "step_3_sub": "Procurement center & scheduled arrival",
        "mandi_label": "Procurement Mandi *",
        "slot_label": "Arrival Time Slot *",
        "slot_green": "🟢 Morning 07:00 - 09:00 (Green Corridor • <20 Mins Fast)",
        "slot_morning": "🌅 Morning 09:00 - 11:00 (Standard)",
        "slot_midday": "☀️ Midday 11:00 - 01:00",
        "slot_afternoon": "🌤️ Afternoon 02:00 - 04:00",
        "slot_evening": "🌇 Evening 04:00 - 06:00",
        "btn_submit_booking": "✨ Book Guaranteed MSP Slot Now →",
        "submit_hint": "SMS token will be sent instantly to your registered mobile.",
        
        // 5-Stage Live Tracker
        "stage_1_title": "1. Slot Booked",
        "stage_1_desc": "Self-booking confirmed",
        "stage_2_title": "2. Gate Entry",
        "stage_2_desc": "Vehicle in mandi queue",
        "stage_3_title": "3. Weighbridge Scale",
        "stage_3_desc": "Digital gross weight recorded",
        "stage_4_title": "4. Quality Lab",
        "stage_4_desc": "Moisture & grade certified (FAQ A)",
        "stage_5_title": "5. DBT Payment Done",
        "stage_5_desc": "Direct bank transfer credited",
        "farmers_ahead_label": "Vehicles Ahead in Queue",
        "est_wait_label": "Estimated Wait Time",
        "progress_title": "Procurement Stage Progress",
        "btn_listen_status": "🔊 Listen Status (Voice)",
        "btn_print_receipt": "🖨️ Print e-Receipt / Save PDF",
        "btn_ai_grain": "📸 AI Grain Scanner",
        "btn_enwr_loan": "🏦 e-NWR 75% Advance Loan @ 4% KCC",
        
        // Toast
        "lang_switched": "Language switched to English"
    },
    hi: {
        "brand_name": "अन्नसेतु",
        "brand_tagline": "“A bridge that connects farmers”",
        "portal_title": "अन्नसेतु पोर्टल",
        
        // Navigation & Header
        "nav_home": "डैशबोर्ड",
        "nav_book": "फसल बेचें",
        "nav_ai": "एआई सलाहकार",
        "nav_prices": "मंडी भाव",
        "nav_centers": "नज़दीकी मंडियां",
        "nav_track": "मंडी टोकन",
        "nav_sales": "मेरी बिक्री व कमाई",
        "nav_staff": "स्टाफ बोर्ड",
        "nav_admin": "मंत्रालय एनालिटिक्स",
        "nav_ivr": "वॉयस / IVR डेमो",
        "nav_offline": "ऑफ़लाइन SMS / USSD",
        "nav_help": "सहायता व सपोर्ट",
        "simple_mode": "सरल किसान मोड",
        "role_farmer": "किसान",
        "role_staff": "मंडी स्टाफ",
        "live_status": "लाइव",
        "ask_voice": "बोलकर पूछें",
        
        // Portals & Login
        "farmer_portal_title": "किसान पोर्टल (Farmer Portal)",
        "farmer_portal_desc": "फसल स्लॉट बुकिंग, लाइव टोकन ट्रैकिंग, नज़दीकी मंडी भाव तुलना एवं कुल बैंक डीबीटी कमाई देखें।",
        "btn_sell_crop": "🌾 फसल बेचें →",
        "staff_portal_title": "मंडी स्टाफ ऑपरेटर कंसोल",
        "staff_portal_desc": "गेट एंट्री चेक-इन, इलेक्ट्रॉनिक धर्मकांटा तौल, लैब नमी जांच एवं प्रत्यक्ष डीबीटी भुगतान मंजूरी।",
        "btn_staff_login": "🏛️ स्टाफ लॉगिन →",
        
        // Step 1: Farmer Details
        "step_1_title": "१. किसान का नाम और पता (Farmer Details)",
        "step_1_sub": "जिसके नाम पर टोकन जारी होगा",
        "farmer_name_label": "👤 किसान का पूरा नाम (Farmer Name) *",
        "farmer_phone_label": "📱 मोबाइल नंबर (10-Digit Mobile) *",
        "farmer_village_label": "🏡 गाँव का नाम (Village / Gram) *",
        "farmer_district_label": "📍 ज़िला (District) *",
        "btn_listen_form": "📢 पूरा फॉर्म सुनें",
        "btn_demo_profile": "⚡ डेमो प्रोफाइल भरें",
        "btn_listen": "🔊 सुनें",
        "bhulekh_title": "e-Bhulekh डिजिटल भूमि रिकॉर्ड सत्यापित",
        "bhulekh_sub": "भूमि: 4.50 एकड़ (खसरा #214/12, तरावड़ी) • अधिकतम स्वीकृत MSP कोटा: 90.0 क्विंटल (गेहूं)",
        "bhulekh_quota_ok": "✓ कोटा सीमा के अंदर",
        "weather_title": "IMD मंडी मौसम गार्ड (Weather Guard)",
        "weather_sub": "करनाल उपार्जन केंद्र: 28.5°C • साफ मौसम • वर्षा जोखिम: 8% (खुली ट्रॉली सुरक्षित)",
        "btn_listen_weather": "🔊 मौसम सुनें (Weather Audio)",
        
        // Step 2: Crop & Quantity
        "step_2_title": "२. फसल और वाहन चुनें (Select Crop & Quantity)",
        "step_2_sub": "चित्र देखकर अपनी फसल पर टच करें",
        "tap_crop_label": "अपनी फसल का चित्र चुनें (Tap your crop):",
        "crop_wheat": "गेहूं (Wheat)",
        "crop_mustard": "सरसों (Mustard)",
        "crop_paddy": "धान (Paddy)",
        "crop_soybean": "सोयाबीन (Soybean)",
        "crop_maize": "मक्का (Maize)",
        "qty_label": "⚖️ अनुमानित फसल मात्रा - क्विंटल में (Quantity in Quintals) *",
        "qty_hint": "1 क्विंटल = 100 किलोग्राम",
        "quick_pick": "त्वरित चुनें:",
        "qtl_suffix": "क्विंटल",
        "vehicle_label": "🚜 वाहन का प्रकार चुनें (Transport Vehicle) *",
        "veh_tractor": "ट्रैक्टर ट्रॉली",
        "veh_large": "बड़ा ट्रैक्टर",
        "veh_mini": "छोटा हाथी / पिकअप",
        "veh_truck": "बड़ा ट्रक",
        "veh_bullock": "बैलगाड़ी / जुगाड़",
        "veh_num_label": "गाड़ी नंबर (Vehicle Number - Optional)",
        "kisan_sawaari_title": "किसान सवारी (Kisan Sawaari) • किराया सांझा पूलिंग",
        "kisan_sawaari_sub": "तरावड़ी के 2 अन्य किसान इसी दिन करनाल मंडी जा रहे हैं। सांझा ट्रॉली से 66% भाड़ा बचाएं।",
        "btn_sawaari": "✓ सांझा ट्रॉली सक्रिय करें",
        "payout_title": "गारंटीड सरकारी MSP भुगतान (Assured Payment)",
        "payout_sub": "मात्रा × सरकारी समर्थन मूल्य (2026 दर) • सीधे बैंक खाते में DBT ट्रांसफर",
        "btn_listen_amount": "🔊 यह राशि आवाज़ में सुनें",
        "rate_label": "सरकारी दर:",
        
        // Step 3: Mandi & Time Slot
        "step_3_title": "३. मंडी और समय चुनें (Select Mandi & Time)",
        "step_3_sub": "उपार्जन केंद्र एवं पहुंचने का स्लॉट",
        "mandi_label": "🏛️ उपार्जन अनाज मंडी (Procurement Mandi) *",
        "slot_label": "⏰ पहुंचने का समय स्लॉट (Arrival Time) *",
        "slot_green": "🟢 सुबह 07:00 - 09:00 (ग्रीन कॉरिडोर • <20 मिनट त्वरित तौल)",
        "slot_morning": "🌅 सुबह 09:00 - 11:00 (मानक स्लॉट)",
        "slot_midday": "☀️ दोपहर 11:00 - 01:00",
        "slot_afternoon": "🌤️ दोपहर 02:00 - 04:00",
        "slot_evening": "🌇 शाम 04:00 - 06:00",
        "btn_submit_booking": "✨ गारंटीड सरकारी MSP स्लॉट बुक करें →",
        "submit_hint": "टोकन बनते ही आपके मोबाइल पर तुरंत SMS संदेश भेजा जाएगा।",
        
        // 5-Stage Live Tracker
        "stage_1_title": "१. स्लॉट बुक (Booked)",
        "stage_1_desc": "टोकन जारी & स्लॉट आवंटित",
        "stage_2_title": "२. गेट एंट्री (Gate Entry)",
        "stage_2_desc": "मंडी गेट में प्रवेश & कतार",
        "stage_3_title": "३. धर्मकांटा तौल (Scale)",
        "stage_3_desc": "गाड़ी का सकल वजन दर्ज",
        "stage_4_title": "४. गुणवत्ता जांच (Lab)",
        "stage_4_desc": "नमी व ग्रेड प्रमाणित (FAQ A)",
        "stage_5_title": "५. बैंक भुगतान (DBT Paid)",
        "stage_5_desc": "सीधे खाते में पैसे ट्रांसफर",
        "farmers_ahead_label": "कतार में आगे वाहन",
        "est_wait_label": "अनुमानित प्रतीक्षा समय",
        "progress_title": "उपार्जन प्रगति (Procurement Stage Progress)",
        "btn_listen_status": "🔊 स्थिति सुनें (Listen)",
        "btn_print_receipt": "🖨️ ई-रसीद प्रिंट करें / Save PDF",
        "btn_ai_grain": "📸 AI दाना स्कैनर",
        "btn_enwr_loan": "🏦 ई-गिरवी ऋण सुविधा (e-NWR 75% Advance Loan @ 4% KCC)",
        
        // Toast
        "lang_switched": "भाषा बदलकर हिन्दी कर दी गई है"
    },
    pa: {
        "brand_name": "ਅੰਨਸੇਤੂ",
        "brand_tagline": "“A bridge that connects farmers”",
        "portal_title": "ਅੰਨਸੇਤੂ ਪੋਰਟਲ",
        
        // Navigation & Header
        "nav_home": "ਡੈਸ਼ਬੋਰਡ",
        "nav_book": "ਫ਼ਸਲ ਵੇਚੋ",
        "nav_ai": "ਏਆਈ ਸਲਾਹਕਾਰ",
        "nav_prices": "ਮੰਡੀ ਭਾਅ",
        "nav_centers": "ਨੇੜਲੀਆਂ ਮੰਡੀਆਂ",
        "nav_track": "ਮੰਡੀ ਟੋਕਨ",
        "nav_sales": "ਮੇਰੀ ਵਿਕਰੀ ਅਤੇ ਕਮਾਈ",
        "nav_staff": "ਸਟਾਫ ਬੋਰਡ",
        "nav_admin": "ਮੰਤਰਾਲਾ ਪ੍ਰਬੰਧਨ",
        "nav_ivr": "ਆਵਾਜ਼ / IVR ਸਿਮ",
        "nav_offline": "ਆਫਲਾਈਨ SMS / USSD",
        "nav_help": "ਸਹਾਇਤਾ",
        "simple_mode": "ਸਰਲ ਕਿਸਾਨ ਮੋਡ",
        "role_farmer": "ਕਿਸਾਨ",
        "role_staff": "ਮੰਡੀ ਸਟਾਫ",
        "live_status": "ਲਾਈਵ",
        "ask_voice": "ਬੋਲ ਕੇ ਪੁੱਛੋ",
        
        // Portals & Login
        "farmer_portal_title": "ਕਿਸਾਨ ਪੋਰਟਲ (Farmer Portal)",
        "farmer_portal_desc": "ਫ਼ਸਲ ਸਲਾਟ ਬੁਕਿੰਗ, ਲਾਈਵ ਟੋਕਨ ਟਰੈਕਿੰਗ, ਨੇੜਲੇ ਮੰਡੀ ਭਾਅ ਅਤੇ ਬੈਂਕ DBT ਕਮਾਈ ਦੇਖੋ।",
        "btn_sell_crop": "🌾 ਫ਼ਸਲ ਵੇਚੋ →",
        "staff_portal_title": "ਸਟਾਫ ਆਪਰੇਟਰ ਲੌਗਿਨ",
        "staff_portal_desc": "ਗੇਟ ਐਂਟਰੀ, ਕੰਪਿਊਟਰ ਕੰਡਾ ਤੋਲ, ਗੁਣਵੱਤਾ ਟੈਸਟਿੰਗ ਅਤੇ ਸਿੱਧਾ ਬੈਂਕ DBT ਭੁਗਤਾਨ।",
        "btn_staff_login": "🏛️ ਸਟਾਫ ਲੌਗਿਨ →",
        
        // Step 1: Farmer Details
        "step_1_title": "੧. ਕਿਸਾਨ ਦਾ ਵੇਰਵਾ (Farmer Details)",
        "step_1_sub": "ਜਿਸਦੇ ਨਾਮ ਤੇ ਟੋਕਨ ਬਣੇਗਾ",
        "farmer_name_label": "👤 ਕਿਸਾਨ ਦਾ ਪੂਰਾ ਨਾਮ (Farmer Name) *",
        "farmer_phone_label": "📱 ਮੋਬਾਈਲ ਨੰਬਰ (10-Digit Mobile) *",
        "farmer_village_label": "🏡 ਪਿੰਡ ਦਾ ਨਾਮ (Village / Gram) *",
        "farmer_district_label": "📍 ਜ਼ਿਲ੍ਹਾ (District) *",
        "btn_listen_form": "📢 ਪੂਰਾ ਫਾਰਮ ਸੁਣੋ",
        "btn_demo_profile": "⚡ ਡੈਮੋ ਪ੍ਰੋਫਾਈਲ ਭਰੋ",
        "btn_listen": "🔊 ਸੁਣੋ",
        "bhulekh_title": "ਈ-ਭੂਲੇਖ ਜ਼ਮੀਨੀ ਰਿਕਾਰਡ ਤਸਦੀਕਸ਼ੁਦਾ",
        "bhulekh_sub": "ਜ਼ਮੀਨ: 4.50 ਏਕੜ (ਖਸਰਾ #214/12) • ਸਰਕਾਰੀ ਕੋਟਾ: 90.0 ਕੁਇੰਟਲ",
        "bhulekh_quota_ok": "✓ ਕੋਟਾ ਸੀਮਾ ਅੰਦਰ",
        "weather_title": "IMD ਮੰਡੀ ਮੌਸਮ ਗਾਰਡ",
        "weather_sub": "ਕਰਨਾਲ ਖਰੀਦ ਕੇਂਦਰ: 28.5°C • ਸਾਫ ਮੌਸਮ • ਮੀਂਹ ਖਤਰਾ: 8% (ਸੁਰੱਖਿਅਤ)",
        "btn_listen_weather": "🔊 ਮੌਸਮ ਸੁਣੋ",
        
        // Step 2: Crop & Quantity
        "step_2_title": "੨. ਫ਼ਸਲ ਅਤੇ ਵਾਹਨ ਚੁਣੋ (Select Crop & Vehicle)",
        "step_2_sub": "ਫੋਟੋ ਦੇਖ ਕੇ ਆਪਣੀ ਫ਼ਸਲ ਚੁਣੋ",
        "tap_crop_label": "ਆਪਣੀ ਫ਼ਸਲ ਚੁਣੋ (Tap your crop):",
        "crop_wheat": "ਕਣਕ (Wheat)",
        "crop_mustard": "ਸਰ੍ਹੋਂ (Mustard)",
        "crop_paddy": "ਝੋਨਾ (Paddy)",
        "crop_soybean": "ਸੋਇਆਬੀਨ (Soybean)",
        "crop_maize": "ਮੱਕੀ (Maize)",
        "qty_label": "⚖️ ਅੰਦਾਜ਼ਨ ਫ਼ਸਲ ਮਾਤਰਾ - ਕੁਇੰਟਲ ਵਿੱਚ *",
        "qty_hint": "1 ਕੁਇੰਟਲ = 100 ਕਿਲੋਗ੍ਰਾਮ",
        "quick_pick": "ਤੁਰੰਤ ਚੁਣੋ:",
        "qtl_suffix": "ਕੁਇੰਟਲ",
        "vehicle_label": "🚜 ਵਾਹਨ ਦੀ ਕਿਸਮ ਚੁਣੋ (Transport Vehicle) *",
        "veh_tractor": "ਟਰੈਕਟਰ ਟਰਾਲੀ",
        "veh_large": "ਵੱਡਾ ਟਰੈਕਟਰ (2 ਟਰਾਲੀ)",
        "veh_mini": "ਛੋਟਾ ਹਾਥੀ / ਪਿਕਅੱਪ",
        "veh_truck": "ਵੱਡਾ ਟਰੱਕ",
        "veh_bullock": "ਬੈਲਗੱਡੀ / ਜੁਗਾੜ",
        "veh_num_label": "ਗੱਡੀ ਨੰਬਰ (ਵਿਕਲਪਿਕ)",
        "kisan_sawaari_title": "ਕਿਸਾਨ ਸਵਾਰੀ (ਸਾਂਝਾ ਟਰਾਲੀ ਪੂਲਿੰਗ)",
        "kisan_sawaari_sub": "ਪਿੰਡ ਦੇ ਹੋਰ ਕਿਸਾਨਾਂ ਨਾਲ ਟਰਾਲੀ ਸਾਂਝੀ ਕਰੋ ਅਤੇ ₹1,200 ਕਿਰਾਇਆ ਬਚਾਓ।",
        "btn_sawaari": "✓ ਸਾਂਝੀ ਟਰਾਲੀ ਚਾਲੂ ਕਰੋ",
        "payout_title": "ਯਕੀਨੀ ਸਰਕਾਰੀ MSP ਭੁਗਤਾਨ",
        "payout_sub": "ਮਾਤਰਾ × ਸਰਕਾਰੀ ਮੁੱਲ (2026 ਦਰ) • ਸਿੱਧਾ ਬੈਂਕ ਖਾਤੇ ਵਿੱਚ DBT",
        "btn_listen_amount": "🔊 ਇਹ ਰਕਮ ਸੁਣੋ",
        "rate_label": "ਸਰਕਾਰੀ ਮੁੱਲ:",
        
        // Step 3: Mandi & Time Slot
        "step_3_title": "੩. ਮੰਡੀ ਅਤੇ ਸਮਾਂ ਚੁਣੋ (Mandi & Time)",
        "step_3_sub": "ਖਰੀਦ ਕੇਂਦਰ ਅਤੇ ਪਹੁੰਚਣ ਦਾ ਸਮਾਂ",
        "mandi_label": "🏛️ ਖਰੀਦ ਅਨਾਜ ਮੰਡੀ *",
        "slot_label": "⏰ ਪਹੁੰਚਣ ਦਾ ਸਮਾਂ ਸਲਾਟ *",
        "slot_green": "🟢 ਸਵੇਰੇ 07:00 - 09:00 (ਗ੍ਰੀਨ ਕੋਰੀਡੋਰ • <20 ਮਿੰਟ ਤੋਲ)",
        "slot_morning": "🌅 ਸਵੇਰੇ 09:00 - 11:00 (ਮਿਆਰੀ ਸਲਾਟ)",
        "slot_midday": "☀️ ਦੁਪਹਿਰ 11:00 - 01:00",
        "slot_afternoon": "🌤️ ਦੁਪਹਿਰ 02:00 - 04:00",
        "slot_evening": "🌇 ਸ਼ਾਮ 04:00 - 06:00",
        "btn_submit_booking": "✨ ਸਰਕਾਰੀ MSP ਸਲਾਟ ਬੁੱਕ ਕਰੋ →",
        "submit_hint": "ਟੋਕਨ ਬਣਦੇ ਹੀ ਤੁਹਾਡੇ ਮੋਬਾਈਲ ਤੇ SMS ਭੇਜਿਆ ਜਾਵੇਗਾ।",
        
        // 5-Stage Live Tracker
        "stage_1_title": "੧. ਸਲਾਟ ਬੁੱਕ (Booked)",
        "stage_1_desc": "ਬੁਕਿੰਗ ਪੱਕੀ ਹੋਈ",
        "stage_2_title": "੨. ਗੇਟ ਐਂਟਰੀ (Gate Entry)",
        "stage_2_desc": "ਮੰਡੀ ਗੇਟ ਤੇ ਆਮਦ",
        "stage_3_title": "੩. ਕੰਪਿਊਟਰ ਕੰਡਾ ਤੋਲ (Scale)",
        "stage_3_desc": "ਡਿਜੀਟਲ ਤੋਲ ਦਰਜ",
        "stage_4_title": "੪. ਗੁਣਵੱਤਾ ਪਰਖ (Lab)",
        "stage_4_desc": "ਨਮੀ ਅਤੇ ਗਰੇਡ ਪਾਸ (FAQ A)",
        "stage_5_title": "੫. ਸਿੱਧਾ ਬੈਂਕ ਭੁਗਤਾਨ (DBT)",
        "stage_5_desc": "ਸਿੱਧਾ ਖਾਤੇ ਵਿੱਚ ਪੈਸੇ ਟਰਾਂਸਫਰ",
        "farmers_ahead_label": "ਅੱਗੇ ਲਾਈਨ ਵਿੱਚ ਗੱਡੀਆਂ",
        "est_wait_label": "ਅੰਦਾਜ਼ਨ ਉਡੀਕ ਸਮਾਂ",
        "progress_title": "ਖਰੀਦ ਪ੍ਰਗਤੀ (Procurement Progress)",
        "btn_listen_status": "🔊 ਸਥਿਤੀ ਸੁਣੋ (Voice)",
        "btn_print_receipt": "🖨️ ਰਸੀਦ ਪ੍ਰਿੰਟ ਕਰੋ / PDF ਸੇਵ ਕਰੋ",
        "btn_ai_grain": "📸 AI ਦਾਣਾ ਸਕੈਨਰ",
        "btn_enwr_loan": "🏦 ਈ-ਗਿਰਵੀ ਕਰਜ਼ਾ (e-NWR 75% Advance @ 4% KCC)",
        
        // Toast
        "lang_switched": "ਭਾਸ਼ਾ ਬਦਲ ਕੇ ਪੰਜਾਬੀ ਕੀਤੀ ਗਈ ਹੈ"
    },
    mr: {
        "brand_name": "अन्नसेतू",
        "brand_tagline": "“A bridge that connects farmers”",
        "portal_title": "अन्नसेतू पोर्टल",
        
        // Navigation & Header
        "nav_home": "डॅशबोर्ड",
        "nav_book": "पीक विका",
        "nav_ai": "एआय सल्लागार",
        "nav_prices": "बाजार भाव",
        "nav_centers": "जवळची मंडई",
        "nav_track": "मंडई टोकन",
        "nav_sales": "माझी विक्री व कमाई",
        "nav_staff": "कर्मचारी बोर्ड",
        "nav_admin": "मंत्रालय विश्लेषण",
        "nav_ivr": "व्हॉईਸ / IVR डेमो",
        "nav_offline": "ऑफलाईन SMS / USSD",
        "nav_help": "मदत व सपोर्ट",
        "simple_mode": "सरल शेतकरी मोड",
        "role_farmer": "शेतकरी",
        "role_staff": "मंडई कर्मचारी",
        "live_status": "थेट",
        "ask_voice": "बोलून विचारा",
        
        // Portals & Login
        "farmer_portal_title": "शेतकरी पोर्टल (Farmer Portal)",
        "farmer_portal_desc": "पीक स्लॉट बुकिंग, थेट टोकन ट्रॅकिंग, बाजार भाव तुलना आणि थेट बँक DBT कमाई पहा.",
        "btn_sell_crop": "🌾 पीक विका →",
        "staff_portal_title": "मंडई कर्मचारी लॉगिन",
        "staff_portal_desc": "गेट एंट्री, इलेक्ट्रॉनिक वजन काटा, गुणवत्ता तपासणी आणि थेट बँक खात्यात DBT मंजुरी.",
        "btn_staff_login": "🏛️ कर्मचारी लॉगिन →",
        
        // Step 1: Farmer Details
        "step_1_title": "१. शेतकऱ्याचे नाव व पत्ता (Farmer Details)",
        "step_1_sub": "ज्यांच्या नावे टोकन जारी होईल",
        "farmer_name_label": "👤 शेतकऱ्याचे पूर्ण नाव (Farmer Name) *",
        "farmer_phone_label": "📱 मोबाईल नंबर (10-Digit Mobile) *",
        "farmer_village_label": "🏡 गावाचे नाव (Village / Gram) *",
        "farmer_district_label": "📍 जिल्हा (District) *",
        "btn_listen_form": "📢 संपूर्ण फॉर्म ऐका",
        "btn_demo_profile": "⚡ डेमो प्रोफाइल भरा",
        "btn_listen": "🔊 ऐका",
        "bhulekh_title": "e-Bhulekh डिजिटल जमीन रेकॉर्ड प्रमाणित",
        "bhulekh_sub": "जमीन: 4.50 एकर (गट #214/12, तरावडी) • कमाल हमीभाव कोटा: 90.0 क्विंटल",
        "bhulekh_quota_ok": "✓ कोटा मर्यादेत",
        "weather_title": "IMD मंडई हवामान गार्ड",
        "weather_sub": "कर्नाल खरेदी केंद्र: 28.5°C • निरभ्र हवामान • पाऊस धोका: 8% (सुरक्षित)",
        "btn_listen_weather": "🔊 हवामान ऐका",
        
        // Step 2: Crop & Quantity
        "step_2_title": "२. पीक आणि वाहन निवडा (Select Crop & Quantity)",
        "step_2_sub": "चित्र पाहून आपले पीक निवडा",
        "tap_crop_label": "आपले पीक निवडा (Tap your crop):",
        "crop_wheat": "गहू (Wheat)",
        "crop_mustard": "मोहरी (Mustard)",
        "crop_paddy": "भात (Paddy)",
        "crop_soybean": "सोयाबीन (Soybean)",
        "crop_maize": "मका (Maize)",
        "qty_label": "⚖️ अंदाजे पीक प्रमाण - क्विंटल मध्ये *",
        "qty_hint": "1 क्विंटल = 100 किलोग्राम",
        "quick_pick": "जलद निवडा:",
        "qtl_suffix": "क्विंटल",
        "vehicle_label": "🚜 वाहन प्रकार निवडा (Transport Vehicle) *",
        "veh_tractor": "ट्रॅक्टर ट्रॉली",
        "veh_large": "मोठा ट्रॅक्टर",
        "veh_mini": "छोटा हत्ती / पिकअप",
        "veh_truck": "मोठा ट्रक",
        "veh_bullock": "बैलगाडी / जुगाड",
        "veh_num_label": "गाडी क्रमांक (ऐच्छिक)",
        "kisan_sawaari_title": "शेतकरी सवारी (सामायिक वाहतूक पूलिंग)",
        "kisan_sawaari_sub": "गावातील इतर शेतकऱ्यांसोबत सामायिक वाहतूक करा, ₹1,200 भाडे वाचवा.",
        "btn_sawaari": "✓ सामायिक वाहतूक सुरू करा",
        "payout_title": "हमीभाव सरकारी MSP रक्कम (Assured Payment)",
        "payout_sub": "प्रमाण × हमीभाव दर (2026 दर) • थेट बँक खात्यात DBT",
        "btn_listen_amount": "🔊 ही रक्कम आवाजात ऐका",
        "rate_label": "सरकारी दर:",
        
        // Step 3: Mandi & Time Slot
        "step_3_title": "३. मंडई व वेळ निवडा (Mandi & Time)",
        "step_3_sub": "खरेदी केंद्र व पोहोचण्याची वेळ",
        "mandi_label": "🏛️ खरेदी धान्य मंडई *",
        "slot_label": "⏰ वेळ स्लॉट (Arrival Time) *",
        "slot_green": "🟢 सकाळी 07:00 - 09:00 (ग्रीन कॉरिडॉर • <20 मिनिटे जलद)",
        "slot_morning": "🌅 सकाळी 09:00 - 11:00 (मानक स्लॉट)",
        "slot_midday": "☀️ दुपारी 11:00 - 01:00",
        "slot_afternoon": "🌤️ दुपारी 02:00 - 04:00",
        "slot_evening": "🌇 संध्याकाळी 04:00 - 06:00",
        "btn_submit_booking": "✨ हमीभाव स्लॉट बुक करा →",
        "submit_hint": "टोकन तयार होताच आपल्या मोबाईलवर SMS पाठवला जाईल.",
        
        // 5-Stage Live Tracker
        "stage_1_title": "१. स्लॉट बुक (Booked)",
        "stage_1_desc": "नोंदणी निश्चित",
        "stage_2_title": "२. गेट एंट्री (Gate Entry)",
        "stage_2_desc": "मंडई प्रवेश द्वारावर आगमन",
        "stage_3_title": "३. वजन काटा (Scale)",
        "stage_3_desc": "गाडीचे डिजिटल वजन नोंदवले",
        "stage_4_title": "४. गुणवत्ता व आर्द्रता (Lab)",
        "stage_4_desc": "आर्द्रता व दर्जा प्रमाणित (FAQ A)",
        "stage_5_title": "५. बँक खात्यात DBT जमा",
        "stage_5_desc": "थेट बँक खात्यात पैसे जमा",
        "farmers_ahead_label": "रांगेत पुढे असलेली वाहने",
        "est_wait_label": "अपेक्षित प्रतीक्षा वेळ",
        "progress_title": "खरेदी प्रगती (Procurement Progress)",
        "btn_listen_status": "🔊 स्थिती ऐका (Voice)",
        "btn_print_receipt": "🖨️ ई-पावती प्रिंट करा / PDF सेव्ह करा",
        "btn_ai_grain": "📸 AI धान्य स्कॅनर",
        "btn_enwr_loan": "🏦 ई-तारण कर्ज (e-NWR 75% Advance @ 4% KCC)",
        
        // Toast
        "lang_switched": "भाषा मराठी मध्ये बदलली आहे"
    },
    te: {
        "brand_name": "అన్నసేతు",
        "brand_tagline": "“A bridge that connects farmers”",
        "portal_title": "అన్నసేతు పోర్టల్",
        
        // Navigation & Header
        "nav_home": "డ్యాష్‌బోర్డ్",
        "nav_book": "పంట అమ్మండి",
        "nav_ai": "ఏఐ సలహాదారు",
        "nav_prices": "మార్కెట్ ధరలు",
        "nav_centers": "సమీప మార్కెట్లు",
        "nav_track": "మార్కెట్ టోకెన్",
        "nav_sales": "నా అమ్మకాలు & ఆదాయం",
        "nav_staff": "సిబ్బంది బోర్డ్",
        "nav_admin": "మంత్రిత్వ శాఖ అడ్మిన్",
        "nav_ivr": "వాయిస్ / IVR డెమో",
        "nav_offline": "ఆఫ్‌లైన్ SMS / USSD",
        "nav_help": "సహాయం",
        "simple_mode": "రైతు సరళ మోడ్",
        "role_farmer": "రైతు",
        "role_staff": "మార్కెట్ సిబ్బంది",
        "live_status": "లైవ్",
        "ask_voice": "మాట్లాడి అడగండి",
        
        // Portals & Login
        "farmer_portal_title": "రైతు పోర్టల్ (Farmer Portal)",
        "farmer_portal_desc": "పంట స్లాట్ బుకింగ్, లైవ్ టోకెన్ క్యూ ట్రాకింగ్, మార్కెట్ ధరల పోలిక మరియు నేరుగా బ్యాంక్ ఖాతాలో DBT జమ.",
        "btn_sell_crop": "🌾 పంట అమ్మండి →",
        "staff_portal_title": "మార్కెట్ సిబ్బంది లాగిన్",
        "staff_portal_desc": "గేట్ ఎంట్రీ, డిజిటల్ వేబ్రిడ్జి బరువు, నాణ్యత పరీక్ష మరియు తక్షణ DBT ఆమోదం.",
        "btn_staff_login": "🏛️ సిబ్బంది లాగిన్ →",
        
        // Step 1: Farmer Details
        "step_1_title": "1. రైతు వివరాలు (Farmer Details)",
        "step_1_sub": "ఎవరి పేరు మీద టోకెన్ జారీ చేయబడుతుందో",
        "farmer_name_label": "👤 రైతు పూర్తి పేరు (Farmer Name) *",
        "farmer_phone_label": "📱 మొబైల్ నంబర్ (10-Digit Mobile) *",
        "farmer_village_label": "🏡 గ్రామం పేరు (Village / Gram) *",
        "farmer_district_label": "📍 జిల్లా (District) *",
        "btn_listen_form": "📢 పూర్తి ఫారమ్ వినండి",
        "btn_demo_profile": "⚡ డెమో ప్రొఫైల్ నింపండి",
        "btn_listen": "🔊 వినండి",
        "bhulekh_title": "e-Bhulekh డిజిటల్ భూమి రికార్డు ధృవీకరించబడింది",
        "bhulekh_sub": "భూమి: 4.50 ఎకరాలు (ఖస్రా #214/12) • గరిష్ట MSP కోటా: 90.0 క్వింటాళ్లు",
        "bhulekh_quota_ok": "✓ కోటా పరిమితిలో ఉంది",
        "weather_title": "IMD మార్కెట్ వాతావరణ గార్డ్",
        "weather_sub": "కర్నాల్ కేంద్రం: 28.5°C • నిర్మలమైన ఆకాశం • వర్షం ప్రమాదం: 8% (సురక్షితం)",
        "btn_listen_weather": "🔊 వాతావరణం వినండి",
        
        // Step 2: Crop & Quantity
        "step_2_title": "2. పంట మరియు రవాణా వాహనం (Crop & Vehicle)",
        "step_2_sub": "చిత్రం చూసి మీ పంటను ఎంచుకోండి",
        "tap_crop_label": "మీ పంట చిత్రాన్ని ఎంచుకోండి (Tap your crop):",
        "crop_wheat": "గోధుమ (Wheat)",
        "crop_mustard": "ఆవాలు (Mustard)",
        "crop_paddy": "వరి (Paddy)",
        "crop_soybean": "సోయాబీన్ (Soybean)",
        "crop_maize": "మొక్కజొన్న (Maize)",
        "qty_label": "⚖️ అంచనా వేసిన పంట పరిమాణం - క్వింటాళ్లలో *",
        "qty_hint": "1 క్వింటాల్ = 100 కిలోగ్రాములు",
        "quick_pick": "త్వరిత ఎంపిక:",
        "qtl_suffix": "క్వింటాళ్లు",
        "vehicle_label": "🚜 రవాణా వాహనం ఎంచుకోండి (Transport Vehicle) *",
        "veh_tractor": "ట్రాక్టర్ ట్రాలీ",
        "veh_large": "పెద్ద ట్రాక్టర్",
        "veh_mini": "మినీ ట్రక్ / పికప్",
        "veh_truck": "పెద్ద ట్రక్",
        "veh_bullock": "ఎడ్ల బండి / జుగాడ్",
        "veh_num_label": "వాహనం నంబర్ (ఐచ్ఛికం)",
        "kisan_sawaari_title": "రైతు సవారీ (రవాణా ఖర్చు పంచుకోవడం)",
        "kisan_sawaari_sub": "సమీప రైతులతో కలిసి రవాణా చేయండి, ₹1,200 ఆదా చేయండి.",
        "btn_sawaari": "✓ భాగస్వామ్య ట్రాలీని ప్రారంభించండి",
        "payout_title": "హామీ ఇవ్వబడిన ప్రభుత్వ MSP చెల్లింపు",
        "payout_sub": "పరిమాణం × ప్రభుత్వ మద్దతు ధర (2026) • నేరుగా బ్యాంక్ ఖాతాలో DBT",
        "btn_listen_amount": "🔊 ఈ మొత్తం వాయిస్‌లో వినండి",
        "rate_label": "ప్రభుత్వ ధర:",
        
        // Step 3: Mandi & Time Slot
        "step_3_title": "3. మార్కెట్ మరియు సమయం (Mandi & Time)",
        "step_3_sub": "కొనుగోలు కేంద్రం మరియు సమయం",
        "mandi_label": "🏛️ కొనుగోలు మార్కెట్ *",
        "slot_label": "⏰ చేరుకునే సమయ స్లాట్ (Arrival Time) *",
        "slot_green": "🟢 ఉదయం 07:00 - 09:00 (గ్రీన్ కారిడార్ • <20 నిమిషాల వేగవంతమైనది)",
        "slot_morning": "🌅 ఉదయం 09:00 - 11:00 (ప్రామాణిక స్లాట్)",
        "slot_midday": "☀️ మధ్యాహ్నం 11:00 - 01:00",
        "slot_afternoon": "🌤️ మధ్యాహ్నం 02:00 - 04:00",
        "slot_evening": "🌇 సాయంత్రం 04:00 - 06:00",
        "btn_submit_booking": "✨ ప్రభుత్వ MSP స్లాట్ బుక్ చేయండి →",
        "submit_hint": "టోకెన్ జారీ అయిన వెంటనే మీ మొబైల్‌కు SMS పంపబడుతుంది.",
        
        // 5-Stage Live Tracker
        "stage_1_title": "1. స్లాట్ బుక్ చేయబడింది (Booked)",
        "stage_1_desc": "రిజిస్ట్రేషన్ ధృవీకరించబడింది",
        "stage_2_title": "2. గేట్ ఎంట్రీ (Gate Entry)",
        "stage_2_desc": "మార్కెట్ గేట్ వద్ద వాహనం రాక",
        "stage_3_title": "3. వేబ్రిడ్జి బరువు (Scale)",
        "stage_3_desc": "డిజిటల్ బరువు రికార్డ్ అయింది",
        "stage_4_title": "4. నాణ్యత పరీక్ష (Lab)",
        "stage_4_desc": "తేమ మరియు గ్రేడ్ ధృవీకరించబడింది (FAQ A)",
        "stage_5_title": "5. DBT చెల్లింపు పూర్తయింది",
        "stage_5_desc": "బ్యాంక్ ఖాతాలో జమ అయింది",
        "farmers_ahead_label": "క్యూలో ముందున్న వాహనాలు",
        "est_wait_label": "అంచనా వేచి ఉండే సమయం",
        "progress_title": "కొనుగోలు పురోగతి (Procurement Progress)",
        "btn_listen_status": "🔊 స్థితి వినండి (Voice)",
        "btn_print_receipt": "🖨️ రసీదు ప్రింట్ / PDF సేవ్ చేయండి",
        "btn_ai_grain": "📸 AI గింజల నాణ్యత స్కానర్",
        "btn_enwr_loan": "🏦 ఈ-తాకట్టు రుణం (e-NWR 75% Advance @ 4% KCC)",
        
        // Toast
        "lang_switched": "భాష తెలుగులోకి మార్చబడింది"
    }
};

let currentLang = localStorage.getItem("annasetu_lang") || "en";

/**
 * Universal Recursive Full-DOM Translation Function
 */
function setLanguage(lang) {
    if (!I18N_DICTIONARY[lang]) lang = "en";
    currentLang = lang;
    localStorage.setItem("annasetu_lang", lang);

    const targetDict = I18N_DICTIONARY[lang];
    const enDict = I18N_DICTIONARY.en;
    const hiDict = I18N_DICTIONARY.hi;

    // 1. Explicit data-i18n Tag Translation
    document.querySelectorAll("[data-i18n]").forEach(elem => {
        const key = elem.getAttribute("data-i18n");
        if (targetDict[key]) {
            if (elem.tagName === "INPUT" || elem.tagName === "TEXTAREA") {
                if (elem.getAttribute("placeholder")) elem.placeholder = targetDict[key];
            } else {
                elem.innerText = targetDict[key];
            }
        }
    });

    // 2. Comprehensive Direct DOM Text Replacements
    // Helper to find and replace text inside selector or by direct text match
    function updateText(selector, newText) {
        if (!newText) return;
        const els = document.querySelectorAll(selector);
        els.forEach(el => {
            if (el.children.length === 0 || el.childNodes.length === 1) {
                el.innerText = newText;
            }
        });
    }

    // Header & Brand
    updateText("#role-farmer-btn span.hidden", targetDict.role_farmer);
    updateText("#role-staff-btn span.hidden", targetDict.role_staff);
    updateText("#ws-status-text", targetDict.live_status);
    updateText(".floating-voice-btn span:last-child, button[onclick='openVoiceQueryModal()'] span:last-child", targetDict.ask_voice);
    updateText("#simple-mode-text", targetDict.simple_mode);

    // Navigation Links
    updateText("#nav-dash span:last-child", targetDict.nav_home);
    updateText("#nav-sell span:last-child", targetDict.nav_book);
    updateText("#nav-ai span:first-child", targetDict.nav_ai);
    updateText("button[onclick='openPricesModal()'] span:last-child", targetDict.nav_prices);
    updateText("#nav-mandis span:last-child", targetDict.nav_centers);
    updateText("#nav-token span:last-child", targetDict.nav_track);
    updateText("#nav-sales span:last-child", targetDict.nav_sales);
    updateText("#nav-staff span:last-child", targetDict.nav_staff);
    updateText("#nav-admin span:last-child", targetDict.nav_admin);
    updateText("#nav-ivr span:last-child", targetDict.nav_ivr);
    updateText("button[onclick='openOfflineSmsModal()'] span.font-bold span:first-child", targetDict.nav_offline);
    updateText("button[onclick='openHelpModal()'] span:last-child", targetDict.nav_help);

    // Form Section 1
    updateText("#slot-booking-form h3[data-i18n='step_1_title'], #slot-booking-form .step-1-title", targetDict.step_1_title);
    updateText("button[onclick*=\"speakSectionHelp('intro')\"] span:last-child", targetDict.btn_listen_form);
    updateText("button[onclick*=\"fillDemoFarmerProfile\"] span:last-child", targetDict.btn_demo_profile);
    updateText("button[onclick*=\"speakSectionHelp('profile')\"] span:last-child", targetDict.btn_listen);
    updateText("button[onclick*=\"speakSectionHelp('crop')\"] span:last-child", targetDict.btn_listen);
    updateText("button[onclick*=\"speakSectionHelp('slot')\"] span:last-child", targetDict.btn_listen);

    // Labels
    document.querySelectorAll("label").forEach(lbl => {
        const txt = lbl.innerText.trim();
        if (txt.includes("किसान का पूरा नाम") || txt.includes("Farmer Name") || txt.includes("రైతు పూర్తి పేరు") || txt.includes("ਸ਼ਾਨ ਦਾ ਪੂਰਾ ਨਾਮ")) {
            lbl.innerText = targetDict.farmer_name_label;
        } else if (txt.includes("मोबाइल नंबर") || txt.includes("Mobile") || txt.includes("ਮੋਬਾਈਲ") || txt.includes("మొబైల్")) {
            lbl.innerText = targetDict.farmer_phone_label;
        } else if (txt.includes("गाँव का नाम") || txt.includes("Village") || txt.includes("ਪਿੰਡ") || txt.includes("గ్రామం")) {
            lbl.innerText = targetDict.farmer_village_label;
        } else if (txt.includes("ज़िला") || txt.includes("District") || txt.includes("ਜ਼ਿਲ੍ਹਾ") || txt.includes("జిల్లా") || txt.includes("जिल्हा")) {
            lbl.innerText = targetDict.farmer_district_label;
        } else if (txt.includes("मात्रा") || txt.includes("Quantity in Quintals") || txt.includes("ਮਾਤਰਾ") || txt.includes("పరిమాణం")) {
            lbl.innerText = targetDict.qty_label;
        } else if (txt.includes("वाहन का प्रकार") || txt.includes("Transport Vehicle") || txt.includes("ਵਾਹਨ") || txt.includes("వాహనం")) {
            lbl.innerText = targetDict.vehicle_label;
        } else if (txt.includes("गाड़ी नंबर") || txt.includes("Vehicle Number") || txt.includes("గdraft")) {
            lbl.innerText = targetDict.veh_num_label;
        } else if (txt.includes("उपार्जन अनाज मंडी") || txt.includes("Procurement Mandi") || txt.includes("కొనుగోలు మార్కెట్")) {
            lbl.innerText = targetDict.mandi_label;
        } else if (txt.includes("पहुंचने का समय") || txt.includes("Arrival Time") || txt.includes("చేరుకునే సమయ")) {
            lbl.innerText = targetDict.slot_label;
        }
    });

    // Step Titles & Subtitles
    updateText("#quota-status-badge", targetDict.bhulekh_quota_ok);
    updateText("#crop-card-wheat h4", targetDict.crop_wheat);
    updateText("#crop-card-mustard h4", targetDict.crop_mustard);
    updateText("#crop-card-paddy h4", targetDict.crop_paddy);
    updateText("#crop-card-soybean h4", targetDict.crop_soybean);
    updateText("#crop-card-maize h4", targetDict.crop_maize);

    updateText("#vehicle-card-tractor p", targetDict.veh_tractor);
    updateText("#vehicle-card-large p", targetDict.veh_large);
    updateText("#vehicle-card-mini p", targetDict.veh_mini);
    updateText("#vehicle-card-commercial p", targetDict.veh_truck);
    updateText("#vehicle-card-bullock p", targetDict.veh_bullock);

    updateText("#submit-book-btn span:last-child", targetDict.btn_submit_booking);
    updateText("#pooling-toggle-btn", targetDict.btn_sawaari);

    // Dynamic Time Slot Options Translation
    const slotSelect = document.getElementById("slot-select");
    if (slotSelect) {
        const slotMap = {
            "07:00 AM - 09:00 AM": targetDict.slot_green,
            "09:00 AM - 11:00 AM": targetDict.slot_morning,
            "11:00 AM - 01:00 PM": targetDict.slot_midday,
            "02:00 PM - 04:00 PM": targetDict.slot_afternoon,
            "04:00 PM - 06:00 PM": targetDict.slot_evening
        };
        Array.from(slotSelect.options).forEach(opt => {
            if (slotMap[opt.value]) {
                opt.innerText = slotMap[opt.value];
            }
        });
    }

    // Dynamic Placeholders Translation
    const nameInput = document.getElementById("farmer-name");
    const phoneInput = document.getElementById("farmer-phone");
    const villageInput = document.getElementById("farmer-village");
    const districtInput = document.getElementById("farmer-district");
    const vehicleNumInput = document.getElementById("vehicle-num");

    if (nameInput) {
        nameInput.placeholder = {
            en: "Enter Farmer Full Name",
            hi: "किसान का पूरा नाम दर्ज करें",
            pa: "ਕਿਸਾਨ ਦਾ ਪੂਰਾ ਨਾਮ ਭਰੋ",
            mr: "शेतकऱ्याचे पूर्ण नाव प्रविष्ट करा",
            te: "రైతు పూర్తి పేరు నమోదు చేయండి"
        }[lang] || "Enter Farmer Full Name";
    }
    if (phoneInput) {
        phoneInput.placeholder = {
            en: "Enter 10-Digit Mobile Number",
            hi: "10-अंकों का मोबाइल नंबर दर्ज करें",
            pa: "10-ਅੰਕਾਂ ਦਾ ਮੋਬਾਈਲ ਨੰਬਰ ਭਰੋ",
            mr: "10-अंकी मोबाईल नंबर टाका",
            te: "10 అంకెల మొబైల్ నంబర్ నమోదు చేయండి"
        }[lang] || "Enter 10-Digit Mobile Number";
    }
    if (villageInput) {
        villageInput.placeholder = {
            en: "Enter Village Name",
            hi: "गाँव का नाम दर्ज करें",
            pa: "ਪਿੰਡ ਦਾ ਨਾਮ ਭਰੋ",
            mr: "गावाचे नाव प्रविष्ट करा",
            te: "గ్రామం పేరు నమోదు చేయండి"
        }[lang] || "Enter Village Name";
    }
    if (districtInput) {
        districtInput.placeholder = {
            en: "Enter District Name",
            hi: "ज़िले का नाम दर्ज करें",
            pa: "ਜ਼ਿਲ੍ਹੇ ਦਾ ਨਾਮ ਭਰੋ",
            mr: "जिल्ह्याचे नाव प्रविष्ट करा",
            te: "జిల్లా పేరు నమోదు చేయండి"
        }[lang] || "Enter District Name";
    }
    if (vehicleNumInput) {
        vehicleNumInput.placeholder = {
            en: "e.g. HR-05-AE-4421 (Optional)",
            hi: "उदा. HR-05-AE-4421 (वैकल्पिक)",
            pa: "ਉਦਾ. HR-05-AE-4421 (ਵਿਕਲਪਿਕ)",
            mr: "उदा. HR-05-AE-4421 (ऐच्छिक)",
            te: "ఉదా. HR-05-AE-4421 (ఐచ్ఛికం)"
        }[lang] || "e.g. HR-05-AE-4421 (Optional)";
    }

    // 3. Sync Language Dropdowns
    document.querySelectorAll("#lang-select, .lang-selector-dropdown").forEach(sel => {
        sel.value = lang;
    });

    // 4. Dispatch Event for page-specific JS modules (e.g. farmer.js, staff.js)
    window.dispatchEvent(new CustomEvent("languageChanged", { detail: { lang, dict: targetDict } }));

    // 5. Toast Confirmation in active language
    if (typeof showToast === "function") {
        showToast(targetDict.lang_switched, "info");
    }
}

// Toast Helper
function showToast(message, type = "success") {
    const container = document.getElementById("toast-container");
    if (!container) return;

    const toast = document.createElement("div");
    const bgColors = {
        success: "bg-emerald-600 border-emerald-500",
        info: "bg-blue-600 border-blue-500",
        warning: "bg-amber-600 border-amber-500",
        error: "bg-rose-600 border-rose-500"
    };

    toast.className = `flex items-center space-x-3 text-white px-4 py-3 rounded-xl shadow-lg border ${bgColors[type] || bgColors.success} transform transition-all duration-300 translate-y-2 opacity-0 text-sm font-medium z-50`;
    toast.innerHTML = `
        <div class="flex-shrink-0">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
        </div>
        <div class="flex-1">${message}</div>
    `;

    container.appendChild(toast);

    // Animate in
    setTimeout(() => {
        toast.classList.remove("translate-y-2", "opacity-0");
    }, 10);

    // Remove after 3.5s
    setTimeout(() => {
        toast.classList.add("translate-y-2", "opacity-0");
        setTimeout(() => toast.remove(), 300);
    }, 3500);
}

// Global Audio Chime Synthesizer using Web Audio API
function playChime(type = "stage_advance") {
    try {
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.connect(gain);
        gain.connect(audioCtx.destination);

        if (type === "stage_advance") {
            osc.frequency.setValueAtTime(523.25, audioCtx.currentTime);
            osc.frequency.exponentialRampToValueAtTime(783.99, audioCtx.currentTime + 0.2);
            gain.gain.setValueAtTime(0.3, audioCtx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.4);
            osc.start();
            osc.stop(audioCtx.currentTime + 0.4);
        } else if (type === "payment") {
            osc.frequency.setValueAtTime(440, audioCtx.currentTime);
            osc.frequency.setValueAtTime(659.25, audioCtx.currentTime + 0.15);
            osc.frequency.setValueAtTime(880, audioCtx.currentTime + 0.3);
            gain.gain.setValueAtTime(0.3, audioCtx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.6);
            osc.start();
            osc.stop(audioCtx.currentTime + 0.6);
        }
    } catch (e) {
        console.warn("Audio chime error:", e);
    }
}

// Global Voice Speech Synthesizer for Announcements & Stage Approvals
function speakVoiceAnnouncement(text, lang = null) {
    if (!('speechSynthesis' in window)) return;
    try {
        window.speechSynthesis.cancel();
        
        const targetLang = lang || (
            currentLang === "en" ? "en-IN" :
            currentLang === "pa" ? "pa-IN" :
            currentLang === "mr" ? "mr-IN" :
            currentLang === "te" ? "te-IN" : "hi-IN"
        );

        const utter = new SpeechSynthesisUtterance(text);
        utter.lang = targetLang;
        utter.rate = 1.0;
        utter.pitch = 1.02;
        
        const voices = window.speechSynthesis.getVoices();
        if (voices.length > 0) {
            const matchedVoice = voices.find(v => 
                (targetLang.startsWith("hi") && (v.lang.includes("hi") || v.name.includes("Hindi") || v.name.includes("India") || v.name.includes("Google हिन्दी"))) ||
                (targetLang.startsWith("en") && (v.lang.includes("en-IN") || v.name.includes("Indian") || v.name.includes("India"))) ||
                (targetLang.startsWith("pa") && (v.lang.includes("pa") || v.name.includes("Punjabi"))) ||
                (targetLang.startsWith("mr") && (v.lang.includes("mr") || v.name.includes("Marathi"))) ||
                (targetLang.startsWith("te") && (v.lang.includes("te") || v.name.includes("Telugu")))
            );
            if (matchedVoice) utter.voice = matchedVoice;
        }

        window.speechSynthesis.speak(utter);
    } catch(e) {
        console.warn("Speech synthesis error:", e);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    // Apply saved language immediately on load
    setLanguage(currentLang);
    
    const langSelect = document.getElementById("lang-select");
    if (langSelect) {
        langSelect.value = currentLang;
        langSelect.addEventListener("change", (e) => setLanguage(e.target.value));
    }
    
    // MutationObserver to auto-translate dynamically inserted DOM nodes
    const observer = new MutationObserver(() => {
        // Debounce translation
        clearTimeout(window.__i18n_timer);
        window.__i18n_timer = setTimeout(() => {
            const targetDict = I18N_DICTIONARY[currentLang];
            if (!targetDict) return;
            document.querySelectorAll("[data-i18n]").forEach(elem => {
                const key = elem.getAttribute("data-i18n");
                if (targetDict[key] && elem.innerText !== targetDict[key]) {
                    elem.innerText = targetDict[key];
                }
            });
        }, 150);
    });
    
    observer.observe(document.body, { childList: true, subtree: true });

    // Pre-load speech voices
    if ('speechSynthesis' in window) {
        window.speechSynthesis.getVoices();
    }
});
