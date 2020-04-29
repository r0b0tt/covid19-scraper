import os
import secrets

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS

from services.faqs import faqs_bp

# Load environment variables from .env file
load_dotenv()

# Initialize flask application
app = Flask(__name__)
app.config["DEBUG"] = os.getenv("DEBUG", False)
app.config["SECRET_KEY"] = secrets.token_hex()

# Set up cors
CORS(app)

# Init blueprints
app.register_blueprint(faqs_bp, url_prefix="/faqs")

if __name__ == "__main__":
    app.run()
