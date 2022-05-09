from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'Survey'


@app.route('/')
def index():
    session['is_comments'] = False
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['locations']
    session['fav_language'] = request.form['fav_language']
    try:
        session['comments'] = request.form['comments']
        session['is_comments'] = True
        print(session['is_comments'])
        return redirect('/result')
    except KeyError:
        return redirect('/result')


@app.route('/result')
def result():
    return render_template('result.html', name = session['name'], location = session['location'], fav_language = session['fav_language'], comments = session['comments'], is_comments = session['is_comments'])


if __name__ == '__main__':
    app.run(debug=True)