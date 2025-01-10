from flask import Blueprint, request, session
import hashlib

auth_failures = Blueprint('auth_failures', __name__)

@auth_failures.route('/login', methods=['POST'])
def login():
    # Vulnerability: Weak password hashing
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Vulnerability: SQL Injection in login
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    user = c.execute(query).fetchone()
    conn.close()
    
    if user:
        session['user'] = username
        return 'Login successful'
    return 'Login failed'
