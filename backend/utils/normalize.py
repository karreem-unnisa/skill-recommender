import json
import os

# Load the synonym map from a JSON file
def load_synonym_map(path=None):
    if path is None:
        path = os.path.join(os.path.dirname(__file__), 'synonym_map.json')
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{path} not found, proceeding with empty map.")
        return {}


# Normalize a skill: lowercase, strip spaces, and apply synonym map
def normalize_skill(skill, synonym_map=None):
    skill_clean = skill.lower().strip()
    if synonym_map and skill_clean in synonym_map:
        return synonym_map[skill_clean]
    return skill_clean
