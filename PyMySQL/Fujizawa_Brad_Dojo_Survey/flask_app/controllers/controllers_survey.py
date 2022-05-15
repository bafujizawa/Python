from flask_app.models.models_survey import Survey
from flask_app import app
from flask import session, request, render_template, redirect

@app.route('/')
def index():
    session.pop('comments', None)
    is_comments = False
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    if not Survey.validate_survey(session['name']):
        return redirect('/')
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