from flask_wtf import Form
from wtforms import StringField, validators, PasswordField
from wtforms.fields.html5 import EmailField

class ResgisterForm(Form):
    first_name = StringField('', [validators.Required()])
    last_name = StringField('', [validators.Required()])
    email = EmailField('', [validators.DataRequired(), validators.Email()])
    username = StringField('', [
        validators.Required(),
        validators.length(min=4, max=25)
    ])
    password = PasswordField('', [
        validators.Required(),
        validators.length(min=4, max=80),
        validators.EqualTo('confirm', message="Password must match")
    ])
    confirm = PasswordField('')

class LoginForm(Form):
        username = StringField('', [
            validators.Required(),
            validators.length(min=4, max=25)
        ])
        password = PasswordField('', [
            validators.Required(),
            validators.length(min=4, max=80),
        ])
