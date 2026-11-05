from database import db
class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    state_id = db.Column(db.Integer,db.ForeignKey("states.id"),nullable=False)
    source_id = db.Column(db.Integer, db.ForeignKey("sources.id"), nullable=False)

    # Event information
    external_id = db.Column(db.String(100), nullable=False)
    event_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    # Date
    event_date = db.Column(db.Date, nullable=False)

    # Geographic location
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    # Relationships
    state = db.relationship("State", back_populates="events")
    source = db.relationship("Source", back_populates="events")

    # Prevent importing the same provider event twice
    __table_args__ = (db.UniqueConstraint("source_id","external_id",name="uq_source_external_event"),)
