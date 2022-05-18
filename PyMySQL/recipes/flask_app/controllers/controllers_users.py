from flask import flash, redirect, render_template, request, session
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.models_users import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/register', methods=['POST'])
def register_user():
    if not User.validate_registration(request.form):
        return redirect('/')
    if User.get_user_by_email({'email':request.form['email']}):
        flash('Email address already exists', 'err_user_email')
        return redirect('/')

    User.register_user({
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['register_password'])})
    return redirect('/')
    
@app.route('/users/login', methods=['POST'])
def login():
    user_in_db = User.get_user_by_email({'email':request.form['login_email']})
    if not user_in_db:
        flash('Invalid Email Address/Password', 'err_login_attempt')
        return redirect('/users')
    if not bcrypt.check_password_hash(user_in_db['password'], request.form['login_password']):
        flash('Invalid Email Address/Password', 'err_login_attempt')
        return redirect('/users')

    session['user_id'] = user_in_db['id']
    return redirect('/dashboard')

