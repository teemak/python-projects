from flask import Flask, render_template, url_for, request, redirect
from app import app, db
from app.models import Blog

@app.route('/', methods=['GET'])
def index():
    db.create_all()
    #GETS all the posts from db
    posts = Blog.query.all()
    return render_template('index.html', posts=posts)
    return render_template('index.html')

@app.route('/add_blog', methods=["GET", "POST"])
def add_blog():
    count = Blog.query.all()
    count = int(len(count))

    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        post = Blog(title=title, content=content)
        db.session.add(post)
        db.session.commit()
        #Link to specific post
        return redirect(url_for('blog',id=count+1))
    return render_template('add_blog.html')

@app.route('/blog/<int:id>')
def blog(id):
    #Query for post's id
    post = Blog.query.get(id)
    return render_template('blog.html', post=post);
