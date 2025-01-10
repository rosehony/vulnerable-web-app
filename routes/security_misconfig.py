from flask import Blueprint, request
import os

security_misconfig = Blueprint('security_misconfig', __name__)

@security_misconfig.route('/debug')
def debug_info():
    # Vulnerability: Exposing sensitive debug information
    debug_info = {
        'environment': os.environ,
        'python_path': sys.path,
        'app_config': app.config
    }
    return str(debug_info)

@security_misconfig.route('/phpinfo')
def php_info():
    # Vulnerability: Exposing configuration information
    return '<h1>PHP Configuration (Enabled)</h1>'
