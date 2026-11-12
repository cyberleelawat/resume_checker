import io
import re
from datetime import datetime

import streamlit as st
from docx import Document
from pypdf import PdfReader

# ============================================================
# CYBER LEELEWAT | RESUME INTELLIGENCE
# Python + Streamlit | Rule-based resume review
# ============================================================

st.set_page_config(
    page_title="Cyber Leelawat | Resume Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -------------------------- CYBER UI --------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Orbitron:wght@500;600;700;800&display=swap');

    :root {
        --bg: #050b14;
        --panel: rgba(8, 20, 34, .94);
        --line: #123b5a;
        --cyan: #00c8ff;
        --yellow: #ffc928;
        --red: #ff334f;
        --green: #28e08b;
        --muted: #a8bfd4;
        --white: #f4f8ff;
    }

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp {
        color: var(--white);
        background:
          radial-gradient(ellipse at 15% 18%, rgba(0, 110, 190, .18), transparent 34%),
          radial-gradient(ellipse at 88% 20%, rgba(180, 0, 35, .16), transparent 30%),
          linear-gradient(135deg, #030811 0%, #071321 55%, #030811 100%);
    }
    [data-testid="stHeader"] { background: rgba(2, 8, 16, .65); }
    .block-container { max-width: 1450px; padding-top: 1.2rem; padding-bottom: 1.2rem; }
    #MainMenu, footer { visibility: hidden; }

    .topbar {
        display:flex; align-items:center; justify-content:space-between; gap:20px;
        padding: 14px 22px; margin-bottom: 18px;
        background: rgba(3, 10, 19, .94); border:1px solid #123650;
        border-radius: 14px; box-shadow: 0 0 25px rgba(0,200,255,.07);
    }
    .brand { display:flex; align-items:center; gap:12px; }
    .brand-shield {
        width:48px; height:48px; display:flex; align-items:center; justify-content:center;
        border:2px solid var(--red); color:var(--yellow); font-weight:900; font-size:17px;
        clip-path: polygon(50% 0, 94% 17%, 88% 72%, 50% 100%, 12% 72%, 6% 17%);
        background:rgba(255,51,79,.08);
    }
    .brand-name { font-family:'Orbitron',sans-serif; font-size:20px; font-weight:800; letter-spacing:.5px; }
    .brand-name span { color:var(--yellow); }
    .brand-sub { color:#9ab2c9; font-size:10px; letter-spacing:1.4px; margin-top:3px; }
    .nav { color:#d6e7f7; font-size:12px; font-weight:700; letter-spacing:.5px; }
    .nav b { color:var(--yellow); margin:0 12px; }

    .hero {
        position:relative; overflow:hidden; min-height:245px; padding:30px 34px;
        border:1px solid #07547b; border-radius:18px;
        background:
          radial-gradient(circle at 78% 45%, rgba(0,174,255,.22), transparent 26%),
          radial-gradient(circle at 92% 70%, rgba(255,35,65,.17), transparent 22%),
          linear-gradient(110deg, rgba(4,14,27,.98), rgba(4,24,43,.94) 58%, rgba(10,9,20,.98));
        box-shadow: inset 0 0 35px rgba(0,174,255,.08), 0 12px 38px rgba(0,0,0,.28);
    }
    .hero:after {
        content:""; position:absolute; right:7%; top:-45px; width:310px; height:310px;
        border:1px solid rgba(0,200,255,.16); border-radius:50%;
        box-shadow:0 0 0 22px rgba(0,200,255,.025), 0 0 0 48px rgba(0,200,255,.02);
        pointer-events:none;
    }
    .hero-kicker { color:var(--red); font-family:monospace; font-size:12px; letter-spacing:2px; font-weight:800; }
    .hero h1 { font-family:'Orbitron',sans-serif; font-size:clamp(30px,4vw,48px); line-height:1.15; margin:10px 0; color:#fff; }
    .hero h1 span { color:var(--yellow); text-shadow:0 0 18px rgba(255,201,40,.2); }
    .hero-desc { color:#c0d5e8; font-size:15px; max-width:720px; line-height:1.65; }
    .hero-tags { margin-top:16px; display:flex; flex-wrap:wrap; gap:9px; }
    .tag { border:1px solid #24516d; border-radius:7px; padding:7px 11px; color:#d9efff; background:rgba(0,20,38,.7); font-size:11px; font-weight:700; }
    .tag.yellow { border-color:#80621a; color:var(--yellow); }
    .tag.red { border-color:#8c1d32; color:#ff8291; }
    .terminal {
        position:absolute; right:35px; top:38px; width:300px; padding:15px 17px;
        border:1px solid #155276; border-radius:12px; background:rgba(1,8,16,.78);
        box-shadow:0 0 24px rgba(0,190,255,.10); color:#65d9ff;
        font-family:monospace; font-size:11px; line-height:1.9;
    }
    .terminal .t-red { color:#ff6679; } .terminal .t-yellow { color:#ffd45c; }
    .feature-row { display:grid; grid-template-columns:repeat(5,1fr); gap:12px; margin:18px 0; }
    .feature {
        background:linear-gradient(145deg,rgba(10,26,43,.96),rgba(4,12,23,.96));
        border:1px solid #183e5b; border-radius:12px; padding:14px 12px; text-align:center;
        box-shadow:0 7px 18px rgba(0,0,0,.18);
    }
    .feature-icon { font-size:22px; margin-bottom:5px; }
    .feature-title { font-weight:800; font-size:12px; color:#f5f9ff; }
    .feature-sub { color:#91abc2; font-size:10px; margin-top:4px; line-height:1.4; }

    .section-kicker { color:var(--cyan); font-family:monospace; font-size:11px; letter-spacing:2px; font-weight:800; }
    .section-heading { color:#f7fbff; font-size:23px; font-weight:900; margin:3px 0 4px; }
    .muted { color:#9fb7cd; font-size:12px; }
    .upload-shell {
        background:linear-gradient(135deg,rgba(5,20,36,.98),rgba(5,13,25,.98));
        border:1px solid #087db2; border-radius:17px; padding:22px;
        box-shadow:0 0 25px rgba(0,174,255,.11), inset 0 0 25px rgba(0,174,255,.035);
    }
    div[data-testid="stFileUploader"] {
        background:rgba(1,10,20,.65); border:1px dashed #00aeea; border-radius:12px; padding:12px;
    }
    div[data-testid="stFileUploader"] section { border:0; }
    .stTextInput label, .stTextArea label, .stSelectbox label, .stFileUploader label {
        color:#e9f5ff !important; font-weight:800 !important;
    }
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div {
        background:#061321 !important; color:#eff8ff !important; border-color:#27516f !important;
        border-radius:9px !important;
    }
    .stButton>button, .stDownloadButton>button {
        border-radius:9px; font-weight:900; min-height:45px; border:1px solid #ff334f;
        background:linear-gradient(90deg,#ff334f,#b81235); color:white;
        box-shadow:0 0 18px rgba(255,51,79,.18);
    }
    .stButton>button:hover, .stDownloadButton>button:hover {
        border-color:#ffc928; color:#fff; box-shadow:0 0 20px rgba(255,201,40,.24);
    }
    div[data-testid="stProgressBar"] > div > div { background:linear-gradient(90deg,#00c8ff,#ffc928); }
    .result-card { background:rgba(5,17,30,.94); border:1px solid #17415e; border-radius:13px; padding:17px; }
    .result-card.red { border-color:#8c2439; }
    .result-card.yellow { border-color:#80621a; }
    .score-ring {
        width:180px; height:180px; border-radius:50%; margin:6px auto 12px;
        display:flex; flex-direction:column; align-items:center; justify-content:center;
        background:radial-gradient(circle at center,#061321 57%,transparent 58%),
        conic-gradient(var(--yellow) 0deg, var(--red) 130deg, var(--cyan) 260deg, var(--yellow) 360deg);
        box-shadow:0 0 26px rgba(0,200,255,.14);
    }
    .score-number { font-family:'Orbitron',sans-serif; color:var(--yellow); font-size:39px; font-weight:900; }
    .score-label { color:#d5e6f6; font-size:12px; font-weight:800; }
    .check-row { padding:10px 0; border-bottom:1px solid rgba(45,83,112,.45); }
    .check-row:last-child { border-bottom:0; }
    .good { color:#28e08b; font-weight:800; } .warn { color:#ffc928; font-weight:800; }
    .bad { color:#ff6679; font-weight:800; }
    .example-box { background:#071321; border-left:3px solid #00c8ff; padding:12px 14px; border-radius:7px; color:#d9edff; font-size:13px; white-space:pre-wrap; }
    .footer {
        border-top:1px solid #17415e; margin-top:28px; padding:17px 5px 5px;
        display:flex; justify-content:space-between; flex-wrap:wrap; gap:10px;
        color:#91abc2; font-size:11px;
    }
    .footer strong { color:#ffc928; }
    @media (max-width: 900px) {
        .terminal { display:none; } .feature-row { grid-template-columns:repeat(2,1fr); }
        .hero { padding:24px 20px; } .nav { display:none; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------- TEXT EXTRACTION --------------------------
def extract_resume(uploaded_file):
    raw = uploaded_file.getvalue()
    filename = uploaded_file.name.lower()
    if filename.endswith(".pdf"):
        reader = PdfReader(io.BytesIO(raw))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    if filename.endswith(".docx"):
        doc = Document(io.BytesIO(raw))
        content = [p.text for p in doc.paragraphs]
        for table in doc.tables:
            for row in table.rows:
                content.append(" | ".join(cell.text for cell in row.cells))
        return "\n".join(content)
    raise ValueError("Unsupported file type. Please upload a PDF or DOCX file.")

def normalize(text):
    return re.sub(r"\s+", " ", text.lower()).strip()

def contains(text, phrase):
    if phrase == "@":
        return "@" in text
    return re.search(r"(?<!\w)" + re.escape(phrase.lower()) + r"(?!\w)", text) is not None

def analyze_resume(text, job_description=""):
    low = normalize(text)
    word_count = len(re.findall(r"\b[\w+#.-]+\b", low))

    email_found = re.search(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b", low) is not None
    phone_found = re.search(r"(?:\+?\d[\d\s().-]{8,}\d)", text) is not None

    checks = [
        {
            "name": "Contact Information",
            "ok": email_found and phone_found,
            "why": "A recruiter may not be able to contact you if your email address or phone number is missing.",
            "fix": "Add a professional email address and phone number near the top of your resume. Add LinkedIn or portfolio links when relevant.",
            "example": "Alex Morgan\nalex.morgan@email.com | +91 98765 43210\nlinkedin.com/in/alexmorgan | github.com/alexmorgan",
        },
        {
            "name": "Professional Summary",
            "ok": any(contains(low, x) for x in ["professional summary", "career summary", "profile", "objective", "about me"]),
            "why": "A short introduction helps recruiters understand your role, strengths, and career direction quickly.",
            "fix": "Write 2–4 concise lines tailored to the target role. Mention your level, strongest relevant skills, and evidence of practical work.",
            "example": "Entry-level Cybersecurity Analyst with hands-on experience in networking, Linux, vulnerability assessment, and security labs. Familiar with Nmap, Wireshark, and OWASP fundamentals.",
        },
        {
            "name": "Work Experience",
            "ok": any(contains(low, x) for x in ["work experience", "professional experience", "employment history", "internship", "experience"]),
            "why": "Recruiters need to see where you applied your skills and what impact your work had.",
            "fix": "List roles in reverse chronological order. For each role, include title, organization, dates, and 2–4 outcome-focused bullet points.",
            "example": "Security Intern | ABC Technologies | Jan 2025 – Jun 2025\n• Assisted with vulnerability assessments across 5 lab applications.\n• Documented findings and remediation steps for the engineering team.",
        },
        {
            "name": "Education",
            "ok": any(contains(low, x) for x in ["education", "academic background", "qualification", "bachelor", "master", "university", "college"]),
            "why": "Education details help employers understand your academic background and relevant qualifications.",
            "fix": "Include your degree or course, institution, location if useful, and graduation year. Add grades only when they strengthen your application.",
            "example": "B.Tech in Computer Science | XYZ University\n2022 – 2026 | CGPA: 8.2/10",
        },
        {
            "name": "Technical & Professional Skills",
            "ok": any(contains(low, x) for x in ["technical skills", "skills", "core competencies", "key skills"]),
            "why": "A dedicated skills section makes relevant capabilities easier to find during a quick review.",
            "fix": "Group skills into categories and list only tools and abilities you can confidently explain in an interview.",
            "example": "Security: Vulnerability Assessment, OWASP Top 10\nTools: Nmap, Burp Suite, Wireshark\nSystems: Linux, Windows\nProgramming: Python, Bash",
        },
        {
            "name": "Projects",
            "ok": any(contains(low, x) for x in ["projects", "selected projects", "personal projects", "academic projects"]),
            "why": "Projects provide evidence that you can apply your knowledge, especially if you are early in your career.",
            "fix": "Add 2–3 relevant projects. Explain the problem, technologies used, your contribution, and the result.",
            "example": "Web Security Lab | Python, Flask, OWASP\n• Built a local practice application and tested common web security issues.\n• Documented findings and recommended secure coding fixes.",
        },
        {
            "name": "Certifications & Training",
            "ok": any(contains(low, x) for x in ["certification", "certifications", "courses", "licenses", "training"]),
            "why": "Relevant training can support your skills, but credentials should be accurate and verifiable.",
            "fix": "List relevant completed certifications with issuer and year. Do not list courses you have not completed.",
            "example": "Google Cybersecurity Certificate | Google / Coursera | 2025",
        },
        {
            "name": "Measurable Achievements",
            "ok": bool(re.search(r"\b\d+\s?%|\b\d+\+|\b\d+\s?(users|clients|projects|hours|days|systems|reports)\b", low)),
            "why": "Specific outcomes make your contributions more convincing than generic responsibility statements.",
            "fix": "Add honest numbers where possible: scale, time saved, number of users, systems reviewed, projects delivered, or quality improvements.",
            "example": "Weak: Worked on network monitoring.\nStronger: Monitored 12 lab endpoints and documented 8 configuration issues during a 4-week security exercise.",
        },
    ]

    passed = sum(item["ok"] for item in checks)
    structure_score = (passed / len(checks)) * 60
    length_score = 10 if 250 <= word_count <= 900 else 6 if 150 <= word_count <= 1200 else 2

    matched, missing = [], []
    jd_score = 0
    if job_description.strip():
        jd = normalize(job_description)
        skill_bank = [
            "python", "java", "javascript", "typescript", "sql", "html", "css", "react",
            "node.js", "django", "flask", "fastapi", "git", "linux", "aws", "azure",
            "docker", "kubernetes", "machine learning", "data analysis", "excel",
            "power bi", "cybersecurity", "networking", "penetration testing", "burp suite",
            "owasp", "wireshark", "nmap", "metasploit", "communication", "leadership",
            "problem solving", "project management", "rest api", "testing", "agile",
            "cloud", "security", "firewall", "incident response", "siem", "soc",
            "vulnerability assessment", "risk assessment",
        ]
        candidates = [term for term in skill_bank if contains(jd, term)]
        filler = {
            "the", "and", "for", "with", "you", "will", "our", "are", "this", "that",
            "from", "have", "has", "your", "who", "all", "job", "role", "work",
            "years", "year", "experience", "required", "preferred", "ability",
            "must", "should", "team", "responsibilities", "requirements",
        }
        extras = [
            term for term in set(re.findall(r"\b[a-z][a-z0-9+#.-]{3,}\b", jd))
            if term not in filler and term not in candidates
        ]
        candidates = list(dict.fromkeys(candidates + sorted(extras)[:20]))
        matched = [term for term in candidates if contains(low, term)]
        missing = [term for term in candidates if term not in matched]
        jd_score = (len(matched) / len(candidates) * 30) if candidates else 0
        score = round(structure_score + length_score + jd_score)
        score_basis = "60% section completeness + 10% resume length + 30% job-description keyword alignment"
    else:
        score = round(((structure_score + length_score) / 70) * 100)
        score_basis = "General resume completeness estimate. Add a job description for role-specific matching."

    return {
        "score": max(0, min(100, score)),
        "checks": checks,
        "word_count": word_count,
        "passed": passed,
        "matched": matched,
        "missing": missing,
        "has_jd": bool(job_description.strip()),
        "score_basis": score_basis,
    }

# -------------------------- HEADER --------------------------
st.markdown(
    """
    <div class="topbar">
      <div class="brand">
        <div class="brand-shield">CL</div>
        <div>
          <div class="brand-name">CYBER <span>LEELEWAT</span></div>
          <div class="brand-sub">CYBER SECURITY · TRAINING · TOOLS · RESEARCH</div>
        </div>
      </div>
      <div class="nav">⌂ HOME <b>│</b> ◉ RESUME ANALYZER <b>│</b> ✦ FEATURES <b>│</b> ▤ RESUME TIPS <b>│</b> ⓘ ABOUT</div>
    </div>
    <div class="hero">
      <div class="hero-kicker">▰ CAREER INTELLIGENCE PLATFORM / CL-TOOLS</div>
      <h1>Resume <span>Intelligence</span></h1>
      <div class="hero-desc">
        Analyze your resume. Identify missing details. Improve your job alignment.
        Get clear, practical feedback with examples you can use.
      </div>
      <div class="hero-tags">
        <span class="tag yellow">✦ RESUME AUDIT</span>
        <span class="tag">⌕ JOB MATCHING</span>
        <span class="tag red">⚑ SKILL GAP REVIEW</span>
        <span class="tag">▣ ACTIONABLE EXAMPLES</span>
      </div>
      <div class="terminal">
        <div><span class="t-yellow">root@cyber-leelewat</span>:~# resume-check</div>
        <div>[+] Document parser initialized</div>
        <div>[+] Section analysis module ready</div>
        <div>[+] Job keyword matcher ready</div>
        <div><span class="t-red">[*] Awaiting resume upload_</span></div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="feature-row">
      <div class="feature"><div class="feature-icon">🎯</div><div class="feature-title">Job Match Score</div><div class="feature-sub">Compare resume with a target role</div></div>
      <div class="feature"><div class="feature-icon">🛡️</div><div class="feature-title">ATS Readiness</div><div class="feature-sub">Review structure and searchable text</div></div>
      <div class="feature"><div class="feature-icon">⌕</div><div class="feature-title">Section Analysis</div><div class="feature-sub">Review each important resume section</div></div>
      <div class="feature"><div class="feature-icon">💡</div><div class="feature-title">Improvement Examples</div><div class="feature-sub">See how to fix identified gaps</div></div>
      <div class="feature"><div class="feature-icon">📊</div><div class="feature-title">Detailed Report</div><div class="feature-sub">Download your review summary</div></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------------- UPLOAD PANEL --------------------------
st.markdown('<div class="section-kicker">01 / DOCUMENT INTAKE</div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">Upload Your Resume</div>', unsafe_allow_html=True)
st.markdown('<div class="muted">Choose your resume first, then start the analysis. PDF and DOCX are supported.</div><br>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="upload-shell">', unsafe_allow_html=True)
    col_upload, col_job = st.columns([1.05, 1], gap="large")
    with col_upload:
        uploaded = st.file_uploader(
            "Choose Resume File",
            type=["pdf", "docx"],
            help="Upload a text-based PDF or DOCX file. Scanned PDFs may require OCR.",
        )
        if uploaded:
            st.success(f"Selected file: {uploaded.name}")
        else:
            st.caption("Drag and drop your resume here, or browse to select a file.")
    with col_job:
        job_role = st.text_input(
            "Target Job Role (optional)",
            placeholder="e.g. Cyber Security Analyst, SOC Analyst, Python Developer",
        )
        job_description = st.text_area(
            "Job Description (optional)",
            height=112,
            placeholder="Paste the job description here for a more relevant keyword match...",
        )
    analyze_clicked = st.button(
        "⚡  ANALYZE MY RESUME",
        type="primary",
        use_container_width=True,
        disabled=uploaded is None,
    )
    st.markdown('</div>', unsafe_allow_html=True)

if analyze_clicked and uploaded:
    try:
        with st.spinner("Initializing document analysis..."):
            resume_text = extract_resume(uploaded)
        if not resume_text.strip():
            st.error("No selectable text was found. If this is a scanned PDF, run OCR and upload a searchable PDF or DOCX.")
        else:
            progress = st.progress(0, text="Starting analysis...")
            stages = [
                "Extracting document text",
                "Checking contact information and resume sections",
                "Reviewing projects, skills, and achievements",
                "Comparing content with the target job description",
                "Preparing your improvement report",
            ]
            import time
            for i, stage in enumerate(stages, start=1):
                progress.progress(i * 20, text=stage)
                time.sleep(0.18)
            result = analyze_resume(resume_text, job_description)
            st.session_state["cl_result"] = result
            st.session_state["cl_filename"] = uploaded.name
            st.session_state["cl_role"] = job_role
            st.session_state["cl_jd"] = job_description
            progress.empty()
    except Exception as error:
        st.error(f"Unable to analyze this file: {error}")

# -------------------------- RESULTS --------------------------
if "cl_result" in st.session_state:
    result = st.session_state["cl_result"]
    st.divider()
    st.markdown('<div class="section-kicker">02 / ANALYSIS OUTPUT</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Resume Analysis Report</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="muted">File: {st.session_state["cl_filename"]} &nbsp; | &nbsp; '
        f'Generated: {datetime.now().strftime("%d %b %Y, %I:%M %p")} &nbsp; | &nbsp; '
        f'Target: {st.session_state.get("cl_role") or "General review"}</div><br>',
        unsafe_allow_html=True,
    )

    score_col, stats_col = st.columns([0.75, 2.1], gap="large")
    with score_col:
        st.markdown(
            f"""
            <div class="result-card" style="text-align:center;">
              <div class="muted">OVERALL RESUME SCORE</div>
              <div class="score-ring">
                <div class="score-number">{result["score"]}%</div>
                <div class="score-label">READINESS</div>
              </div>
              <div class="muted">{result["passed"]} of 8 checks detected</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.progress(result["score"] / 100)
    with stats_col:
        a, b, c = st.columns(3)
        a.markdown(f'<div class="result-card"><div class="muted">WORD COUNT</div><div style="font-size:27px;font-weight:900;color:#00c8ff">{result["word_count"]}</div></div>', unsafe_allow_html=True)
        b.markdown(f'<div class="result-card"><div class="muted">CHECKS PASSED</div><div style="font-size:27px;font-weight:900;color:#28e08b">{result["passed"]}/8</div></div>', unsafe_allow_html=True)
        c.markdown(f'<div class="result-card"><div class="muted">ITEMS TO REVIEW</div><div style="font-size:27px;font-weight:900;color:#ffc928">{8-result["passed"]}</div></div>', unsafe_allow_html=True)
        st.write("")
        st.markdown(
            f'<div class="result-card"><b style="color:#ffc928">SCORING METHOD</b><br>'
            f'<span class="muted">{result["score_basis"]}</span></div>',
            unsafe_allow_html=True,
        )

    st.markdown('<div class="section-heading">03 / Section-by-Section Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="muted">Expand any item to understand the finding and see a practical correction example.</div><br>', unsafe_allow_html=True)

    for index, item in enumerate(result["checks"], start=1):
        status = "PASS" if item["ok"] else "REVIEW"
        icon = "🟢" if item["ok"] else "🟡"
        with st.expander(f"{icon}  {index:02d}. {item['name']}  —  {status}", expanded=not item["ok"]):
            if item["ok"]:
                st.markdown('<span class="good">SECTION DETECTED</span>', unsafe_allow_html=True)
                st.write("This section appears to be present. Review it for accuracy, relevance, and clear evidence.")
            else:
                st.markdown('<span class="warn">IMPROVEMENT RECOMMENDED</span>', unsafe_allow_html=True)
                st.write("**What is missing / why it matters**")
                st.write(item["why"])
                st.write("**How to improve it**")
                st.write(item["fix"])
                st.write("**Example you can adapt**")
                st.markdown(f'<div class="example-box">{item["example"]}</div>', unsafe_allow_html=True)

    if result["has_jd"]:
        st.markdown('<div class="section-heading">04 / Job Description Match</div>', unsafe_allow_html=True)
        match_col, missing_col = st.columns(2, gap="large")
        with match_col:
            st.markdown('<div class="result-card"><b style="color:#28e08b">✓ MATCHED KEYWORDS</b></div>', unsafe_allow_html=True)
            st.write(", ".join(result["matched"]) if result["matched"] else "No clear keyword matches were detected.")
        with missing_col:
            st.markdown('<div class="result-card red"><b style="color:#ff6679">! KEYWORDS TO REVIEW</b></div>', unsafe_allow_html=True)
            st.write(", ".join(result["missing"][:35]) if result["missing"] else "No missing terms were detected by this basic check.")
        st.caption("Only add a keyword if it truthfully represents your knowledge or experience. Never add skills just to manipulate a score.")

    st.markdown('<div class="section-heading">05 / Recommended Improvement Plan</div>', unsafe_allow_html=True)
    gaps = [item for item in result["checks"] if not item["ok"]]
    if not gaps and not result["missing"]:
        st.success("No major gaps were detected by these basic checks. Tailor your achievements and summary to each target role.")
    else:
        for number, item in enumerate(gaps, start=1):
            st.markdown(f"**{number}. {item['name']}**")
            st.write(item["fix"])
        if result["missing"]:
            st.markdown("**Job-description terms to verify:** " + ", ".join(result["missing"][:20]))

    report_lines = [
        "CYBER LEELEWAT | RESUME INTELLIGENCE REPORT",
        f"Resume: {st.session_state['cl_filename']}",
        f"Target role: {st.session_state.get('cl_role') or 'Not specified'}",
        f"Overall score: {result['score']}%",
        f"Word count: {result['word_count']}",
        f"Scoring method: {result['score_basis']}",
        "",
        "SECTION ANALYSIS",
    ]
    for item in result["checks"]:
        report_lines.append(f"{'PASS' if item['ok'] else 'REVIEW'}: {item['name']}")
        if not item["ok"]:
            report_lines.extend([f"Why: {item['why']}", f"Fix: {item['fix']}", f"Example: {item['example']}", ""])
    report_lines.extend([
        "MATCHED KEYWORDS: " + ", ".join(result["matched"]),
        "KEYWORDS TO REVIEW: " + ", ".join(result["missing"]),
        "",
        "Disclaimer: This is a rule-based estimate, not a hiring probability or guaranteed ATS score.",
    ])
    st.download_button(
        "⬇  DOWNLOAD ANALYSIS REPORT (.TXT)",
        data="\n".join(report_lines),
        file_name="Cyber_Leelawat_Resume_Analysis.txt",
        mime="text/plain",
        use_container_width=True,
    )
    st.caption("Note: This version uses rule-based checks and keyword overlap. It does not predict hiring decisions or guarantee an ATS score.")

# -------------------------- FOOTER --------------------------
st.markdown(
    """
    <div class="footer">
      <div><strong>🛡 CYBER LEELEWAT</strong> &nbsp; | &nbsp; Resume Intelligence v2.0</div>
      <div>© 2026 Cyber Leelawat. All Rights Reserved. &nbsp; | &nbsp; Cyber Security · Training · Tools · Research</div>
    </div>
    """,
    unsafe_allow_html=True,
)
