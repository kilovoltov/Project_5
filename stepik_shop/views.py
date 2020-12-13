import csv
import os
from functools import wraps

from flask import abort, flash, session, redirect, request, render_template

from stepik_shop import app, db
from stepik_shop.models import User, Category, Order, Meal
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
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


# admin = Admin(app)
# admin.add_view(ModelView(User, db.session))
# admin.add_view(ModelView(Order, db.session))
# admin.add_view(ModelView(Meal, db.session))
# admin.add_view(ModelView(Category, db.session))

@app.route('/fill-database/')
def to_db():
    """
    Используется для первоначального импорта данных в таблицы БД
    """
    category_rows = []
    with open('stepik_shop/data/delivery_categories.csv') as f:
        reader = csv.DictReader(f)
        for line in reader:
            category_rows.append(Category(title=line['title']))
    db.session.add_all(category_rows)
    db.session.commit()

    meals = []
    with open('stepik_shop/data/delivery_items.csv') as f:
        reader = csv.DictReader(f)
        for line in reader:
            meals.append(Meal(title=line['title'],
                              price=int(line['price']),
                              description=line['description'],
                              picture=line['picture'],
                              category_id=int(line['category_id'])))
    db.session.add_all(meals)
    db.session.commit()
    return "Данные записаны в БД"
