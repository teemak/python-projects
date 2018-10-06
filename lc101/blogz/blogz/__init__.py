from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ASDF'
user = 'wjgzgrgf'
pw = 'UPPylyT1N-tDr29wk7hvCV-d3N1qOdzB'
server = 'pellefant.db.elephantsql.com'
port = 5432
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgres://{user}:{pw}@{server}:{port}/{user}'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
#Value is the name of function -- Sends user if not logged in
login_manager.login_view = 'login'
#Style for flash message to warn user 
login_manager.login_message_category = "info"

from blogz import routes
