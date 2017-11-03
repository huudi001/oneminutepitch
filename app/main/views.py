from flask import render_template,redirect,url_for
from .. import db
from flask_login import login_user,logout_user,login_required,current_user
from . import main
from ..models import User,Pitch,Feedback,Category
from .forms import PitchForm,FeedbackForm

@main.route('/')
def index():
    category = Category.query.all()
    title = 'Home'
    return render_template('index.html', title = title, category= category)

@main.route('/new-pitch', methods = ['GET','POST'])

@main.route('/category/<int:id>')
def category(id):
    category = Category.query.get(id)
    title = {category.name}
    pitch = Pitch.get_pitches(category.id)

    return render_template('category.html', title = title, category = category, pitch = pitch)

@main.route('/category/pitch/new/<int:id>', methods = ["GET", "POST"])
@login_required
def new_pitch(id):

    form = PitchForm()
    category = Category.query.filter_by(id = id).first()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data

        new_pitch = Pitch(category_id = category.id, title = title, body = body, user = current_user)
        new_pitch.save_pitch()
        return redirect(url_for('.category', id = category.id))
    title = {category.name}
    return render_template('new_pitch.html', title = title, pitch_form = form, category = category)

@main.route('/pitch/feedback/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_feedback(id):
    form = FeedbackForm()
    pitch = Pitch.query.filter_by(id = id).first()
    if form.validate_on_submit():
        feedback = form.feedback.data
        new_feedback.save_feedback()
        return redirect(url_for('.feedback', id = pitch.id ))
    title = {pitch.title}
    return render_template('new_feedback.html', title = title, feedback_form = form, pitch = pitch)

@main.route('/pitch/feedbacks/<int:id>')
def feedbacks(id):
    pitch = Pitch.query.get(id)
    feedback = Feedback.get_feedbacks(pitch.id)
    title = {pitch.title}

    return render_template('feedbacks.html', title = title, pitch = pitch, feedback = feedback)

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
