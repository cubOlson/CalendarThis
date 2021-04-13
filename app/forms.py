from wtforms.fields import (
    BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField
)
from wtforms.widgets.html5 import DateInput, TimeInput

from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

class AppointmentForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    start_date = DateField('start_datetime', widget = DateInput(), validators=[DataRequired()])
    start_time = TimeField('start_datetime', widget = TimeInput(), validators=[DataRequired()])
    end_date = DateField('end_datetime', widget = DateInput(), validators=[DataRequired()])
    end_time = TimeField('end_datetime', widget = TimeInput(), validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    private = BooleanField('private')
    submit = SubmitField()