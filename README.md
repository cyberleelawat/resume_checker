
# 🚀 Cyber Leelawat Resume Intelligence

## 📌 About the Project

**Cyber Leelawat Resume Intelligence** is a Python-based resume analysis tool built using Streamlit. It helps users analyse their resumes, identify missing sections, compare resume content with job descriptions, and get professional suggestions for improvement.

The tool supports PDF and DOCX resume formats and generates an estimated resume score with section-wise feedback.

---

## ✨ Features

- 📄 Upload Resume in PDF and DOCX formats
- 📊 Generate an Estimated Resume Score
- 🧠 Analyse Important Resume Sections
- 🎯 Job Description Keyword Matching
- 🔍 Identify Missing Resume Information
- 💡 Get Actionable Resume Improvement Suggestions
- 📥 Download Resume Analysis Report
- 🌙 Professional Dark-Themed Interface
- 🛡️ Cyber Leelawat Branding

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core Application Logic |
| Streamlit | Web Application Interface |
| pypdf | PDF Text Extraction |
| python-docx | DOCX Text Extraction |

---

## 📂 Project Structure

```text
resume_checker/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/cyberleelawat/resume_checker.git
cd resume_checker
```

### 2️⃣ Create Virtual Environment

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Use

### 1️⃣ Start the Application

```bash
streamlit run app.py
```

### 2️⃣ Open the Application

```text
http://localhost:8501
```

### 3️⃣ Upload Your Resume

- Upload your resume in PDF or DOCX format.
- Enter your target job role.
- Add a job description for keyword matching (optional).

### 4️⃣ Analyse Your Resume

- Click on the **Analyze Resume** button.
- Wait for the analysis to complete.
- Review your estimated score.
- Check section-wise feedback.
- Identify missing information.
- Follow the improvement recommendations.

### 5️⃣ Download Your Report

Download the generated resume analysis report from the application.

---

## 📊 Resume Analysis

The tool analyses the following resume sections:

| Section | Analysis |
|---|---|
| Contact Information | Email, phone number and contact details |
| Professional Summary | Career introduction and profile summary |
| Skills | Technical and professional skills |
| Work Experience | Employment history and responsibilities |
| Education | Academic qualifications |
| Projects | Practical projects and contributions |
| Certifications | Relevant certifications and courses |
| Job Description Match | Keyword alignment with job requirements |

---

## 🎯 Resume Scoring Methodology

The current rule-based scoring model uses the following components:

| Component | Weight |
|---|---:|
| Section Completeness | 60% |
| Resume Length | 10% |
| Job Description Keyword Match | 30% |

**Note:** If no job description is provided, the application uses its general resume checks to calculate an estimated score.

---

## 💡 Resume Improvement Example

### ❌ Weak Resume Statement

```text
Worked on network security.
```

### ✅ Improved Resume Statement

```text
Performed network security assessments,
reviewed security configurations, and documented
findings with practical remediation recommendations.
```

#### 📝 Recommendations

- Use professional action verbs.
- Mention relevant tools and technologies.
- Include measurable achievements when accurate.
- Keep your skills and experience truthful.

---

### PDF Text Extraction Issue

- Ensure that the PDF contains selectable text.
- Scanned image-only PDFs may not work with the basic text extraction workflow.
- OCR support can be added in a future version.

### Application Not Starting

- Verify Python installation.
- Activate your virtual environment.
- Install all required dependencies.
- Check the terminal error message.

---

## 🔐 Privacy & Security

- Upload only resumes you are authorised to process.
- Do not upload another person's resume without permission.
- Never publish personal resume data on GitHub.
- Do not commit API keys, passwords, or secrets.
- Review data handling before deploying the application publicly.

---

## 🗺️ Future Improvements

- OCR Support for Scanned Resumes
- Advanced Job Role Matching
- Detailed Resume Recommendations
- Additional Report Export Formats
- Multi-Language Resume Analysis
- Enhanced Resume Evaluation Rules

---

## ⚠️ Disclaimer

This project is developed for educational purposes and resume improvement. The generated score is an estimated assessment based on rule-based checks. It is not an official ATS score and does not guarantee interview calls, job offers, or selection.

Users are responsible for verifying all recommendations and ensuring that their resumes contain accurate information.

---

## 📚 References

- https://docs.python.org/3/
- https://docs.streamlit.io/
- https://pypdf.readthedocs.io/
- https://python-docx.readthedocs.io/

---

## 👨‍💻 Project Information

**Project Name:** Cyber Leelawat Resume Intelligence

**Repository:** resume_checker

**Developer:** Cyber Leelawat

**GitHub:** https://github.com/cyberleelawat

---

**© Cyber Leelawat. All Rights Reserved.**
