from app.extensions import ma
from app.models.inspection import Inspection
from marshmallow import fields

class InspectionSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Inspection

    id = ma.auto_field(dump_only=True)

    parking_id = ma.auto_field(required=True)
    professional_id = ma.auto_field(required=True)

    data = fields.DateTime(required=True)