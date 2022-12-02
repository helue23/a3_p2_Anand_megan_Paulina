from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
engine = app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///pos.db'
db = SQLAlchemy(app)

from my_app.catalog.routes import catalog
app.register_blueprint(catalog)

db.create_all()
