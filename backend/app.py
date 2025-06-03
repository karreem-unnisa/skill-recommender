# backend/app.py
from flask import Flask
from flask_cors import CORS
from routes import skill_routes
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

app.register_blueprint(skill_routes, url_prefix='/api')


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

