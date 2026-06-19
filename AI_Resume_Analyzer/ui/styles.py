import streamlit as st

def load_css():

    st.markdown("""
    <style>

    /* =========================
       APP BACKGROUND
    ========================= */

    .stApp {
        background: linear-gradient(
            135deg,
            #0B1120,
            #111827
        );
    }

    /* =========================
       TEXT STYLING
    ========================= */

    .stMarkdown p,
    .stMarkdown li {
        color: #E2E8F0 !important;
        font-weight: 500;
        line-height: 1.7;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #F8FAFC !important;
        font-weight: 700 !important;
        text-shadow: 0px 0px 10px rgba(56,189,248,0.15);
    }

    /* =========================
       HERO SECTION
    ========================= */

    .hero-title {
        text-align: center;
        font-size: 48px;
        font-weight: 800;
        color: #F8FAFC;
        text-shadow: 0px 0px 15px rgba(56,189,248,0.4);
    }

    .hero-subtitle {
        text-align: center;
        color: #CBD5E1;
        font-size: 18px;
        font-weight: 500;
        line-height: 1.6;
    }

    /* =========================
       SIDEBAR
    ========================= */

    section[data-testid="stSidebar"] {
        background-color: #F8FAFC;
    }

    section[data-testid="stSidebar"] * {
        color: #111827 !important;
    }

    /* =========================
       METRIC CARDS
    ========================= */

    div[data-testid="metric-container"] {
        background: #1E293B;
        border-radius: 15px;
        padding: 15px;
        border: 1px solid #334155;
        box-shadow: 0 0 20px rgba(56,189,248,0.08);
    }

    /* =========================
       METRIC VALUE
    ========================= */

    div[data-testid="stMetricValue"] {
        color: #38BDF8 !important;
        font-weight: 800 !important;
        font-size: 32px !important;
    }

    /* =========================
       LABELS
    ========================= */

    label {
        color: #F8FAFC !important;
        font-weight: 700 !important;
    }

    /* =========================
       SELECTBOX
    ========================= */

    div[data-baseweb="select"] > div {
        background-color: white !important;
        color: black !important;
        border-radius: 10px;
    }

    div[data-baseweb="select"] span {
        color: black !important;
    }

    div[role="listbox"] {
        background-color: white !important;
    }

    div[role="option"] {
        color: black !important;
        background-color: white !important;
    }

    div[role="option"]:hover {
        background-color: #E2E8F0 !important;
    }

    /* =========================
       FILE UPLOADER
    ========================= */

    [data-testid="stFileUploaderDropzone"] {
        background-color: white !important;
        border-radius: 15px;
        border: 2px dashed #94A3B8 !important;
        padding: 20px;
    }

    /* Upload Resume Label */
    [data-testid="stFileUploader"] label {
        color: #F8FAFC !important;
        font-weight: 700 !important;
    }

    /* Drag & Drop Text */
    [data-testid="stFileUploaderDropzone"] * {
        color: black !important;
        font-weight: 600 !important;
    }

    /* Browse Files Button */
    [data-testid="stFileUploader"] button {
        background-color: white !important;
        color: black !important;
        font-weight: 700 !important;
        border: 1px solid #94A3B8 !important;
        border-radius: 10px;
    }

    [data-testid="stFileUploader"] button:hover {
        background-color: #E2E8F0 !important;
    }
                /* =========================
   BUTTON HOVER EFFECT
========================= */

.stButton button:hover {
    transform: translateY(-3px);
    transition: 0.3s;
    box-shadow: 0 0 20px rgba(56,189,248,0.4);
}
                

    /* Uploaded Filename */
    [data-testid="stFileUploaderFileName"] {
        color: white !important;
        font-weight: 600 !important;
    }

    /* Uploaded File Size */
    [data-testid="stFileUploaderFileSize"] {
        color: #38BDF8 !important;
    }

    /* File Icon */
    [data-testid="stFileUploaderFile"] svg {
        fill: White !important;
        color: black !important;
    }

    /* Remove (X) Button */
    [data-testid="stFileUploaderFile"] button {
        background: white !important;
        color: black !important;
        border-radius: 10px !important;
    }

    [data-testid="stFileUploaderFile"] button svg {
        fill: black !important;
        color: black !important;
    }

    /* =========================
       EXPANDER
    ========================= */

    .streamlit-expanderContent {
        color: #E2E8F0 !important;
        font-weight: 500;
    }

    /* =========================
       ALERTS
    ========================= */

    .stSuccess,
    .stWarning,
    .stError {
        font-weight: 600;
    }

    /* =========================
       SPACING
    ========================= */

    .section-gap {
        margin-top: 20px;
        margin-bottom: 20px;
    }
                /* File size text */
                [data-testid="stFileUploaderFile"] small {
                color: #38BDF8 !important;
                opacity: 1 !important;
                }
                /* Spinner text */
                [data-testid="stSpinner"] p {
                color: #38BDF8 !important;
                font-weight: 600 !important;
                }
               
                /* Expander title */
                .streamlit-expanderHeader {
                color: #E2E8F0 !important;
                font-weight: 600 !important;
                }
/* =========================
   CAREER ROADMAP CHECKBOXES
========================= */

div[data-testid="stCheckbox"] label,
div[data-testid="stCheckbox"] p,
div[data-testid="stCheckbox"] span {
    color: #E2E8F0 !important;
    opacity: 1 !important;
    font-weight: 500 !important;
}

/* Force checkbox styling */
div[data-testid="stCheckbox"] input[type="checkbox"] {
    accent-color: #38BDF8 !important; /* cyan accent */
    width: 20px !important;
    height: 20px !important;
    cursor: pointer !important;
}

/* Hover glow */
div[data-testid="stCheckbox"] input[type="checkbox"]:hover {
    box-shadow: 0 0 8px rgba(56,189,248,0.8) !important;
}

/* Checked state */
div[data-testid="stCheckbox"] input[type="checkbox"]:checked {
    accent-color: #38BDF8 !important;
    background-color: #38BDF8 !important;
    border-color: #38BDF8 !important;
}
                

/* =========================
   RESUME PREVIEW
========================= */

[data-testid="stTextArea"] textarea {
    background-color: #1E293B !important;
    color: #E2E8F0 !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
}

/* Keep dark when clicked */
[data-testid="stTextArea"] textarea:focus {
    background-color: #1E293B !important;
    color: #E2E8F0 !important;
    border: 1px solid #38BDF8 !important;
    box-shadow: 0 0 10px rgba(56,189,248,0.4) !important;
}
                
/* =========================
   EXPANDER HEADER
========================= */

details {
    background-color: #1E293B !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
}

details summary {
    background-color: #334155 !important;
    color: #F8FAFC !important;
    font-weight: 600 !important;
}

/* Prevent white hover effect */
details summary:hover {
    background-color: #334155 !important;
    color: #F8FAFC !important;
}

/* Prevent white focus effect */
details summary:focus,
details summary:active {
    background-color: #334155 !important;
    color: #F8FAFC !important;
    outline: none !important;
}
/* =========================
   INPUT BAR FIX
========================= */

/* Target text inputs */
input[type="text"],
input[type="search"],
textarea {
    background-color: #1E293B !important;  /* dark background */
    color: #E2E8F0 !important;             /* light text */
    border: 1px solid #334155 !important;  /* subtle border */
    border-radius: 8px !important;
}

/* Focus state (when clicked/active) */
input[type="text"]:focus,
input[type="search"]:focus,{
    background-color: #0B1120 !important;  /* keep dark */
    color: #F8FAFC !important;
    border: 1px solid #38BDF8 !important;  /* cyan border highlight */
    box-shadow: 0 0 10px rgba(56,189,248,0.4) !important;
}
/* =========================
   ANIMATED PROGRESS BAR
========================= */

.stProgress > div > div > div {
    background: linear-gradient(
        90deg,
        #38BDF8,
        #60A5FA,
        #38BDF8
    ) !important;

    background-size: 200% 100%;
    animation: progressGlow 3s linear infinite;
}

@keyframes progressGlow {
    0% {
        background-position: 0% 50%;
    }
    100% {
        background-position: 200% 50%;
    }
}

/* =========================
   FLOATING HERO TITLE
========================= */

@keyframes floatTitle {
    0% {
        transform: translateY(0px);
    }
    50% {
        transform: translateY(-8px);
    }
    100% {
        transform: translateY(0px);
    }
}

.hero-title {
    animation: floatTitle 4s ease-in-out infinite;
}

/* =========================
   GLOWING METRIC CARDS
========================= */

@keyframes glowPulse {
    0% {
        box-shadow:
            0 0 10px rgba(56,189,248,0.10),
            0 0 20px rgba(56,189,248,0.05);
    }

    100% {
        box-shadow:
            0 0 20px rgba(56,189,248,0.35),
            0 0 40px rgba(56,189,248,0.15);
    }
}

div[data-testid="metric-container"] {
    background: rgba(30,41,59,0.75);
    backdrop-filter: blur(12px);

    border-radius: 15px;
    padding: 15px;
    border: 1px solid #334155;

    box-shadow: 0 0 20px rgba(56,189,248,0.08);
}
                /* =========================
   ANIMATED NEURAL BACKGROUND
========================= */

.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    inset: 0;

    background-image:
        radial-gradient(circle,
        rgba(56,189,248,0.15) 2px,
        transparent 2px);

    background-size: 120px 120px;

    animation: neuronMove 30s linear infinite;

    pointer-events: none;
    z-index: -1;
}

@keyframes neuronMove {
    from {
        transform: translateY(0px);
    }
    to {
        transform: translateY(-120px);
    }
}
                /* AI-style divider */
hr {
    border: none !important;
    height: 2px !important;

    background: linear-gradient(
        90deg,
        transparent,
        #38BDF8,
        transparent
    ) !important;

    box-shadow: 0 0 10px rgba(56,189,248,0.5);
}
                /* =========================
   FADE IN PAGE
========================= */

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(15px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.block-container {
    animation: fadeIn 0.8s ease-out;
}
                
                
    </style>
    """, unsafe_allow_html=True)  