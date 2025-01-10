from flask import Blueprint, request, session
import hashlib

auth_failures = Blueprint('auth_failures', __name__)

# VULNERABILITY: Hardcoded credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"
API_KEY = "1234-5678-9012-3456"

@auth_failures.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # VULNERABILITY: Weak cryptography
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    
    # VULNERABILITY: Hard-coded comparison
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        session['logged_in'] = True
        return "Login successful"
    
    return "Login failed"

@auth_failures.route('/reset_password', methods=['POST'])
def reset_password():
    # VULNERABILITY: No rate limiting
    email = request.form.get('email')
    # VULNERABILITY: Information disclosure
    if email in ['admin@example.com', 'user@example.com']:
        return "Password reset email sent"
    return "Email not found"
