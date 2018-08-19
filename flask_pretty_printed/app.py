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

@app.route('/api/edit_language/<string:name>', methods=["GET","POST"])
def edit_language(name):

    if request.method == "POST":
        language_to_update = [language for language in languages if language['name'] == name][0]
        updated_language = request.form['updated_language']
        language_to_update['name'] = updated_language

        return redirect(url_for('index'))

    return render_template('edit.html', language = name)

@app.route('/api/delete', methods=["POST"])
def delete(name):
    #language_to_delete = [language for language in languages if language['name'] == name][0]
    #print(language_to_delete)
    print('DELETE function run')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=3000)
