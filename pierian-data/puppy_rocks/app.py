from flask import Flask, render_template, request, url_for
import re
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/thank_you')
def thank_you():
    lower_char = False
    upper_char = False
    digit_char = False
    name = request.args.get('name')
    #Check for lowercase
    lower_char = any(char.islower() for char in name)
    #check for uppercase
    upper_char = any(char.isupper() for char in name)
    #Check for digit
    digit_char = bool(re.search(r'\d',name))
    if lower_char and upper_char and digit_char:
        return render_template('thank_you.html', name=name)
    else:
        return render_template('not_valid.html', lower_char=lower_char,
            upper_char=upper_char, digit_char=digit_char)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == "__main__":
    app.run()
