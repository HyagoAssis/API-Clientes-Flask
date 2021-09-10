from flask import Flask
from blueprints.routes import api
from flask_migrate import Migrate
from database import db, migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:drb49f@localhost/prova'
db.init_app(app)
migrate.init_app(app, db)
app.register_blueprint(api)

