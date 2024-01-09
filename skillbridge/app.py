import os
from flask import Flask, jsonify, request
import db
import services as s
from skillbridge.models import *

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

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE= os.path.join(app.instance_path, 'skillbridge.db'),
        DEBUG=True
        )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    register_api_routes(app)

    return app

def register_api_routes(app):

    @app.route('/')
    def hello():
        return 'Hello, World!'
    
    # faculty routes
    @app.route('/api/faculties', methods=['GET'])
    def get_all_faculties():
        faculties = s.get_all_faculties()
        return to_json(faculties)

    @app.route('/api/faculties/<int:faculty_id>', methods=['GET'])
    def get_faculty_by_id(faculty_id):
        faculty = s.get_faculty_by_id(faculty_id)
        if(faculty is None):
            return jsonify({"error": "Faculty not found"}), 404
        return to_json(faculty)
    
    @app.route('/api/faculties', methods=['POST'])
    def add_new_faculty():
        request_data = request.get_json()
        if 'name' not in request_data:
            return jsonify({"error": "Faculty name is required"}), 400
        if s.faculty_exists(request_data['name']):
            return jsonify({"error": "Faculty already exists"}), 400
        new_faculty_id = s.add_new_faculty(request_data['name'])
        faculty = s.get_faculty_by_id(new_faculty_id)
        return to_json(faculty), 201
    
    @app.route('/api/faculties/<int:faculty_id>', methods=['PUT'])
    def update_faculty(faculty_id):
        request_data = request.get_json()
        if 'name' not in request_data:
            return jsonify({"error": "Faculty name is required"}), 400
        faculty = s.get_faculty_by_id(faculty_id)
        if(faculty is None):
            return jsonify({"error": "Faculty not found"}), 404
        faculty.name = request_data['name']
        s.update_faculty(faculty)
        return to_json(faculty), 200
    
    @app.route('/api/faculties/<int:faculty_id>', methods=['DELETE'])
    def delete_faculty(faculty_id):
        faculty = s.get_faculty_by_id(faculty_id)
        if(faculty is None):
            return jsonify({"error": "Faculty not found"}), 404
        s.delete_faculty(faculty_id)
        return jsonify({"message": "Faculty deleted successfully"}), 200
    
app = create_app()
if __name__ == "__main__":
    app.run()
