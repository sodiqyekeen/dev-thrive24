from flask import jsonify

def to_json(data):
    if isinstance(data, list):
        # If the data is a list, convert each item to a dictionary
        return jsonify([item.__dict__() if hasattr(item, '__dict__') else item for item in data])
    elif hasattr(data, '__dict__'):
        # If the data is a single object, convert it to a dictionary
        return jsonify(data.__dict__())
    else:
        # If the data is a simple type, convert it directly
        return jsonify(data)