import csv
from flask import Flask
from flask_migrate import Migrate

from stepik_shop.config import Config
from stepik_shop.models import db, User, Order, Meal, Category

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
from stepik_shop.views import *


def to_db():
    """
    Используется для первоначального импорта данных в таблицы БД
    """
    item = Category(title='Test')
    print(item)
    db.session.add(item)
    # category_rows = []
    # print(os.getcwd())
    # with open(__name__ + '/data/delivery_categories.csv') as f:
    #     reader = csv.DictReader(f)
    #     for line in reader:
    #         category_rows.append(Category(title=line['title']))
    #         print(category_rows)
    # db.session.add_all(category_rows)
    # db.session.commit()
