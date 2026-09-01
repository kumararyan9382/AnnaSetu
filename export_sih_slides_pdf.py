import os
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def build_slides_pdf():
    target_dir = r"C:\Users\kumar\OneDrive\Documents\Aryan\Hackathon"
    os.makedirs(target_dir, exist_ok=True)
    pdf_path = os.path.join(target_dir, "AnnaSetu_SIH2026_Idea_Presentation.pdf")
    alt_pdf_path = r"C:\Users\kumar\Documents\Aryan\Edit\AnnaSetu_SIH2026_Idea_Presentation.pdf"

    # Widescreen 16:9 dimensions: 11 x 6.1875 inches or landscape letter
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=landscape(letter),
        rightMargin=35,
        leftMargin=35,
        topMargin=30,
        bottomMargin=30
    )

    styles = getSampleStyleSheet()

    # Custom styles for 16:9 presentation slides
    slide_title_style = ParagraphStyle(
        'SlideTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#0c4a28'),
        spaceAfter=4
    )

    slide_subtitle_style = ParagraphStyle(
        'SlideSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#2e7d32'),
        spaceAfter=12
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=15,
        textColor=colors.HexColor('#1b5e20'),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    bullet_style = ParagraphStyle(
        'SlideBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#1f2937'),
        leftIndent=14,
        spaceAfter=3
    )

    footer_style = ParagraphStyle(
        'SlideFooter',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#6b7280'),
        alignment=2
    )

    story = []

    # ========================================================
    # SLIDE 1: TITLE PAGE
    # ========================================================
    story.append(Spacer(1, 35))
    story.append(Paragraph("SMART INDIA HACKATHON 2026", ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=26, leading=30, textColor=colors.HexColor('#0c4a28'), alignment=1, spaceAfter=6)))
    story.append(Paragraph("IDEA SUBMISSION PRESENTATION", ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=14, leading=17, textColor=colors.HexColor('#1b5e20'), alignment=1, spaceAfter=18)))
    story.append(HRFlowable(width="85%", thickness=2, color=colors.HexColor('#1b5e20'), spaceAfter=18))

    title_info = [
        [Paragraph("<b>Problem Statement ID:</b>", bullet_style), Paragraph("<b>SIH26032</b>", bullet_style)],
        [Paragraph("<b>Problem Statement Title:</b>", bullet_style), Paragraph("Smart Automation of Agricultural Procurement, Queue Scheduling, Multi-Mandi Price Discovery & Direct DBT Tracking", bullet_style)],
        [Paragraph("<b>Theme:</b>", bullet_style), Paragraph("Smart Automation", bullet_style)],
        [Paragraph("<b>Category:</b>", bullet_style), Paragraph("Software", bullet_style)],
        [Paragraph("<b>Sponsoring Ministry:</b>", bullet_style), Paragraph("Ministry of Consumer Affairs, Food & Public Distribution", bullet_style)],
        [Paragraph("<b>Team Name:</b>", bullet_style), Paragraph("AnnaSetu Innovators", bullet_style)],
        [Paragraph("<b>Idea Title:</b>", bullet_style), Paragraph("<b>AnnaSetu</b> - Smart Farmer Procurement & Multi-Mandi Scheduling Platform", bullet_style)]
    ]
    t1 = Table(title_info, colWidths=[180, 520])
    t1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f0fdf4')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#86efac')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#dcfce7')),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(t1)
    story.append(Spacer(1, 35))
    story.append(Paragraph("Slide 1 / 6 | @SIH Idea Submission Template | Team AnnaSetu", footer_style))
    story.append(PageBreak())

    # ========================================================
    # SLIDE 2: PROPOSED SOLUTION
    # ========================================================
    story.append(Paragraph("IDEA TITLE & PROPOSED SOLUTION", slide_title_style))
    story.append(Paragraph("AnnaSetu – Smart Farmer Procurement & Multi-Mandi Scheduling Platform", slide_subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0c4a28'), spaceAfter=8))

    story.append(Paragraph("1. Detailed Proposed Solution & Architecture:", section_heading))
    story.append(Paragraph("• <b>Smart Capacity-Aware Slot Booking:</b> Staggers farmer arrivals into 2-hour windows based on mandi weighbridge capacity, completely ending 24-36 hr tractor queues.", bullet_style))
    story.append(Paragraph("• <b>Dual Dedicated Role Portals:</b> Dedicated <b>Farmer Portal</b> (Booking, Live Token Tracking & DBT Passbook) + <b>Mandi Staff Operator Board</b> (Gate Entry, Electronic Weighbridge & Quality Lab).", bullet_style))
    story.append(Paragraph("• <b>Multi-Mandi Real-Time Spot Price Aggregator:</b> Displays live spot buying rates across Govt APMC and Private Mandis (ITC e-Choupal, Adani Silos, Reliance Kisan).", bullet_style))

    story.append(Paragraph("2. How It Addresses the Problem:", section_heading))
    story.append(Paragraph("• <b>Zero Waiting Bottlenecks:</b> Replaces chaotic roadside queues with an automated live token queue (#148).", bullet_style))
    story.append(Paragraph("• <b>Eliminates Distress Sales:</b> Farmers see verified spot rates before leaving their village, preventing 20% distress selling below MSP.", bullet_style))
    story.append(Paragraph("• <b>100% Transparent Weighing & Payout:</b> Direct digital scale logging with instant Aadhaar-linked PFMS Direct Benefit Transfer (DBT).", bullet_style))

    story.append(Paragraph("3. Innovation & Uniqueness:", section_heading))
    story.append(Paragraph("• <b>Free Kisan AI Mandi Advisor:</b> Recommends highest-paying mandi by calculating net profit after deducting round-trip diesel transport costs.", bullet_style))
    story.append(Paragraph("• <b>Full-Duplex WebSockets Live Sync:</b> Sub-50ms live updates to farmer's screen when staff approves each stage with spoken Hindi voice audio.", bullet_style))

    story.append(Spacer(1, 15))
    story.append(Paragraph("Slide 2 / 6 | @SIH Idea Submission Template | Team AnnaSetu", footer_style))
    story.append(PageBreak())

    # ========================================================
    # SLIDE 3: TECHNICAL APPROACH
    # ========================================================
    story.append(Paragraph("TECHNICAL APPROACH & SYSTEM ARCHITECTURE", slide_title_style))
    story.append(Paragraph("End-to-End Smart Automation Framework & Asynchronous Real-Time Stack", slide_subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0c4a28'), spaceAfter=8))

    story.append(Paragraph("1. Technology Stack & Frameworks:", section_heading))
    story.append(Paragraph("• <b>Backend Engine:</b> FastAPI (High-performance asynchronous Python event loops, RESTful OpenAPI /docs).", bullet_style))
    story.append(Paragraph("• <b>Real-Time Pub/Sub:</b> Full-Duplex WebSockets Manager for sub-50ms queue synchronization across all active devices.", bullet_style))
    story.append(Paragraph("• <b>Database & Security:</b> SQLite / PostgreSQL with ACID transactional integrity, masked Aadhaar, and cryptographic token hashing.", bullet_style))
    story.append(Paragraph("• <b>Frontend UI & Voice:</b> Modern TailwindCSS, responsive mobile-first Kisan UI ('Saral Mode'), Web Speech Synthesis API.", bullet_style))
    story.append(Paragraph("• <b>Offline Access:</b> Integrated 5-Language IVR Voice Hotline & SMS Gateway for keypad feature phones.", bullet_style))

    story.append(Paragraph("2. 5-Stage End-to-End Procurement Workflow:", section_heading))
    story.append(Paragraph("• <b>Stage 1 (Slot Booking):</b> Farmer books delivery slot ➔ Capacity balancer issues time-stamped token.", bullet_style))
    story.append(Paragraph("• <b>Stage 2 (Gate Check-in):</b> Gate officer scans QR/Token ➔ System validates slot & checks in vehicle (Voice announcement).", bullet_style))
    story.append(Paragraph("• <b>Stage 3 (Weighbridge):</b> Vehicle drives onto scale ➔ Gross weight captured directly from digital scale indicator.", bullet_style))
    story.append(Paragraph("• <b>Stage 4 (Quality Moisture Lab):</b> Grain assay sampled ➔ Moisture % recorded ➔ Certified Grade A assigned.", bullet_style))
    story.append(Paragraph("• <b>Stage 5 (DBT Payout):</b> Empty vehicle re-weighed (Tare weight) ➔ Net Qtl calculated ➔ Instant PFMS bank payout triggered ➔ Digital e-Voucher generated.", bullet_style))

    story.append(Spacer(1, 15))
    story.append(Paragraph("Slide 3 / 6 | @SIH Idea Submission Template | Team AnnaSetu", footer_style))
    story.append(PageBreak())

    # ========================================================
    # SLIDE 4: FEASIBILITY AND VIABILITY
    # ========================================================
    story.append(Paragraph("FEASIBILITY, SCALABILITY & RISK MITIGATION", slide_title_style))
    story.append(Paragraph("Operational Viability, Rural Adoption & Robust Fallback Mechanisms", slide_subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0c4a28'), spaceAfter=8))

    story.append(Paragraph("1. Technical & Operational Feasibility:", section_heading))
    story.append(Paragraph("• <b>Lightweight & Low Bandwidth:</b> Bundle size < 2 MB, loads in under 300ms, fully operational on 2G/3G networks.", bullet_style))
    story.append(Paragraph("• <b>Zero Capital Hardware Burden:</b> Mandi staff requires only basic Android smartphones/tablets; no proprietary hardware.", bullet_style))
    story.append(Paragraph("• <b>Plug-and-Play Interoperability:</b> Standard REST APIs enable rapid integration with state portals (e-Kharid, Meri Fasal Mera Byora, e-NAM).", bullet_style))

    story.append(Paragraph("2. Potential Challenges & Strategic Mitigations:", section_heading))
    story.append(Paragraph("• <b>Rural Internet Barriers:</b> <i>Mitigation:</i> Offline-first IVR Voice Hotline (/ivr) & SMS token dispatch operable with zero internet.", bullet_style))
    story.append(Paragraph("• <b>Digital Literacy Gap:</b> <i>Mitigation:</i> 1-Click 'Saral Mode' with large touch targets, multilingual audio readouts & Hindi voice guidance.", bullet_style))
    story.append(Paragraph("• <b>Queue Manipulation & Bribery:</b> <i>Mitigation:</i> Immutable cryptographic token ledger tied to vehicle number & Aadhaar hash.", bullet_style))
    story.append(Paragraph("• <b>Weighbridge Downtime:</b> <i>Mitigation:</i> Real-time load balancer automatically diverts incoming farmer bookings to nearest active center.", bullet_style))

    story.append(Spacer(1, 15))
    story.append(Paragraph("Slide 4 / 6 | @SIH Idea Submission Template | Team AnnaSetu", footer_style))
    story.append(PageBreak())

    # ========================================================
    # SLIDE 5: IMPACT AND BENEFITS
    # ========================================================
    story.append(Paragraph("SOCIO-ECONOMIC IMPACT & NATIONAL BENEFITS", slide_title_style))
    story.append(Paragraph("Transforming Rural Livelihoods, Post-Harvest Logistics & Governance", slide_subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0c4a28'), spaceAfter=8))

    story.append(Paragraph("1. Target Beneficiaries & National Scope:", section_heading))
    story.append(Paragraph("• 150+ Million Indian Farmers, APMC Mandi Staff, Private Corporate Hubs, State Civil Supplies & Food Corporation of India (FCI).", bullet_style))

    story.append(Paragraph("2. Direct Economic Impact for Farmers:", section_heading))
    story.append(Paragraph("• <b>+15% to 20% Higher Realized Income:</b> Access to private mandi bonus rates (+Rs. 85/Qtl on Wheat, +Rs. 170/Qtl on Mustard).", bullet_style))
    story.append(Paragraph("• <b>Saves Rs. 500 - Rs. 1,200 per Trip:</b> Completely eliminates 24-36 hrs of tractor diesel idling in mandi queues.", bullet_style))
    story.append(Paragraph("• <b>100% Elimination of Middlemen Cuts:</b> Full sale value credited directly to farmer's Aadhaar-linked bank account via DBT.", bullet_style))

    story.append(Paragraph("3. Social, Environmental & Governance Impact:", section_heading))
    story.append(Paragraph("• <b>Dignified 2-Hour Procurement:</b> Replaces grueling multi-day roadside wait times without food or sanitation.", bullet_style))
    story.append(Paragraph("• <b>Carbon Footprint Reduction:</b> Eliminates millions of liters of diesel exhaust from idling tractor fleets nationwide.", bullet_style))
    story.append(Paragraph("• <b>Ministry Analytics Hub:</b> Live state-wise procurement velocity, weighbridge telemetry, and automated anti-hoarding alerts.", bullet_style))

    story.append(Spacer(1, 15))
    story.append(Paragraph("Slide 5 / 6 | @SIH Idea Submission Template | Team AnnaSetu", footer_style))
    story.append(PageBreak())

    # ========================================================
    # SLIDE 6: RESEARCH AND REFERENCES
    # ========================================================
    story.append(Paragraph("RESEARCH, POLICY ALIGNMENT & REFERENCES", slide_title_style))
    story.append(Paragraph("Government Frameworks, Agricultural Policy Reports & Interoperability Standards", slide_subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0c4a28'), spaceAfter=8))

    ref_items = [
        ("1. SIH 2026 Problem Statement SIH26032:", " Ministry of Consumer Affairs, Food & Public Distribution (Smart Automation)."),
        ("2. Commission for Agricultural Costs & Prices (CACP):", " Price Policy Reports for Kharif & Rabi Crops 2026-27 (MSP Rate & FAQ moisture standards)."),
        ("3. e-NAM (National Agriculture Market):", " Guidelines on Unified Agricultural Marketing & Private Mandi / e-Choupal Interoperability."),
        ("4. Public Financial Management System (PFMS):", " Standard Operating Procedures for Direct Benefit Transfer (DBT) Direct Bank Credit."),
        ("5. NITI Aayog & FAO Supply Chain Reports:", " 'Transforming Agricultural Logistics, Post-Harvest Management & Mandi Modernization in India'."),
        ("6. Digital India Bhashini Initiative:", " Multi-lingual Indic speech synthesis frameworks for rural digital accessibility.")
    ]

    for idx, (r_label, r_val) in enumerate(ref_items):
        p = Paragraph(f"• <b>{r_label}</b>{r_val}", bullet_style)
        story.append(p)
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 30))
    story.append(Paragraph("Slide 6 / 6 | @SIH Idea Submission Template | Team AnnaSetu", footer_style))

    doc.build(story)

    # Copy to alt directory
    with open(pdf_path, 'rb') as src, open(alt_pdf_path, 'wb') as dst:
        dst.write(src.read())

    print("Slides PDF Generated successfully at:")
    print("1.", pdf_path)
    print("2.", alt_pdf_path)

if __name__ == "__main__":
    build_slides_pdf()
