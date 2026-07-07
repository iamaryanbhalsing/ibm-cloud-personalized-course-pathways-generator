# src/roadmap_builder.py

from src.model_client import generate_roadmap_text
from src.utils import load_courses, filter_courses, df_to_course_dicts


def build_roadmap(user_profile):
    """
    Select relevant courses and ask watsonx.ai to generate a roadmap.
    """

    domain = user_profile.get("domain", "")
    level = user_profile.get("level", "")

    # Load and filter courses
    df = load_courses()
    df_filtered = filter_courses(df, domain, level)

    # Pick up to 5 courses to feed into the model
    df_selected = df_filtered.head(5)
    selected_courses = df_to_course_dicts(df_selected)

    # Call watsonx.ai to generate roadmap text
    roadmap_text = generate_roadmap_text(user_profile, selected_courses)

    return {
        "selected_courses": selected_courses,
        "roadmap_text": roadmap_text,
    }