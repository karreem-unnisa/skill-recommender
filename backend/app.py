from flask import Flask
from flask_cors import CORS
from routes import skill_routes
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Explicitly allow your Vercel frontend domain
CORS(app, resources={r"/api/*": {"origins": "https://skill-based-business-recommendation.vercel.app"}})

app.register_blueprint(skill_routes, url_prefix='/api')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
