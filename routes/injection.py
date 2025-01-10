from flask import Blueprint, request
import sqlite3
import subprocess
import os

injection = Blueprint('injection', __name__)

@injection.route('/search', methods=['GET', 'POST'])
def search():
    username = request.args.get('username', '')
    password = request.args.get('password', '')
    
    # VULNERABILITY: Direct SQL injection
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    sql_query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(sql_query)  # Direct SQL injection vulnerability
    
    # VULNERABILITY: OS Command injection
    os.system(f"echo {username} >> /tmp/users.txt")  # Command injection
    
    # VULNERABILITY: Unsafe deserialization
    import pickle
    data = request.args.get('data')
    pickle.loads(data)  # Unsafe deserialization

    return "Query executed"

@injection.route('/exec')
def execute_command():
    # VULNERABILITY: Direct command execution
    cmd = request.args.get('cmd', 'ls')
    output = subprocess.check_output(cmd, shell=True)  # Command injection
    return output

@injection.route('/file')
def read_file():
    # VULNERABILITY: Path traversal
    filename = request.args.get('filename')
    with open(filename, 'r') as f:  # Path traversal vulnerability
        content = f.read()
    return content
