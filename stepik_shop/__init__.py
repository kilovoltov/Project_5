import csv
from flask import Flask
from flask_admin import Admin
from flask_migrate import Migrate
from flask_admin.contrib.sqla import ModelView

from stepik_shop.config import Config
from stepik_shop.models import db, User, Order, Meal, Category

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

admin = Admin(app)
# admin.add_view(ModelView(User, db.session))
# admin.add_view(ModelView(Order, db.session))
# admin.add_view(ModelView(Meal, db.session))
# admin.add_view(ModelView(Category, db.session))

from stepik_shop.views import *


def to_db():
    """
    Используется для первоначального импорта данных в таблицы БД
    """
    with open(__name__ + '/data/delivery_categories.csv') as f:
        reader = csv.DictReader(f)
        # for line in reader:
            # print(line)

    with open(__name__ + '/data/delivery_items.csv') as f:
        reader = csv.DictReader(f)
        # for line in reader:
            # print(line)

    with open(__name__ + '/data/meals.csv') as f:
        reader = csv.DictReader(f)
        for line in reader:
            print(line)
    # for k, v in goals.items():
    #     goals_rows.append(Goal(key=k, title=v))
    # db.session.add_all(goals_rows)
    # db.session.commit()
    #
    # with open('teachers.json') as f:
    #     teachers = json.load(f)
    #
    # for teacher in teachers:
    #     teacher_goals = db.session.query(Goal).filter(Goal.key.in_(teacher['goals'])).all()
    #     row = Teacher(name=teacher['name'],
    #                   about=teacher['about'],
    #                   rating=teacher['rating'],
    #                   picture=teacher['picture'],
    #                   price=teacher['price'],
    #                   free=teacher['free'])
    #     db.session.add(row)
    #     row.goals = teacher_goals
    #
    # db.session.commit()


if __name__ == '__main__':
    app.run()
