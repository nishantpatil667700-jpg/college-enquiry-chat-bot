import os
from pathlib import Path
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from groq import Groq

INFO_FILE = Path(__file__).parent / "college_info.txt"

# Page configuration
st.set_page_config(
    page_title="College Enquiry Chatbot",
    page_icon="🎓",
    layout="wide"
)

def load_college_info():
    if not INFO_FILE.exists():
        return ""
    return INFO_FILE.read_text(encoding="utf-8")

college_info = load_college_info()

# Sidebar Setup
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # API Key Handling (checks .env first, fallback to sidebar input)
    env_api_key = os.getenv("GROQ_API_KEY", "").strip()
    is_placeholder = env_api_key == "gsk_your_actual_groq_api_key" or not env_api_key
    
    if not is_placeholder:
        api_key = env_api_key
        st.success("✅ Groq API key loaded from .env")
    else:
        api_key = st.text_input(
            "Enter Groq API Key:",
            type="password",
            placeholder="gsk_...",
            help="Get your free key from https://console.groq.com/keys"
        )
    
    model_choice = st.selectbox(
        "LLM Model:",
        options=["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "mixtral-8x7b-32768"],
        index=0
    )
    
    temperature = st.slider("Temperature (lower = more factual):", min_value=0.0, max_value=1.0, value=0.1, step=0.05)
    
    st.divider()
    st.subheader("💡 Quick Sample Questions")
    quick_queries = [
        "What undergraduate courses are offered?",
        "What is the fee structure for B.Tech CSE?",
        "What is the admission procedure and eligibility?",
        "What hostel and sports facilities are available?",
        "What was the highest placement package?",
        "What is the capital of France?" # refusal test
    ]
    
    for q in quick_queries:
        if st.button(q, key=f"btn_{q}", use_container_width=True):
            st.session_state.pending_query = q
            
    st.divider()
    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
        
    with st.expander("📄 View Ground Truth (college_info.txt)"):
        st.text_area("Info Sheet", value=college_info, height=250, disabled=True)

# Main UI
st.title("🎓 College Enquiry Chatbot")
st.caption("AI-Powered Admission & Campus Enquiry Assistant — Strictly Grounded in College Knowledge Base")

if not college_info.strip():
    st.error("⚠️ 'college_info.txt' is missing or empty. Please add college information to proceed.")
    st.stop()

if not api_key:
    st.warning("👉 Please enter your Groq API key in the sidebar (or add GROQ_API_KEY to your .env file) to begin.")
    st.info("💡 You can get a free Groq API key in 30 seconds at [console.groq.com](https://console.groq.com).")
    st.stop()

# Grounding System Prompt
SYSTEM_PROMPT = f"""You are a helpful and polite college enquiry assistant for Apex Institute of Engineering & Technology (AIET).
Your job is to answer student and parent questions using ONLY the college information provided below.

STRICT INSTRUCTIONS:
1. Answer using ONLY facts explicitly mentioned in the COLLEGE INFORMATION sheet.
2. Do not use outside knowledge, speculate, or invent facts.
3. If the answer cannot be found in the college information, reply EXACTLY:
   "Sorry, this information is not available in the college information provided. Please contact the college admission office at admissions@aiet.edu.in or call +91 20 2765 4321."
4. If the user asks questions completely unrelated to the college (e.g. general knowledge, recipes, general coding, politics), politely state:
   "I can only assist with college-related enquiries such as courses, fees, admissions, facilities, and placements."
5. Keep your tone polite, professional, and clear. Format lists or fee breakdowns with bullet points for readability.

COLLEGE INFORMATION:
{college_info}
"""

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! 👋 Welcome to the College Enquiry Desk. I can assist you with details regarding our courses, fee structure, admission criteria, campus facilities, and placements. How may I help you today?"
        }
    ]

# Display conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle quick button click query or user typed input
query_to_send = None
if "pending_query" in st.session_state and st.session_state.pending_query:
    query_to_send = st.session_state.pending_query
    st.session_state.pending_query = None

user_input = st.chat_input("Ask a question about courses, admissions, fees...")
if user_input:
    query_to_send = user_input

if query_to_send:
    # Append and render user message
    st.session_state.messages.append({"role": "user", "content": query_to_send})
    with st.chat_message("user"):
        st.markdown(query_to_send)

    # Call LLM
    with st.chat_message("assistant"):
        with st.spinner("Consulting college records..."):
            try:
                client = Groq(api_key=api_key)
                # Filter history for API call
                api_history = [
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ]
                
                response = client.chat.completions.create(
                    model=model_choice,
                    messages=[{"role": "system", "content": SYSTEM_PROMPT}] + api_history,
                    temperature=temperature,
                )
                answer = response.choices[0].message.content or "Sorry, I couldn't generate an answer."
            except Exception as exc:
                answer = f"⚠️ API Error: {exc}\nPlease check your Groq API key and network connection."
        
        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
