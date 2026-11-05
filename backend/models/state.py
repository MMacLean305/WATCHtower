from database import db
class State(db.Model):
    __tablename__ = "states"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique = True, nullable=False)
    official_name = db.Column(db.String(200))
    iso_code = db.Column(db.String(3), unique=True, nullable=False)
    region = db.Column(db.String(50), nullable=False)
    subregion = db.Column(db.String(100))

