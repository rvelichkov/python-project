from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config 

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:def12345@localhost/app'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models here to ensure they are known to Flask-SQLAlchemy before creating tables
from .models import user

# Import and register Blueprints
#from .api import user_routes, recipe_routes, meal_plan_routes
#app.register_blueprint(user_routes.bp)
#app.register_blueprint(recipe_routes.bp)
#app.register_blueprint(meal_plan_routes.bp)

