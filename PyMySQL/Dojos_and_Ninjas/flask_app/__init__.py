from flask import Flask
app = Flask(__name__)
app.secret_key = 'Dojos And Ninjas'
DATABASE = 'dojos_and_ninjas'