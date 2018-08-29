from flask import Flask, render_template, session, redirect, url_for
#FlaskForm class 
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
    RadioField, SelectField, TextField, TextAreaField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "asdfasdf"

class InfoForm(FlaskForm):
    breed = StringField("What breed are you?", validators=[DataRequired()])
    spayed = BooleanField("Have you been spayed?")
    mood = RadioField("Please choose your mood: ", choices=[('mood_one', 'happy'), ('mood_two','hungry')])
    food = SelectField(u"Pick your favorite food: ", choices=[('chi','Chicken'),('bf','Beef'),('pz','Pizza')])
    feedback = TextAreaField()
    submit = SubmitField("Submit")

@app.route('/', methods=["GET","POST"])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['spayed'] = form.spayed.data
        session['mood'] = form.mood.data
        session['food'] = form.food.data
        session['feedback'] = form.feedback.data
        return redirect(url_for("thankyou"))

    return render_template('index.html', form=form)

@app.route('/thankyou')
def thankyou():
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run()
