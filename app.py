# app.py

import os

# Limit BLAS threads to avoid OpenBLAS errors on some systems
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["GOTO_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import streamlit as st
from src.roadmap_builder import build_roadmap


# ----- Streamlit page and theme config -----

st.set_page_config(
    page_title="Personalized Course Pathways",
    page_icon="🎓",
    layout="wide",
)

DARK_THEME_CSS = """
<style>
/* Global dark background */
body {
    background-color: #0f172a;
    color: #e5e7eb;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

/* Hide default header/footer */
header, footer {
    visibility: hidden;
}

/* Main container tweaks */
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 1.5rem;
}

/* Title and subtitle */
.main-title {
    font-size: 2.1rem;
    font-weight: 600;
    margin-bottom: 0.25rem;
    color: #e5e7eb;
}

.subtitle {
    font-size: 0.95rem;
    color: #9ca3af;
    margin-bottom: 1.25rem;
}

/* Section headers */
.section-header {
    font-size: 1.1rem;
    font-weight: 500;
    margin-top: 1rem;
    margin-bottom: 0.5rem;
    color: #e5e7eb;
}

/* Course cards */
.course-card {
    border: 1px solid #1f2937;
    border-radius: 10px;
    padding: 0.75rem;
    margin-bottom: 0.75rem;
    background: #111827;
    box-shadow: 0 1px 3px rgba(15, 23, 42, 0.35);
    color: #e5e7eb;
}

/* Links */
.course-card a {
    color: #60a5fa;
    text-decoration: none;
}

/* Roadmap text */
.roadmap-text {
    white-space: pre-wrap;
    font-family: "SF Mono", Menlo, Monaco, Consolas, "Liberation Mono", monospace;
    font-size: 0.95rem;
    line-height: 1.4;
    padding: 0.75rem;
    border-radius: 10px;
    border: 1px solid #1f2937;
    background: #020617;
    box-shadow: 0 1px 3px rgba(15, 23, 42, 0.35);
    color: #e5e7eb;
}

/* Footer credit + social links */
.footer-wrapper {
    margin-top: 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.85rem;
    color: #6b7280;
}

.footer-left {
    text-align: left;
}

.footer-right {
    text-align: right;
}

.footer-links a {
    color: #93c5fd;
    text-decoration: none;
    margin-left: 0.75rem;
}

.footer-links a:hover {
    color: #bfdbfe;
}
</style>
"""

st.markdown(DARK_THEME_CSS, unsafe_allow_html=True)


def main():
    # ---- Top title ----
    st.markdown('<div class="main-title">Personalized Course Pathways</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">AI-powered weekly learning plans with IBM watsonx.ai (Llama 3.3 70B Instruct)</div>',
        unsafe_allow_html=True,
    )

    # ---- Layout: form (left) and results (right) ----
    col_form, col_results = st.columns([1, 2])

    with col_form:
        st.markdown('<div class="section-header">Student profile</div>', unsafe_allow_html=True)

        with st.form("student_form"):
            name = st.text_input("Name")
            goal = st.text_area("Goal (what do you want to achieve?)")
            level = st.selectbox("Current level", ["beginner", "intermediate", "advanced"])
            hours_per_week = st.number_input(
                "Available study time per week (hours)",
                min_value=1,
                max_value=40,
                value=5,
            )
            domain = st.selectbox(
                "Preferred domain",
                ["", "frontend", "backend", "fullstack", "uiux", "cybersecurity", "data", "ai-ml", "devops", "cloud", "mobile"],
            )

            submitted = st.form_submit_button("Generate My Roadmap")

    # ---- Sidebar summary + links (optional) ----
    st.sidebar.title("Pathway summary")

    st.sidebar.markdown("### About")
    st.sidebar.write("Made by Aryan Bhalsing")

    st.sidebar.markdown("### Connect")
    st.sidebar.markdown(
        "- [GitHub](https://github.com/iamaryanbhalsing/iamaryanbhalsing)\n"
        "- [LinkedIn](https://www.linkedin.com/in/iamaryanbhalsing/)\n"
        "- [Instagram](https://www.instagram.com/iam._aryanbhalsing/)",
    )

    if submitted:
        user_profile = {
            "name": name or "Student",
            "goal": goal,
            "level": level,
            "hours_per_week": hours_per_week,
            "domain": domain,
        }

        st.sidebar.write(f"Name: {user_profile['name']}")
        st.sidebar.write(f"Goal: {user_profile['goal'][:60]}..." if user_profile['goal'] else "Goal: not set")
        st.sidebar.write(f"Level: {user_profile['level']}")
        st.sidebar.write(f"Domain: {user_profile['domain'] or 'not set'}")
        st.sidebar.write(f"Hours/week: {user_profile['hours_per_week']}")

        # ---- Build roadmap (courses + AI text) ----
        plan = build_roadmap(user_profile)

        with col_results:
            tabs = st.tabs(["Courses", "AI Roadmap"])

            # Courses tab
            with tabs[0]:
                st.markdown('<div class="section-header">Recommended courses</div>', unsafe_allow_html=True)
                if plan["selected_courses"]:
                    for c in plan["selected_courses"]:
                        st.markdown(
                            f"""
<div class="course-card">
<strong>{c['course_name']}</strong><br>
Domain: {c['domain']} | Level: {c['level']} | Duration: {c['duration_weeks']} weeks<br>
Skills: {c['skills']}<br>
Provider: {c['provider']}<br>
<a href="{c['link']}">Course link</a>
</div>
                            """,
                            unsafe_allow_html=True,
                        )
                else:
                    st.info("No matching courses found in the catalog. Try a different domain or level.")

            # AI Roadmap tab
            roadmap_html = plan["roadmap_text"].replace("\n", "<br>")
            with tabs[1]:
                st.markdown('<div class="section-header">AI-generated roadmap</div>', unsafe_allow_html=True)
                st.markdown(
                    f"<div class='roadmap-text'>{plan['roadmap_text'].replace('\\n', '<br>')}</div>",
                    unsafe_allow_html=True,
                )

    # ---- Footer credit with social links ----
    footer_html = """
<div class="footer-wrapper">
  <div class="footer-left">
    Made by Aryan Bhalsing
  </div>
  <div class="footer-right footer-links">
    <span>Connect:</span>
    <a href="https://github.com/iamaryanbhalsing/iamaryanbhalsing" target="_blank">GitHub</a>
    <a href="https://www.linkedin.com/in/iamaryanbhalsing/" target="_blank">LinkedIn</a>
    <a href="https://www.instagram.com/iam._aryanbhalsing/" target="_blank">Instagram</a>
  </div>
</div>
"""
    st.markdown(footer_html, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
