from flask import Blueprint, request, jsonify

from app.controllers.parkingspot_controller import (
    criar_spot,
    listar_spots,
    atualizar_spot
)

spots_bp = Blueprint("spots", __name__)

@spots_bp.route("/", methods=["POST"])
def post_spot():
    data = request.get_json()
    response, status = criar_spot(data)
    return jsonify(response), status

@spots_bp.route("/", methods=["GET"])
def get_spots():
    response, status = listar_spots()
    return jsonify(response), status

@spots_bp.route("/<int:id>", methods=["PATCH"])
def patch_spot(id):
    data = request.get_json()
    response, status = atualizar_spot(id, data)
    return jsonify(response), status