from database import db
from datetime import datetime, timezone
class Risk(db.Model):
    __tablename__ = "risks"
    id = db.Column(db.Integer, primary_key=True)
    state_id = db.Column(db.Integer, db.ForeignKey("states.id"), unique=True, nullable=False)
    risk_score = db.Column(db.Float, nullable=False)
    anomaly_score = db.Column(db.Float)
    model_version = db.Column(db.String(50))
    last_updated = db.Column(db.DateTime(timezone=True),default=lambda: datetime.now(timezone.utc),onupdate=lambda: datetime.now(timezone.utc),nullable=False)
    state = db.relationship("State",back_populates="risk")
