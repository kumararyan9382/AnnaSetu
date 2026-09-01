"""
Generate the Official Hackathon Day Action Plan PDF for AnnaSetu
Focused strictly on: What to do, What to say, Exact Clicks, Timeline, and Winning Judge Q&A.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

PDF_PATH = r"C:\Users\kumar\OneDrive\Documents\Aryan\Hackathon\AnnaSetu_Hackathon_Day_Action_Plan.pdf"
os.makedirs(os.path.dirname(PDF_PATH), exist_ok=True)

class ActionPlanCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(ActionPlanCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            super(ActionPlanCanvas, self).showPage()
        super(ActionPlanCanvas, self).save()

    def draw_header_footer(self, page_count):
        self.saveState()
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor("#15803d"))
            self.drawString(40, 755, "ANNASÈTU (अन्नसेतु) -- Official Hackathon Day Action Plan")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#64748b"))
            self.drawRightString(572, 755, "Smart India Hackathon 2026 | SIH26032")
            
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
        self.drawString(40, 28, "Ministry of Consumer Affairs, Food & Public Distribution | SIH Finalist Team")
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(572, 28, page_text)

        self.restoreState()

def build_action_plan_pdf():
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
    blue_bg = colors.HexColor("#eff6ff")
    amber_bg = colors.HexColor("#fffbeb")

    title_style = ParagraphStyle(
        'DocTitle',
        fontName='Helvetica-Bold',
        fontSize=17,
        leading=21,
        textColor=primary_green,
        spaceAfter=2
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#64748b"),
        spaceAfter=6
    )

    h2_style = ParagraphStyle(
        'H2_Style',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=dark_slate,
        spaceBefore=6,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Style',
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.8,
        textColor=text_slate,
        spaceAfter=3
    )

    box_title = ParagraphStyle(
        'BoxTitle',
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#14532d")
    )

    box_content = ParagraphStyle(
        'BoxContent',
        fontName='Helvetica',
        fontSize=8.2,
        leading=11.5,
        textColor=colors.HexColor("#1e293b")
    )

    table_cell = ParagraphStyle(
        'TableCell',
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=text_slate
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
            Paragraph("<b>ANNASÈTU (अन्नसेतु)</b><br/><font size='8' color='#166534'>Smart Procurement Scheduling & Live Queue Management</font>", ParagraphStyle('H', fontName='Helvetica-Bold', fontSize=13, textColor=colors.HexColor("#14532d"), leading=15)),
            Paragraph("<font size='7.5' color='#0f172a'><b>SIH 2026 Problem ID:</b> SIH26032<br/><b>Theme:</b> Smart Automation (Software)<br/><b>Ministry:</b> Consumer Affairs, Food & Public Distribution</font>", ParagraphStyle('R', fontName='Helvetica', fontSize=7.5, leading=10, alignment=2))
        ]
    ]
    banner_table = Table(banner_data, colWidths=[314, 222])
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), green_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#86efac")),
        ('PADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(banner_table)
    story.append(Spacer(1, 5))

    story.append(Paragraph("<b>OFFICIAL HACKATHON DAY ACTION PLAN & PITCH SCRIPT</b>", title_style))
    story.append(Paragraph("A quick, foolproof cheatsheet of exactly what to do from morning arrival to your final judge presentation.", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#e2e8f0"), spaceAfter=6))

    # -------------------------------------------------------------
    # SECTION 1: MORNING SETUP
    # -------------------------------------------------------------
    setup_data = [
        [Paragraph("<b>PHASE 1: Morning Setup (15 Mins Before Judges Arrive)</b>", box_title)],
        [Paragraph("<b>1. Start Server:</b> Open Windows PowerShell and run:<br/>"
                   "&nbsp;&nbsp;&nbsp;&nbsp;<code>cd C:\\Users\\kumar\\.gemini\\antigravity\\scratch\\annasetu</code><br/>"
                   "&nbsp;&nbsp;&nbsp;&nbsp;<code>python run.py</code><br/>"
                   "&nbsp;&nbsp;&nbsp;&nbsp;<i>(Verify terminal shows: 'Server running at: http://127.0.0.1:8000')</i><br/>"
                   "<b>2. Setup Chrome Screen:</b> Open Google Chrome and set up <b>Two Split Windows</b> side-by-side:<br/>"
                   "&nbsp;&nbsp;&nbsp;&nbsp;• <b>Left Window:</b> Farmer Portal (<code>http://127.0.0.1:8000/</code>)<br/>"
                   "&nbsp;&nbsp;&nbsp;&nbsp;• <b>Right Window:</b> Mandi Staff Board (<code>http://127.0.0.1:8000/staff</code>)<br/>"
                   "<b>3. Keep Extra Tabs Ready:</b> Mandi Tracker (<code>/centers</code>), Voice Simulator (<code>/ivr</code>), Ministry Admin (<code>/admin</code>).", box_content)]
    ]
    setup_table = Table(setup_data, colWidths=[536])
    setup_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), green_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#86efac")),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(setup_table)
    story.append(Spacer(1, 6))

    # -------------------------------------------------------------
    # SECTION 2: 4-MINUTE LIVE PITCH SCRIPT
    # -------------------------------------------------------------
    story.append(Paragraph("<b>PHASE 2: The 4-Minute Winning Demo Script (When Jury Arrives)</b>", h2_style))

    pitch_data = [
        [
            Paragraph("Time", table_header),
            Paragraph("Screen Action & What to Click", table_header),
            Paragraph("Spoken Pitch (What to Say to Judges)", table_header)
        ],
        [
            Paragraph("<b>0:00 - 0:45</b><br/><i>The Problem & Booking</i>", table_cell),
            Paragraph("<b>On Left Window (Home):</b><br/>"
                      "1. Scroll to registration form.<br/>"
                      "2. Name: <code>Harishchandra Verma</code><br/>"
                      "3. Crop: <code>Wheat</code>, Qty: <code>50 Quintals</code>.<br/>"
                      "4. Mandi: <code>Karnal Main Anaj Mandi</code>.<br/>"
                      "5. Click <b>'Confirm & Generate Token'</b>.", table_cell),
            Paragraph("<i>\"Respected jury, during peak procurement, farmers wait 24-48 hours in chaotic mandi queues, risking distress sales. AnnaSetu solves this with slot scheduling. Notice how our system immediately guarantees the official MSP payout of <b>Rs. 1,21,250</b> upfront!\"</i>", table_cell)
        ],
        [
            Paragraph("<b>0:45 - 2:00</b><br/><i>Live Real-Time Sync (WOW Factor)</i>", table_cell),
            Paragraph("<b>Left:</b> Live Tracker (<code>/track/AS-26-WHT-XXX</code>)<br/>"
                      "<b>Right:</b> Staff Board (<code>/staff</code>)<br/>"
                      "1. Right Screen: Click <b>'Check-in Gate Entry'</b> ➔ Confirm.<br/>"
                      "2. Right Screen: Click <b>'Send to Weighbridge'</b> (7,450 kg) ➔ Confirm.<br/>"
                      "3. Right Screen: Click <b>'Send to Quality Lab'</b> (11.4% Moisture) ➔ Confirm.<br/>"
                      "4. Right Screen: Click <b>'Authorize & Pay DBT'</b> ➔ Confirm.", table_cell),
            Paragraph("<i>\"Watch how the farmer's screen on the left updates in real time via WebSockets without any page reload! The gate entry registers, gross scale reading logs 7,450 kg, quality moisture tests at 11.4% Grade A, and instant Direct Benefit Transfer clears to the farmer's Aadhaar-linked account.\"</i>", table_cell)
        ],
        [
            Paragraph("<b>2:00 - 2:45</b><br/><i>Verified Receipt & Printing</i>", table_cell),
            Paragraph("<b>On Left Window:</b><br/>"
                      "1. Scroll down to the <b>Official Government Procurement e-Receipt</b>.<br/>"
                      "2. Point to the AnnaSetu watermark and DBT Ref No: <code>DBT-2026-WHT-XXXXXXX</code>.<br/>"
                      "3. Click <b>'Print e-Receipt Now'</b>.", table_cell),
            Paragraph("<i>\"Upon final weighing, a tamper-proof digital e-receipt with digital watermark is issued instantly for full audit transparency and farmer peace of mind.\"</i>", table_cell)
        ],
        [
            Paragraph("<b>2:45 - 3:30</b><br/><i>Inclusive Tech & Optimization</i>", table_cell),
            Paragraph("<b>Tab 2 (/centers):</b> Show Mandi load balancer.<br/>"
                      "<b>Tab 6 (/ivr):</b> Select Hindi/Punjabi, tap mic to simulate 1800-180-2626 call.<br/>"
                      "<b>Tab 5 (/admin):</b> Show Ministry Admin overview with MT volume & funds.", table_cell),
            Paragraph("<i>\"For rural farmers without smartphones, our toll-free Voice IVR speaks status aloud in 5 regional languages. Furthermore, our load balancer redistributes traffic to avoid mandi bottlenecks, giving the Ministry complete real-time oversight.\"</i>", table_cell)
        ]
    ]

    pitch_table = Table(pitch_data, colWidths=[65, 230, 241])
    pitch_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0f172a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, card_bg]),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(pitch_table)
    story.append(Spacer(1, 6))

    # -------------------------------------------------------------
    # SECTION 3: JURY Q&A DEFENSE
    # -------------------------------------------------------------
    story.append(Paragraph("<b>PHASE 3: Jury Q&A Defense (High-Scoring Answers)</b>", h2_style))

    qa_data = [
        [
            Paragraph("Jury Question", table_header),
            Paragraph("Your Winning Answer (Point-by-Point)", table_header)
        ],
        [
            Paragraph("<b>Q1: What if farmers don't have smartphones or internet?</b>", table_cell),
            Paragraph("<i>\"We have built a toll-free IVR system (1800-180-2626). A farmer can call from any basic keypad phone, enter their phone or token number, and hear their live queue position and payment status in Hindi, Punjabi, Marathi, Telugu, or English.\"</i>", table_cell)
        ],
        [
            Paragraph("<b>Q2: What happens if a farmer is delayed by traffic/breakdown?</b>", table_cell),
            Paragraph("<i>\"Tokens feature flexible 2-hour arrival windows. If delayed, the vehicle enters a dynamic standby buffer instead of cancelling, ensuring farmers never lose their turn or face distress sales.\"</i>", table_cell)
        ],
        [
            Paragraph("<b>Q3: How do you prevent corruption or fake weighings?</b>", table_cell),
            Paragraph("<i>\"Weighbridge readings and moisture percentages log directly into an immutable audit trail. MSP rates and final net payouts are calculated deterministically by backend code, eliminating manual tampering.\"</i>", table_cell)
        ],
        [
            Paragraph("<b>Q4: What if the internet fails at the Mandi during procurement?</b>", table_cell),
            Paragraph("<i>\"AnnaSetu is built with a local-first offline architecture. Staff can log entries locally on SQLite; all records sync automatically to the Ministry central cloud once connectivity restores.\"</i>", table_cell)
        ]
    ]

    qa_table = Table(qa_data, colWidths=[176, 360])
    qa_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#15803d")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, card_bg]),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(qa_table)
    story.append(Spacer(1, 6))

    # -------------------------------------------------------------
    # SECTION 4: EMERGENCY PRO-TIPS
    # -------------------------------------------------------------
    tips_data = [
        [Paragraph("<b>💡 Emergency Hacks & Pro-Tips on Hackathon Day:</b><br/>"
                   "• <b>Want an automatic 10-second demo?</b> Click the green <b>'▶ Auto-Play Demo'</b> button on <code>/track</code>, or run <code>python auto_demo_bot.py</code> in terminal.<br/>"
                   "• <b>Port 8000 already in use?</b> Run: <code>Stop-Process -Name 'python' -Force</code> then <code>python run.py</code>.<br/>"
                   "• <b>Syncing Two Windows:</b> Ensure both the Farmer tracker and Staff dashboard are watching the <b>same Mandi & Token ID</b>.", ParagraphStyle('Tips', fontName='Helvetica', fontSize=8, leading=11, textColor=colors.HexColor("#78350f")))]
    ]
    tips_table = Table(tips_data, colWidths=[536])
    tips_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), amber_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#fde68a")),
        ('PADDING', (0,0), (-1,-1), 4.5),
    ]))
    story.append(tips_table)

    doc.build(story, canvasmaker=ActionPlanCanvas)
    print(f"[OK] Official Hackathon Day Action Plan PDF built at: {PDF_PATH}")

if __name__ == "__main__":
    build_action_plan_pdf()
