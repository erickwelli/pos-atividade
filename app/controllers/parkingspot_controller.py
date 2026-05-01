from app.extensions import db
from app.models.parking import Parking
from app.models.parkingspot import ParkingSpot
from app.schemas.parkingspot_schema import ParkingSpotSchema
from app.utils.response import success_response

spot_schema = ParkingSpotSchema()
spots_schema = ParkingSpotSchema(many=True)


def criar_spot(data):
    dados = spot_schema.load(data)

    Parking.query.get_or_404(dados["parking_id"])

    spot = ParkingSpot(**dados)

    db.session.add(spot)
    db.session.commit()

    return success_response(spot_schema.dump(spot), 201)


def listar_spots():
    spots = ParkingSpot.query.all()
    return success_response(spots_schema.dump(spots))


def atualizar_spot(id, data):
    spot = ParkingSpot.query.get_or_404(id)

    for campo, valor in data.items():
        setattr(spot, campo, valor)

    db.session.commit()

    return success_response(spot_schema.dump(spot))