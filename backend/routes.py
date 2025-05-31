# backend/routes.py
from flask import Blueprint, request, jsonify
from recommender import get_recommendations

skill_routes = Blueprint('skill_routes', __name__)

@skill_routes.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    skills = data.get("skills", [])
    recommendations = get_recommendations(skills)
    return jsonify({"recommendations": recommendations})
