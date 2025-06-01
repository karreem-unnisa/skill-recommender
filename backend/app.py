# backend/app.py
import os
from flask import Flask
from flask_cors import CORS
from routes import skill_routes
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

app.register_blueprint(skill_routes)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's port or default 5000
    app.run(host="0.0.0.0", port=port, debug=True)
