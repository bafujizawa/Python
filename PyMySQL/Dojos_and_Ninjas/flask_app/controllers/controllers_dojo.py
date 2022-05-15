from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.models_dojo import Dojo


@app.route('/')
@app.route('/dojos')
def dojos_index():
    return render_template('dojos.html', dojos = Dojo.get_all_dojos())

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    Dojo.save({'new_dojo':request.form['new_dojo']})
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    print(dojo_id)
    data = {
        'id':dojo_id
    }
    ninjas = Dojo.get_ninjas(data)
    dojo = Dojo.get_one_dojo(data)
    print(ninjas)
    return render_template('showdojo.html', ninjas = ninjas)