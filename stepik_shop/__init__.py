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

if __name__ == '__main__':
    app.run()
