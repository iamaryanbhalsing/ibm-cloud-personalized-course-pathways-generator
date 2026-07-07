# src/recommender.py

import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
COURSES_PATH = DATA_DIR / "courses.csv"


def load_courses():
    df = pd.read_csv(COURSES_PATH)
    return df


def recommend_courses(domain, level, max_courses=3):
    df = load_courses()

    if domain:
        df = df[df["domain"].str.lower() == domain.lower()]

    if level:
        # Try to match level; if nothing found, ignore level filter
        filtered = df[df["level"].str.lower() == level.lower()]
        if not filtered.empty:
            df = filtered

    # If still empty, just use all courses as fallback
    if df.empty:
        df = load_courses()

    # Take top N courses
    df = df.head(max_courses)

    # Convert rows to simple dicts
    courses = []
    for _, row in df.iterrows():
        courses.append(
            {
                "course_name": row["course_name"],
                "domain": row["domain"],
                "level": row["level"],
                "duration_weeks": int(row["duration_weeks"]),
                "skills": row["skills"],
                "provider": row["provider"],
                "link": row["link"],
            }
        )
    return courses