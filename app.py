import streamlit as st
import streamlit.components.v1 as components

# --- 1. CONFIGURATION AND INITIAL SETUP ---
st.set_page_config(
    layout="wide",
    page_title="Lisa Silva: AI and Data Science Portfolio",
    initial_sidebar_state="expanded"
)

# --- 2. CONTENT DEFINITION: External Project URLs ---
# Note: Since the core apps (CSV, Web Scraper, Quiz) are separate Streamlit deployments,
# we use Markdown to create clickable links that open in a new tab for now.
# This ensures the user can access them while keeping the master portfolio clean.

# Replace these URLs with the correct, active links for your deployed projects
PROJECT_URLS = {
1.  "CSV Data Analyzer": "https://csv-data-analyzer-lisa-silva.streamlit.app/",
2.  "Web Scraper": "https://web-scraper-lisa-silva.streamlit.app/",
3.  "Sentiment Analyzer": "https://online-review-sentiment-analyzer-lisa-silva.streamlit.app/",
4.  "Dark Triad Quiz": "https://dark-triad-detector-quiz-lisa-silva-v2.streamlit.app/",
5.  "Finance Tracker (Integration)": "https://finance-tracker-app-lisa-silva.streamlit.app/",
6.  "LeaseSync AI (Integration)": "https://lease-sync-ai-lisa-silva.streamlit.app/",

}


# --- 3. PAGE FUNCTIONS ---

def welcome_page():
    """The main dashboard/landing page."""
    st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;"><h1 style="color: #FF4B4B; font-size: 3em;">⭐ Capstone Portfolio Dashboard</h1></div>', unsafe_allow_html=True)

    st.subheader("Lisa Silva: Data Science & Application Development")
 
    st.markdown("""
    Welcome to my unified portfolio dashboard! This single application demonstrates a comprehensive range of skills including **data processing (Pandas), web scraping, natural language
    processing (TextBlob), financial tracking, and AI integration.**
 
    Use the **sidebar menu** on the left to navigate between the six live applications.
    """)
 
    st.info("Status: All six core projects are linked below. Click any project in the sidebar to view a summary and access the live application in a new tab.")

    st.markdown("## Live Project Summary")
 
    cols = st.columns(3)
 
    projects = list(PROJECT_URLS.keys())
 
    # Dynamically display project links on the main page
    for i, project_name in enumerate(projects):
        col = cols[i % 3]
        with col:
            st.markdown(f"""
            <div style="border: 1px solid #ddd; padding: 10px; margin-bottom: 10px; border-radius: 8px; background-color: #fff; box-shadow: 2px 2px 5px rgba(0,0,0,0.05);">
                <h3 style="font-size: 1.25em; color: #333;">{project_name}</h3>
                <p>Click <a href="{PROJECT\\\_URLS\\\[project\\\_name]}" target="\\\_blank" style="color: #FF4B4B; font-weight: bold;">here</a> to launch the app.</p>
            </div>
            """, unsafe_allow_html=True)

def project_page_template(project_name):
    """Template for individual project pages."""
    url = PROJECT_URLS.get(project_name, "#")
    st.header(f"Project Focus: {project_name}")
    st.markdown("---")
 
    # Create the clickable link button that opens in a new tab
    st.markdown(f"""
    <a href="{url}" target="\\\_blank">
        <button style="
            background-color: #FF4B4B;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            font-size: 1.1em;
            cursor: pointer;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            transition: background-color 0.3s;
        ">
        Launch Live Application
        </button>
    </a>
    """, unsafe_allow_html=True)
 
    st.markdown("---")

    # Placeholder for the description of the app
    if project_name == "CSV Data Analyzer":
        st.subheader("Goal:")
        st.write("Demonstrate core data manipulation and visualization skills using Python (Pandas) and Streamlit. This app allows users to upload, clean, and visualize data immediately.")
        st.subheader("Key Skills Demonstrated:")
        st.markdown("- Data ingestion and validation (CSV file upload)")
        st.markdown("- Data cleaning (handling missing values)")
        st.markdown("- Dynamic plotting (Matplotlib/Plotly integration)")

    elif project_name == "Web Scraper":
        st.subheader("Goal:")
        st.write("Showcase proficiency in web scraping techniques for extracting structured data from the web. This is essential for building custom datasets for analysis.")
        st.subheader("Key Skills Demonstrated:")
        st.markdown("- HTTP request handling")
        st.markdown("- HTML parsing and element selection")
        st.markdown("- Data structuring into tabular format")

    elif project_name == "Sentiment Analyzer":
        st.subheader("Goal:")
        st.write("Display expertise in Natural Language Processing (NLP) by analyzing text input (simulated reviews) to determine sentiment and objectivity.")
        st.subheader("Key Skills Demonstrated:")
        st.markdown("- Text preprocessing and tokenization")
        st.markdown("- Using NLP libraries (TextBlob) for analysis")
        st.markdown("- UI design for visualizing NLP results")

    elif project_name == "Dark Triad Quiz":
        st.subheader("Goal:")
        st.write("Create a complex, multi-stage application that manages state and aggregates user input to provide a calculated result (score).")
        st.subheader("Key Skills Demonstrated:")
        st.markdown("- State management using `st.session\\\_state`")
        st.markdown("- Complex scoring logic based on psychological scales")
        st.markdown("- User-friendly, progressive form design")
 
    elif project_name == "Finance Tracker (Integration)":
        st.subheader("Goal:")
        st.write("Showcase the integration of external data (or API mock data) for practical, real-world applications like personal finance tracking.")
        st.subheader("Key Skills Demonstrated:")
        st.markdown("- Data persistence/database conceptualization (e.g., Firestore integration proof)")
        st.markdown("- Financial calculation and reporting")
        st.markdown("- Secure handling of sensitive data inputs")
 
    elif project_name == "LeaseSync AI (Integration)":
        st.subheader("Goal:")
        st.write("Demonstrate the ability to connect a front-end application to a conceptual AI backend (LLM) to perform complex, domain-specific tasks (e.g., contract analysis).")
        st.subheader("Key Skills Demonstrated:")
        st.markdown("- API request handling (mock or real)")
        st.markdown("- Structured output generation from LLMs")
        st.markdown("- Presenting complex, structured legal/financial data clearly")


# --- 4. MAIN APPLICATION LOGIC ---

# Dynamically create the page mapping for the sidebar
PAGES = {
    "⭐ Welcome & Overview": welcome_page,
    "CSV Data Analyzer": lambda: project_page_template("CSV Data Analyzer"),
    "Web Scraper": lambda: project_page_template("Web Scraper"),
    "Sentiment Analyzer": lambda: project_page_template("Sentiment Analyzer"),
    "Dark Triad Quiz": lambda: project_page_template("Dark Triad Quiz"),
    "Finance Tracker (Integration)": lambda: project_page_template("Finance Tracker (Integration)"),
    "LeaseSync AI (Integration)": lambda: project_page_template("LeaseSync AI (Integration)"),
}

# --- Sidebar Navigation ---
st.sidebar.title("Portfolio Projects")
selection = st.sidebar.radio("Go to:", list(PAGES.keys()))

# Call the function associated with the selected page
page = PAGES[selection]
page()
