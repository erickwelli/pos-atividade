from app.extensions import db
from app.models.inspection import Inspection
from app.models.parking import Parking
from app.models.professional import Professional
from app.schemas.inspection_schema import InspectionSchema
from app.utils.response import success_response

inspection_schema = InspectionSchema()
inspections_schema = InspectionSchema(many=True)

def criar_inspection(data):
    dados = inspection_schema.load(data)

    parking = Parking.query.get_or_404(dados["parking_id"])
    professional = Professional.query.get_or_404(dados["professional_id"])

    nova = Inspection(
        parking=parking,
        professional=professional,
        data=dados["data"]
    )

    db.session.add(nova)
    db.session.commit()

    return success_response(inspection_schema.dump(nova), 201)


def listar_inspections_por_parking(parking_id):
    parking = Parking.query.get_or_404(parking_id)
    return success_response(inspections_schema.dump(parking.inspections))


def listar_inspections_por_professional(professional_id):
    prof = Professional.query.get_or_404(professional_id)
    return success_response(inspections_schema.dump(prof.inspections))