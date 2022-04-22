import wtforms
from  wtforms.validators import length,EqualTo

class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=3, max=20)])
    # email = wtforms.StringField(validators=[email()])
    # captcha = wtforms.StringField(validators=[length(min=4, max=4)])
    password = wtforms.StringField(validators=[length(min=6, max=16)])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])