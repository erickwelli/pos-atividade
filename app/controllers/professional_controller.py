from app.extensions import db
from app.models.professional import Professional
from app.schemas.professional_schema import ProfessionalSchema
from app.utils.response import success_response

professional_schema = ProfessionalSchema()
professionals_schema = ProfessionalSchema(many=True)

def listar_profissionais():
    profs = Professional.query.all()
    return success_response(professionals_schema.dump(profs))


def criar_profissional(data):
    dados = professional_schema.load(data)

    novo = Professional(**dados)

    db.session.add(novo)
    db.session.commit()

    return success_response(professional_schema.dump(novo), 201)