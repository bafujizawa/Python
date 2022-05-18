from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Recipe:
    
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.description = data['descriptions']
        self.instruction = data['instructions']
        self.recipe_date = data['recipe_date']
        self.under_30 = data['under_30']
        self.user_id = data['user_id']

    @classmethod
    def add_recipe(cls, data):
        
        query = 'INSERT INTO recipes(name, descriptions, instructions, recipe_date, under_30, user_id, created_at, updated_at) '
        query += 'VALUES (%(name)s, %(recipe_description)s, %(recipe_instruction)s, %(recipe_date)s, %(under_30)s, %(user_id)s, NOW(), NOW())'
        print(query)
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all_recipes(cls):
        query = 'SELECT * FROM recipes;'
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes