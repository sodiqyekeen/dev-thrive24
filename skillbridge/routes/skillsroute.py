from flask import request, jsonify, Blueprint
from services  import skills_service as s
from utilities import to_json
from flasgger import swag_from
skills_endpoint= Blueprint('skills_endpoint', __name__)


@skills_endpoint.route('/', methods=['GET'])
@swag_from({
    'description': 'Get all skills',
    'responses': {
        '200': {
            'description': 'All skills retrieved successfully',
        },
    },
})
def get_all_skills():
    skills = s.get_all_skills()
    return to_json(skills)


@skills_endpoint.route('/<int:skill_id>', methods=['GET'])
@swag_from({
    'description': 'Get a skill by ID',
    'parameters': [
        {
            'name': 'skill_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the skill to retrieve',
        }
    ],
    'responses': {
        '200': {
            'description': 'skill retrieved successfully',
        },
        '404': {
            'description': 'skill not found',
        },
    },
})
def get_skill_by_id(skill_id):
    skill = s.get_skill_by_id(skill_id)
    if skill is None:
        return jsonify({"error": "Skill not found"}), 404
    return to_json(skill)


@skills_endpoint.route('/', methods=['POST'])
@swag_from({
    'description': 'Add a new skill',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'Skill_Name': 'name of skill',
                'Description':'description of skill',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'Name of the skill',
                    },
                },
                'required': ['Skill_Name', 'Description']
            },
        }
    ],
    'responses': {
        '201': {
            'description': 'Skill created successfully',
        },
        '400': {
            'description': 'Skill name and Description is required',
        },
        '400': {
            'description': 'Skill already exists',
        },
    },
})
def add_new_skill():
    request_data = request.get_json()
    if 'Skill_Name' and 'Description' not in request_data:
        return jsonify({"error": "Skill name and Description is required"}), 400
    if s.skill_exists(request_data['Skill_Nmae'], request_data['Description']):
        return jsonify({"error": "Skill already exists"}), 400
    new_skill_id = s.add_new_skill(request_data['Skill_Name'], request_data['Description'])
    skill = s.get_skill_by_id(new_skill_id)
    return to_json(skill), 201


@skills_endpoint.route('/<int:skill_id>', methods=['PUT'])
@swag_from({
    'description': 'Update a skill',
    'parameters': [
        {
            'name': 'skill_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the skill to update',
        },
        {
            'Skill_Name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'Skill_Name': 'name of skill',
                'Description':'description of skill',
                'properties': {
                    'Skill_Name': {
                        'type': 'string',
                        'description': 'The new name of the skill',
                    },
                },
                'required': ['Skill_Name', 'Description']
            },
        }
    ],
    'responses': {
        '200': {
            'description': 'Skill updated successfully',
        },
        '400': {
            'description': 'Skill name and Description is required',
        },
        '404': {
            'description': 'Skill not found',
        },
    },
})
def update_skill(skill_id):
    request_data = request.get_json()
    if 'Skill_Name' and 'Description' not in request_data:
        return jsonify({"error": "Skill name and description is required"}), 400
    skill = s.get_skill_by_id(skill_id)
    if (skill is None):
        return jsonify({"error": "skill not found"}), 404
    skill.Skill_Name, skill.Description = request_data['Skill_Name'], request_data['Description']
    s.update_skill(skill)
    return to_json(skill), 200


@skills_endpoint.route('/<int:skill_id>', methods=['DELETE'])
@swag_from({
    'description': 'Delete a skill',
    'parameters': [
        {
            'name': 'skill_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the skill to delete',
        }
    ],
    'responses': {
        '200': {
            'description': 'skill deleted successfully',
        },
        '404': {
            'description': 'skill not found',
        },
    },
})
def delete_skill(skill_id):
    skill = s.get_skill_by_id(skill_id)
    if (skill is None):
        return jsonify({"error": "skill not found"}), 404
    s.delete_skill(skill_id)
    return jsonify({"message": "skill deleted successfully"}), 200
