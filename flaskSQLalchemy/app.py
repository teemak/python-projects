from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jxxghzyf:2Y4xDjk6rDFI2pFAMP0yT5EjlIn1e5nt@stampy.db.elephantsql.com:5432/jxxghzyf'

@app.route('/')
def index():
    return 'This is the index'

if __name__ == '__main__':
    app.run(debug=True)
