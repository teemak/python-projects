from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/information')
def info():
    return "<h1>Puppies are cute!</h1>"

@app.route('/variables')
def variables():
    name = 'Tee'
    letters = list(name)
    pup_dict = {'pup_name': 'Erza'}
    return render_template('variables.html', my_variable=name,
        letters=letters, pup_dict=pup_dict)

@app.route("/puppy/<name>")
##URL param gets passed as an argument to puppy function
def puppy(name):
    #print(type(name)) == <class 'str'>
    #return "<h1>This is a page for {}</h1>".format(name.upper())
    #return "<h1>{}</h1>".format(name[100])
    if(name[-1] == 'y'):
        return name[:-1] + "iful"
    else:
        return name + "y"

if __name__ == "__main__":
    app.run()
