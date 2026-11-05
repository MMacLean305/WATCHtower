from database import db
class Source(db.Model):
    __tablename__ = "sources"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    url = db.Column(db.String(500))
    description = db.Column(db.Text)
    last_updated = db.Column(db.DateTime(timezone=True))
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    events = db.relationship("Event", back_populates="source")
