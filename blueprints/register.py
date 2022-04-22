from flask import Blueprint,request,redirect,url_for,render_template
from werkzeug.security import generate_password_hash
from .forms import RegisterForm
from model import db,UserModel

bp = Blueprint('user',__name__,url_prefix='/user')

@bp.route('/register',methods=['POST','GET'])
def register():
    form = RegisterForm(request.form)
    if form.validate():
        username =form.username.data
        password =form.password.data

        hash_password = generate_password_hash(password)

        user = UserModel(username=username,password=hash_password)
        print(user)
        db.session.add(user)
        db.session.commit()
        # return redirect(url_for("user.login"))
        return render_template("index.html")
    else:
        # return redirect(url_for("user.register"))
        return render_template("register.html")