from functools import wraps

from flask import abort, flash, session, redirect, request, render_template

from stepik_shop import app, db
from stepik_shop.models import User
from stepik_shop.forms import *


# ------------------------------------------------------
# Декораторы авторизации
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print("login_required")
        if not session.get('user'):
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print("admin_only")
        if session.get('user')["role"] != "admin":
            abort(403, description="Вам сюда нельзя")
        return f(*args, **kwargs)
    return decorated_function


# ------------------------------------------------------
# Главная страница
@app.route('/')
def home():
    return render_template("main.html")


@app.route('/cart/')
def cart():
    return render_template("cart.html")


@app.route('/account/')
def account():
    return render_template("account.html")


@app.route('/auth/')
def auth():
    return render_template("auth.html")


@app.route('/ordered/')
def order():
    return render_template("ordered.html")


@app.route('/register/')
def register():
    return render_template("login.html")


@app.route('/logout/')
def logout():
    return render_template("login.html")
