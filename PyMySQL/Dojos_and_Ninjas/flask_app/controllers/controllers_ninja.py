from flask import redirect, render_template, request
from flask_app import app
from flask_app.models.models_dojo import Dojo
from flask_app.models.models_ninja import Ninja

@app.route('/ninjas')
def ninjas_index():
    return render_template('ninjas.html', dojos = Dojo.get_all_dojos())

@app.route('/ninjas/create', methods=['POST'])
def ninja_create():
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age':request.form['age'],
        'dojo_id':request.form['dojos']
    }
    Ninja.create_ninja(data)
    return redirect('/dojos')