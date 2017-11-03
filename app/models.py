from . import db
from . import login_manager
from flask_login import UserMixin

from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure =  db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
    feedbacks = db.relationship('Feedback', backref='user', lazy='dynamic')




    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return  {{self.username}}


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), index = True)
    pitches = db.relationship('Pitch', backref = 'category', lazy = "dynamic")

    @classmethod
    def get_categories(cls):
        categories = Category.query.all()
        return categories

class Pitch(db.Model):


    __tablename__ = 'pitches'


    id = db.Column(db.Integer, primary_key = True)
    pitch_body = db.Column(db.String(255))
    title = db.Column(db.String(255))
    categories_id = db.Column(db.Integer, db.ForeignKey("categories.id") )
    user_id= db.Column(db.Integer, db.ForeignKey("users.id") )
    feedbacks= db.relationship('Feedback', backref='pitch', lazy='dynamic')


    def save_pitch(self):

        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, id):
        pitches = Pitch.query.filter_by(category_id = id).all()
        return pitches




class Feedback(db.Model):
     __tablename__ = 'feedbacks'
     id = db.Column(db.Integer, primary_key = True)
     title = db.Column(db.String(255))
     feedback = db.Column(db.String(255))
     user_id = db.Column(db.Integer, db.ForeignKey("users.id") )
     pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id") )
    # pitch_id  = db.Column(db.Integer)

     def save_feedback(self):
        db.session.add(self)
        db.session.commit()

     @classmethod
     def get_feedbacks(cls,pitch_id):
         feedbacks= Feedback.query.filter_by(pitch_id=pitch_id).all()
         return feedbacks
