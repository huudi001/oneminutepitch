from flask import render_template,redirect,url_for
from .. import db
from flask_login import login_user,logout_user,login_required,current_user
from . import main
from ..models import User,Pitch,Feedback
from .forms import PitchForm,FeedbackForm

@main.route('/')
def index():
    # category = Category.query.all()
    pitches = Pitch.query.all()
    return render_template('index.html', pitches = pitches)

@main.route('/new-pitch', methods = ['GET','POST'])
@login_required
def new_pitch():
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        title= pitch_form.title.data
        pitch_body = pitch_form.body.data
        new_pitch = Pitch(title = title,pitch_body = pitch_body)
        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('new_pitch.html', pitch_form = pitch_form)

@main.route('/pitch/<int:id>')
def pitch(id):
    pitch = Pitch.query.get(id)
    return render_template('pitch.html', pitch = pitch)

@main.route('/feedback/<int:id>',methods =['GET','POST'])
def feedback(id):
    feedback_form = FeedbackForm()
    if feedback_form.validate_on_submit():
        title =   feedback_form.title.data
        feedback =  feedback_form.feedback.data
        new_feedback = Feedback(title= title, feedback = feedback)
        db.session.add(new_feedback)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('new_feedback.html', feedback_form = feedback_form)
