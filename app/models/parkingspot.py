from app.extensions import db

class ParkingSpot(db.Model):
    __tablename__ = "parking_spots"

    id = db.Column(db.Integer, primary_key=True)

    codigo = db.Column(db.String(10), nullable=False)
    ocupada = db.Column(db.Boolean, default=False)
    parking_id = db.Column(
        db.Integer,
        db.ForeignKey("parkings.id"),
        nullable=False
    )

    parking = db.relationship("Parking", backref="spots")