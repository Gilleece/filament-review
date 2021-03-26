from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    SubmitField,
    PasswordField,
    SelectField,
    IntegerField,
    SelectField
)
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
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


class loginForm(FlaskForm):
    """Log in to existing account."""
    name = StringField(
        'Username',
        [
            DataRequired()
        ]
    )
    password = PasswordField(
        'Password',
        [
            DataRequired()
        ]
    )
    submit = SubmitField('Submit')


class ReviewForm(FlaskForm):
    """Form for submitting a review"""
    material_name = SelectField(
        'Filament type',
        [DataRequired()],
        choices=[
            ('ABS', 'ABS'),
            ('ASA', 'ASA'),
            ('Carbon', 'Carbon Fiber'),
            ('HIPS', 'HIPS'),
            ('Metal', 'Metal'),
            ('Nylon', 'Nylon'),
            ('PETG', 'PETG'),
            ('PLA', 'PLA'),
            ('Polycarbonate', 'Polycarbonate'),
            ('PVA', 'PVA'),
            ('TPU', 'TPU'),
            ('Wood', 'Wood')
        ]
    )
    brand = StringField(
        'Made by',
        [DataRequired()]
    )
    filament_name = StringField(
        'Filament name',
        [DataRequired()]
    )
    rating = SelectField(
        'Overall rating (1 = Terrible)',
        [DataRequired()],
        choices=[
            ('1'),
            ('2'),
            ('3'),
            ('4'),
            ('5')
        ]
    )
    cost = SelectField(
        'Cost (1 = cheap)',
        [DataRequired()],
        choices=[
            ('1'),
            ('2'),
            ('3')
        ]
    )
    temp = IntegerField(
        'Printing Temperature',
        [DataRequired()]
    )
    colour = StringField(
        'Colour',
        [DataRequired()]
    )
    finish = SelectField(
        'Finish',
        [DataRequired()],
        choices=[
            ('Standard'),
            ('Matte'),
            ('Silk'),
            ('Satin'),
            ('Glitter'),
            ('Glow in the dark'),
            ('Other')
        ]
    )
    review = StringField(
        'Review text',
        [
            DataRequired(),
            Length(
                max=250,
                message="Please keep reviews short and concise (250 char max)."
                )
        ]
    )
    image = StringField(
        'Image URL',
        [DataRequired(message="Need to upload an image? Try Imgur!")]
    )
    submit = SubmitField('Submit')


class EditForm(FlaskForm):
    """Form for editing a review"""
    material_name = SelectField(
        'Filament type',
        [DataRequired()],
        choices=[
            ('ABS', 'ABS'),
            ('ASA', 'ASA'),
            ('Carbon', 'Carbon Fiber'),
            ('HIPS', 'HIPS'),
            ('Metal', 'Metal'),
            ('Nylon', 'Nylon'),
            ('PETG', 'PETG'),
            ('PLA', 'PLA'),
            ('Polycarbonate', 'Polycarbonate'),
            ('PVA', 'PVA'),
            ('TPU', 'TPU'),
            ('Wood', 'Wood')
        ]
    )
    brand = StringField(
        'Made by',
        [DataRequired()]
    )
    filament_name = StringField(
        'Filament name',
        [DataRequired()]
    )
    rating = SelectField(
        'Overall rating (1 = Terrible)',
        [DataRequired()],
        choices=[
            ('1'),
            ('2'),
            ('3'),
            ('4'),
            ('5')
        ]
    )
    cost = SelectField(
        'Cost (1 = cheap)',
        [DataRequired()],
        choices=[
            ('1'),
            ('2'),
            ('3')
        ]
    )
    temperature = IntegerField(
        'Printing Temperature',
        [DataRequired()]
    )
    colour = StringField(
        'Colour',
        [DataRequired()]
    )
    finish = SelectField(
        'Finish',
        [DataRequired()],
        choices=[
            ('Standard'),
            ('Matte'),
            ('Silk'),
            ('Satin'),
            ('Glitter'),
            ('Glow in the dark'),
            ('Other')
        ]
    )
    review_text = StringField(
        'Review text',
        [
            DataRequired(),
            Length(
                max=250,
                message="Please keep reviews short and concise (250 char max)."
                )
        ]
    )
    image_url = StringField(
        'Image URL',
        [DataRequired(message="Need to upload an image? Try Imgur!")]
    )
    submit = SubmitField('Submit')


class SearchForm(FlaskForm):
    """Search Reviews"""
    query = StringField(
        'Search Query',
        [
            DataRequired(),
            Length(
                min=3,
                message="Minimum length of search is 3 characters."
                )
        ]
    )
    submit = SubmitField('Search')
