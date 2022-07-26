# coding: utf-8
from flask import Flask
from flask_restful import Api, Resource, reqparse
from quotes import ai_quotes
import random

app = Flask(__name__)
api = Api(app)


class Quote(Resource):
    def get(self, id=0):
        if id == 0:
            return random.choice(ai_quotes), 200
        for quote in ai_quotes:
            if (quote["id"] == id):
                return quote, 200
        return "Quote not found", 404


    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        params = parser.parse_args()
        for quote in ai_quotes:
            if (id == quote["id"]):
                return f"Quote with id {id} already exists", 400
        quote = {
            "id": int(id),
            "author": params["author"],
            "quote": params["quote"]
        }
        ai_quotes.append(quote)

        return quote, 201


api.add_resource(Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:id>")
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=1234)
