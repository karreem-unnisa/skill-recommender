from pathlib import Path
import pandas as pd
import json
import os

# Base directory for dataset paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_PATH = os.path.join(BASE_DIR, 'dataset', 'custom.xlsx')
SYNONYM_PATH = os.path.join(BASE_DIR, 'dataset', 'synonyms.json')

# Load dataset and synonyms once
try:
    df = pd.read_excel(DATASET_PATH)
    print("Dataset loaded successfully.")
    print("Columns:", df.columns.tolist())
except Exception as e:
    print("Failed to load dataset:", e)
    df = pd.DataFrame()  # fallback empty dataframe

try:
    with open(SYNONYM_PATH, "r") as f:
        synonym_map = json.load(f)
    print("Synonyms loaded successfully.")
except Exception as e:
    print("Failed to load synonyms:", e)
    synonym_map = {}

def normalize_skill(skill):
    skill = skill.lower().strip()
    for key, values in synonym_map.items():
        if skill == key or skill in values:
            return key
    return skill

def get_recommendations(user_skills):
    print("User skills received:", user_skills)
    normalized = [normalize_skill(skill) for skill in user_skills]
    print("Normalized skills:", normalized)
    matches = []

    if df.empty:
        print("Dataset is empty, no matches.")
        return matches

    for _, row in df.iterrows():
        try:
            skill_cell = row["Skill"]
            if not isinstance(skill_cell, str):
                # If skill data is missing or NaN, skip row
                continue
            business_skills = [normalize_skill(s.strip()) for s in skill_cell.split(",")]

            if any(skill in business_skills for skill in normalized):
                print(f"Match found: {row.get('Business Idea', 'N/A')}")

                # Safe access to columns with default "N/A"
                def safe_get(column):
                    return row[column] if column in row and pd.notna(row[column]) else "N/A"

                matches.append({
                    "business_idea": safe_get("Business Idea"),
                    "matched_skills": list(set(business_skills) & set(normalized)),
                    "business_type": safe_get("Business Type"),
                    "tools_needed": safe_get("Tools Needed"),
                    "initial_investment": safe_get("Initial Investment (INR)"),
                    "monthly_income": safe_get("Monthly Income (INR)"),
                    "getting_started_plan": safe_get("Getting Started Plan"),
                    "growth_plan": safe_get("Growth Plan"),
                    "tips": safe_get("Tips"),
                    "learning_resources": safe_get("Learning Resources"),
                })
        except Exception as e:
            print(f"Error processing row: {e}")
            continue

    print(f"Total matches found: {len(matches)}")
    return matches
