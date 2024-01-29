from flask import request, jsonify, Blueprint
from services import student_service as s
from utilities import to_json
from flasgger import swag_from
student_endpoint = Blueprint('student_endpoint', __name__)


@student_endpoint.route('/', methods=['GET'])
@swag_from({
    'description': 'Get all students',
    'responses': {
        '200': {
            'description': 'All students retrieved successfully',
        },
    },
})
def get_all_students():
    students = s.get_all_students()
    return to_json(students)


@student_endpoint.route('/<int:student_id>', methods=['GET'])
@swag_from({
    'description': 'Get a student by ID',
    'parameters': [
        {
            'name': 'student_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the student to retrieve',
        }
    ],
    'responses': {
        '200': {
            'description': 'student retrieved successfully',
        },
        '404': {
            'description': 'student not found',
        },
    },
})
def get_student_by_id(student_id):
    student = s.get_student_by_id(student_id)
    if student is None:
        return jsonify({"error": "student not found"}), 404
    return to_json(student)


@student_endpoint.route('/', methods=['POST'])
@swag_from({
    'description': 'Add a new student',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'id': 'Student',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'Name of the student',
                    },
                },
                'required': ['name']
            },
        }
    ],
    'responses': {
        '201': {
            'description': 'Student created successfully',
        },
        '400': {
            'description': 'Student name is required',
        },
        '400': {
            'description': 'Student already exists',
        },
    },
})
def add_new_student():
    request_data = request.get_json()
    if 'matric_no' and 'first_name' and 'last_name' and 'department_id' and 'level' and 'username' and 'password' and 'email' not in request_data:
        return jsonify({"error": "[matric_no, first_name, last_name, department_id, level, username, password, email] all field is required"}), 400
    if s.student_exists(request_data['matric_no']):
        return jsonify({"error": "Student already exists"}), 400
    new_student = s.add_new_student(request_data['name'], request_data['matric_no'], request_data['first_name'], request_data['last_name'], request_data['department_id'], request_data['level'], request_data['username'], request_data['password'], request_data['email'])
    student = s.add_new_student(new_student)
    return to_json(student), 201


@student_endpoint.route('/<int:student_id>', methods=['PUT'])
@swag_from({
    'description': 'Update a student',
    'parameters': [
        {
            'name': 'student_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the student to update',
        },
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'id': 'Student',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'The new name of the Student',
                    },
                },
                'required': ['name']
            },
        }
    ],
    'responses': {
        '200': {
            'description': 'Student updated successfully',
        },
        '400': {
            'description': 'Student name is required',
        },
        '404': {
            'description': 'Student not found',
        },
    },
})
def update_student(student_id):
    request_data = request.get_json()
    if 'matric_no' not in request_data:
        return jsonify({"error": "Matric_no is required"}), 400
    student = s.get_student_by_id(student_id)
    if (student is None):
        return jsonify({"error": "Student not found"}), 404
    student.matric_no = request_data['matric_no']
    student.first_name = request_data['first_name']
    student.last_name = request_data['last_name']
    student.username = request_data['username']
    student.password = request_data['password']
    student.email = request_data['email']
    s.update_student(student)
    return to_json(student), 200


@student_endpoint.route('/<int:student_id>', methods=['DELETE'])
@swag_from({
    'description': 'Delete a student',
    'parameters': [
        {
            'name': 'stuident_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the student to delete',
        }
    ],
    'responses': {
        '200': {
            'description': 'Student deleted successfully',
        },
        '404': {
            'description': 'Student not found',
        },
    },
})
def delete_student(student_matric_no):
    student = s.get_student_by_matric_no(student_matric_no)
    if (student is None):
        return jsonify({"error": "Student not found"}), 404
    s.delete_student(student_matric_no)
    return jsonify({"message": "Student deleted successfully"}), 200
