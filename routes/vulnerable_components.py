from flask import Blueprint
import hashlib
from outdated_library import process_data  # Simulated outdated library

vulnerable_components = Blueprint('vulnerable_components', __name__)

@vulnerable_components.route('/process')
def process():
    # Vulnerability: Using outdated components
    return process_data(request.args.get('data', ''))
