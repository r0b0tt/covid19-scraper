from flask import jsonify
from flask_restful import Resource
from flasgger import swag_from

from spiders.who import who_spider


class FaqsResource(Resource):
    """
    Returns a dictionary of all faqs from various spiders.
    """

    @swag_from("../../docs/faqs/all_faqs.yml")
    def get(self):
        who_faqs = who_spider()
        return jsonify(who_faqs)
