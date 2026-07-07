import streamlit as st
from ibm_watsonx_ai.foundation_models import ModelInference

# Fetch credentials from Streamlit Secrets
BASE_URL = st.secrets.get("WATSONX_BASE_URL")
API_KEY = st.secrets.get("WATSONX_API_KEY")
PROJECT_ID = st.secrets.get("WATSONX_PROJECT_ID")
MODEL_ID = st.secrets.get("WATSONX_MODEL_ID")

print("DEBUG WATSONX CONFIG:")
print("  BASE_URL =", BASE_URL)
print("  API_KEY missing?", API_KEY is None or API_KEY == "")
print("  PROJECT_ID =", PROJECT_ID)
print("  MODEL_ID =", MODEL_ID)


def _get_model():
    """Create a watsonx.ai foundation model client for IBM Cloud (SaaS)."""

    if not BASE_URL or not API_KEY or not PROJECT_ID or not MODEL_ID:
        raise RuntimeError(
            "Watsonx.ai credentials missing in Streamlit Secrets"
        )

    # SaaS credentials: url + apikey
    my_credentials = {
        "url": BASE_URL,
        "apikey": API_KEY,
    }

    # Use simple parameter keys supported by ModelInference
    gen_parms = {
        "decoding_method": "sample",
        "max_new_tokens": 800,
        "temperature": 0.4,
        "top_p": 0.9,
    }

    print("DEBUG: Creating ModelInference client for", MODEL_ID)
    model = ModelInference(
        model_id=MODEL_ID,
        credentials=my_credentials,
        params=gen_parms,
        project_id=PROJECT_ID,
        space_id=None,
        verify=True,
    )
    return model


def generate_roadmap_text(user_profile, selected_courses):
    """Call IBM watsonx.ai foundation model to generate a personalized roadmap."""

    name = user_profile.get("name", "Student")
    goal = user_profile.get("goal", "")
    level = user_profile.get("level", "")
    hours = user_profile.get("hours_per_week", 5)
    domain = user_profile.get("domain", "")

    # Build a compact summary of the selected courses
    course_lines = []
    for c in selected_courses:
        course_lines.append(
            f"- {c['course_name']} | domain={c['domain']} | level={c['level']} | duration={c['duration_weeks']} weeks | skills={c['skills']} | provider={c['provider']}"
        )
    courses_summary = (
        "\n".join(course_lines) if course_lines else "No courses available."
    )

    prompt = f"""
You are an expert career and learning pathway coach for university students.

Given the student's profile and a small catalog of courses, your task is to generate a clear, structured, 6–8 week learning roadmap that helps the student move towards their goal.

Student profile:
- Name: {name}
- Goal: {goal}
- Current skill level: {level}
- Available study time per week: {hours} hours
- Preferred domain: {domain}

Course catalog:
{courses_summary}

Your task:
1. Choose 3–5 courses from the catalog that best match the student's goal, level, and available time.
2. Build a weekly roadmap for 6–8 weeks.
3. For each week, specify:
   - focus topic,
   - recommended course(s),
   - key skills to practice,
   - a small task or mini-project.
4. At the end, add a short motivational message explaining why this path is suitable for the student.

Output format:
Overview:
- Goal: ...
- Domain: ...
- Level: ...

Roadmap:
- Week 1:
  - Focus: ...
  - Course: ...
  - Skills: ...
  - Task: ...
- Week 2:
  - Focus: ...
  - Course: ...
  - Skills: ...
  - Task: ...
(continue up to Week 6–8)

RecommendedCourses:
- Course 1: ...
- Course 2: ...
- Course 3: ...

Motivation:
- Message: ...
"""

    model = _get_model()

    print("DEBUG: Sending prompt to watsonx.ai...")
    try:
        response = model.generate(prompt)
        print("DEBUG: Raw response from watsonx.ai:", response)

        text = ""

        if isinstance(response, dict):
            results = response.get("results", [])
            if results and isinstance(results[0], dict):
                text = results[0].get("generated_text", "")
        else:
            text = str(response)

        if not text:
            text = (
                "Unable to generate roadmap at the moment. Please try again."
            )

    except Exception as e:
        print("ERROR: watsonx.ai generate() failed:", repr(e))
        text = "Unable to generate roadmap due to an AI service error. Please check configuration."

    return text
