from flask import request, jsonify, Blueprint
from services import skill_exchange_service as s
from utilities import to_json
from flasgger import swag_from
skill_exchange_endpoint = Blueprint('skill_exchange_endpoint', __name__)

@skill_exchange_endpoint.route('/', methods=['GET'])
@swag_from({
    'description': 'Get all skill exchange',
    'responses': {
        '200': {
            'description': 'All skill exchange retrieved successfully',
        },
    },
})
def get_all_skill_exchanges():
    skill_exchanges = s.get_all_skill_exchanges()
    return to_json(skill_exchanges)


@skill_exchange_endpoint.route('/<int:skill_exch_id>', methods=['GET'])
@swag_from({
    'description': 'Get a skill exchange by ID',
    'parameters': [
        {
            'name': 'skill_exch_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the skill exchange to retrieve',
        }
    ],
    'responses': {
        '200': {
            'description': 'skill exchange retrieved successfully',
        },
        '404': {
            'description': 'skill exchange not found',
        },
    },
})
def get_Skill_Exchange_by_id(skill_exch_id):
    skill_exchange = s.get_Skill_Exchange_by_id(skill_exch_id)
    if skill_exchange is None:
        return jsonify({"error": "Skill exchange not found"}), 404
    return to_json(skill_exchange)


@skill_exchange_endpoint.route('/', methods=['POST'])
@swag_from({
    'description': 'Add a new skill exchange',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'ID_1': 'student1_ID',
                'ID_2':  'student2_ID', 
                'ID_3': 'skill_ID', 
                'stats': 'Satatus', 
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'student1_ID, student2_ID, skill_ID and Satatus of skill exchange',
                    },
                },
                'required': ['student1_ID', 'student2_ID', 'skill_ID', 'Satatus']
            },
        }
    ],
    'responses': {
        '201': {
            'description': 'Skill Exchange created successfully',
        },
        '400': {
            'description': 'student1_ID, student2_ID, skill_ID and Satatus is required',
        },
        '400': {
            'description': 'Skill Exchange already exists',
        },
    },
})
def add_new_Skill_Exchange():
    request_data = request.get_json()
    if 'student1_ID' and 'student2_ID' and 'skill_ID' and 'Satatus' not in request_data:
        return jsonify({"error": "student1_ID, student2_ID, skill_ID and Satatus is required"}), 400
    if s.Skill_Exchange_exists(request_data['student1_ID'], request_data['student2_ID'], request_data['skill_ID'], request_data['Satatus']):
        return jsonify({"error": "Skill Exchange already exists"}), 400
    new_skill_exch_id = add_new_Skill_Exchange(request_data['student1_ID'], request_data['student2_ID'], request_data['skill_ID'], request_data['Satatus'])
    skill_exch = get_Skill_Exchange_by_id(new_skill_exch_id)
    return to_json(skill_exch), 201


@skill_exchange_endpoint.route('/<int:skill_exch_id>', methods=['PUT'])
@swag_from({
    'description': 'Update a skill Exchange',
    'parameters': [
        {
            'name': 'skill_exch_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the skill to update',
        },
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'ID_1': 'student1_ID',
                'ID_2':  'student2_ID', 
                'ID_3': 'skill_ID', 
                'stats': 'Satatus', 
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'student1_ID, student2_ID, skill_ID and Satatus of updated skill exchange',
                    },
                },
                'required': ['name']
            },
        }
    ],
    'responses': {
        '200': {
            'description': 'Skill Exchange created successfully',
        },
        '400': {
            'description': 'student1_ID, student2_ID, skill_ID and Satatus is required',
        },
        '404': {
            'description': 'Skill Exchange already exists',
        },
    },
})
def update_Skill_Exchange(skill_exch_id):
    request_data = request.get_json()
    if 'student1_ID' and 'student2_ID' and 'skill_ID' and 'Satatus' not in request_data:
        return jsonify({"error": "student1_ID, student2_ID, skill_ID and Satatus is required"}), 400
    skill_exch = s.get_Skill_Exchange_by_id(skill_exch_id)
    if (skill_exch is None):
        return jsonify({"error": "Skill Exchange not found"}), 404
    skill_exch.student1_ID, skill_exch.student2_ID, skill_exch.skill_ID, skill_exch.Status = request_data['student1_ID'], request_data['student2_ID'], request_data['skill_ID'], request_data['Satatus']
    update_Skill_Exchange(skill_exch)
    return to_json(skill_exch), 200


@skill_exchange_endpoint.route('/<int:skill_exch_id>', methods=['DELETE'])
@swag_from({
    'description': 'Delete a skill Exchange',
    'parameters': [
        {
            'name': 'skill_exch_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the skill exchage to delete',
        }
    ],
    'responses': {
        '200': {
            'description': 'skill exchange deleted successfully',
        },
        '404': {
            'description': 'skill exchange not found',
        },
    },
})
def delete_Skill_Exchange(skill_exch_id):
    skill_exch = s.get_Skill_Exchange_by_id(skill_exch_id)
    if (skill_exch is None):
        return jsonify({"error": "skill exchange not found"}), 404
    s.delete_Skill_Exchange(skill_exch_id)
    return jsonify({"message": "skill exchange deleted successfully"}), 200
