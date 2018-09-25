from flask import Flask, render_template, url_for, request
from caesar import rotate_string

app = Flask(__name__)

main = '''
<!DOCTYPE html>
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <form method="post" action="/encrypt">
                <label for="name">ROTATION</label>
                <input name="rot" type="text"></input>
                <textarea name="text">{text}</textarea>
                <button type="submit">Submit</button>
            </form>
            <a href="/">HOME</a>
        </body>
    </html>
'''
@app.route('/')
def index():
    text = ''
    return main.format(text=text)

@app.route('/encrypt', methods=["POST"])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    result = rotate_string(text, int(rot))
    return main.format(text=result)

if __name__ == "__main__":
    app.run()
