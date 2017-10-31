from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class FeedbackForm(FlaskForm):

    title = StringField('Feedback title',validators=[Required()])
    feedback = TextAreaField('Pitch feedback', validators=[Required()])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):

    choice = [("science","science"),("technology", "technology"),("entertainment","entertainment")]
    title = StringField('Feedback title',validators=[Required()])
     pitch= TextAreaField('Pitch review', validators=[Required()])
     category = SelectField('category'choices = choice)
    submit = SubmitField('Submit')
