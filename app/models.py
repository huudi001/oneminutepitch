from . import db
from flask_login import UserMixin

from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email =email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = password_hash = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))

    @property
        def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    @login_manager.user_loader
    def load_user(user_id):
    return User.query.get(int(user_id))



    def __repr__(self):
        return  self.username


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key= True)
    title = db.Column(db.String(255))
    body = db.Column(db.String(255))
    category = db.Column(db.String(255))
    users = db.relationship('User',backref = 'pitch',lazy="dynamic")

class Feedback(db.Model):
    __tablename__ = 'feedbacks'
    title = db.Column(db.String(255))
    id = db.Column(db.Integer,primary_key = True)
    body = db.Column(db.String(255))


class Category(db.Model):
    __tablename__ = 'categories'
    name = db.Column(db.String(255))
    id = db.Column(db.Integer,primary_key = True)
