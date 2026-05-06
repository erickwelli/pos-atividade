from app.extensions import db

class Professional(db.Model):
    __tablename__ = "professionals"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    inspections = db.relationship(
        "Inspection",
        back_populates="professional",
        cascade="all, delete-orphan"
    )