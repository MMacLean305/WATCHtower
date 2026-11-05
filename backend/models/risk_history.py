from database import db
class RiskHistory(db.Model):
    __tablename__ = "risk_history"
    id = db.Column(db.Integer, primary_key=True)
    state_id = db.Column(db.Integer, db.ForeignKey("states.id"), nullable=False)
    risk_score = db.Column(db.Float, nullable=False)
    recorded_at = db.Column(db.DateTime(timezone=True),nullable=False)
    state = db.relationship("State",back_populates="risk_history")
