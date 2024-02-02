from flask import request, jsonify, Blueprint
from services import user_role_service as s
from utilities import to_json
from flasgger import swag_from
user_role_endpoint = Blueprint('user_role_endpoint', __name__)


@user_role_endpoint.route('/', methods=['GET'])
@swag_from({
    'description': 'Get all user_role',
    'responses': {
        '200': {
            'description': 'All user_role retrieved successfully',
        },
    },
})
def get_all_users_role():
    user_role = s.get_all_users_role()
    return to_json(user_role)


@user_role_endpoint.route('/<int:user_role_id>', methods=['GET'])
@swag_from({
    'description': 'Get a user_role by ID',
    'parameters': [
        {
            'name': 'user_role_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the user_role to retrieve',
        }
    ],
    'responses': {
        '200': {
            'description': 'User_role retrieved successfully',
        },
        '404': {
            'description': 'User_role not found',
        },
    },
})
def get_project_by_id(user_role_id):
    user_role = s.get_user_role_by_id(user_role_id)
    if user_role is None:
        return jsonify({"error": "User_role not found"}), 404
    return to_json(user_role)


@user_role_endpoint.route('/', methods=['POST'])
@swag_from({
    'description': 'Add a new user_role',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'id':'user_ro','role_name':'user_role_name',
                'properties': {
                    'review': {
                        'type': 'string',
                        'description': 'Role id and Role name for user',
                    },
                },
                'required': ['id, user_role_name']
            },
        }
    ],
    'responses': {
        '201': {
            'description': 'User_role created successfully',
        },
        '400': {
            'description': 'id and User_role_name is required',
        },
        '400': {
            'description': 'User_role already exists',
        },
    },
})
def add_new_user_role():
    request_data = request.get_json()
    if 'id' and 'role_name' not in request_data:
        return jsonify({"error": "role id and role_name is required"}), 400
    if s.user_role_exists(request_data['id'], request_data['role_name']):
        return jsonify({"error": "User_role exists"}), 400
    new_user_role = s.add_new_user_role(request_data['role_name'])
    return to_json(new_user_role), 201


@user_role_endpoint.route('/<int:user_role_id>', methods=['PUT'])
@swag_from({
    'description': 'Update a user_role',
    'parameters': [
        {
            'name': 'user_role_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the user_role to update',
        },
        {
            'name': 'user_role_name',
            'in': 'body',
            'required': 'true',
            'schema': {
                'id': 'user_role_id', 'name': 'user_role_name',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'Role id and Role name for user',
                    },
                },
                'required': ['id, user_role_name']
            },
        }
    ],
    'responses': {
        '200': {
            'description': 'User_role updated successfully',
        },
        '400': {
            'description': 'id and User_role_name is required',
        },
        '404': {
            'description': 'user_role not found',
        },
    },
})
def update_user_role(user_role_id):
    request_data = request.get_json()
    if 'id' and 'role_name' not in request_data:
        return jsonify({"error": "role id and role_name is required"}), 400
    user_role = s.get_user_role_by_id(user_role_id)
    if (user_role is None):
        return jsonify({"error": "User_role not found"}), 404
    user_role.role_name = request_data['role_name']
    s.update_user_role(user_role)
    return to_json(user_role), 200


@user_role_endpoint.route('/<int:user_role_id>', methods=['DELETE'])
@swag_from({
    'description': 'Delete a user_role',
    'parameters': [
        {
            'name': 'user_role_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the user_role to delete',
        }
    ],
    'responses': {
        '200': {
            'description': 'User_role deleted successfully',
        },
        '404': {
            'description': 'User_role not found',
        },
    },
})
def delete_user_role(user_role_id):
    user_role = s.get_user_role_by_id(user_role_id)
    if user_role is None:
        return jsonify({"error": "User_role not found"}), 404
    s.delete_user_role(user_role_id)
    return jsonify({"message": "User_role deleted successfully"}), 200