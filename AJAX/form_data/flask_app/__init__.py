from flask import Flask
app = Flask(__name__)
app.secret_key = "SHHHHH"
DATABASE = 'user_names'