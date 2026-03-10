from flask import Blueprint, request, jsonify
from services.driver_service import DriverService

driver_bp = Blueprint("driver", __name__)

service = DriverService()


@driver_bp.route("/drivers", methods=["GET"])
def get_drivers():
    drivers = service.get_drivers()
    return jsonify(drivers)


@driver_bp.route("/drivers", methods=["POST"])
def create_driver():
    data = request.get_json()
    driver = service.create_driver(data)
    return jsonify(driver)


@driver_bp.route("/drivers/<int:driver_id>", methods=["DELETE"])
def delete_driver(driver_id):
    service.remove_driver(driver_id)
    return jsonify({"message": "Driver deleted successfully"})