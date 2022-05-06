from flask import Flask

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/coding')
def coding_dojo():
    return 'Dojo'

@app.route('/hi/<string:name>')
def hello(name):
    return f'Hi {name}'

@app.route('/repeat/<string:word><int:times>')
def repeater(word, times):
    return (word * times)

if __name__ == "__main__":
    app.run(debug=True)