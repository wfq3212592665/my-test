from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import Length, EqualTo, Email


class LOGIN(Form):
    username = StringField(validators=[Length(min=3, max=20, message='用户名长度必须为3-16')])
    password = StringField(validators=[Length(min=6, max=20, message='密码长度必须为6-20')])
    email = StringField(validators=[Length(min=3, max=20, message='邮箱长度必须为不能大于20')])
