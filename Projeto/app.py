from flask import Flask
from blueprints.clientsRoutes import api
from database import db, migrate
from config import config

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = config["DB_CONNECTION"]+'://'+config["DB_USERNAME"] + \
    ':'+config["DB_PASSWORD"]+'@'+config["DB_HOST"]+'/'+config["DB_DATABASE"]
db.init_app(app)
migrate.init_app(app, db)
app.register_blueprint(api)
