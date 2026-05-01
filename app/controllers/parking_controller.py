from app.extensions import db
from app.models.parking import Parking
from app.schemas.parking_schema import ParkingSchema
from app.utils.response import success_response

parking_schema = ParkingSchema()
parkings_schema = ParkingSchema(many=True)

def criar_parking(data):
    dados = parking_schema.load(data)

    parking = Parking(**dados)

    db.session.add(parking)
    db.session.commit()

    return success_response(parking_schema.dump(parking), 201)


def listar_parkings():
    parkings = Parking.query.all()
    return success_response(parkings_schema.dump(parkings))