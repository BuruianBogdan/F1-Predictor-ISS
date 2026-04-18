from flask import Blueprint, jsonify
from services.prediction_service import PredictionService

prediction_bp = Blueprint("prediction", __name__)

service = PredictionService()


@prediction_bp.route("/predict/champion", methods=["GET"])
def predict_champion():
    data = service.predict_champion()
    return jsonify(data)


@prediction_bp.route("/predict/race/<int:race_id>", methods=["GET"])
def predict_race(race_id):
    data = service.predict_race(race_id)
    return jsonify(data)