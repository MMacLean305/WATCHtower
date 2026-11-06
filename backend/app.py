import os
from flask import Flask
from dotenv import load_dotenv
from database import db

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    from models import State, Source, Event, Risk, RiskHistory
    db.create_all()