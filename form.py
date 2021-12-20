import flask_bcrypt
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectMultipleField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from __init__ import db
from database import Students, Schools

majors_list = [
    ("1", 'Liceo scientifico tradizionale'),
    ("2", 'Liceo classico'),
    ("3", 'Liceo linguistico'),
    ("4", 'Ingegneria gestionale')
]

degrees_list = [("1", 'Scuola Superiore'), ("2", 'Laurea Triennale'), ("3", 'Laurea Magistrale')]

districts_list = [("1", 'TO'), ("2", 'CN'), ("3", 'AQ'), ("4", 'PE')]


class StudentRegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=25)])
    surname = StringField("Surname", validators=[DataRequired(), Length(min=2, max=25)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=15)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=7)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    degree = SelectField("Degrees", choices=[('1', 'Scuola Superiore'), ('2', 'Laurea Triennale'), ('3', 'Laurea Magistrale')], validators=[DataRequired()])
    submit = SubmitField("Sign Up")

    def duplicate_username(self):
        s = Students.query.filter_by(username=self.username.data).first()

        if s:
            return True  # username already existent
        else:
            return False

class SchoolRegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=25)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=15)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=7)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    district = SelectMultipleField("District", choices=districts_list, validators=[DataRequired()])
    degrees = SelectMultipleField("Degrees", choices=degrees_list, validators=[DataRequired()])
    majors = SelectMultipleField("Majors", choices=majors_list, validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField("Sign Up")

    def duplicate_username(self):
        s = Schools.query.filter_by(username=self.username.data).first()
        # pass_c = form.generate_password_hash(form.password.data)

        if s:
            return True  # username already existent
        else:
            return False


class StudentLoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=7)])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")

    def existent_username(self):
        s = Students.query.filter_by(username=self.username.data).first()

        if s is not None:
            b = flask_bcrypt.check_password_hash(s.password, self.password.data)
            if b:
                return s
        else:
            return None


class SchoolLoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=7)])
    submit = SubmitField("Login")

    def existent_username(self):
        s = Schools.query.filter_by(username=self.username.data).first()

        if s is not None:
            b = flask_bcrypt.check_password_hash(s.password, self.password.data)
            if b:
                return s
        else:
            return None

'''
class StudentProfile(FlaskForm):
    id = current_user.id()
    s = Students.query.filter_by(id=id)
'''






