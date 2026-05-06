from flask import Blueprint, request, jsonify
from app.controllers.inspection_controller import (
    criar_inspection
)

inspections_bp = Blueprint("inspections", __name__)

@inspections_bp.route("/", methods=["POST"])
def post_inspection():
    data = request.get_json()
    response, status = criar_inspection(data)
    return jsonify(response), status