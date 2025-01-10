from flask import Blueprint
import hashlib

crypto_failures = Blueprint('crypto_failures', __name__)

@crypto_failures.route('/hash/<password>')
def hash_password(password):
    # Vulnerability: Using weak hashing algorithm
    return hashlib.md5(password.encode()).hexdigest()

@crypto_failures.route('/store-sensitive')
def store_sensitive():
    # Vulnerability: Storing sensitive data in plaintext
    credit_card = "1234-5678-9012-3456"
    return f"Stored credit card: {credit_card}"
