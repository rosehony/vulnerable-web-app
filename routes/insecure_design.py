from flask import Blueprint, request, session
import json

insecure_design = Blueprint('insecure_design', __name__)

@insecure_design.route('/api/user_data')
def get_user_data():
    # Vulnerability: Insecure Direct Object Reference
    user_id = request.args.get('id', '1')
    user_data = {
        '1': {'name': 'admin', 'role': 'admin', 'salary': '100000'},
        '2': {'name': 'user', 'role': 'user', 'salary': '50000'}
    }
    return json.dumps(user_data.get(user_id, {}))

@insecure_design.route('/deserialize')
def deserialize_data():
    # Vulnerability: Insecure Deserialization
    data = request.args.get('data', '')
    return pickle.loads(data)
