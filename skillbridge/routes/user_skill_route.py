from flask import request, jsonify, Blueprint
from services import user_skill_service as s
from utilities import to_json
from flasgger import swag_from
user_skill_endpoint = Blueprint('user_skill_endpoint', __name__)

@user_skill_endpoint.route('/', methods=['GET'])
@swag_from({
    'description': 'Get all Users skills',
    'responses': {
        '200': {
            'description': 'All Users skills retrieved successfully',
        },
    },
})
def get_all_skills():
    skills = s.get_all_User_Skills()
    return to_json(skills)


@user_skill_endpoint.route('/<int:User_skill_id>', methods=['GET'])
@swag_from({
    'description': 'Get a skill by ID',
    'parameters': [
        {
            'name': 'User_skill_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the user skill to retrieve',
        }
    ],
    'responses': {
        '200': {
            'description': 'User skill retrieved successfully',
        },
        '404': {
            'description': 'User skill not found',
        },
    },
})
def get_skill_by_id(User_skill_id):
    skill = s.get_User_Skill_by_id(User_skill_id)
    if skill is None:
        return jsonify({"error": "User Skill not found"}), 404
    return to_json(skill)


@user_skill_endpoint.route('/', methods=['POST'])
@swag_from({
    'description': 'Add a new user skill',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'proficiency_level':'level of understanding of skill', 
                'student_ID':'ID of user',
                'skill_ID':'ID of skill',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'Name of the skill',
                    },
                },
                'required': ['proficiency_level', 'student_ID', 'skill_ID']
            },
        }
    ],
    'responses': {
        '201': {
            'description': 'User_Skill created successfully',
        },
        '400': {
            'description': 'proficiency_level, student_ID, skill_ID is required',
        },
        '400': {
            'description': 'User Skill already exists',
        },
    },
})
def add_new_skill():
    request_data = request.get_json()
    if 'proficiency_level' and 'student_ID' and 'skill_ID' not in request_data:
        return jsonify({"error": "proficiency_level, student_ID, skill_ID is required"}), 400
    if s.User_Skill_exists(request_data['proficiency_level'], request_data['student_ID'], request_data['skill_ID']):
        return jsonify({"error": "User Skill already exists"}), 400
    new_skill_id = s.add_new_User_Skill(request_data['proficiency_level'], request_data['student_ID'], request_data['skill_ID'])
    skill = s.get_all_User_Skills(new_skill_id)
    return to_json(skill), 201


@user_skill_endpoint.route('/<int:user_skill_id>', methods=['PUT'])
@swag_from({
    'description': 'Update a skill',
    'parameters': [
        {
            'name': 'user_skill_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the user skill to update',
        },
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'proficiency_level':'level of understanding of skill', 
                'student_ID':'ID of user',
                'skill_ID':'ID of skill',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'The new name of the skill',
                    },
                },
                'required': ['proficiency_level', 'student_ID', 'skill_ID']
            },
        }
    ],
    'responses': {
        '200': {
            'description': 'User Skill updated successfully',
        },
        '400': {
            'description': 'proficiency_level, student_ID, skill_ID is required',
        },
        '404': {
            'description': 'User Skill not found',
        },
    },
})
def update_skill(user_skill_id):
    request_data = request.get_json()
    if 'proficiency_level' and 'student_ID' and 'skill_ID' not in request_data:
        return jsonify({"error": "proficiency_level, student_ID, skill_ID is required"}), 400
    skill = s.get_User_Skill_by_id(user_skill_id)
    if (skill is None):
        return jsonify({"error": "user skill not found"}), 404
    skill.Proficiency_level, skill.student_ID, skill.Skill_ID = request_data['proficiency_level'], request_data['student_ID'], request_data['skill_ID']
    s.update_User_Skill(skill)
    return to_json(skill), 200


@user_skill_endpoint.route('/<int:user_skill_id>', methods=['DELETE'])
@swag_from({
    'description': 'Delete a user skill',
    'parameters': [
        {
            'name': 'user_skill_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the user skill to delete',
        }
    ],
    'responses': {
        '200': {
            'description': 'user skill deleted successfully',
        },
        '404': {
            'description': 'user skill not found',
        },
    },
})
def delete_skill(user_skill_id):
    skill = s.get_User_Skill_by_id(user_skill_id)
    if (skill is None):
        return jsonify({"error": "user skill not found"}), 404
    s.delete_User_skill(user_skill_id)
    return jsonify({"message": "User skill deleted successfully"}), 200
