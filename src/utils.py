# src/utils.py

import pandas as pd


def load_courses(csv_path: str = "data/courses.csv") -> pd.DataFrame:
    """
    Load the courses catalog from CSV.
    """
    return pd.read_csv(csv_path)


def filter_courses(df: pd.DataFrame, domain: str, level: str) -> pd.DataFrame:
    """
    Filter courses by domain and level, if provided.
    """
    if domain:
        df = df[df["domain"].str.lower() == domain.lower()]

    if level:
        df = df[df["level"].str.lower() == level.lower()]

    return df


def df_to_course_dicts(df: pd.DataFrame):
    """
    Convert a DataFrame of courses into a list of dicts.
    """
    return df.to_dict(orient="records")