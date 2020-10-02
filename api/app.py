#  FLASK_APP=airbnb:APP FLASK_ENV=development flask run
from flask import Flask, request, jsonify
from .predict import add_prediction
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def root():
        return 'airbnb predictive project'

    @app.route('/predict', methods=['POST'])
    def predict():
        try:
            # find authorization header
            listing = request.get_json(force=True)
            # content['predicted_price'] = 99
            content = jsonify(add_prediction(listing))
        except Exception as identifier:
            # content = {}
            content = str(identifier)
        return content

    return app
