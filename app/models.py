from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Category(db.Model):
    __tablename__ = 'categories'


    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))

    def save_category(self):

        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        categories = Category.query.all()
        return categories
class Pitch(db.Model):
    all_pitches = []
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    category_id = db.Column(db.Integer,db.ForeignKey("categories.id"))
    feedback = db.relationship("Feedback", backref="pitch", lazy = "dynamic")



    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()


    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.filter_by(category_id=id).all()
        return pitches




class User(UserMixin,db.Model):
    __tablename__ = 'users'


    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email=db.Column(db.String(255),unique=True,index=True)
    password_hash=db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship("Pitch", backref="user", lazy = "dynamic")
    feedback = db.relationship("Feedback", backref="user", lazy = "dynamic")


    @property
    def password(self):
        raise AttributeError('You can not read the password Attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)



    def __repr__(self):
        return  {self.username}


class Feedback(db.Model):

    __tablename__ = 'feedback'

    id = db.Column(db. Integer,primary_key = True)
    feedback_section_id = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitches_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))

    def save_feedback(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_feedback(self,id):
        feedback = Feedback.query.filter_by(pitches_id=id).all()
        return feedback
