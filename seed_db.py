"""Initial data for Stellar"""

from models import User, Square
from models import connect_to_db, db
from server import app
import functions

import random
from datetime import datetime

USER_LIST = [['Mason', 'zewlie@gmail.com', 'password']]


def create_users(user_list):
    """Creates initial user accounts"""

    for user in user_list:
        user = User(username=user[0],
                    email=user[1],
                    password=user[2],
                    account_made=datetime.now())

        db.session.add(user)
    db.session.commit()


def create_squares():
    """Generates the squares for the Q grid"""

    for x in range(0,26):
        for y in range(0,26):
            square = Square(x=x,
                            y=y,
                            fill=functions.color_green(x, y) or "#84898c")

            db.session.add(square)
        db.session.commit()



##############################################################################


if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    create_users(USER_LIST)
    create_squares()


