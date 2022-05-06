from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def main(number=8):
    num1 = int(number/2)
    num2 = int(number/2)
    return render_template('index.html', num1=num1, num2=num2)

@app.route('/choose/<int:number>')
def choose(number):
    num1 = int(number/2)
    num2 = int(number/2)
    return render_template('index.html', num1 = num1, num2=num2)


@app.route('/choose2/<int:num1>/<int:num2>')
def choose2(num1, num2):
    num1 = int(num1/2)
    num2 = int(num2/2)
    return render_template('index.html', num1=num1, num2=num2)


if __name__ == '__main__':
    app.run(debug=True)

