from flask import request, jsonify, Blueprint
from services import project_service as s
from utilities import to_json
from flasgger import swag_from
project_endpoint = Blueprint('project_endpoint', __name__)


@project_endpoint.route('/', methods=['GET'])
@swag_from({
    'description': 'Get all projects',
    'responses': {
        '200': {
            'description': 'All projects retrieved successfully',
        },
    },
})
def get_all_projects():
    projects = s.get_all_projects()
    return to_json(projects)


@project_endpoint.route('/<int:project_id>', methods=['GET'])
@swag_from({
    'description': 'Get a project by ID',
    'parameters': [
        {
            'name': 'project_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the project to retrieve',
        }
    ],
    'responses': {
        '200': {
            'description': 'Project retrieved successfully',
        },
        '404': {
            'description': 'Project not found',
        },
    },
})
def get_project_by_id(project_id):
    project = s.get_project_by_id(project_id)
    if project is None:
        return jsonify({"error": "Project not found"}), 404
    return to_json(project)


@project_endpoint.route('/', methods=['POST'])
@swag_from({
    'description': 'Add a new project',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'project_title':'title', 'project_description': 'description', 'project_status':'status',
                'properties': {
                    'review': {
                        'type': 'string',
                        'description': 'project_title, project_description, project_status of project',
                    },
                },
                'required': ['project_title', 'project_description', 'project_status']
            },
        }
    ],
    'responses': {
        '201': {
            'description': 'Project created successfully',
        },
        '400': {
            'description': 'Project_title, Project_description and Project status is required',
        },
        '400': {
            'description': 'Project already exists',
        },
    },
})
def add_new_project():
    request_data = request.get_json()
    if 'project_title' and 'project_description' and 'project_status' not in request_data:
        return jsonify({"error": "Project_title, Project_description and Project status is required"}), 400
    if s.project_exists(request_data['Project_title'], request_data['Project_description'], request_data['project_status']):
        return jsonify({"error": "Project already exists"}), 400
    new_project_id = s.add_new_project(request_data['Project_title'], request_data['Project_description'], request_data['project_status'])
    project = s.get_project_by_id(new_project_id)
    return to_json(project), 201


@project_endpoint.route('/<int:project_id>', methods=['PUT'])
@swag_from({
    'description': 'Update a project',
    'parameters': [
        {
            'name': 'project_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the project to update',
        },
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'project_title':'title', 'project_description': 'description', 'project_status':'status',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'project_title, project_description, project_status of the new project',
                    },
                },
                'required': ['project_title', 'project_description', 'project_status']
            },
        }
    ],
    'responses': {
        '200': {
            'description': 'Project updated successfully',
        },
        '400': {
            'description': 'Project_title, Project_description and Project status is required',
        },
        '404': {
            'description': 'project not found',
        },
    },
})
def update_project(project_id):
    request_data = request.get_json()
    if 'project_title' and 'project_description' and 'project_status' not in request_data:
        return jsonify({"error": "Project_title, Project_description and Project status is required"}), 400
    project = s.get_project_by_id(project_id)
    if (project is None):
        return jsonify({"error": "Project not found"}), 404
    project.project_title, project.project_description, project.project_status = request_data['Project_title'], request_data['Project_description'], request_data['project_status']
    s.update_project(project)
    return to_json(project), 200


@project_endpoint.route('/<int:project_id>', methods=['DELETE'])
@swag_from({
    'description': 'Delete a project',
    'parameters': [
        {
            'name': 'project_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the project to delete',
        }
    ],
    'responses': {
        '200': {
            'description': 'Project deleted successfully',
        },
        '404': {
            'description': 'Project not found',
        },
    },
})
def delete_project(project_id):
    project = s.get_project_by_id(project_id)
    if (project is None):
        return jsonify({"error": "Project not found"}), 404
    s.delete_project(project_id)
    return jsonify({"message": "Project deleted successfully"}), 200