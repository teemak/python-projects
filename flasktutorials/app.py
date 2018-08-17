from flask import Flask, jsonify, request
app = Flask(__name__)

languages = [{'name': 'JavaScript'}, {'name': 'Python'}, {'name': 'Java'}]

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'It works'})

@app.route('/languages', methods=['GET'])
def returnAll():
    return jsonify({'languages': languages})

@app.route('/languages/<string:name>', methods=['GET'])
def returnOne(name):
    langs = [language for language in languages if language['name'] == name.lower()]
    return jsonify({'language': langs[0]})

if __name__ == '__main__':
    app.run()
