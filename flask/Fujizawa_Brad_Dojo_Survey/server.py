from flask import Flask, render_template, session, request, redirect, url_for
app = Flask(__name__)
app.secret_key = 'Survey'


@app.route('/')
def index():
    session.pop('comments', None)
    is_comments = False
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['locations']
    session['fav_language'] = request.form['fav_language']
    session['comments'] = request.form['comments']
    return redirect('/result')
    

@app.route('/result')
def result():
    if len(session['comments']) > 0:
        is_comments = True
        return render_template('result.html', name = session['name'], location = session['location'], fav_language = session['fav_language'], comments = session['comments'], is_comments=is_comments)
    else:
        return render_template('result.html', name = session['name'], location = session['location'], fav_language = session['fav_language'], comments = session['comments'])
    # try:
    #     session['comments'] = request.form['comments']
    #     is_comments = True
    #     print(session['is_comments'])
    #     return render_template('result.html', name = session['name'], location = session['location'], fav_language = session['fav_language'], comments = session['comments'], is_comments=is_comments)
    # except KeyError:
    #     return render_template('result.html', name = session['name'], location = session['location'], fav_language = session['fav_language'], comments = session['comments'])
    print()
    


if __name__ == '__main__':
    app.run(debug=True)