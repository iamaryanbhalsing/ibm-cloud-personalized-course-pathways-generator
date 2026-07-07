# src/storage.py

# Very simple in-memory storage for now.
# In a real app, replace this with SQLite or IBM Cloud database.

_saved_plans = {}


def save_plan(user_name, plan):
    _saved_plans[user_name] = plan


def get_plan(user_name):
    return _saved_plans.get(user_name)