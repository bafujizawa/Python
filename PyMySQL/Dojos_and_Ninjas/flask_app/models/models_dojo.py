from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Dojo():

    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = 'SELECT * FROM dojos'
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos(name, created_at, updated_at) '
        query += 'VALUES (%(new_dojo)s, NOW(), NOW())'
        print(query)
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one_dojo(cls, data):
        query = 'SELECT * FROM dojos '
        query += 'WHERE id = %(id)s'
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_ninjas(cls, data):
        query = 'SELECT * FROM dojos '
        query += 'LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id '
        query += 'WHERE dojos.id = %(id)s'
        print(query)
        return connectToMySQL(DATABASE).query_db(query, data)