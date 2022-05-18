from flask import flash, redirect, render_template, request, session
from flask_app import app
from flask_app.models.models_users import User
from flask_app.models.models_recipes import Recipe

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', user = User.get_user_by_id({'id': session['user_id']}), recipes = Recipe.get_all_recipes())

@app.route('/recipes/create')
def create_recipe():
    return render_template('new_recipe.html')

@app.route('/recipes/submit', methods=['POST'])
def add_recipe():

    Recipe.add_recipe({
        'name': request.form['recipe_name'],
        'recipe_description': request.form['recipe_description'],
        'recipe_instruction': request.form['recipe_instruction'],
        'recipe_date':request.form['recipe_date'],
        'under_30':request.form['under_30'],
        'user_id': session['user_id'],
    })
    return redirect('/dashboard')

@app.route('/recipes/<int:recipe_id>/edit')
def edit_recipe():
    return render_template('edit_recipe.html', recipes = Recipe.get_all_recipes())