from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, NoneOf, ValidationError, Optional

class RegistrationForm(FlaskForm):
    regex = ["a-zA-Z0-9"]

    def check_for_space(FlaskForm, field):
        if chr(32) in field.data:
            raise ValidationError('Contains a space')

    def if_empty(FlaskForm, field):
        #Checks for data in field
        if len(field.data) > 1:
            #check for valid email - must not contain space - length of 3 - 20 characters
            if chr(32) in field.data or len(field.data) < 3 or len(field.data) > 20:
                raise ValidationError('Invalid email')
            #check for single @ symbol
            if chr(46) in field.data or chr(64) in field.data:
                dot_symbol = field.data.count(chr(46))
                at_symbol = field.data.count(chr(64))
                if dot_symbol > 1 or at_symbol > 1:
                    raise ValidationError('Too many . or @ symbols')

    username = StringField('Username',
        #Must not be empty
        validators=[DataRequired(), Length(min=3, max=20),
        #No space allowed
        check_for_space
        ])

    password = PasswordField("Password",
        #Must not be empty
        validators=[DataRequired(), Length(min=3, max=20),
        #No space allowed
        check_for_space
        ])

    verify_password = PasswordField("Verify Password",
        #Match passwords
        validators=[DataRequired(), EqualTo("password")])

    email = StringField("Email (Optional)", validators=[Optional(), if_empty])
    '''#Checks for valid email
    email = StringField("Email (Optional)", if_empty)
        #Check for Length
        validators=[Email(), Length(min=3, max=20)])
    '''

    submit = SubmitField('Submit')
