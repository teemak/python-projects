from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TeeMak'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jxxghzyf:2Y4xDjk6rDFI2pFAMP0yT5EjlIn1e5nt@stampy.db.elephantsql.com:5432/jxxghzyf'
db = SQLAlchemy(app)

from app import routes
