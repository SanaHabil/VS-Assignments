from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_bcrypt import Bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*?[A-Z])(?=(.*[\d]){1,}).{8,}$') 

class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30_min = data['under_30_min']
        self.made_at = data['made_at']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_recipe_on_submit(data):
        is_valid = True
        if  len(data['name']) < 3:
            flash(" Name must be at least 3 characters.","create")
            is_valid = False
        if  len(data['description']) < 3:
            flash("Description must be at least 3 characters.","create")
            is_valid = False
        if  len(data['instructions']) < 3:
            flash("Instructions must be at least 3 characters.","create")
            is_valid = False
        if len(data['made_at']) == 0:
            flash("Add Date Made","create")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_recipe_on_update(data):
        is_valid = True
        if  len(data['name']) < 3:
            flash(" Name must be at least 3 characters.","update")
            is_valid = False
        if  len(data['description']) < 3:
            flash("Description must be at least 3 characters.","update")
            is_valid = False
        if  len(data['instructions']) < 3:
            flash("Instructions must be at least 3 characters.","update")
            is_valid = False
        if len(data['made_at']) == 0:
            flash("Add Date Made","update")
            is_valid = False
        return is_valid

    @classmethod
    def add_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, made_at, user_id, under_30_min, created_at, updated_at) VALUES (%(name)s,%(description)s,%(instructions)s,%(made_at)s,%(user_id)s,%(under_30_min)s,NOW(),NOW());"
        result = connectToMySQL('recipes_schema').query_db(query,data)
        return result

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('recipes_schema').query_db(query)
        all_recipes = []
        for recipe in results:
            all_recipes.append(cls(recipe))
        return all_recipes

    @classmethod
    def show_one_recipe(cls,data):
        query ="SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL('recipes_schema').query_db(query,data)
        this_recipe = cls(results[0])
        return this_recipe

    @classmethod
    def update_one_recipe(cls,data):
            query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, under_30_min=%(under_30_min)s, made_at=%(made_at)s, updated_at=NOW() WHERE id = %(id)s;"
            return connectToMySQL('recipes_schema').query_db(query,data)

    @classmethod
    def delete(cls, id):
        query  = f"DELETE FROM recipes WHERE id = {id};"
        return connectToMySQL('recipes_schema').query_db(query)         