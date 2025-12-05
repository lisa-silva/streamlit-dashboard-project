import streamlit as st
import streamlit.components.v1 as components

# --- 1. CONFIGURATION ---
st.set_page_config(
    layout="wide",
    page_title="Lisa Silva: AI and Data Science Portfolio",
    initial_sidebar_state="expanded"
)

# --- 2. PROJECT URLS ---
PROJECT_URLS = {
    "CSV Data Analyzer": "https://csv-data-analyzer-lisa-silva.streamlit.app/",
    "Web Scraper": "https://web-scraper-lisa-silva.streamlit.app/",
    "Sentiment Analyzer": "https://online-review-sentiment-analyzer-lisa-silva.streamlit.app/",
    "Dark Triad Quiz": "https://dark-triad-detector-quiz-lisa-silva-v2.streamlit.app/",
    "Finance Tracker (Integration)": "https://finance-tracker-app-lisa-silva.streamlit.app/",
    "LeaseSync AI (Integration)": "https://lease-sync-ai-lisa-silva.streamlit.app/",
}

# --- 3. PAGE FUNCTIONS ---
def welcome_page():
    st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;"><h1 style="color: #FF4B4B; font-size: 3em;">Capstone Portfolio Dashboard</h1></div>', unsafe_allow_html=True)
    st.subheader("Lisa Silva: Data Science & Application Development")

    st.markdown("""
    Welcome to my unified portfolio dashboard! This single application demonstrates a comprehensive range of skills including **data processing (Pandas), web scraping, natural language processing (TextBlob), financial tracking, and AI integration.**

    Use the **sidebar menu** on the left to navigate between the six live applications.
    """)

    st.info("Status: All six core projects are linked below. Click any project in the sidebar to view a summary and access the live application in a new tab.")
    st.markdown("## Live Project Summary")

    cols = st.columns(3)
    for i, project_name in enumerate(PROJECT_URLS):
        with cols[i % 3]:
            st.markdown(f"""
            <div style="border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 8px; background:#fff; box-shadow: 0 2px 5px rgba(0,0,0,0.1); text-align:center;">
                <h3 style="margin:0; color:#333;">{project_name}</h3>
                <p style="margin:10px 0 0;">
                    <a href="{PROJECT_URLS[project_name]}" target="_blank" style="color:#FF4B4B; font-weight:bold; text-decoration:none;">
                        Launch App →
                    </a>
                </p>
            </div>
            """, unsafe_allow_html=True)

def project_page_template(project_name):
    url = PROJECT_URLS.get(project_name, "#")
    st.header(f"Project: {project_name}")
    st.markdown("---")

    st.markdown(f"""
    <a href="{url}" target="_blank">
        <button style="background:#FF4B4B; color:white; padding:12px 24px; border:none; border-radius:8px; font-size:1.1em; cursor:pointer; box-shadow:0 4px 8px rgba(0,0,0,0.2);">
            Launch Live Application
        </button>
    </a>
    """, unsafe_allow_html=True)

    st.markdown("---")

    descriptions = {
        "CSV Data Analyzer": {
            "Goal": "Demonstrate core data manipulation and visualization skills using Pandas and Streamlit.",
            "Skills": ["CSV upload & validation", "Data cleaning", "Interactive Plotly/Matplotlib charts"]
        },
        "Web Scraper": {
            "Goal": "Extract structured data from websites using requests and BeautifulSoup.",
            "Skills": ["HTTP requests", "HTML parsing", "Data export to CSV"]
        },
        "Sentiment Analyzer": {
            "Goal": "Perform NLP sentiment and subjectivity analysis on user text.",
            "Skills": ["TextBlob NLP", "Real-time results", "Visual sentiment gauge"]
        },
        "Dark Triad Quiz": {
            "Goal": "Multi-page psychological quiz with scoring based on validated scales.",
            "Skills": ["Session state management", "Complex scoring logic", "Progressive forms"]
        },
        "Finance Tracker (Integration)": {
            "Goal": "Personal finance dashboard with mock API / database integration.",
            "Skills": ["Data persistence concept", "Financial calculations", "Secure inputs"]
        },
        "LeaseSync AI (Integration)": {
            "Goal": "AI-powered lease/contract analysis using LLM backend.",
            "Skills": ["API integration", "Structured LLM output", "Legal/financial data display"]
        }
    }

    info = descriptions.get(project_name, {"Goal": "No description available.", "Skills": []})
    st.subheader("Goal")
    st.write(info["Goal"])
    st.subheader("Key Skills Demonstrated")
    for skill in info["Skills"]:
        st.markdown(f"- {skill}")

# --- 4. SIDEBAR & PAGE ROUTING ---
PAGES = {
    "Welcome & Overview": welcome_page,
    "CSV Data Analyzer": lambda: project_page_template("CSV Data Analyzer"),
    "Web Scraper": lambda: project_page_template("Web Scraper"),
    "Sentiment Analyzer": lambda: project_page_template("Sentiment Analyzer"),
    "Dark Triad Quiz": lambda: project_page_template("Dark Triad Quiz"),
    "Finance Tracker (Integration)": lambda: project_page_template("Finance Tracker (Integration)"),
    "LeaseSync AI (Integration)": lambda: project_page_template("LeaseSync AI (Integration)"),
}

st.sidebar.title("Portfolio Projects")
selection = st.sidebar.radio("Navigate →", list(PAGES.keys()))

PAGES[selection]()