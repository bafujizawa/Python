import random
from flask import Flask, render_template, session, request
app = Flask(__name__)
app.secret_key = 'Number Game'
guessedNumbers = []


@app.route('/', methods=['GET', 'POST'])
def index():
    
    if 'random' not in session:
        session['random'] = random.randint(1, 100)
    print(session['random'])
    return render_template('index.html')
    
@app.route('/guess', methods=['GET', 'POST'])
def guess():
    display = ''
    session['guess'] = int(request.form['guess'])
    guessedNumbers.append(session['guess'])
    if session['guess'] > session['random']:
        display = 'Your guess is too high'
    elif session['guess'] < session['random']:
        display = 'Your guess is too low'
    else:
        display = f"{session['guess']} was the number"
        session.pop('guess')
    return render_template('index.html', display = display, guessedNumbers = guessedNumbers)

if __name__ == '__main__':
    app.run(debug=True)