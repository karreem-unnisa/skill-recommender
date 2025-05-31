# backend/recommender.py
import pandas as pd
import json
from pathlib import Path

DATASET_PATH = Path("backend/dataset/custom.xlsx")
SYNONYM_PATH = Path("backend/dataset/synonyms.json")

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
        business_skills = [normalize_skill(s.strip()) for s in row["Skills"].split(",")]
        if any(skill in business_skills for skill in normalized):
            matches.append({
                "business": row["Business Idea"],
                "matched_skills": list(set(business_skills) & set(normalized)),
                "location": row.get("Location", "N/A")
            })
    return matches
