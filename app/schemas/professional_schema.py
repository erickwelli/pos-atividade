from app.extensions import ma
from app.models.professional import Professional

class ProfessionalSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Professional

    id = ma.auto_field(dump_only=True)
    nome = ma.auto_field(required=True)