import os
import secrets
from PIL import Image
from flask import render_template, flash, redirect, url_for, request
from blogz import app, db, bcrypt
from blogz.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from blogz.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

blogs = [
    {
        'author': 'Tee Mak',
        'title': 'Flask',
        'content': 'Using the framework with Python',
        'date_posted': 'Oct 8, 2018'
    },
    {
        'author': 'Erza',
        'title': 'Dogs',
        'content': 'I am a spoiled dog.',
        'date_posted': 'Oct 18, 2018'
    }
]

@app.route('/')
def index():
    return render_template("index.html", blogs=blogs)

@app.route('/posts')
def posts():
    return render_template("posts.html", blogs=blogs)

@app.route('/add_post', methods=["GET", "POST"])
@login_required
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        flash('Your post has been created')
        return redirect(url_for('index'))
    return render_template("add_post.html", title="New Post", form=form)

@app.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    #Create instance of RegistrationForm class
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Please login for {form.username.data}.')
        return redirect(url_for('login'))
    #Pass instance to render_template
    return render_template("register.html", title="Register", form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        #Find if account exists
        user = User.query.filter_by(username=form.username.data).first()
        #User exists then compare passwords = user.password is database password
        #form.password.data is the one that is being sent
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash(f'Login Unsuccessful. Check username and password')
    return render_template("login.html", title="Login", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(2)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)

    #Reduce image resolution
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route('/account', methods=["GET", "POST"])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.add(current_user)
        db.session.commit()
        flash('Your account has been updated')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename=f'images/{current_user.image_file}')
    return render_template('account.html', title="Account", form=form, image_file=image_file)
