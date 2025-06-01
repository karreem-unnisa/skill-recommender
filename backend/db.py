from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]
history_collection = db["recommendation_history"]

def save_user_history(user_id, input_skills, recommended, feedback=None):
    history_collection.insert_one({
        "user_id": user_id,
        "input_skills": input_skills,
        "recommended": recommended,
        "feedback": feedback
    })
