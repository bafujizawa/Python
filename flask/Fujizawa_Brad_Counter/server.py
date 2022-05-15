from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'A secret'


@app.route('/')
def index():
    if 'visits' not in session:
        session['visits'] = 1
    else:
        session['visits'] = int(session['visits']) + 1
    return render_template('index.html', visits = session['visits'])

@app.route('/destroy_session')
def destroySession():
    session.pop('visits')
    return redirect('/')

@app.route('/add_two')
def add_two():
    # the 2nd is the refresh
    session['visits'] += 1
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
    
