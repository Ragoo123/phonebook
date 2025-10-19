from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=1, max=50)])
    phone_number = StringField("Phone Number", validators=[DataRequired(), Length(min=5, max=20)])
    submit = SubmitField("Add")