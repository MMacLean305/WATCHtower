import os
from flask import Flask
from dotenv import load_dotenv
from database import db
from models import State, Source, Event, Risk, RiskHistory
from routes import states_bp, events_bp

load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
app.register_blueprint(states_bp)
app.register_blueprint(events_bp)
with app.app_context():
    db.create_all()