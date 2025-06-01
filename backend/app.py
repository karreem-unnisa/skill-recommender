
# backend/app.py
from flask import Flask
from flask_cors import CORS
from routes import skill_routes
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

app.register_blueprint(skill_routes)

if __name__ == "__main__":
    app.run(debug=True)
