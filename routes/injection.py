from flask import Blueprint, request
import sqlite3
import subprocess

injection = Blueprint('injection', __name__)

@injection.route('/search')
def search():
    query = request.args.get('q', '')
    # Vulnerability: SQL Injection
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM users WHERE username LIKE '%{query}%'")
    results = c.fetchall()
    conn.close()
    return str(results)

@injection.route('/ping')
def ping():
    host = request.args.get('host', 'localhost')
    # Vulnerability: Command Injection
    result = subprocess.check_output(f"ping -c 1 {host}", shell=True)
    return result
