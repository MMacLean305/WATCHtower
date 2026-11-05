from database import db
from datetime import datetime, timezone
class Risk(db.Model):
    __tablename__ = "risks"
    id = db.Column(db.Integer, primary_key=True)
    state_id = db.Column(db.Integer,db.ForeignKey("states.id"),unique=True,nullable=False)

    # Individual risk factors (0-100)
    political_risk = db.Column(db.Float)
    economic_risk = db.Column(db.Float)
    conflict_risk = db.Column(db.Float)
    crime_risk = db.Column(db.Float)
    terrorism_risk = db.Column(db.Float)
    civil_unrest_risk = db.Column(db.Float)

    # Aggregated assessment
    overall_risk = db.Column(db.Float)
    model_version = db.Column(db.String(50))
    last_updated = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc),nullable=False)
    state = db.relationship("State",back_populates="risk")
