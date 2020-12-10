import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from joblib import dump, load

app = Flask(__name__)
api = Api(app)


model = load('model.joblib')


class MakePrediction(Resource):
    @staticmethod
    def post():
        posted_data = request.get_json()
        text = posted_data['text']

        prediction = model.predict([[text]])[0]
       

        return jsonify({
            'Prediction': prediction
        })


api.add_resource(MakePrediction, '/predict')


if __name__ == '__main__':
    app.run(debug=True)