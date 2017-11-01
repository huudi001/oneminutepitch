from flask import render_template,redirect,url_for
from .. import db
from flask_login import login_user,logout_user,login_required
from . import main
from ..models import User,Pitch
from .forms import PitchForm

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
