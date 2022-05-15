from flask import redirect, render_template, request, flash, session
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.models_user import User

@app.route('/')
@app.route('/users')
def index():
    if not User.validate_user(session):
        return render_template('index.html')
    else:
        return redirect('/users/welcome')

@app.route('/users/register', methods=['GET', 'POST'])
def register_user():
    if not User.validate_registration(request.form):
        return redirect('/')
    if len(request.form['password']) > 0:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
    else:
        flash('Password must be greater than 0')
        return redirect('/users')

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }
    User.register_user(data)
    return redirect('/')


@app.route('/users/welcome')
def welcome_user():
    if User.validate_user(session):
        user = User.get_user_by_id({'id':session['user_id']})
        print(user)
        return render_template('welcome_user.html', user = user)
    else:
        return redirect('/')

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    if User.validate_user(session):
        user = User.get_user_by_id({'id':user_id})
        return render_template('edit_user.html', user = user)
    else:
        return redirect('/')

@app.route('/users/login', methods=['GET', 'POST'])
def user_login():
    data = {'email':request.form['login_email']}
    user_in_db = User.get_user_by_email(data)
    if not user_in_db:
        flash('Invalid Email/Password')
        return redirect('/users')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['login_password']):
        flash('Invalid Email/Password')
        return redirect('/users')
    session['user_id'] = user_in_db.id
    return redirect('/users/welcome')

@app.route('/users/update', methods=['POST'])
def update():
    user_id = session['user_id']
    
    if User.validate_user(session):
        if User.validate_registration(request.form):
            data = {
            'id':session['user_id'],
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'email':request.form['email'],
            'password':bcrypt.generate_password_hash(request.form['password'])
            }
            User.update_user(data)
            return redirect('/users')
        else:
            return redirect(f'/users/{user_id}/edit')
        

@app.route('/users/logout')
def logout():
    session.pop('user_id')
    return redirect('/users')