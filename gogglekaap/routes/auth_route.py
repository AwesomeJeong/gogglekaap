from flask import Blueprint, render_template, redirect, flash, url_for, session, request
from gogglekaap.forms.auth_form import LoginForm, RegisterForm
from werkzeug import security

NAME = "auth"
bp = Blueprint(NAME, __name__, url_prefix="/auth")

''' only for testing '''
from dataclasses import dataclass
USERS = []

@dataclass
class User:
    '''
        class User:
            def __init__(self, user_id, user_name, password):
                self.user_id = user_id
                self.user_name = user_name
                serl.password = password
    '''
    user_id: str
    user_name: str
    password: str

USERS.append(User("awesome", "AWESOME", security.generate_password_hash("1234")))
USERS.append(User("admin", "ADMIN", security.generate_password_hash("1234")))
USERS.append(User("tester", "TESTER", security.generate_password_hash("1234")))

print(USERS)

@bp.route("/")
def index():
    return redirect(url_for(f"{NAME}.login"))

@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    # POST, validate OK!
    if form.validate_on_submit():
        # TODO:
        # 1) 유저조회
        # 2) 유저 이미 존재하는지 체크
        # 3) 없으면 유저 생성
        # 4) 로그인 유지(세션)

        user_id = form.data.get("user_id")
        password = form.data.get("password")
        user = [user for user in USERS if user.user_id == user_id]
        if user:
            user = user[0]
            if not security.check_password_hash(user.password, password):
                flash("Password is not valid.")
            else:
                session["user_id"] = user_id
                return redirect(url_for("base.index"))
        else:
            flash("User ID is not exists.")
    else:
        flash_form_errors(form)
    return render_template(f"{NAME}/login.html", form=form)

@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # TODO:
        # 1) 유저조회
        # 2) 유저 이미 존재하는지 체크
        # 3) 없으면 유저 생성
        # 4) 로그인 유지(세션)
        user_id = form.data.get("user_id")
        user_name = form.data.get("user_name")
        password = form.data.get("password")
        repassword = form.data.get("repassword")
        user = [user for user in USERS if user.user_id == user_id]
        if user:
            flash("User ID is already exists.")
            return redirect(request.path) # /register path 와 같음
        else:
            USERS.append(
                User(
                    user_id = user_id,
                    user_name = user_name,
                    password = security.generate_password_hash(password)
                )
            )
            session["user_id"] = user_id
            print(USERS)
            return redirect(url_for("base.index"))
    else:
        flash_form_errors(form)
    return render_template(f"{NAME}/register.html", form=form)

@bp.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for(f"{NAME}.login"))

def flash_form_errors(form):
    for _, errors in form.errors.items():
        for e in errors:
            flash(e)