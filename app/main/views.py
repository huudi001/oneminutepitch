from flask import render_template,redirect,url_for,abort
from . import main
from ..models import Category, User,Pitch, Feedback
from .. import db
from flask_login import login_required, current_user
from .forms import PitchForm,FeedbackForm
@main.route('/')
def index():

    categories = Category.get_categories()
    title = 'Home - Welcome to One Minute Pitch'
    return render_template('index.html', title = title, categories = categories)

@main.route('/category/<int:id>')
def category(id):

    category = Category.query.get(id)

    if category is None:
        abort(404)

    pitches = Pitch.get_pitches(id)
    title = "Pitches"
    return render_template('category.html', title = title, category = category,pitches = pitches)

@main.route('/category/pitch/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_pitch(id):
    form = PitchForm()
    category = Category.query.filter_by(id=id).first()

    if category is None:
        abort(404)

    if form.validate_on_submit():
        content = form.content.data
        # user = current_user._get_current_object()
        new_pitch = Pitch(content=content,user_id=current_user.id,category_id=category.id)
        new_pitch.save_pitch()
        return redirect(url_for('.category', id = category.id))

    title = 'New pitch'
    return render_template('new_pitch.html', title = title, pitch_form = form)

# Dynamic routing for one pitch
@main.route('/pitch/<int:id>', methods = ['GET','POST'])
@login_required
def single_pitch(id):

    pitches = Pitch.query.get(id)

    if pitches is None:
        abort(404)

    feedback = Feedback.get_feedback(id)
    title = 'feedback Section'
    return render_template('feedback.html', title = title, pitches = pitches, feedback = feedback)



@main.route('/pitch/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_feedback(id):
    form = FeedbackForm()
    pitches = Pitch.query.filter_by(id=id).first()

    if pitches is None:
        abort(404)

    if form.validate_on_submit():
        feedback_section_id = form.feedback_section_id.data
        new_feedback = Feedback(feedback_section_id=feedback_section_id,user_id=current_user.id,pitches_id=pitches.id)
        new_feedback.save_feedback()
        return redirect(url_for('.category', id = pitches.id))

    title = 'New Feedback'
    return render_template('feedbacks.html', title = title, feedback_form = form)
