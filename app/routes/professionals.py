from flask import Blueprint, request, jsonify
from app.controllers.professional_controller import (
    listar_profissionais,
    criar_profissional
)

from app.controllers.inspection_controller import listar_inspections_por_professional

professionals_bp = Blueprint("professionals", __name__)

@professionals_bp.route("/", methods=["GET"])
def get_professionals():
    response, status = listar_profissionais()
    return jsonify(response), status

@professionals_bp.route("/", methods=["POST"])
def post_professional():
    data = request.get_json()
    response, status = criar_profissional(data)
    return jsonify(response), status

@professionals_bp.route("/<int:professional_id>/inspections", methods=["GET"])
def get_professional_inspections(professional_id):
    response, status = listar_inspections_por_professional(professional_id)
    return jsonify(response), status