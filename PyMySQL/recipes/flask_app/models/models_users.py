from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []

    @classmethod
    def register_user(cls, data):
        
        query = 'INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) '
        query += 'VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW())'
        print(query)
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_user_by_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s'
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        return results[0]

    @classmethod
    def get_user_by_id(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s'
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        return results[0]

    @staticmethod
    def validate_registration(user):
        is_valid = True
        if(len(user['first_name']) < 3):
            flash('First name must be at least 3 characters', 'err_user_first_name')
            is_valid = False
        if(len(user['last_name']) < 3):
            flash('Last name must be at least 3 characters', 'err_user_last_name')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address', 'err_user_email')
            is_valid = False
        if(user['register_password'] != user['confirm_password']):
            flash('The passwords do not match', 'err_user_password')
            is_valid = False
        if len(user['register_password']) < 2:
            flash('Password is too short', 'err_user_password')
            is_valid = False
        return is_valid