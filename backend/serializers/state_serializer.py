def serialize_state(state):
    return {
        "id": state.id,
        "name": state.name,
        "official_name": state.official_name,
        "iso3": state.iso_code,
        "region": state.region,
        "subregion": state.subregion
    }