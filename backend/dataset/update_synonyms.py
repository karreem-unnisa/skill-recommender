# backend/scripts/update_synonyms.py

import json
import os
from pathlib import Path
from pymongo import MongoClient
from dotenv import load_dotenv
from collections import defaultdict

# Load environment variables
load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]
history_collection = db["recommendation_history"]

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
SYNONYM_FILE = BASE_DIR / "dataset" / "synonyms.json"

# Load existing synonyms
with open(SYNONYM_FILE, "r") as f:
    synonyms = json.load(f)

existing_synonyms_flat = set()
for key, values in synonyms.items():
    existing_synonyms_flat.add(key.lower())
    existing_synonyms_flat.update([v.lower() for v in values])

# Track new unmatched skills
new_skills = defaultdict(set)

# Fetch all user history
all_histories = history_collection.find()

for history in all_histories:
    for skill in history.get("input_skills", []):
        skill = skill.strip().lower()
        if skill not in existing_synonyms_flat:
            new_skills["misc"].add(skill)

# Update and write if there are new entries
if new_skills:
    for key, values in new_skills.items():
        if key in synonyms:
            synonyms[key].extend(v for v in values if v not in synonyms[key])
        else:
            synonyms[key] = list(values)

    # Remove duplicates
    for key in synonyms:
        synonyms[key] = sorted(list(set(synonyms[key])))

    # Save back to file
    with open(SYNONYM_FILE, "w") as f:
        json.dump(synonyms, f, indent=2)
    
    print("✅ Synonyms updated with new skills:")
    for k, v in new_skills.items():
        print(f"- {k}: {', '.join(v)}")
else:
    print("✅ No new unmatched skills found. Synonyms are up to date.")
