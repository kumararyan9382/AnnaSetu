"""
Generate Comprehensive Step-by-Step Tutorial & Playbook PDF for AnnaSetu
Includes: What to do, How to do, Exact Clicks, Screenshots breakdown, Judge Pitch & Q&A.
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

PDF_OUTPUT_PATH = r"C:\Users\kumar\OneDrive\Documents\Aryan\Hackathon\AnnaSetu_Complete_Step_by_Step_Tutorial_Guide.pdf"
os.makedirs(os.path.dirname(PDF_OUTPUT_PATH), exist_ok=True)

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_header_footer(self, page_count):
        self.saveState()
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor("#15803d"))
            self.drawString(40, 755, "ANNASÈTU (AnnaSetu) -- Complete Step-by-Step Tutorial & Demo Guide")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#64748b"))
            self.drawRightString(572, 755, "SIH 2026 Problem Statement: SIH26032")
            
            # Header line
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.8)
            self.line(40, 748, 572, 748)

        # Footer (all pages)
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.8)
        self.line(40, 40, 572, 40)

        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(40, 28, "Ministry of Consumer Affairs, Food & Public Distribution | Track: Software")
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(572, 28, page_text)

        self.restoreState()

def build_pdf():
    doc = SimpleDocTemplate(
        PDF_OUTPUT_PATH,
        pagesize=letter,
        leftMargin=38,
        rightMargin=38,
        topMargin=44,
        bottomMargin=44
    )

    # Color Palette
    primary_green = colors.HexColor("#15803d")
    dark_slate = colors.HexColor("#0f172a")
    text_color = colors.HexColor("#334155")
    card_bg = colors.HexColor("#f8fafc")
    green_bg = colors.HexColor("#f0fdf4")
    blue_bg = colors.HexColor("#eff6ff")
    amber_bg = colors.HexColor("#fffbeb")

    title_style = ParagraphStyle(
        'DocTitle',
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=primary_green,
        spaceAfter=3
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#64748b"),
        spaceAfter=8
    )

    step_title_style = ParagraphStyle(
        'StepTitle',
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=15,
        textColor=dark_slate,
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=text_color,
        spaceAfter=3
    )

    code_style = ParagraphStyle(
        'CodeStyle',
        fontName='Courier-Bold',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#0f172a"),
        backColor=colors.HexColor("#f1f5f9"),
        spaceAfter=3
    )

    table_cell = ParagraphStyle(
        'TableCell',
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=text_color
    )

    table_header = ParagraphStyle(
        'TableHeader',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )

    box_content = ParagraphStyle(
        'BoxContent',
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#1e293b")
    )

    story = []

    # -------------------------------------------------------------
    # TOP HEADER BANNER
    # -------------------------------------------------------------
    banner_data = [
        [
            Paragraph("<b>ANNASÈTU (AnnaSetu)</b><br/><font size='8.5' color='#166534'>Smart Farmer Procurement Tracking & Scheduling Platform</font>", ParagraphStyle('H', fontName='Helvetica-Bold', fontSize=13.5, textColor=colors.HexColor("#14532d"), leading=16)),
            Paragraph("<font size='7.5' color='#0f172a'><b>SIH 2026 Problem Statement:</b> SIH26032<br/><b>Theme:</b> Smart Automation | <b>Track:</b> Software<br/><b>Ministry:</b> Consumer Affairs, Food & Public Distribution</font>", ParagraphStyle('R', fontName='Helvetica', fontSize=7.5, leading=10, alignment=2))
        ]
    ]
    banner_table = Table(banner_data, colWidths=[314, 222])
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), green_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#86efac")),
        ('PADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(banner_table)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>COMPLETE STEP-BY-STEP TUTORIAL & DEMO GUIDE</b>", title_style))
    story.append(Paragraph("Master Guide: Exactly what to do, what to click, what to type, and how to present each feature to the Smart India Hackathon jury.", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#e2e8f0"), spaceAfter=8))

    # -------------------------------------------------------------
    # STEP 1: START SERVER
    # -------------------------------------------------------------
    s1_data = [
        [Paragraph("<b>STEP 1: Start the Local Backend Server (5 Mins Before Demo)</b>", ParagraphStyle('S1H', fontName='Helvetica-Bold', fontSize=9.5, textColor=colors.HexColor("#14532d")))],
        [Paragraph("<b>What to Do:</b> Open Windows PowerShell on your laptop and run these exact two commands:<br/>"
                   "<code>cd C:\\Users\\kumar\\.gemini\\antigravity\\scratch\\annasetu<br/>python run.py</code><br/>"
                   "<b>What You Will See:</b> The terminal displays: <i>'Server running at: http://127.0.0.1:8000'</i>.<br/>"
                   "<b>Why this matters:</b> AnnaSetu runs 100% locally. Zero internet lag even if venue Wi-Fi goes down!", box_content)]
    ]
    s1_table = Table(s1_data, colWidths=[536])
    s1_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), green_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#86efac")),
        ('PADDING', (0,0), (-1,-1), 5.5),
    ]))
    story.append(s1_table)
    story.append(Spacer(1, 6))

    # -------------------------------------------------------------
    # STEP 2: BROWSER TABS LAYOUT
    # -------------------------------------------------------------
    s2_data = [
        [Paragraph("<b>STEP 2: Open Google Chrome & Arrange Your 6 Tabs</b>", ParagraphStyle('S2H', fontName='Helvetica-Bold', fontSize=9.5, textColor=colors.HexColor("#1e3a8a")))],
        [Paragraph("Open Google Chrome and keep these 6 tabs ready in this exact order:", box_content)],
        [
            Table([
                [Paragraph("Tab #", table_header), Paragraph("Portal Name", table_header), Paragraph("URL to Open", table_header), Paragraph("What it Shows", table_header)],
                [Paragraph("<b>Tab 1</b>", table_cell), Paragraph("Home / Booking", table_cell), Paragraph("<code>127.0.0.1:8000/</code>", table_cell), Paragraph("Farmer details form + live guaranteed MSP payout calculator.", table_cell)],
                [Paragraph("<b>Tab 2</b>", table_cell), Paragraph("Mandi Tracker", table_cell), Paragraph("<code>127.0.0.1:8000/centers</code>", table_cell), Paragraph("Multi-mandi queue loads + intelligent traffic load balancer.", table_cell)],
                [Paragraph("<b>Tab 3</b>", table_cell), Paragraph("Live Tracker", table_cell), Paragraph("<code>127.0.0.1:8000/track</code>", table_cell), Paragraph("5-Stage progression bar, 1-Click Advance, & digital e-voucher.", table_cell)],
                [Paragraph("<b>Tab 4</b>", table_cell), Paragraph("Staff Board", table_cell), Paragraph("<code>127.0.0.1:8000/staff</code>", table_cell), Paragraph("Mandi operator console to log weighbridge & lab grades.", table_cell)],
                [Paragraph("<b>Tab 5</b>", table_cell), Paragraph("Ministry Admin", table_cell), Paragraph("<code>127.0.0.1:8000/admin</code>", table_cell), Paragraph("District throughput (MT), ₹ Cr disbursed, bottleneck analytics.", table_cell)],
                [Paragraph("<b>Tab 6</b>", table_cell), Paragraph("Voice / IVR", table_cell), Paragraph("<code>127.0.0.1:8000/ivr</code>", table_cell), Paragraph("Toll-free phone simulator (1800-180-2626) in 5 Indian languages.", table_cell)]
            ], colWidths=[35, 95, 110, 276], style=[
                ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
                ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
                ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, card_bg]),
                ('PADDING', (0,0), (-1,-1), 2.5),
            ])
        ]
    ]
    s2_table = Table(s2_data, colWidths=[536])
    s2_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), blue_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#93c5fd")),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(s2_table)
    story.append(Spacer(1, 6))

    # -------------------------------------------------------------
    # STEP 3: LIVE BOOKING ON FRONT PAGE
    # -------------------------------------------------------------
    s3_data = [
        [Paragraph("<b>STEP 3: Front-Page Farmer Registration & Booking (Minute 1 Demo)</b>", ParagraphStyle('S3H', fontName='Helvetica-Bold', fontSize=9.5, textColor=colors.HexColor("#78350f")))],
        [Paragraph("<b>1. Go to Tab 1:</b> Open <code>http://127.0.0.1:8000/</code> and scroll to the registration form.<br/>"
                   "<b>2. Fill Details:</b> Name: <code>Harishchandra Verma</code> | Phone: <code>9876501234</code> | Crop: <code>Wheat (Rs. 2,425/Qtl)</code> | Quantity: <code>50.0 Quintals</code>.<br/>"
                   "<b>3. Point out to Judges:</b> <i>\"Notice how the system immediately calculates and guarantees the official MSP payout: <b>Rs. 1,21,250</b>.\"</i><br/>"
                   "<b>4. Click:</b> <b>'Confirm & Generate Token'</b>. The browser will chime and redirect to the Live Tracker with Token <code>AS-26-WHT-XXX</code>!", box_content)]
    ]
    s3_table = Table(s3_data, colWidths=[536])
    s3_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), amber_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#fde68a")),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(s3_table)
    story.append(Spacer(1, 6))

    # -------------------------------------------------------------
    # STEP 4: ADVANCING ALL 5 STAGES LIVE
    # -------------------------------------------------------------
    s4_data = [
        [Paragraph("<b>STEP 4: Live 5-Stage Demonstration (Minute 2 'WOW' Factor)</b>", ParagraphStyle('S4H', fontName='Helvetica-Bold', fontSize=9.5, textColor=colors.HexColor("#14532d")))],
        [Paragraph("On the <b>Live Tracker page (/track)</b>, you have two amazing ways to demonstrate live progression:<br/>"
                   "<b>• Option A (1-Click Auto-Play):</b> Click the green <b>'▶ Auto-Play Demo'</b> button. The token automatically advances through all 5 stages every 3 seconds while playing audio chimes!<br/>"
                   "<b>• Option B (Manual Control via '⚡ Advance Stage'):</b><br/>"
                   "&nbsp;&nbsp;1. Click <b>'⚡ Advance Stage'</b> ➔ Advances to <b>Stage 2: Gate Entry</b> 🚛.<br/>"
                   "&nbsp;&nbsp;2. Click <b>'⚡ Advance Stage'</b> ➔ Advances to <b>Stage 3: Weighbridge</b> (Gross: 7,450 kg) ⚖️.<br/>"
                   "&nbsp;&nbsp;3. Click <b>'⚡ Advance Stage'</b> ➔ Advances to <b>Stage 4: Quality Lab</b> (Moisture: 11.4%, Grade A) 🔬.<br/>"
                   "&nbsp;&nbsp;4. Click <b>'⚡ Advance Stage'</b> ➔ Advances to <b>Stage 5: DBT Payment Done</b> (Net: 50 Qtls, Disbursed: <b>Rs. 1,21,250</b>, Ref: DBT-2026-WHT-XXXXXXX) 💳.", box_content)]
    ]
    s4_table = Table(s4_data, colWidths=[536])
    s4_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), green_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#86efac")),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(s4_table)
    story.append(Spacer(1, 6))

    # -------------------------------------------------------------
    # STEP 5: PRINTING PAYMENT VOUCHER
    # -------------------------------------------------------------
    s5_data = [
        [Paragraph("<b>STEP 5: Verified Government Digital e-Receipt & Printing</b>", ParagraphStyle('S5H', fontName='Helvetica-Bold', fontSize=9.5, textColor=colors.HexColor("#0f172a")))],
        [Paragraph("1. Scroll to the bottom of the Live Tracker page to see the verified <b>Government Procurement e-Receipt</b>.<br/>"
                   "2. Point to the <b>'AnnaSetu Verified'</b> watermark, Net Quantity (50 Quintals), and DBT bank reference.<br/>"
                   "3. Click <b>'🖨️ Print e-Receipt Now'</b>. The browser print preview will open with only the official receipt framed!", box_content)]
    ]
    s5_table = Table(s5_data, colWidths=[536])
    s5_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), card_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(s5_table)
    story.append(Spacer(1, 6))

    # -------------------------------------------------------------
    # STEP 6: OTHER MODULES & JUDGE DEFENSE
    # -------------------------------------------------------------
    s6_data = [
        [Paragraph("<b>STEP 6: Mandi Load Balancer, Voice IVR, & Ministry Oversight (Minute 3 Demo)</b>", ParagraphStyle('S6H', fontName='Helvetica-Bold', fontSize=9.5, textColor=colors.HexColor("#78350f")))],
        [Paragraph("<b>• Tab 2 (/centers):</b> Show 'System Recommended' badge: <i>\"Heuristic computes Travel Time + Queue Delay to redirect harvest traffic.\"</i><br/>"
                   "<b>• Tab 6 (/ivr):</b> Toggle Hindi/Punjabi, tap 🎙️ mic or enter mobile: <i>\"Toll-free IVR (1800-180-2626) speaks live status aloud in 5 languages for basic phone users.\"</i><br/>"
                   "<b>• Tab 5 (/admin):</b> Show total MT procured, ₹ Cr disbursed, and bottleneck diagnosis table.", box_content)]
    ]
    s6_table = Table(s6_data, colWidths=[536])
    s6_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), amber_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#fde68a")),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(s6_table)
    story.append(Spacer(1, 6))

    # Judge Q&A Box
    qa_summary_data = [
        [Paragraph("<b>Quick Judge Q&A Cheat Sheet:</b><br/>"
                   "<b>Q: Poor farmers without smartphones?</b> ➔ <i>\"Toll-free IVR (1800-180-2626) reads live status in 5 languages over basic feature phone.\"</i><br/>"
                   "<b>Q: Late arrival?</b> ➔ <i>\"2-hour arrival windows; delayed vehicles enter dynamic standby pool without token cancellation.\"</i><br/>"
                   "<b>Q: Anti-fraud?</b> ➔ <i>\"Weighbridge & lab values log directly to immutable audit trail; payout is computed automatically by code.\"</i>", ParagraphStyle('QAS', fontName='Helvetica', fontSize=8, leading=11, textColor=colors.HexColor("#1e293b")))]
    ]
    qa_summary_table = Table(qa_summary_data, colWidths=[536])
    qa_summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), green_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#86efac")),
        ('PADDING', (0,0), (-1,-1), 4.5),
    ]))
    story.append(qa_summary_table)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[OK] Complete Step-by-Step Tutorial PDF generated successfully at: {PDF_OUTPUT_PATH}")

if __name__ == "__main__":
    build_pdf()
