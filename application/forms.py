from wtforms import Form, StringField, PasswordField, validators, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length


class SignupForm(Form):
    """User Signup."""

    name = StringField('Name', [
        validators.DataRequired(message=('Don\'t be shy!'))
    ])
    email = StringField('Email', [
        Length(min=6, message=(u'Little short for an email address?')),
        Email(message=('That\'s not a valid email address.')),
        DataRequired(message=('That\'s not a valid email address.'))
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message="Please enter a password."),
    ])
    confirm = PasswordField('Repeat Password', validators=[
            EqualTo(password, message='Passwords must match.')
            ])
    website = StringField('Website')
    submit = SubmitField('Register')


class LoginForm(Form):
    """User Login."""

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class addItems(Form):
    """Add items to roadmap."""

    add = SelectField(label="Add to your roadmap.")
    submit = SubmitField('OK')
