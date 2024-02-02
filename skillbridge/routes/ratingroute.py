from flask import request, jsonify, Blueprint
from services import rating_service as s
from utilities import to_json
from flasgger import swag_from
rating_endpoint = Blueprint('rating_endpoint', __name__)


@rating_endpoint.route('/', methods=['GET'])
@swag_from({
    'description': 'Get all ratings',
    'responses': {
        '200': {
            'description': 'All ratings retrieved successfully',
        },
    },
})
def get_all_ratings():
    ratings = s.get_all_ratings()
    return to_json(ratings)


@rating_endpoint.route('/<int:rating_id>', methods=['GET'])
@swag_from({
    'description': 'Get a rating by ID',
    'parameters': [
        {
            'name': 'rating_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the rating to retrieve',
        }
    ],
    'responses': {
        '200': {
            'description': 'Rating retrieved successfully',
        },
        '404': {
            'description': 'Rating not found',
        },
    },
})
def get_rating_by_id(rating_id):
    rating = s.get_rating_by_id(rating_id)
    if rating is None:
        return jsonify({"error": "Rating not found"}), 404
    return to_json(rating)


@rating_endpoint.route('/', methods=['POST'])
@swag_from({
    'description': 'Add a new rating',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'tutor_id': 'ID_1',
                'user_id' : 'ID_2', 
                'rating': 'number of stars', 
                'review': 'comment',
                'properties': {
                    'review': {
                        'type': 'string',
                        'description': 'Tutor id, User id, Rating and Review of new Rating',
                    },
                },
                'required': ['tutor_id', 'user_id', 'rating', 'review']
            },
        }
    ],
    'responses': {
        '201': {
            'description': 'Rating created successfully',
        },
        '400': {
            'description': 'tutor_id, user_id, rating, and review is required',
        },
        '400': {
            'description': 'Rating already exists',
        },
    },
})
def add_new_rating():
    request_data = request.get_json()
    if 'tutor_id' and 'user_id' and 'rating' and 'review' not in request_data:
        return jsonify({"error": "tutor_id, user_id, rating, and review is required"}), 400
    if s.rating_exists(request_data['tutor_id'], request_data['user_id'], request_data['rating'], request_data['review']):
        return jsonify({"error": "rating already exists"}), 400
    new_rating_id = s.add_new_rating(request_data['tutor_id'], request_data['user_id'], request_data['rating'], request_data['review'])
    rating = s.get_rating_by_id(new_rating_id)
    return to_json(rating), 201


@rating_endpoint.route('/<int:rating_id>', methods=['PUT'])
@swag_from({
    'description': 'Update a rating',
    'parameters': [
        {
            'name': 'rating_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the rating to update',
        },
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'tutor_id': 'ID_1',
                'user_id' : 'ID_2', 
                'rating': 'number of stars', 
                'review': 'comment',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'Tutor id, User id, Rating and Review of updated Rating',
                    },
                },
                'required': ['tutor_id', 'user_id', 'rating', 'review']
            },
        }
    ],
    'responses': {
        '200': {
            'description': 'Rating updated successfully',
        },
        '400': {
            'description': 'tutor_id, user_id, rating, and review is required',
        },
        '404': {
            'description': 'Rating not found',
        },
    },
})
def update_rating(rating_id):
    request_data = request.get_json()
    if 'tutor_id' and 'user_id' and 'rating' and 'review' not in request_data not in request_data:
        return jsonify({"error": "tutor_id, user_id, rating, and review is required"}), 400
    rating = s.get_faculty_by_id(rating_id)
    if (rating is None):
        return jsonify({"error": "Rating not found"}), 404
    rating.tutor_id, rating.user_id, rating.rating, rating.review = request_data['tutor_id'], request_data['user_id'], request_data['rating'], request_data['review']
    s.update_rating(rating)
    return to_json(rating), 200


@rating_endpoint.route('/<int:rating_id>', methods=['DELETE'])
@swag_from({
    'description': 'Delete a rating',
    'parameters': [
        {
            'name': 'rating_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the rating to delete',
        }
    ],
    'responses': {
        '200': {
            'description': 'Rating deleted successfully',
        },
        '404': {
            'description': 'Rating not found',
        },
    },
})
def delete_rating(rating_id):
    rating = s.get_rating_by_id(rating_id)
    if (rating is None):
        return jsonify({"error": "Rating not found"}), 404
    s.delete_rating(rating_id)
    return jsonify({"message": "Rating deleted successfully"}), 200