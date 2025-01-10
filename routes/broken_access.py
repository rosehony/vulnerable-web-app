from flask import Blueprint, request, session

broken_access = Blueprint('broken_access', __name__)

@broken_access.route('/admin')
def admin_panel():
    # Vulnerability: No proper access control
    return "Admin Panel: All user data"

@broken_access.route('/user/<user_id>')
def user_profile(user_id):
    # Vulnerability: IDOR (Insecure Direct Object Reference)
    return f"User profile for ID: {user_id}"
