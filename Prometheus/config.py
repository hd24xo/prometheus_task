import os
import secrets

# Function to generate a secret key
def generate_secret_key():
    return secrets.token_hex(16)  # Generate a 32-character hex string

# Base directory of the application
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Secret key for CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY') or generate_secret_key()

    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False