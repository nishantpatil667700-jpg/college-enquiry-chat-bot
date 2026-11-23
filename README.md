# 🎓 College Enquiry Chatbot (Problem Statement 11)

**Student Name:** Nishant Patil  
**Roll No:** 11  
**Project:** LLM Mini Project (10-Mark Evaluation)  
**Submission Deadline:** 22 November 2026, 11:30 AM  

---

## 📌 Problem Statement
Admission offices receive hundreds of repetitive questions regarding courses, eligibility, fee structures, hostel facilities, and placements.  
This project implements an intelligent, grounded **College Enquiry Chatbot** using Python, Streamlit, and the Groq API (Llama 3.3 70B). It answers prospective student queries using **only** the official college info sheet (`college_info.txt`), with zero hallucination.

---

## 🚀 Key Features
- **Strict Grounding:** Restricts answers strictly to `college_info.txt`.
- **Zero Hallucination:** Politely refuses out-of-context or unknown queries with a standard fallback notice.
- **Interactive Streamlit UI:** Modern chat interface with `st.chat_input`, `st.chat_message`, and avatars.
- **1-Click Quick Sample Questions:** Sidebar buttons to test all primary FAQs instantly.
- **Session State History:** Maintains conversation memory across multi-turn interactions.
- **Secure API Key Handling:** Seamlessly loads from `.env` or accepts direct input via the sidebar UI.
- **Ground Truth Inspector:** Collapsible sidebar view of `college_info.txt` for real-time verification.

---

## 🛠️ Tech Stack & Model
- **Language:** Python 3.10+
- **Frontend / UI:** Streamlit 1.67
- **LLM Provider:** Groq Cloud API
- **Model:** `llama-3.3-70b-versatile` (Temperature: 0.1)
- **Environment Management:** `python-dotenv`

---

## ⚙️ Installation & Running

### 1. Clone or Open the Repository
```bash
git clone https://github.com/nishantpatil667700-jpg/college-enquiry-chat-bot.git
cd college_enquiry_chatbot
```

### 2. Set Up Virtual Environment (macOS / Linux)
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Key
Obtain a free Groq API key from [Groq Console](https://console.groq.com/keys).  
Create `.env` from `.env.example`:
```bash
cp .env.example .env
```
Add your key to `.env`:
```ini
GROQ_API_KEY=gsk_your_actual_key_here
```
*(Alternatively, you can leave `.env` empty and enter your key directly in the sidebar password box).*

### 5. Run the Application
```bash
streamlit run app.py
```
The app will open automatically at `http://localhost:8501`.

---

## 🧪 Sample Evaluation Test Cases

| # | Test Query | Expected Response Behavior |
|---|---|---|
| 1 | *What undergraduate courses are offered?* | Lists B.Tech in CSE (180), AI&DS (120), E&TC (120), IT (60), ME (60). |
| 2 | *What is the fee structure for B.Tech CSE?* | Breaks down Tuition (₹1,20,000), Dev (₹25,000), Total (₹1,45,000/yr). |
| 3 | *What is the admission procedure and eligibility?* | 10+2 with PCM (min 50%), MHT-CET/JEE Main, 80% CAP / 20% Institute seats. |
| 4 | *What hostel and sports facilities are available?* | Boys (500) & Girls (400) hostel (₹85k/yr), sports grounds, courts & gym. |
| 5 | *Do you offer MBBS or Aviation degrees?* | **Refusal:** "Sorry, this information is not available in the college information provided..." |
| 6 | *What is the capital of France?* | **Domain Boundary:** "I can only assist with college-related enquiries..." |

---

## 📁 Submission Folder Layout

```
Your individual folder/
├── Report.pdf         (2-page procedure report)
├── Code.zip           (full project code, without API keys)
├── github_link.txt    (your GitHub repository URL)
├── screenshots/       (3–5 output screenshots)
└── demo_video.mp4     (optional, 1–2 minutes)
```

To create `Code.zip` cleanly:
```bash
python package_submission.py
```

---

## 🔒 Security
- `.env` and virtual environment folders are listed in `.gitignore` to prevent any credentials from being committed to GitHub.
