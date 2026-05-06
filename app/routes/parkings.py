from flask import Blueprint, request, jsonify

from app.controllers.parking_controller import (
    criar_parking,
    listar_parkings
)
from app.controllers.inspection_controller import listar_inspections_por_parking

from app.controllers.parkingspot_controller import (
    listar_spots_por_parking
)

parkings_bp = Blueprint("parkings", __name__)

@parkings_bp.route("/", methods=["POST"])
def post_parking():
    data = request.get_json()
    response, status = criar_parking(data)
    return jsonify(response), status

@parkings_bp.route("/", methods=["GET"])
def get_parkings():
    response, status = listar_parkings()
    return jsonify(response), status

@parkings_bp.route("/<int:parking_id>/spots", methods=["GET"])
def get_parking_spots(parking_id):
    response, status = listar_spots_por_parking(parking_id)
    return jsonify(response), status

@parkings_bp.route("/<int:parking_id>/inspections", methods=["GET"])
def get_parking_inspections(parking_id):
    response, status = listar_inspections_por_parking(parking_id)
    return jsonify(response), status