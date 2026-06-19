import streamlit as st

from resume_parser import extract_text
from gemini_feedback import get_ai_feedback
from ats_score import calculate_score

from ui.styles import load_css
from ui.dashboard import show_metrics
from ui.components import show_skills

from job_roles import JOB_ROLES


# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🚀",
    layout="wide"
)

# =========================
# LOAD CSS
# =========================
load_css()

# =========================
# HERO SECTION
# =========================
st.markdown("""
<div class='hero-title'>
🚀 AI Resume Analyzer
</div>

<div class='hero-subtitle'>
AI-Powered Resume Intelligence Platform
<br>
ATS Scoring • Skill Gap Analysis • AI Recruiter Insights
</div>
""", unsafe_allow_html=True)

# =========================
# INPUT SECTION
# =========================
st.divider()

col1, col2 = st.columns([1,1])

with col1:
    uploaded_file = st.file_uploader(
        "📄 Upload Resume",
        type=["pdf", "docx", "jpg", "jpeg", "png"]
    )

with col2:
    selected_role = st.selectbox(
        "🎯 Select Target Role",
        ["Select a Job Role"] + list(JOB_ROLES.keys())
    )

# =========================
# ANALYZE BUTTON
# =========================
if uploaded_file is not None:

    if st.button("🚀 Analyze Resume", use_container_width=True):

        if selected_role == "Select a Job Role":
            st.warning("⚠️ Please select a target role.")
            st.stop()

        try:
            # =========================
            # TEXT EXTRACTION
            # =========================
            resume_text = extract_text(uploaded_file)

            if not resume_text.strip():
                st.error("❌ No text could be extracted from the uploaded resume.")
                st.stop()

            # =========================
            # ATS SCORING
            # =========================
            score, matched, missing = calculate_score(
                resume_text,
                selected_role
            )

            # =========================
            # AI FEEDBACK
            # =========================
            with st.spinner("🧠 Generating AI Recruiter Insights..."):
                feedback = get_ai_feedback(
                    resume_text,
                    selected_role
                )

            st.success("✅ Resume Analysis Complete")
            st.divider()

            # =========================
            # METRICS
            # =========================
            show_metrics(score, selected_role, matched)
            st.divider()

            # =========================
            # RESUME STRENGTH INDEX
            # =========================
            st.subheader("📈 Resume Strength Index")
            st.progress(score / 100)

            if score >= 80:
                st.success(f"🚀 Excellent Resume Match ({score}%)")
            elif score >= 60:
                st.warning(f"⚡ Good Resume Match ({score}%)")
            else:
                st.error(f"🔥 Resume Needs Improvement ({score}%)")

            st.divider()

            # =========================
            # SKILL GAP ANALYSIS
            # =========================
            show_skills(matched, missing)
            st.divider()

            # =========================
            # AI INSIGHTS
            # =========================
            with st.expander("🧠 AI Recruiter Insights", expanded=True):
                st.markdown(feedback)
                st.divider()

            # =========================
            # CAREER ROADMAP
            # =========================
            st.subheader("🚀 Career Roadmap")

            if missing:
                for skill in missing:
                    st.checkbox(f"Learn {skill}")
            else:
                st.success("🎉 No major skill gaps detected.")

            st.divider()

            # =========================
            # RESUME PREVIEW
            # =========================
            with st.expander("📄 Extracted Resume Content"):
                st.text_area("", resume_text, height=350)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

else:
    st.info("📄 Upload a resume to begin analysis.") 