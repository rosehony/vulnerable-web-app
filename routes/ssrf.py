from flask import Blueprint, request
import requests

ssrf = Blueprint('ssrf', __name__)

@ssrf.route('/fetch')
def fetch_url():
    # Vulnerability: SSRF
    url = request.args.get('url', '')
    response = requests.get(url)
    return response.text
