from flask import Flask, render_template, request, session, redirect, url_for
from routes.broken_access import broken_access
from routes.crypto_failures import crypto_failures
from routes.injection import injection
from routes.insecure_design import insecure_design
from routes.security_misconfig import security_misconfig
from routes.vulnerable_components import vulnerable_components
from routes.auth_failures import auth_failures
from routes.integrity_failures import integrity_failures
from routes.logging_failures import logging_failures
from routes.ssrf import ssrf

app = Flask(__name__)
app.secret_key = "very_secret_key_123"  # Vulnerability: Hardcoded secret key

# Register blueprints
app.register_blueprint(broken_access, url_prefix='/broken-access')
app.register_blueprint(crypto_failures, url_prefix='/crypto-failures')
app.register_blueprint(injection, url_prefix='/injection')
app.register_blueprint(insecure_design, url_prefix='/insecure-design')
app.register_blueprint(security_misconfig, url_prefix='/security-misconfig')
app.register_blueprint(vulnerable_components, url_prefix='/vulnerable-components')
app.register_blueprint(auth_failures, url_prefix='/auth-failures')
app.register_blueprint(integrity_failures, url_prefix='/integrity-failures')
app.register_blueprint(logging_failures, url_prefix='/logging-failures')
app.register_blueprint(ssrf, url_prefix='/ssrf')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
