from flask import Blueprint
from flask_restful import Api

from services.faqs.views import FaqsResource

# Initialize blueprint and api
faqs_bp = Blueprint("faqs", __name__)
faqs_api = Api(faqs_bp)

# Register api routes
faqs_api.add_resource(FaqsResource, "/")
