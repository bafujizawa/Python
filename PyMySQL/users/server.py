from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/users')


@app.route('/users')
def show_users():    
    users = User.get_all()
    return render_template('readall.html', users = users)

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

@app.route('/users/<int:number>')
def show_one(number):
    users = User.get_all()
    for user in users:
        if user.id == number:
            return render_template('readone.html', user = user)

@app.route('/users/delete')
def delete():
    User.delete()

if __name__ == '__main__':
    app.run(debug=True)