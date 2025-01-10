from flask import Blueprint, request
import logging

logging_failures = Blueprint('logging_failures', __name__)

@logging_failures.route('/admin_action')
def admin_action():
    # Vulnerability: Insufficient logging
    action = request.args.get('action')
    target = request.args.get('target')
    # No logging of critical actions
    return f'Action {action} performed on {target}'
