from flask import Flask, request, redirect, url_for, render_template
from student import Student

app = Flask(__name__)

students = []

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/students', methods=["GET", "POST"])
def index():
    return render_template('index.html', students=students)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
