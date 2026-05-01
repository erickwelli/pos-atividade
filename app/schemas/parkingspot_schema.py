from app.extensions import ma
from app.models.parkingspot import ParkingSpot
from marshmallow import fields

class ParkingSpotSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ParkingSpot

    id = ma.auto_field(dump_only=True)
    codigo = ma.auto_field(required=True)
    ocupada = ma.auto_field()
    parking_id = ma.auto_field(required=True)
    parking = fields.Nested(
        "ParkingSchema",
        only=("id", "nome")
    )