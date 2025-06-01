from flask import Blueprint, request, jsonify
from recommender import get_recommendations
from learn import get_learning_resources  # Assuming you keep this


skill_routes = Blueprint('skill_routes', __name__)

@skill_routes.route("/recommend", methods=["POST"])
def recommend():
    try:
        data = request.get_json()
        skills = data.get("skills", [])
        feedback = data.get("feedback", None)

        recommendations = get_recommendations(skills)

     

        return jsonify({"recommendations": recommendations})
    except Exception as e:
        print("Error in /recommend route:", e)
        return jsonify({"error": str(e)}), 500


@skill_routes.route("/feedback", methods=["POST"])
def feedback():
    # Since no MongoDB, either remove or implement feedback saving locally
    # Here's a placeholder response for now:
    return jsonify({"message": "Feedback saving not implemented without DB."}), 501


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
