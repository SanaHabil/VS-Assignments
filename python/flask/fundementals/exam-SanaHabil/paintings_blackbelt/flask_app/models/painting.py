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
        self.quantity = data['quantity']
        self.painter_id = data['painter_id']
        self.buyer_id = data['buyer_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.buyer = data['buyer']
        self.buyer_last_name = data['buyer_last_name']
        self.painter = data['painter']
        self.number_purchased = data['number_purchased']
        self.painter_last_name = data['painter_last_name']

    @classmethod
    def get_all_paintings(cls):
        query = "SELECT users.first_name as painter, users.last_name as painter_last_name, users2.first_name as buyer, users2.last_name as buyer_last_name, paintings.* FROM users JOIN paintings ON users.id = paintings.painter_id LEFT JOIN users as users2 ON users2.id = paintings.buyer_id;"
        results = connectToMySQL('paintings_blackbelt_schema').query_db(query)
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
        if  int(data['quantity']) == 0:
            flash("Quantity must be greater than 0.","update")
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
        if  int(data['quantity']) == 0:
            flash("Quantity must be greater than 0.","update")
            is_valid = False 
        return is_valid



    @classmethod
    def add_painting(cls, data):
        query = "INSERT INTO paintings (title, description, price, quantity,number_purchased, painter_id, buyer_id, created_at, updated_at) VALUES (%(title)s,%(description)s,%(price)s,%(quantity)s,%(number_purchased)s, %(painter_id)s,%(buyer_id)s,NOW(),NOW());"
        result = connectToMySQL('paintings_blackbelt_schema').query_db(query,data)
        return result
    @classmethod
    def buy_painting(cls,data):
        query = "UPDATE paintings SET quantity=%(quantity)s, number_purchased=%(number_purchased)s, buyer_id =%(buyer_id)s, painter_id=%(painter_id)s, updated_at=NOW() WHERE id = %(id)s;"
        result = connectToMySQL('paintings_blackbelt_schema').query_db(query,data)    

    
    @classmethod
    def show_one_painting(cls,data):
        query ="SELECT users.first_name as painter, users.last_name as painter_last_name, users2.first_name as buyer, users2.last_name as buyer_last_name, paintings.* FROM users LEFT JOIN paintings ON users.id = paintings.painter_id LEFT JOIN users as users2 ON users2.id = paintings.buyer_id WHERE paintings.id = %(id)s;"
        results = connectToMySQL('paintings_blackbelt_schema').query_db(query,data)
        this_painting = cls(results[0])
        return this_painting

    @classmethod
    def update_one_painting(cls,data):
            query = "UPDATE paintings SET title=%(title)s, description=%(description)s, price=%(price)s, quantity=%(quantity)s, updated_at=NOW() WHERE id = %(id)s;"
            return connectToMySQL('paintings_blackbelt_schema').query_db(query,data)

    @classmethod
    def delete(cls, id):
        query  = f"DELETE FROM paintings WHERE id = {id};"
        return connectToMySQL('paintings_blackbelt_schema').query_db(query)         