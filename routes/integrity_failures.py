from flask import Blueprint, request
import json

integrity_failures = Blueprint('integrity_failures', __name__)

@integrity_failures.route('/update', methods=['POST'])
def update_settings():
    # Vulnerability: No integrity checking for updates
    settings = request.get_json()
    with open('config.json', 'w') as f:
        json.dump(settings, f)
    return 'Settings updated'
