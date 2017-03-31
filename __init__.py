from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)

# migrations
Migrate = Migrate(app, db)

from user import views
from dashboard import views
