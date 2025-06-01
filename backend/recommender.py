from pathlib import Path
import pandas as pd
import json
import os
import random
# Get absolute path to this file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_PATH = os.path.join(BASE_DIR, 'dataset', 'custom.xlsx')
SYNONYM_PATH = os.path.join(BASE_DIR, 'dataset', 'synonyms.json')

# Load dataset
df = pd.read_excel(DATASET_PATH)

# Load synonyms
with open(SYNONYM_PATH, "r") as f:
    synonym_map = json.load(f)


def normalize_skill(skill):
    skill = skill.lower().strip()
    for key, values in synonym_map.items():
        if skill in values or skill == key:
            return key
    return skill

def get_recommendations(user_skills):
    normalized = [normalize_skill(skill) for skill in user_skills]
    matches = []

    for _, row in df.iterrows():
        business_skills = [normalize_skill(s.strip()) for s in row["Skill"].split(",")]
        if any(skill in business_skills for skill in normalized):
            matches.append({
                "business_idea": row["Business Idea"],
                "matched_skills": list(set(business_skills) & set(normalized)),
                "business_type": row.get("Business Type", "N/A"),
                "tools_needed": row.get("Tools Needed", "N/A"),
                "initial_investment": row.get("Initial Investment (INR)", "N/A"),
                "monthly_income": row.get("Monthly Income (INR)", "N/A"),
                "getting_started_plan": row.get("Getting Started Plan", "N/A"),
                "growth_plan": row.get("Growth Plan", "N/A"),
                "tips": row.get("Tips", "N/A"),
                "learning_resources": row.get("Learning Resources", "N/A")
            })

    return matches