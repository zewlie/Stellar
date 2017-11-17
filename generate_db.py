"""Generates the database tables for PonyRiot"""

from models import db, connect_to_db
# from model import User

from server import app


if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()
