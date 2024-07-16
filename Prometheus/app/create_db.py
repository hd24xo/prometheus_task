# create_db.py

from app import db
from app.models import User

# Create all tables
db.create_all()
