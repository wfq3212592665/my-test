from flask import Blueprint, request, render_template
from models import User
from exts import db
from forms import LOGIN

bp_tai = Blueprint('kuyue_tai', __name__, url_prefix='/tai/', static_folder='static', template_folder='templates')


@bp_tai.route('/regist/', method=['GET', 'POST'])
def Regist():
    if request.method == 'GET':
        render_template('register.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        user = User(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()


@bp_tai.route('/login/')
def Login():
    if request.method == 'GET':
        render_template('login.html')
    else:
        LOGIN.username.data == request.form.get('username')

