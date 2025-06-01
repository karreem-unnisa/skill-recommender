from flask import Blueprint, request, jsonify
from recommender import get_recommendations
from learn import get_learning_resources  # ✅ Add this import!
from utils.history_saver import save_user_history
from datetime import datetime, timezone

skill_routes = Blueprint('skill_routes', __name__)

@skill_routes.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    skills = data.get("skills", [])
    feedback = data.get("feedback", None)

    recommendations = get_recommendations(skills)

    save_user_history(skills, [rec["business_idea"] for rec in recommendations], feedback)

    return jsonify({"recommendations": recommendations})

@skill_routes.route("/feedback", methods=["POST"])
def feedback():
    data = request.get_json()
    feedback_value = data["feedback"]

    from db import history_collection
    latest = history_collection.find_one(sort=[("timestamp", -1)])
    if latest:
        history_collection.update_one(
            {"_id": latest["_id"]},
            {"$set": {"feedback": feedback_value}}
        )

    return jsonify({"message": "Feedback saved!"})

@skill_routes.route('/learn', methods=['POST'])
def learn_route():
    try:
        data = request.get_json()
        skills = data.get('skills', [])
        limit = int(data.get('limit', 3))

        print("Received skills for /learn:", skills)
        print("Limit requested:", limit)

        response = get_learning_resources(skills, limit)
        return jsonify(response)
    except Exception as e:
        print("Error in /learn route:", e)
        return jsonify({"error": str(e)}), 500

