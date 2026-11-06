def serialize_state(state):
    return {
        "id": state.id,
        "name": state.name,
        "iso3": state.iso_code
    }