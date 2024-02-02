from flask import request, jsonify, Blueprint
from services import department_service as s
from utilities import to_json
from flasgger import swag_from
department_endpoint = Blueprint('department_endpoint', __name__)


@department_endpoint.route('/', methods=['GET'])
@swag_from({
    'description': 'Get all Departments',
    'responses': {
        '200': {
            'description': 'All departments retrieved successfully',
        },
    },
})
def get_all_departments():
    departments = s.get_all_departments()
    return to_json(departments)


@department_endpoint.route('/<int:department_id>', methods=['GET'])
@swag_from({
    'description': 'Get a department by ID',
    'parameters': [
        {
            'name': 'department_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the department to retrieve',
        }
    ],
    'responses': {
        '200': {
            'description': 'Department retrieved successfully',
        },
        '404': {
            'description': 'Department not found',
        },
    },
})
def get_department_by_id(department_id):
    department = s.get_department_by_id(department_id)
    if department is None:
        return jsonify({"error": "Department not found"}), 404
    return to_json(department), 200


@department_endpoint.route('/', methods=['POST'])
@swag_from({
    'description': 'Add a new department',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'name': 'Department_name', 'faculty_id': 'faculty_id',
                'properties': {
                    'review': {
                        'type': 'string',
                        'description': 'name of the department and its faculty id',
                    },
                },
                'required': ['name', 'faculty_id']
            },
        }
    ],
    'responses': {
        '201': {
            'description': 'Department created successfully',
        },
        '400': {
            'description': 'Name and Faculty_id is required',
        },
        '400': {
            'description': 'Department already exists',
        },
    },
})
def add_new_department():
    request_data = request.get_json()
    if 'name' and 'faculty_id' not in request_data:
        return jsonify({"error": "Name and Faculty_id is required"}), 400
    if s.department_exists(request_data['name'], request_data['faculty_id']):
        return jsonify({"error": "department already exists"}), 400
    new_department_id = s.add_new_department(request_data['name'], request_data['faculty_id'])
    department = s.get_department_by_id(new_department_id)
    return to_json(department), 201


@department_endpoint.route('/<int:department_id>', methods=['PUT'])
@swag_from({
    'description': 'Update a department',
    'parameters': [
        {
            'name': 'department_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the department to update',
        },
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'name': 'department name', 'faculty_id': 'int',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'The new name of the Department',
                    },
                },
                'required': ['name', 'faculty_id']
            },
        }
    ],
    'responses': {
        '200': {
            'description': 'Department updated successfully',
        },
        '400': {
            'description': 'name and faculty_id is required',
        },
        '404': {
            'description': 'Department not found',
        },
    },
})
def update_department(department_id):
    request_data = request.get_json()
    if 'name' and 'faculty_id' not in request_data:
        return jsonify({"error": "Name and Faculty_id is required"}), 400
    department = s.get_department_by_id(department_id)
    if (department is None):
        return jsonify({"error": "Department not found"}), 404
    department.name = request_data['name']
    department.faculty_id = request_data['faculty_id']
    s.update_department(department)
    return to_json(department), 200


@department_endpoint.route('/<int:department_id>', methods=['DELETE'])
@swag_from({
    'description': 'Delete a department',
    'parameters': [
        {
            'name': 'department_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the department to delete',
        }
    ],
    'responses': {
        '200': {
            'description': 'Department deleted successfully',
        },
        '404': {
            'description': 'Department not found',
        },
    },
})
def delete_department(department_id):
    department = s.get_department_by_id(department_id)
    if (department is None):
        return jsonify({"error": "Department not found"}), 404
    s.delete_rating(department_id)
    return jsonify({"message": "Department deleted successfully"}), 200