from flask import request, jsonify, Blueprint
from services import notification_service  as s
from utilities import to_json
from flasgger import swag_from
notification_service_endpoint = Blueprint('notification_service_endpoint', __name__)


@notification_service_endpoint.route('/', methods=['GET'])
@swag_from({
    'description': 'Get all notifications',
    'responses': {
        '200': {
            'description': 'All notifications retrieved successfully',
        },
    },
})
def get_all_notifications():
    notifications = s.get_all_notifications()
    return to_json(notifications)


@notification_service_endpoint.route('/<int:notification_id>', methods=['GET'])
@swag_from({
    'description': 'Get a notification by ID',
    'parameters': [
        {
            'name': 'notification_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the notification to retrieve',
        }
    ],
    'responses': {
        '200': {
            'description': 'notification retrieved successfully',
        },
        '404': {
            'description': 'Notiification not found',
        },
    },
})
def get_notification_by_id(notification_id):
    notification = s.get_notification_by_id(notification_id)
    if notification is None:
        return jsonify({"error": "Notification not found"}), 404
    return to_json(notification)


@notification_service_endpoint.route('/', methods=['POST'])
@swag_from({
    'description': 'Add a new notification',
    'parameters': [
        {
            'user_id': 'body',
            'content': 'body',

            'in': 'body',
            'required': 'true',
            'schema': {
                'user_id': 'body',
                'content': 'body',
                'properties': {
                    'review': {
                        'type': 'string',
                        'description': 'The user_id and content for notification',
                    },
                },
                'required': ['user_id and content']
            },
        }
    ],
    'responses': {
        '201': {
            'description': 'Notification created successfully',
        },
        '400': {
            'description': 'user_id and content is required',
        },
        '400': {
            'description': 'Notification already exists',
        },
    },
})
def add_new_notification():
    request_data = request.get_json()
    if 'user_id' and 'content' not in request_data:
        return jsonify({"error": "user_id and content is required"}), 400
    if s.notification_exists(request_data['user_id'], request_data['content']):
        return jsonify({"error": "Notification already exists"}), 400
    new_notification = s.add_new_notification(request_data['user_id'], request_data['content'])
    project = s.add_new_notification(new_notification)
    return to_json(project), 201


@notification_service_endpoint.route('/<int:notification_id>', methods=['PUT'])
@swag_from({
    'description': 'Update a notification',
    'parameters': [
        {
            'name': 'notification_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the notification to update',
        },
        {
            'user_id': 'body',
            'content': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'user_id': 'body',
                'content': 'body',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'The user_id and content for of the new notification',
                    },
                },
                'required': ['user_id and content']
            },
        }
    ],
    'responses': {
        '200': {
            'description': 'Notification updated successfully',
        },
        '400': {
            'description': 'user_id and contentis required',
        },
        '404': {
            'description': 'notification not found',
        },
    },
})
def update_notification(notification_id):
    request_data = request.get_json()
    if 'user_id' and 'content' not in request_data:
        return jsonify({"error": "user_id and content is required"}), 400
    notification = s.get_notification_by_id(notification_id)
    if (notification is None):
        return jsonify({"error": "Notification not found"}), 404
    notification= s.update_notification(request_data['user_id'], request_data['content'])
    return to_json(notification), 200


@notification_service_endpoint.route('/<int:notification_id>', methods=['DELETE'])
@swag_from({
    'description': 'Delete a notification',
    'parameters': [
        {
            'name': 'notification_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the notification to delete',
        }
    ],
    'responses': {
        '200': {
            'description': 'notification deleted successfully',
        },
        '404': {
            'description': 'Notification not found',
        },
    },
})
def delete_notification(notification_id):
    notification = s.get_notification_by_id(notification_id)
    if (notification is None):
        return jsonify({"error": "Notification not found"}), 404
    s.delete_notification(notification_id)
    return jsonify({"message": "Notification deleted successfully"}), 200