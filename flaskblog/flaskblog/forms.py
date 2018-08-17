from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
        validators = [ DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
        validators = [ DataRequired(), Email() ])
    password = PasswordField('Password',
        validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password',
        validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user_exists = User.query.filter_by(username = username.data).first()

        if user_exists:
            raise ValidationError('User name already taken.')

    def validate_email(self, email):
        email_exists = User.query.filter_by(email = email.data).first()

        if email_exists:
            raise ValidationError('Account already exists.')

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators = [ DataRequired(), Email() ])
    password = PasswordField('Password',
        validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField( 'Email', validators=[DataRequired(), Email()] )
    picture = FileField( 'Update Picture', validators=[ FileAllowed( ['jpg','png'] ) ] )
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username taken. Please choose another')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email taken. Please choose another')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
