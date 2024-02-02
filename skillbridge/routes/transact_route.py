from flask import request, jsonify, Blueprint
from services import transact_services as s
from utilities import to_json
from flasgger import swag_from
transaction_endpoint = Blueprint('transaction_endpoint', __name__)


@transaction_endpoint.route('/', methods=['GET'])
@swag_from({
    'description': 'Get all transaction',
    'responses': {
        '200': {
            'description': 'All tansaction retrieved successfully',
        },
    },
})
def get_all_transactions():
    transactions = s.get_all_transactions()
    return to_json(transactions)


@transaction_endpoint.route('/<int:transaction_id>', methods=['GET'])
@swag_from({
    'description': 'Get a transaction by ID',
    'parameters': [
        {
            'name': 'transaction_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the transaction to retrieve',
        }
    ],
    'responses': {
        '200': {
            'description': 'Transaction retrieved successfully',
        },
        '404': {
            'description': 'Transaction not found',
        },
    },
})
def get_project_by_id(user_role_id):
    user_role = s.get_user_role_by_id(user_role_id)
    if user_role is None:
        return jsonify({"error": "User_role not found"}), 404
    return to_json(user_role)


@transaction_endpoint.route('/', methods=['POST'])
@swag_from({
    'description': 'Add a new transaction',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'payment_reference': 'refrence of payment', 'payment_status': 'paid/ free /not paid/ pending',
                'properties': {
                    'review': {
                        'type': 'string',
                        'description': 'payment refrence and payment status of skill transaction',
                    },
                },
                'required': ['payment_reference', 'payment_status']
            },
        }
    ],
    'responses': {
        '201': {
            'description': 'Transaction created successfully',
        },
        '400': {
            'description': 'payment reference and payment status is required',
        },
        '400': {
            'description': 'This transaction already exists',
        },
    },
})
def add_new_transaction():
    request_data = request.get_json()
    if 'payment_reference' and 'payment_status' not in request_data:
        return jsonify({"error": "payment reference and payment status is required"}), 400
    if s.transaction_exists(request_data['payment_reference'], request_data['payment_status']):
        return jsonify({"error": "This Transaction  exists"}), 400
    new_transaction_id = s.add_new_transaction(request_data['payment_reference'], request_data['payment_status'])
    transaction = s.get_transaction_by_id(new_transaction_id)
    return to_json(transaction), 201


@transaction_endpoint.route('/<int:transaction_id>', methods=['PUT'])
@swag_from({
    'description': 'Update a transaction',
    'parameters': [
        {
            'name': 'transaction_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the transaction to update',
        },
        {
            'name': 'body',
            'in': 'body',
            'required': 'true',
            'schema': {
                'payment_reference': 'refrence of payment', 'payment_status': 'paid/ free /not paid/ pending',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'payment refrence and payment status of skill transaction',
                    },
                },
                'required': ['payment_reference', 'payment_status']
            },
        }
    ],
    'responses': {
        '200': {
            'description': 'Transaction updated successfully',
        },
        '400': {
            'description': 'payment refrence and payment status is required',
        },
        '404': {
            'description': 'transaction not found',
        },
    },
})
def update_tranaction(transaction_id):
    request_data = request.get_json()
    if  'payment_reference' and 'payment_status' not in request_data:
        return jsonify({"error": "rpayment refrence and payment status is required"}), 400
    transaction = s.get_transaction_by_id(transaction_id)
    if (transaction is None):
        return jsonify({"error": "Transaction not found"}), 404
    transaction.payment_reference, transaction.payment_status = request_data['id'], request_data['role_name']
    s.update_tranaction(transaction)
    return to_json(transaction), 200


@transaction_endpoint.route('/<int:transaction_id>', methods=['DELETE'])
@swag_from({
    'description': 'Delete a transaction',
    'parameters': [
        {
            'name': 'transaction_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
            'description': 'ID of the transaction to delete',
        }
    ],
    'responses': {
        '200': {
            'description': 'Transaction deleted successfully',
        },
        '404': {
            'description': 'transaction not found',
        },
    },
})
def delete_transaction(transaction_id):
    transaction = s.get_transaction_by_id(transaction_id)
    if transaction is None:
        return jsonify({"error": "transaction not found"}), 404
    s.delete_transaction(transaction_id)
    return jsonify({"message": "transaction deleted successfully"}), 200
