from flask import Blueprint, request, Response
import os
import sys

security_misconfig = Blueprint('security_misconfig', __name__)

@security_misconfig.route('/debug')
def debug_info():
    # VULNERABILITY: Information disclosure
    debug_info = {
        'environment': os.environ,
        'python_path': sys.path,
        'system': os.uname(),
        'env_vars': dict(os.environ),
    }
    return str(debug_info)

@security_misconfig.route('/phpinfo')
def php_info():
    # VULNERABILITY: Version disclosure
    server_info = {
        'server': 'Apache/2.4.49',
        'php_version': '7.4.1',
        'mysql_version': '5.7.35'
    }
    return server_info

@security_misconfig.route('/headers')
def headers():
    # VULNERABILITY: Missing security headers
    response = Response("Sensitive Data")
    return response
