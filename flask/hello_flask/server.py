from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/success')
def success():
    return "success"

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return f"Hello, {name}"

@app.route('/repeat/<string:banana><int:num>')
def repeater(banana, num):
    return render_template('hello.html', banana=banana, num=num)

if __name__ == "__main__":
    app.run(debug=True)