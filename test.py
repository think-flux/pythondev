def validate(data):
    if data['username'].startswith('_'):
        raise ValueError("Username must not begin with an underscore.")
