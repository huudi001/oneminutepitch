from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class FeedbackForm(FlaskForm):

    title = StringField('Feedback title',validators=[Required()])
    feedback = TextAreaField(' feedback', validators=[Required()])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):

    choice = [("science","science"),("technology", "technology"),("entertainment","entertainment")]
    title = StringField('Pitch title',validators=[Required()])
    body= TextAreaField('Pitch body', validators=[Required()])
    submit = SubmitField('Submit')
