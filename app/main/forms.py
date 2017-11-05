from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField

class PitchForm(FlaskForm):
    content = TextAreaField('New Pitch')
    submit = SubmitField('Submit')

class FeedbackForm(FlaskForm):
    feedback_section_id = TextAreaField('New feedback')
    submit = SubmitField('Submit')
