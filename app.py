import os
import secrets

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger

from services.faqs import faqs_bp

# Load environment variables from .env file
load_dotenv()

# Initialize flask application
app = Flask(__name__)
app.config["DEBUG"] = os.getenv("DEBUG", False)
app.config["SECRET_KEY"] = secrets.token_hex()

app.config["SWAGGER"] = {"title": "covid19-scraper", "uiversion": 3}

# Init Swagger
template = {
    "swagger": "2.0",
    "info": {
        "title": "Covid-19 Scraper",
        "description": "Covid-19 Scraper API",
        "contact": {
            "responsibleDeveloper": "Antonio Maina",
            "email": "antoniomainakn@gmail.com",
        },
        "version": "1.0.0",
    },
    "host": "localhost:5000",  # overrides localhost:500
    "basePath": "/",  # base bash for blueprint registration
    "schemes": ["http", "https"],
}
swag = Swagger(app, template=template)

# Set up cors
CORS(app)

# Init blueprints
app.register_blueprint(faqs_bp, url_prefix="/faqs")

if __name__ == "__main__":
    app.run()
