import os
from flask import Flask, jsonify
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

@app.route("/api/states", methods=["GET"])
def get_states():
    states = State.query.all()
    results = []
    for state in states:
        results.append({
            "id": state.id,
            "name": state.name,
            "iso3": state.iso_code
        })
    return jsonify(results), 200

@app.route("/api/states/<string:iso_code>", methods=["GET"])
def get_state_by_iso3(iso_code):
    state = State.query.filter_by(iso_code=iso_code.upper()).first()
    if state is None:
        return jsonify({"error": "State not found"}), 404
    result = {"id": state.id, "name": state.name, "iso_code": state.iso_code}
    return jsonify(result), 200