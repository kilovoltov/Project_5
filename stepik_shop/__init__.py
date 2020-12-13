from flask import Flask
from flask_migrate import Migrate

from stepik_shop.config import Config
from stepik_shop.models import db, User, Order, Meal, Category

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
from stepik_shop.views import *
