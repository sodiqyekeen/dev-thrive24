from flask import request, jsonify, Blueprint
import services as s
from utilities import to_json
from flasgger import swag_from
api = Blueprint('api', __name__)


@api.route('/', methods=['GET'])
@swag_from({
    'description': 'Get all faculties',
    'responses': {
        '200': {
            'description': 'All faculties retrieved successfully',
        },
    },
})
def get_all_faculties():
    faculties = s.get_all_faculties()
    return to_json(faculties)


@api.route('/<int:faculty_id>', methods=['GET'])
@swag_from({
    'description': 'Get a faculty by ID',
    'parameters': [
        {
            'name': 'faculty_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the faculty to retrieve',
        }
    ],
    'responses': {
        '200': {
            'description': 'Faculty retrieved successfully',
        },
        '404': {
            'description': 'Faculty not found',
        },
    },
})
def get_faculty_by_id(faculty_id):
    faculty = s.get_faculty_by_id(faculty_id)
    if faculty is None:
        return jsonify({"error": "Faculty not found"}), 404
    return to_json(faculty)


@api.route('/', methods=['POST'])
@swag_from({
    'description': 'Add a new faculty',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'id': 'Faculty',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'Name of the faculty',
                    },
                },
                'required': ['name']
            },
        }
    ],
    'responses': {
        '201': {
            'description': 'Faculty created successfully',
        },
        '400': {
            'description': 'Faculty name is required',
        },
        '400': {
            'description': 'Faculty already exists',
        },
    },
})
def add_new_faculty():
    request_data = request.get_json()
    if 'name' not in request_data:
        return jsonify({"error": "Faculty name is required"}), 400
    if s.faculty_exists(request_data['name']):
        return jsonify({"error": "Faculty already exists"}), 400
    new_faculty_id = s.add_new_faculty(request_data['name'])
    faculty = s.get_faculty_by_id(new_faculty_id)
    return to_json(faculty), 201


@api.route('/<int:faculty_id>', methods=['PUT'])
@swag_from({
    'description': 'Update a faculty',
    'parameters': [
        {
            'name': 'faculty_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the faculty to update',
        },
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'id': 'Faculty',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'The new name of the faculty',
                    },
                },
                'required': ['name']
            },
        }
    ],
    'responses': {
        '200': {
            'description': 'Faculty updated successfully',
        },
        '400': {
            'description': 'Faculty name is required',
        },
        '404': {
            'description': 'Faculty not found',
        },
    },
})
def update_faculty(faculty_id):
    request_data = request.get_json()
    if 'name' not in request_data:
        return jsonify({"error": "Faculty name is required"}), 400
    faculty = s.get_faculty_by_id(faculty_id)
    if (faculty is None):
        return jsonify({"error": "Faculty not found"}), 404
    faculty.name = request_data['name']
    s.update_faculty(faculty)
    return to_json(faculty), 200


@api.route('/<int:faculty_id>', methods=['DELETE'])
@swag_from({
    'description': 'Delete a faculty',
    'parameters': [
        {
            'name': 'faculty_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the faculty to delete',
        }
    ],
    'responses': {
        '200': {
            'description': 'Faculty deleted successfully',
        },
        '404': {
            'description': 'Faculty not found',
        },
    },
})
def delete_faculty(faculty_id):
    faculty = s.get_faculty_by_id(faculty_id)
    if (faculty is None):
        return jsonify({"error": "Faculty not found"}), 404
    s.delete_faculty(faculty_id)
    return jsonify({"message": "Faculty deleted successfully"}), 200
