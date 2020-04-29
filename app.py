from flask import Flask, jsonify
from flask_restful import Api, Resource
from spiders.who import who_spider
from dotenv import load_dotenv
import os
import secrets

# Load environment variables from .env file
load_dotenv()

# Initialize flask application
app = Flask(__name__)
app.config["DEBUG"] = os.getenv("DEBUG", False)
app.config["SECRET_KEY"] = secrets.token_hex()

# Initialize Api
api = Api(app)


class FaqsResource(Resource):
    """
    Returns a dictionary of all faqs from various spiders.
    """

    def get(self):
        who_faqs = who_spider()
        return jsonify(who_faqs)


api.add_resource(FaqsResource, "/faqs")

if __name__ == "__main__":
    app.run()
