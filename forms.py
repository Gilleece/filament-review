from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    SubmitField,
    PasswordField,
    DateField,
    SelectField
)
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    URL,
    Regexp
)



class RegistrationForm(FlaskForm):
    """Sign up for a user account."""
    name = StringField(
        'Username',
        [
            DataRequired(),
            Regexp(
                "^[a-zA-Z0-9]{5,15}$",
                flags=0,
                message="Usernames may only contain letters and numbers."
                ),
            Length(
                min=5,
                max=15,
                message="Usernames must be between 5 and 15 characters long."
                )
        ]
    )
    email = StringField(
        'Email',
        [
            Email(message='Not a valid email address.'),
            DataRequired()
        ]
    )
    password = PasswordField(
        'Password',
        [
            DataRequired(message="Please enter a password."),
            EqualTo('confirmPassword', message='Passwords must match.')
        ]
    )
    confirmPassword = PasswordField(
        'Repeat Password',
        [
            DataRequired(message="Please enter your password again.")
        ]
    )
    submit = SubmitField('Submit')
