from flask import Blueprint, jsonify
from models import State, Event
from serializers import serialize_state, serialize_event

states_bp = Blueprint("states", __name__)


@states_bp.route("/api/states", methods=["GET"])
def get_states():
    states = State.query.all()
    return jsonify([serialize_state(state) for state in states]), 200


@states_bp.route("/api/states/<string:iso_code>", methods=["GET"])
def get_state_by_iso3(iso_code):
    state = State.query.filter_by(iso_code=iso_code.upper()).first()
    if state is None:
        return jsonify({"error": "State not found"}), 404
    return jsonify(serialize_state(state)), 200


@states_bp.route("/api/states/<string:iso3>/events", methods=["GET"])
def get_events_by_state(iso3):
    state = State.query.filter_by(iso_code=iso3.upper()).first()
    if state is None:
        return jsonify({"error": "State not found"}), 404
    events = Event.query.filter_by(state_id=state.id).all()
    return jsonify([serialize_event(event) for event in events]), 200