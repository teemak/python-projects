from flask import Flask, render_template

app = Flask(__name__)

foods = {
    'pizza': {
        'best': 'pepperoni',
        'second': 'brooklyn style',
        'last': 'hawaiian'
    },
    'Empanada': {
        'best': 'beef',
        'second': 'beef',
        'last': 'beef'
    },
    'Curry and naan': {
        'best': 'butter',
        'second': 'beef',
        'last': 'beef'
    },
    'Cola': {
        'best': 'butter',
        'second': 'beef',
        'last': 'beef'
    }
}

@app.route('/')
def index():
    title = "Favorite foods and drinks"
    foods_list = ['Pizza', 'Empanada', 'Curry and naan', 'Cola']

    return render_template('index.html', title=title, foods=foods_list)

@app.route('/foods')
def food():
    return render_template('foods.html')

if __name__ == '__main__':
    app.run()

