from flask import Blueprint, jsonify
from database import db
from models import Event
from serializers import serialize_event

events_bp = Blueprint("events", __name__)

@events_bp.route("/api/events", methods=["GET"])
def get_events():
    events = Event.query.all()
    return jsonify([serialize_event(event) for event in events]), 200

@events_bp.route("/api/events/<int:event_id>", methods=["GET"])
def get_event_by_id(event_id):
    event = db.session.get(Event, event_id)

    if event is None:
        return jsonify({"error": "Event not found"}), 404

    return jsonify(serialize_event(event)), 200