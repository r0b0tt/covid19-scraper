from flask import Flask, jsonify
from flask_restful import Api, Resource
from spiders.who import who_spider

app = Flask(__name__)
api = Api(app)


class FaqsResource(Resource):
    def get(self):
        who_faqs = who_spider()
        return jsonify(who_faqs)


api.add_resource(FaqsResource, "/faqs")

if __name__ == "__main__":
    app.run()
