from flask import Flask, render_template, url_for, flash, request, redirect
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "TeeMak"

@app.route('/', methods=["GET", "POST"])
def index():
    form = RegistrationForm()

    if form.validate_on_submit():
        return redirect(url_for('success', username=form.username.data))

    return render_template('index.html', title="Signup", form=form)

@app.route('/success/<string:username>')
def success(username):
    return render_template('success.html', username=username)

if __name__ == "__main__":
    app.run()
