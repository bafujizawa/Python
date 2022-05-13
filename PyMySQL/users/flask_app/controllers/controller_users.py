from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.model_user import User

@app.route('/')
def home():
    return redirect('/users')

@app.route('/users')
def show_users():    
    
    return render_template('readall.html', users = User.get_all())

@app.route('/users/new')
def index():
    return render_template('create.html')

@app.route('/users/create', methods=["POST"])
def create_user():
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/users')

@app.route('/users/<int:user_id>')
def show_one(user_id):
    users = User.get_all()
    for user in users:
        if user.id == user_id:
            return render_template('readone.html', user = user)

@app.route('/users/<int:user_id>/delete')
def user_delete(user_id):
    User.delete({'id':user_id})
    return redirect('/')
    
@app.route('/users/<int:user_id>/edit')
def edit(user_id):
    users = User.get_all()
    for user in users:
        if user.id == user_id:
            return render_template('update.html', user = user)

@app.route('/users/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/')