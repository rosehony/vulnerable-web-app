from flask import Blueprint, request
import subprocess
import pickle
import base64

critical = Blueprint('critical', __name__)

@critical.route('/rce', methods=['POST'])
def remote_code_exec():
    # CRITICAL: Remote Code Execution
    code = request.form.get('code', '')
    return eval(code)  # Critical vulnerability

@critical.route('/deserialize')
def unsafe_deserialize():
    # CRITICAL: Unsafe Deserialization
    data = base64.b64decode(request.args.get('data', ''))
    return pickle.loads(data)  # Critical vulnerability

@critical.route('/ssrf')
def ssrf_vuln():
    # CRITICAL: Server-Side Request Forgery
    url = request.args.get('url', '')
    import urllib.request
    return urllib.request.urlopen(url).read()

@critical.route('/sqli')
def sql_injection():
    # CRITICAL: SQL Injection with string concatenation
    user_id = request.args.get('id', '')
    query = "SELECT * FROM users WHERE id = " + user_id
    return query
