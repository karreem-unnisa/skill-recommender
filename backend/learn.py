import pandas as pd
import random
from pathlib import Path
from utils.normalize import normalize_skill, load_synonym_map

BASE_DIR = Path(__file__).resolve().parent
synonym_map = load_synonym_map(BASE_DIR / "dataset" / "synonyms.json")

learning_df = pd.read_csv(BASE_DIR / "dataset" / "learning_resources.csv")
business_df = pd.read_excel(BASE_DIR / "dataset" / "custom.xlsx")

def get_learning_resources(user_skills, limit=5):
    # Normalize user skills with synonym map
    normalized_skills = [normalize_skill(skill, synonym_map) for skill in user_skills]
    matches = []

    # Find learning resources matching normalized skills
    for _, row in learning_df.iterrows():
        # Normalize skills in resource (comma-separated)
        resource_skills = [normalize_skill(s.strip(), synonym_map) for s in str(row["Skill_Name"]).split(",")]
        if any(skill in resource_skills for skill in normalized_skills):
            matches.append({
                "resource_name": row.get("Resource_Name", "N/A"),
                "platform": row.get("Platform", "N/A"),
                "skill_name": row.get("Skill_Name", "N/A"),
                "resource_type": row.get("Resource_Type", "N/A"),
                "cost": row.get("Cost", "N/A"),
                "skill_level": row.get("Skill_Level", "N/A"),
                "duration": row.get("Duration", "N/A"),
                "earning_potential_after_learning": row.get("Earning_Potential_After_Learning", "N/A")
            })

    # Find bonus business ideas matching normalized skills
    bonus = []
    for _, row in business_df.iterrows():
        # Normalize business skills (comma-separated)
        business_skills = [normalize_skill(s.strip(), synonym_map) for s in str(row.get("Skill", "")).split(",")]
        # Check for any skill overlap
        if any(skill in business_skills for skill in normalized_skills):
            bonus.append({
                "business_idea": row.get("Business Idea", "N/A"),
                "matched_skills": list(
    set(s for s in business_skills if isinstance(s, str)) &
    set(s for s in normalized_skills if isinstance(s, str))
),

                "initial_investment": row.get("Initial Investment (INR)", "N/A"),
                "monthly_income": row.get("Monthly Income (INR)", "N/A")
            })

    random.shuffle(matches)
    random.shuffle(bonus)

    return {
        "recommendations": matches[:limit],
        "bonus_business_ideas": bonus[:3]
    }
