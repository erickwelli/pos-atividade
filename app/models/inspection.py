from app.extensions import db

class Inspection(db.Model):
    __tablename__ = "inspections"

    id = db.Column(db.Integer, primary_key=True)

    parking_id = db.Column(
        db.Integer,
        db.ForeignKey("parkings.id"),
        nullable=False
    )

    professional_id = db.Column(
        db.Integer,
        db.ForeignKey("professionals.id"),
        nullable=False
    )

    data = db.Column(db.DateTime, nullable=False)

    parking = db.relationship(
        "Parking",
        back_populates="inspections"
    )

    professional = db.relationship(
        "Professional",
        back_populates="inspections"
    )