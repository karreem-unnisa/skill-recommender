from pymongo import MongoClient
import os
import json
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# MongoDB setup
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]
history_collection = db["recommendation_history"]

# Path for JSON backup
FEEDBACK_JSON_PATH = Path(__file__).resolve().parent.parent / "dataset" / "user_feedback.json"

def save_user_history(input_skills, recommended, feedback=None):
    data = {
        "input_skills": input_skills,
        "recommended": recommended,
        "feedback": feedback,
        "timestamp": datetime.now().isoformat(),
        "date": datetime.now().date().isoformat()
    }

    # ✅ Save to MongoDB
    inserted = history_collection.insert_one(data)
    
    # Remove MongoDB _id for JSON file
    data.pop("_id", None)

    # ✅ Also save to user_feedback.json
    try:
        if FEEDBACK_JSON_PATH.exists():
            with open(FEEDBACK_JSON_PATH, "r+", encoding="utf-8") as f:
                existing = json.load(f)
                existing.append(data)
                f.seek(0)
                json.dump(existing, f, indent=2)
        else:
            with open(FEEDBACK_JSON_PATH, "w", encoding="utf-8") as f:
                json.dump([data], f, indent=2)
    except Exception as e:
        print(f"Failed to write to JSON: {e}")
