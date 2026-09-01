"""
Generate a Clean, Crisp, Professional Hackathon Day PDF Playbook for AnnaSetu
100% font-safe (no glyph missing boxes), beautiful typography, structured tables and colored cards.
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

PDF_OUTPUT_PATH = r"C:\Users\kumar\OneDrive\Documents\Aryan\Hackathon\AnnaSetu_Hackathon_Day_Detailed_Guide.pdf"
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
            self.drawString(40, 755, "ANNASÈTU -- SIH 2026 Hackathon Day Playbook")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#64748b"))
            self.drawRightString(572, 755, "Problem Statement: SIH26032")
            
            # Header line
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.8)
            self.line(40, 748, 572, 748)

        # Footer (all pages)
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.8)
        self.line(40, 42, 572, 42)

        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(40, 30, "Ministry of Consumer Affairs, Food & Public Distribution | Track: Software")
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(572, 30, page_text)

        self.restoreState()

def build_pdf():
    doc = SimpleDocTemplate(
        PDF_OUTPUT_PATH,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=46,
        bottomMargin=46
    )

    # Palette
    primary_color = colors.HexColor("#15803d")   # Emerald
    dark_slate = colors.HexColor("#0f172a")      # Heading dark
    text_color = colors.HexColor("#334155")      # Body slate
    card_bg = colors.HexColor("#f8fafc")         # Light slate bg
    green_bg = colors.HexColor("#f0fdf4")        # Light green bg
    blue_bg = colors.HexColor("#eff6ff")         # Light blue bg
    amber_bg = colors.HexColor("#fffbeb")        # Light amber bg

    title_style = ParagraphStyle(
        'DocTitle',
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=primary_color,
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#64748b"),
        spaceAfter=10
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=dark_slate,
        spaceBefore=10,
        spaceAfter=5,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=primary_color,
        spaceBefore=6,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=text_color,
        spaceAfter=4
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

    spoken_script_style = ParagraphStyle(
        'SpokenScript',
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#1e293b")
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

    story = []

    # -------------------------------------------------------------
    # HEADER BANNER
    # -------------------------------------------------------------
    banner_data = [
        [
            Paragraph("<b>ANNASÈTU (AnnaSetu)</b><br/><font size='8.5' color='#166534'>Smart Farmer Procurement Tracking & Scheduling Platform</font>", ParagraphStyle('H', fontName='Helvetica-Bold', fontSize=14, textColor=colors.HexColor("#14532d"), leading=17)),
            Paragraph("<font size='7.5' color='#0f172a'><b>SIH 2026 Problem Statement:</b> SIH26032<br/><b>Theme:</b> Smart Automation | <b>Track:</b> Software<br/><b>Ministry:</b> Consumer Affairs, Food & Public Distribution</font>", ParagraphStyle('R', fontName='Helvetica', fontSize=7.5, leading=10.5, alignment=2))
        ]
    ]
    banner_table = Table(banner_data, colWidths=[310, 222])
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), green_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#86efac")),
        ('PADDING', (0,0), (-1,-1), 7),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(banner_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph("<b>HACKATHON DAY PLAYBOOK & LIVE DEMONSTRATION GUIDE</b>", title_style))
    story.append(Paragraph("Master Step-by-Step Instructions: Server Startup, Chrome Browser Layout, 3-Minute Judge Presentation Script, and Q&A Defense.", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#e2e8f0"), spaceAfter=8))

    # -------------------------------------------------------------
    # PART 1: PRE-DEMO SETUP (5 MINUTES BEFORE JUDGES ARRIVE)
    # -------------------------------------------------------------
    story.append(Paragraph("1. Pre-Demo Setup (5 Minutes Before Judges Arrive)", h1_style))
    story.append(Paragraph("<b>Step 1.1: Start the Local Backend Server</b>", h2_style))
    story.append(Paragraph("Open PowerShell or Command Prompt on your laptop and run:", body_style))
    story.append(Paragraph("<code>cd C:\\Users\\kumar\\.gemini\\antigravity\\scratch\\annasetu<br/>python run.py</code>", code_style))
    story.append(Paragraph("<i><b>Offline Advantage:</b> AnnaSetu runs 100% locally on <code>http://127.0.0.1:8000</code>. Even if the hackathon venue Wi-Fi is slow or disconnected, your entire platform, SQLite database, WebSockets, and audio synthesis will work seamlessly with zero lag!</i>", body_style))
    
    story.append(Spacer(1, 3))
    story.append(Paragraph("<b>Step 1.2: Pre-Open Browser Tabs in Google Chrome</b>", h2_style))
    story.append(Paragraph("Keep these 6 tabs pre-arranged in Chrome in this exact order before calling judges over:", body_style))

    tab_data = [
        [Paragraph("Tab #", table_header), Paragraph("Portal Name", table_header), Paragraph("Local URL", table_header), Paragraph("Key Role / Demonstration Purpose", table_header)],
        [Paragraph("<b>Tab 1</b>", table_cell), Paragraph("<b>Home & Booking</b>", table_cell), Paragraph("<code>127.0.0.1:8000/</code>", table_cell), Paragraph("Landing page with direct front-page farmer registration form & live MSP calculator.", table_cell)],
        [Paragraph("<b>Tab 2</b>", table_cell), Paragraph("<b>Mandi Tracker</b>", table_cell), Paragraph("<code>127.0.0.1:8000/centers</code>", table_cell), Paragraph("Multi-mandi comparison, tractor travel time, and load-balancing recommendations.", table_cell)],
        [Paragraph("<b>Tab 3</b>", table_cell), Paragraph("<b>Farmer Tracker</b>", table_cell), Paragraph("<code>127.0.0.1:8000/track</code>", table_cell), Paragraph("Live 5-stage progression timeline, queue countdown, audio readout & e-receipt.", table_cell)],
        [Paragraph("<b>Tab 4</b>", table_cell), Paragraph("<b>Staff Board</b>", table_cell), Paragraph("<code>127.0.0.1:8000/staff</code>", table_cell), Paragraph("Mandi operator pipeline to log weights, quality grades, and trigger live WebSocket sync.", table_cell)],
        [Paragraph("<b>Tab 5</b>", table_cell), Paragraph("<b>Ministry Admin</b>", table_cell), Paragraph("<code>127.0.0.1:8000/admin</code>", table_cell), Paragraph("Macro district oversight, MT throughput, MSP payout (Crores), bottleneck SLA analyzer.", table_cell)],
        [Paragraph("<b>Tab 6</b>", table_cell), Paragraph("<b>Voice / IVR Demo</b>", table_cell), Paragraph("<code>127.0.0.1:8000/ivr</code>", table_cell), Paragraph("Simulated toll-free phone dialpad (1800-180-2626) & multilingual speech assistant.", table_cell)]
    ]
    tab_table = Table(tab_data, colWidths=[38, 95, 110, 289])
    tab_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, card_bg]),
        ('PADDING', (0,0), (-1,-1), 3.5),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(tab_table)
    story.append(Spacer(1, 10))

    # -------------------------------------------------------------
    # PART 2: THE 3-MINUTE WINNING PITCH & DEMONSTRATION SCRIPT
    # -------------------------------------------------------------
    story.append(Paragraph("2. The 3-Minute Live Judge Presentation Script", h1_style))
    story.append(Paragraph("Follow this minute-by-minute script when the jury approaches your presentation table:", body_style))

    # Minute 1 Box
    m1_data = [
        [Paragraph("<b>[0:00 - 1:00] MINUTE 1: Problem Hook & Front-Page Farmer Booking</b>", ParagraphStyle('M1H', fontName='Helvetica-Bold', fontSize=9, textColor=colors.HexColor("#14532d")))],
        [Paragraph("<b>Screen Action:</b> Show <b>Tab 1 (Home Page: 127.0.0.1:8000/)</b>. Point to Problem Statement SIH26032 badge, then scroll to the farmer registration form.<br/>"
                   "<b>Exact Pitch Script:</b><br/>"
                   "<i>\"Good morning, respected judges. We are addressing SIH Problem Statement <b>SIH26032</b> for the Ministry of Consumer Affairs, Food & Public Distribution. Every harvest season, millions of farmers arrive unannounced at mandis, causing 18 to 48 hours of chaotic physical queues, traffic jams, and severe payment uncertainty. We built <b>AnnaSetu</b> to solve this through smart slot scheduling and end-to-end real-time tracking.\"</i><br/>"
                   "<b>Action on Form:</b> Select <b>Wheat</b>, enter <b>50 Quintals</b>. Point to the green payout box: <i>\"Notice how the system immediately calculates and guarantees the official 2025-26 MSP payout: <b>Rs. 1,21,250</b>. When we click 'Confirm & Generate Token', the farmer receives an assured arrival window and unique token ID.\"</i>", spoken_script_style)]
    ]
    m1_table = Table(m1_data, colWidths=[532])
    m1_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), green_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#86efac")),
        ('PADDING', (0,0), (-1,-1), 5.5),
    ]))
    story.append(m1_table)
    story.append(Spacer(1, 6))

    # Minute 2 Box
    m2_data = [
        [Paragraph("<b>[1:00 - 2:00] MINUTE 2: Side-by-Side Two-Window Real-Time WebSocket Sync</b>", ParagraphStyle('M2H', fontName='Helvetica-Bold', fontSize=9, textColor=colors.HexColor("#1e3a8a")))],
        [Paragraph("<b>Screen Action:</b> Snap <b>Farmer Tracker (/track)</b> to the LEFT half and <b>Staff Board (/staff)</b> to the RIGHT half.<br/>"
                   "<b>1. Stage 2 (Gate Entry):</b> Click <i>'Check-in Gate Entry'</i> on staff board. Point to left screen: <i>\"Notice how the farmer screen updates to Stage 2 live via WebSockets without any page reload!\"</i><br/>"
                   "<b>2. Stage 3 (Weighbridge):</b> Click <i>'Send to Weighbridge'</i> -- Enter Gross Weight: <b>7850 kg</b> -- Confirm. <i>\"Gross scale reading is recorded directly into the audit log.\"</i><br/>"
                   "<b>3. Stage 4 (Quality Lab):</b> Click <i>'Send to Quality Lab'</i> -- Enter Moisture: <b>11.4%</b> (Grade A) -- Confirm. <i>\"Moisture and grade are verified against FAQ standards.\"</i><br/>"
                   "<b>4. Stage 5 (DBT Payment Authorization):</b> Click <i>'Authorize & Pay DBT'</i> -- Enter Tare Weight: <b>2850 kg</b> -- Confirm.<br/>"
                   "<b>Highlight Outcome:</b> Net Weight: <b>50.0 Qtls</b> (7850 - 2850 kg) | Total Payout: <b>Rs. 1,21,250</b> | Instant DBT Ref: <b>DBT-2026-WHT-XXXXXXX</b>.<br/>"
                   "Scroll down on farmer screen to show the verified <b>Government Digital e-Receipt</b> with watermark and click <i>'Print e-Voucher'</i>.", spoken_script_style)]
    ]
    m2_table = Table(m2_data, colWidths=[532])
    m2_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), blue_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#93c5fd")),
        ('PADDING', (0,0), (-1,-1), 5.5),
    ]))
    story.append(m2_table)
    story.append(Spacer(1, 6))

    # Minute 3 Box
    m3_data = [
        [Paragraph("<b>[2:00 - 3:00] MINUTE 3: Mandi Load Balancer, Voice IVR & Ministry Analytics</b>", ParagraphStyle('M3H', fontName='Helvetica-Bold', fontSize=9, textColor=colors.HexColor("#78350f")))],
        [Paragraph("<b>1. Mandi Tracker & Load Balancer (Tab 2: /centers):</b> Point to 'System Recommended' badge: <i>\"Our heuristic computes Tractor Travel Time + Live Queue Delay to redirect farmers from congested mandis to free ones, balancing district traffic.\"</i><br/>"
                   "<b>2. Voice & IVR Accessibility (Tab 6: /ivr):</b> Switch language to Hindi or Punjabi. Tap the mic button or click 'Call': <i>\"For elderly or low-literacy farmers with basic feature phones, our toll-free IVR (1800-180-2626) reads live status aloud in 5 Indian languages.\"</i><br/>"
                   "<b>3. Ministry Admin Oversight Hub (Tab 5: /admin):</b> Show metric tons procured, Crores disbursed, and Bottleneck Diagnosis Table (monitoring lab delays against SLA targets). Click <i>'Fast-Forward Stage'</i> to show live data bursts.<br/>"
                   "<b>Conclusion:</b> <i>\"AnnaSetu delivers speed, dignity, and total transparency to agricultural procurement. Thank you!\"</i>", spoken_script_style)]
    ]
    m3_table = Table(m3_data, colWidths=[532])
    m3_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), amber_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#fde68a")),
        ('PADDING', (0,0), (-1,-1), 5.5),
    ]))
    story.append(m3_table)
    story.append(Spacer(1, 8))

    # -------------------------------------------------------------
    # PART 3: JUDGE Q&A DEFENSE MASTER SHEET
    # -------------------------------------------------------------
    story.append(Paragraph("3. Judge Q&A Defense Master Sheet", h1_style))
    story.append(Paragraph("Exact, high-scoring answers to the most critical technical and operational questions judges will ask:", body_style))

    qa_data = [
        [Paragraph("Expected Judge Question", table_header), Paragraph("Winning High-Scoring Defense Answer", table_header)],
        [
            Paragraph("<b>Q1: How will poor farmers without smartphones use this system?</b>", table_cell),
            Paragraph("<i>\"We built a simulated toll-free IVR phone system (Tab 6: 1800-180-2626). Farmers can dial in from any basic keypad phone or send an SMS with their registered mobile number to receive automated spoken voice readouts in Hindi, Punjabi, Marathi, Telugu, or English without needing internet or a smartphone.\"</i>", table_cell)
        ],
        [
            Paragraph("<b>Q2: What happens if a farmer arrives late due to traffic or breakdown?</b>", table_cell),
            Paragraph("<i>\"The scheduling engine allocates 2-hour arrival windows rather than strict minute slots. If delayed, the token is not cancelled; it is automatically re-routed to a dynamic standby pool so they aren't turned away, while keeping on-time farmers moving without disruption.\"</i>", table_cell)
        ],
        [
            Paragraph("<b>Q3: How do you prevent fraud or manipulation in weighing and grading?</b>", table_cell),
            Paragraph("<i>\"Every weighbridge reading and lab test writes directly to an immutable audit trail with operator timestamps and machine IDs. Net weight and MSP amounts are calculated automatically by backend business logic, completely eliminating manual numerical tampering.\"</i>", table_cell)
        ],
        [
            Paragraph("<b>Q4: What is the mathematical formulation of your wait-time heuristic?</b>", table_cell),
            Paragraph("<i>\"Our algorithm computes the bottleneck service rate: mu = max(T_weigh x F_vehicle / N_weighbridges, T_quality / N_labs). It factors vehicle capacity (1.0 for tractor, 1.6 for double trolley, 2.2 for truck) and crop-specific moisture testing durations to provide dynamic queue estimates.\"</i>", table_cell)
        ]
    ]
    qa_table = Table(qa_data, colWidths=[150, 382])
    qa_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), dark_slate),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, card_bg]),
        ('PADDING', (0,0), (-1,-1), 4.5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(qa_table)
    story.append(Spacer(1, 8))

    # -------------------------------------------------------------
    # PART 4: HACKATHON DAY PRO-TIPS & TROUBLESHOOTING
    # -------------------------------------------------------------
    story.append(Paragraph("4. Hackathon Day Pro-Tips & Emergency Cheat Sheet", h1_style))
    tips_data = [
        [Paragraph("<b>* Volume Setting:</b> Set laptop speaker volume to ~70% so judges clearly hear the confirmation chimes and Hindi voice synthesis.<br/>"
                   "<b>* Quick Pre-Check Command:</b> Run <code>python test_system.py</code> in terminal to verify all 12 test suites in 5 seconds before the jury round.<br/>"
                   "<b>* If Terminal Closes by Accident:</b> Re-run <code>cd C:\\Users\\kumar\\.gemini\\antigravity\\scratch\\annasetu; python run.py</code>.<br/>"
                   "<b>* If Browser Shows Loading:</b> Press <code>Ctrl + F5</code> to force refresh the tab.<br/>"
                   "<b>* Team Coordination:</b> Designate Member 1 to operate the laptop, Member 2 to deliver the pitch script, and Members 3-6 to handle technical architecture and judge Q&A defense.", body_style)]
    ]
    tips_table = Table(tips_data, colWidths=[532])
    tips_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), green_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#86efac")),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(tips_table)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[OK] Detailed PDF Playbook generated successfully at: {PDF_OUTPUT_PATH}")

if __name__ == "__main__":
    build_pdf()
