def serialize_event(event):
    return {
        "id": event.id,
        "state_id": event.state_id,
        "source_id": event.source_id,
        "external_id": event.external_id,
        "event_type": event.event_type,
        "description": event.description,
        "event_date": event.event_date.isoformat() if event.event_date else None,
        "latitude": event.latitude,
        "longitude": event.longitude
    }