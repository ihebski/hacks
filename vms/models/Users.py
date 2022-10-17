from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# define what our database user looks like.
class User(db.Model):

    __tablename__ = "users"

    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(20), unique=True, index=True)
    password = db.Column('password', db.String(255))
    email = db.Column('email', db.String(60), unique=True, index=True)
    registered_on = db.Column('registered_on', db.DateTime)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)

    # don't judge me...
    def unique(self):

        e_e = email_e = db.session.query(User.email).filter_by(email=self.email).scalar() is None
        u_e = username_e = db.session.query(User.username).filter_by(username=self.username).scalar() is None

        # none exist
        if e_e and u_e:
            return 0

        # email already exists
        elif e_e == False and u_e == True:
            return -1

        # username already exists
        elif e_e == True and u_e == False:
            return -2

        # both already exists
        else:
            return -3