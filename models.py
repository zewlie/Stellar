"""Classes for ermdash."""
from flask_sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin
from passlib.hash import pbkdf2_sha256

SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy()



class User(db.Model):
    """Basic user class"""

    __tablename__ = "users"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    account_made = db.Column(db.DateTime, nullable=False)
    last_login = db.Column(db.DateTime)

    def __repr__(self):
        """Provides helpful representation when printed."""

        return "<User id={} username={} email={} account_made={}>".format(self.id,
                                                                          self.username,
                                                                          self.email,
                                                                          self.account_made)

    def __init__(self, username, email, password, account_made):
        self.username = username
        self.email = email
        self.password = self.hash_pw(password)
        self.account_made = account_made

    @staticmethod
    def hash_pw(password):
        """Hashes & salts password."""

        return pbkdf2_sha256.encrypt(password, rounds=1111, salt_size=16)

    def verify_pw(self, password):
        """Verifies password; returns True when password matches user's account."""

        return pbkdf2_sha256.verify(password, self.password)

    def next_is_valid(self, next):
        return True

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the user's id to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False


class Square(db.Model):
    """Grid squares for Q"""

    __tablename__ = "squares"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    fill = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        """Provides helpful representation when printed."""

        return "<Square id={} coords={} fill={}>".format(self.id,
                                                        (self.x + ", " + self.y),
                                                         self.fill)

    def __init__(self, x, y, fill):
        self.x = x
        self.y = y
        self.fill = fill



##############################################################################
# Helper functions


def connect_to_db(app, db_uri="sqlite:///stellar.db"):
    """Connect the db to the Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


##############################################################################
