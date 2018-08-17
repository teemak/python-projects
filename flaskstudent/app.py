from flask import Flask, render_template, request, redirect, url_for
from student import Student

app = Flask(__name__)

students = [Student('Tee', 'Mak')]

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/students')
def index():
    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
