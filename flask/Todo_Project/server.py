from importlib.machinery import all_suffixes
from flask import Flask, render_template

app = Flask(__name__)

users = [{
    'first_name' : 'Alex',
    'last_name' : 'Miller',
    'id' : 12345
},
{
    'first_name' : 'John',
    'last_name' : 'Smith',
    'id' : 16587
},
{
    'first_name' : 'Patrick',
    'last_name' : 'Dempsey',
    'id' : 14725
}]

@app.route('/')
def home():
    first_name = 'Alex'
    last_name = 'Miller'
    num_list = [10,20,30,40,50]

    return render_template('index.html', first_name = first_name, last_name = last_name, num_list = num_list)

@app.route('/users', methods=['GET'])
def user():
    return render_template('users.html', users = users)

@app.route('/users/<int:user_id>')
def get_user_by_id(user_id):
    for user in users:
        if users['id'] == user_id:
            return render_template('userID.html', user = user, error_message=False, u_id = user_id)



if __name__ == "__main__":
    app.run(debug=True)