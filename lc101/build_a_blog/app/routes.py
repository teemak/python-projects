from flask import Flask, render_template, url_for
from app import app
from app.models import Blog

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/add_blog')
def add_blog():
    return render_template('add_blog.html')

@app.route('/blog/<int:id>')
def blog():
    return render_template('blog.html');
