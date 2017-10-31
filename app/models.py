from . import db
from flask_login import UserMixin

from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
return User.query.get(int(user_id))

class User(UserMixind,db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email =email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = password_hash = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
    feedbacks = db.relationship('Feedback', backref='user', lazy='dynamic')
    votes = db.relationship('Vote', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return  self.username


class Category(db.Model):

    __tablename__ = 'categories'


    id = db.Column(db.Integer, primary_key = True)

    category_name = db.Column(db.String(255))

    pitches = db.relationship('Pitch', backref='category', lazy='dynamic')

    def save_category(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):


        categories = Category.query.all()

        return categories


class Pitch(db.Model):


    __tablename__ = 'pitches'


    id = db.Column(db.Integer, primary_key = True)
    pitch_body = db.Column(db.String(255))
    categories_id = db.Column(db.Integer, db.ForeignKey("categories.id") )
    user_id = db.Column(db.Integer, db.ForeignKey("users.id") )
    feedbacks = db.relationship('Feedback', backref='pitch', lazy='dynamic')
    votes = db.relationship('Vote', backref='pitch', lazy='dynamic')

    def save_pitch(self):

        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,category_id):
        pitches = Pitch.query.order_by(Pitch.id.desc()).filter_by(category_id=category_id).all()
        return pitches


class Feedback(db.Model):
    __tablename__ = 'feedbacks'
    id = db.Column(db.Integer, primary_key = True)
    feedback_body = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id") )
    user_id = db.Column(db.Integer, db.ForeignKey("users.id") )

    def save_feedback(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_feedbacks(cls,pitch_id):
        feedbacks= Feedback.query.filter_by(pitch_id=pitch_id).all()
        return feedbacks

class Vote(db.Model):
    __tablename__ = 'votes'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id")
    vote_count =  db.Column(db.Integer)

    def save_vote(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def count_vote(cls, user_id, pitch_id):
        retrieved_votes = Vote.query.filter(user_id==user_id,pitch_id==pitch_id).with_entities(Vote.vote_count).count()
        return retrieved_votes
