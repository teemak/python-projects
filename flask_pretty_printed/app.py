from flask import Flask, jsonify, request, render_template, redirect, url_for
app = Flask(__name__)

languages = [
    {'name': 'JavaScript'},
    {'name': 'Python'},
    {'name': 'Java'}
]

@app.route('/')
def index():
    return redirect(url_for('render_languages'))

@app.route('/languages', methods=["GET"])
def render_languages():
    return render_template('add.html', languages=languages)

@app.route('/languages/<string:name>')
def render_language(name):
    result = [language for language in languages if language['name'] == name]
    if result:
        return jsonify({ 'language': result[0] })
    return 'Language not found'

@app.route('/api/add_language', methods=["POST"])
def add_language():
    language = {'name': request.form['new_language']}
    languages.append(language)
    return redirect(url_for('render_languages'))

@app.route('/api/edit_language')
def edit_language():
    return render_template('edit.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
