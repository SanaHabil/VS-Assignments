from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
from flask_app.models import user
import re
from flask_bcrypt import Bcrypt


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*?[A-Z])(?=(.*[\d]){1,}).{8,}$') 

class Painting:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.price = data['price']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.painter = data['painter']
        self.painter_last_name = data['painter_last_name']

    @classmethod
    def get_all_paintings(cls,data):
        query = "SELECT users.first_name as painter, users.last_name as painter_last_name, paintings.* FROM users LEFT JOIN paintings ON users.id = paintings.user_id;"
        results = connectToMySQL('paintings_schema').query_db(query,data)
        all_results = []
        for row in results:
            all_results.append( cls(row) )
        return all_results

    @staticmethod
    def validate_painting_on_submit(data):
        is_valid = True
        if  len(data['title']) < 2:
            flash(" Title must be at least 2 characters.","create")
            is_valid = False
        if  len(data['description']) < 10:
            flash("Description must be at least 10 characters.","create")
            is_valid = False
        if  int(data['price']) == 0:
            flash("Price must be greater than 0.","create")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_painting_on_update(data):
        is_valid = True
        if  len(data['title']) < 2:
            flash(" Title must be at least 2 characters.","update")
            is_valid = False
        if  len(data['description']) < 10:
            flash("Description must be at least 10 characters.","update")
            is_valid = False
        if  int(data['price']) == 0:
            flash("Price must be greater than 0.","update")
            is_valid = False
        return is_valid



    @classmethod
    def add_painting(cls, data):
        query = "INSERT INTO paintings (title, description, price, user_id, created_at, updated_at) VALUES (%(title)s,%(description)s,%(price)s,%(user_id)s,NOW(),NOW());"
        result = connectToMySQL('paintings_schema').query_db(query,data)
        return result

    
    @classmethod
    def show_one_painting(cls,data):
        query ="SELECT users.first_name as painter, users.last_name as painter_last_name, paintings.* FROM users LEFT JOIN paintings ON users.id = paintings.user_id WHERE paintings.id = %(id)s;"
        results = connectToMySQL('paintings_schema').query_db(query,data)
        this_painting = cls(results[0])
        return this_painting

    @classmethod
    def update_one_painting(cls,data):
            query = "UPDATE paintings SET title=%(title)s, description=%(description)s, price=%(price)s, updated_at=NOW() WHERE id = %(id)s;"
            return connectToMySQL('paintings_schema').query_db(query,data)

    @classmethod
    def delete(cls, id):
        query  = f"DELETE FROM paintings WHERE id = {id};"
        return connectToMySQL('paintings_schema').query_db(query)         