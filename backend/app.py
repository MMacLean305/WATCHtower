import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from database import db
from serializers import serialize_event, serialize_state
load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
with app.app_context():
    from models import State, Source, Event, Risk, RiskHistory
    db.create_all()


# State Endpoints
@app.route("/api/states", methods=["GET"])
def get_states():
    states = State.query.all()
    return jsonify([serialize_state(state) for state in states]), 200

@app.route("/api/states/<string:iso_code>", methods=["GET"])
def get_state_by_iso3(iso_code):
    state = State.query.filter_by(iso_code=iso_code.upper()).first()
    if state is None:
        return jsonify({"error": "State not found"}), 404
    return jsonify(serialize_state(state)), 200

# Event Endpoints
@app.route("/api/events", methods=["GET"])
def get_events():
    events = Event.query.all()
    return jsonify([serialize_event(event) for event in events]), 200

@app.route("/api/events/<int:event_id>", methods=["GET"])
def get_event_by_id(event_id):
    event = db.session.get(Event, event_id)
    if event is None:
        return jsonify({"error": "Event not found"}), 404
    return jsonify(serialize_event(event)), 200

@app.route("/api/states/<string:iso3>/events", methods=["GET"])
def get_events_by_state(iso3):
    state = State.query.filter_by(iso_code=iso3.upper()).first()
    if state is None:
        return jsonify({"error": "State not found"}), 404
    events = Event.query.filter_by(state_id=state.id).all()
    return jsonify([serialize_event(event) for event in events]), 200
