"""
Generate Word-for-Word Spoken Presentation Script PDF for AnnaSetu
Includes: English Script, Hinglish/Hindi Script, Screen Action Cues, and Jury Q&A Delivery.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

PDF_PATH = r"C:\Users\kumar\OneDrive\Documents\Aryan\Hackathon\AnnaSetu_Spoken_Presentation_Script.pdf"
os.makedirs(os.path.dirname(PDF_PATH), exist_ok=True)

class ScriptCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(ScriptCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            super(ScriptCanvas, self).showPage()
        super(ScriptCanvas, self).save()

    def draw_header_footer(self, page_count):
        self.saveState()
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor("#15803d"))
            self.drawString(40, 755, "ANNASÈTU (अन्नसेतु) -- Word-for-Word Jury Presentation Speech Script")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#64748b"))
            self.drawRightString(572, 755, "SIH 2026 | Ministry of Consumer Affairs, Food & Public Distribution")
            
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.8)
            self.line(40, 748, 572, 748)

        # Footer (all pages)
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.8)
        self.line(40, 40, 572, 40)

        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(40, 28, "AnnaSetu Pitch Deck | Problem Statement: SIH26032")
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(572, 28, page_text)

        self.restoreState()

def build_script_pdf():
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        leftMargin=38,
        rightMargin=38,
        topMargin=44,
        bottomMargin=44
    )

    primary_green = colors.HexColor("#15803d")
    dark_slate = colors.HexColor("#0f172a")
    text_slate = colors.HexColor("#334155")
    card_bg = colors.HexColor("#f8fafc")
    green_bg = colors.HexColor("#f0fdf4")
    amber_bg = colors.HexColor("#fffbeb")

    title_style = ParagraphStyle(
        'DocTitle',
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=primary_green,
        spaceAfter=2
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        textColor=colors.HexColor("#64748b"),
        spaceAfter=6
    )

    h2_style = ParagraphStyle(
        'H2_Style',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13.5,
        textColor=dark_slate,
        spaceBefore=5,
        spaceAfter=2.5,
        keepWithNext=True
    )

    cue_style = ParagraphStyle(
        'CueStyle',
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#15803d")
    )

    spoken_en_style = ParagraphStyle(
        'SpokenEn',
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#0f172a")
    )

    spoken_hi_style = ParagraphStyle(
        'SpokenHi',
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=11.5,
        textColor=colors.HexColor("#475569")
    )

    table_header = ParagraphStyle(
        'TableHeader',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )

    story = []

    # TOP BANNER
    banner_data = [
        [
            Paragraph("<b>ANNASÈTU (अन्नसेतु)</b><br/><font size='8' color='#166534'>Smart Procurement Scheduling & Live Queue Management</font>", ParagraphStyle('H', fontName='Helvetica-Bold', fontSize=12.5, textColor=colors.HexColor("#14532d"), leading=15)),
            Paragraph("<font size='7.5' color='#0f172a'><b>SIH 2026 Problem ID:</b> SIH26032<br/><b>Theme:</b> Smart Automation (Software)<br/><b>Ministry:</b> Consumer Affairs, Food & Public Distribution</font>", ParagraphStyle('R', fontName='Helvetica', fontSize=7.5, leading=10, alignment=2))
        ]
    ]
    banner_table = Table(banner_data, colWidths=[314, 222])
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), green_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#86efac")),
        ('PADDING', (0,0), (-1,-1), 4.5),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(banner_table)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>WORD-FOR-WORD SPOKEN PRESENTATION SCRIPT</b>", title_style))
    story.append(Paragraph("Exact spoken words, screen actions, timing cues, and judge defense for the Smart India Hackathon jury.", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#e2e8f0"), spaceAfter=5))

    # TABLE SCRIPT
    script_data = [
        [
            Paragraph("Part & Time", table_header),
            Paragraph("Screen Action (What to do)", table_header),
            Paragraph("Word-for-Word Spoken Script (What to say)", table_header)
        ],
        [
            Paragraph("<b>PART 1</b><br/>(0:00 - 0:45)<br/><i>Hook & Problem</i>", ParagraphStyle('P1', fontName='Helvetica', fontSize=8, leading=10.5)),
            Paragraph("<b>Screen:</b> Show Home Page (<code>http://127.0.0.1:8000/</code>).<br/>"
                      "Scroll to the registration form.", ParagraphStyle('P1A', fontName='Helvetica', fontSize=7.8, leading=10.5)),
            Paragraph("<b>[English]:</b> <i>\"Respected Jury members, good morning! During peak harvest season, Indian farmers face 24 to 48 hours of chaotic mandi traffic jams, leading to crop spoilage, middlemen exploitation, and distress selling below MSP. We present <b>AnnaSetu</b> -- an intelligent procurement scheduling and live queue tracking platform designed for the Ministry of Consumer Affairs, Food & Public Distribution.\"</i><br/>"
                      "<b>[Hindi]:</b> <i>\"नमस्ते सर! रबी और खरीफ के समय किसानों को मंडियों में 2-2 दिन तक ट्रैक्टरों की लंबी लाइनों में खड़ा रहना पड़ता है। अन्नसेतु किसानों को डिजिटल स्लॉट बुकिंग और रियल-टाइम टोकन ट्रैकिंग की सुविधा देता है।\"</i>", ParagraphStyle('P1S', fontName='Helvetica', fontSize=8, leading=11))
        ],
        [
            Paragraph("<b>PART 2</b><br/>(0:45 - 1:30)<br/><i>Smart Booking & MSP Lock</i>", ParagraphStyle('P2', fontName='Helvetica', fontSize=8, leading=10.5)),
            Paragraph("<b>Fill Form:</b><br/>"
                      "• Name: <code>Harishchandra Verma</code><br/>"
                      "• Crop: <code>Wheat (Rs. 2,425/Qtl)</code><br/>"
                      "• Qty: <code>50 Quintals</code>.<br/>"
                      "• Point to <b>Rs. 1,21,250</b> box.<br/>"
                      "• Click <b>Generate Token</b>.", ParagraphStyle('P2A', fontName='Helvetica', fontSize=7.8, leading=10.5)),
            Paragraph("<b>[English]:</b> <i>\"Let us simulate a live booking. As Harishchandra enters 50 Quintals of Wheat, notice how AnnaSetu instantly calculates and guarantees the official MSP payout of <b>Rs. 1,21,250</b>. When I click 'Confirm', token <b>AS-26-WHT-XXX</b> is generated with a 2-hour arrival slot, eliminating queue uncertainty!\"</i><br/>"
                      "<b>[Hindi]:</b> <i>\"जैसे ही किसान 50 क्विंटल गेहूं भरता है, सिस्टम तुरंत गारंटीड एमएसपी राशि 1,21,250 रुपये स्क्रीन पर लॉक कर देता है। टोकन बनते ही किसान को उसकी तारीख और स्लॉट मिल जाता है।\"</i>", ParagraphStyle('P2S', fontName='Helvetica', fontSize=8, leading=11))
        ],
        [
            Paragraph("<b>PART 3</b><br/>(1:30 - 2:45)<br/><i>Live Real-Time Sync (WOW Moment)</i>", ParagraphStyle('P3', fontName='Helvetica', fontSize=8, leading=10.5)),
            Paragraph("<b>Two Windows Side-by-Side:</b><br/>"
                      "• <b>Left:</b> Farmer Tracker (<code>/track</code>)<br/>"
                      "• <b>Right:</b> Staff Board (<code>/staff</code>)<br/>"
                      "Click: 1. Gate Entry ➔ 2. Weighbridge (7,450 kg) ➔ 3. Quality Lab (11.4% Moisture) ➔ 4. Authorize DBT.", ParagraphStyle('P3A', fontName='Helvetica', fontSize=7.8, leading=10.5)),
            Paragraph("<b>[English]:</b> <i>\"Now look at the live synchronization between the Mandi Operator on the right and the Farmer Tracker on the left. As the Mandi Staff logs vehicle Gate Entry, gross scale reading of 7,450 kg at the Weighbridge, and certified 11.4% moisture at the Quality Lab, the farmer's screen updates <b>instantly via WebSockets without any page refresh!</b> Finally, when staff authorizes payment, tare weight is deducted and instant DBT transfer is triggered!\"</i><br/>"
                      "<b>[Hindi]:</b> <i>\"दाहिनी तरफ मंडी स्टाफ जैसे ही गेट एंट्री, धर्मकांटा वजन और लैब जांच पास करता है, बाईं तरफ किसान का ट्रैकर बिना पेज रिफ्रेश किए तुरंत ग्रीन अपडेट होता है!\"</i>", ParagraphStyle('P3S', fontName='Helvetica', fontSize=8, leading=11))
        ],
        [
            Paragraph("<b>PART 4</b><br/>(2:45 - 3:30)<br/><i>Verified e-Receipt & Print</i>", ParagraphStyle('P4', fontName='Helvetica', fontSize=8, leading=10.5)),
            Paragraph("<b>On Left Screen:</b><br/>"
                      "Scroll down to receipt.<br/>"
                      "Point to Net 50 Qtls, Rs. 1,21,250, DBT Ref No.<br/>"
                      "Click <b>'Print e-Receipt Now'</b>.", ParagraphStyle('P4A', fontName='Helvetica', fontSize=7.8, leading=10.5)),
            Paragraph("<b>[English]:</b> <i>\"Once completed, AnnaSetu issues a tamper-proof <b>Government Digital e-Receipt</b> featuring the official AnnaSetu Verified security watermark, net weight of 50 Quintals, and unique DBT reference number: DBT-2026-WHT-XXXXXXX. The farmer can print or save it with a single click.\"</i><br/>"
                      "<b>[Hindi]:</b> <i>\"उपार्जन पूरा होते ही डिजिटल वाटरमार्क के साथ सरकारी ई-रसीद तैयार हो जाती है, जिसे किसान तुरंत प्रिंट या पीडीएफ सेव कर सकता है।\"</i>", ParagraphStyle('P4S', fontName='Helvetica', fontSize=8, leading=11))
        ],
        [
            Paragraph("<b>PART 5</b><br/>(3:30 - 4:30)<br/><i>Inclusive IVR & Ministry Admin</i>", ParagraphStyle('P5', fontName='Helvetica', fontSize=8, leading=10.5)),
            Paragraph("• <b>Tab 2 (/centers):</b> Mandi load balancer.<br/>"
                      "• <b>Tab 6 (/ivr):</b> Select Hindi, tap mic to simulate toll-free call.<br/>"
                      "• <b>Tab 5 (/admin):</b> Ministry Admin stats & throughput.", ParagraphStyle('P5A', fontName='Helvetica', fontSize=7.8, leading=10.5)),
            Paragraph("<b>[English]:</b> <i>\"What about farmers without smartphones? We built a <b>Toll-Free Voice IVR (1800-180-2626)</b> that speaks live token status in 5 languages over basic keypad feature phones! In addition, our <b>Mandi Load Balancer</b> dynamically reroutes traffic to decongest centers, and our <b>Ministry Admin Hub</b> gives officials macro visibility over metric tons procured and crore rupees disbursed.\"</i><br/>"
                      "<b>[Hindi]:</b> <i>\"बिना स्मार्टफोन वाले किसान टोल-फ्री 1800-180-2626 पर कॉल करके हिंदी और क्षेत्रीय भाषाओं में अपनी लाइव स्थिति सुन सकते हैं।\"</i>", ParagraphStyle('P5S', fontName='Helvetica', fontSize=8, leading=11))
        ]
    ]

    script_table = Table(script_data, colWidths=[65, 145, 326])
    script_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0f172a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, card_bg]),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 3.5),
    ]))
    story.append(script_table)
    story.append(Spacer(1, 5))

    # CLOSING & DEFENSE
    closing_data = [
        [Paragraph("<b>🎯 Winning Closing Line:</b> <i>\"AnnaSetu eliminates middlemen, prevents distress selling, and guarantees every farmer gets their rightful MSP on time. Thank you, we are ready for your questions!\"</i>", ParagraphStyle('Close', fontName='Helvetica-Bold', fontSize=8.5, leading=11.5, textColor=colors.HexColor("#14532d")))],
        [Paragraph("<b>⚡ Tough Jury Q&A Quick Answers:</b><br/>"
                   "• <b>Keypad Phones?</b> ➔ <i>'Toll-free IVR (1800-180-2626) speaks live updates in 5 languages.'</i><br/>"
                   "• <b>Late arrival?</b> ➔ <i>'2-hour arrival windows; delayed vehicles enter dynamic standby pool without cancellation.'</i><br/>"
                   "• <b>Anti-corruption?</b> ➔ <i>'Weighbridge readings log directly to immutable audit trail; payouts calculated deterministically by code.'</i><br/>"
                   "• <b>Offline Mandi?</b> ➔ <i>'Runs 100% locally on SQLite with automatic cloud sync when connectivity restores.'</i>", ParagraphStyle('Ans', fontName='Helvetica', fontSize=8, leading=11, textColor=colors.HexColor("#1e293b")))]
    ]
    closing_table = Table(closing_data, colWidths=[536])
    closing_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), green_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#86efac")),
        ('PADDING', (0,0), (-1,-1), 4.5),
    ]))
    story.append(closing_table)

    doc.build(story, canvasmaker=ScriptCanvas)
    print(f"[OK] Spoken Presentation Script PDF generated at: {PDF_PATH}")

if __name__ == "__main__":
    build_script_pdf()
