from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_bcrypt import Bcrypt


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*?[A-Z])(?=(.*[\d]){1,}).{8,}$') 
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email_address = data['email_address']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']        


    @staticmethod
    def validate_user(data):
        query = "SELECT * FROM users WHERE email_address=%(email_address)s;"
        result = connectToMySQL('recipes_schema').query_db(query,data)
        is_valid = True
        if len(result) >= 1:
            flash("Email Address is in use!","register")
            is_valid = False
        if not EMAIL_REGEX.match(data['email_address']): 
            flash("Invalid email address!","register")
            is_valid = False 
        if  len(data['first_name']) < 3:
            flash(" Name must be at least 2 characters.","register")
            is_valid = False
        if  len(data['last_name']) < 3:
            flash("Last Name must be at least 2 characters.","register")
            is_valid = False
        if  not PASSWORD_REGEX.match(data['password']):
            flash("PLease Choose a Password at least 8 characters, one Uppercase, and One number.", "register")
            is_valid = False
        if  data['password'] != data['confirm_password']:
            flash("Passwords don't match, try again!", "register")
            is_valid = False        
        return is_valid

    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email_address, password,created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,%(email_address)s,%(password)s,NOW(),NOW());"
        result = connectToMySQL('recipes_schema').query_db(query,data)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('login_schema').query_db(query)
        emails = []
        for email in results:
            emails.append(cls(email) )
        return emails

    @classmethod
    def show_user(cls, data):
        query = "SELECT * FROM users WHERE id= %(id)s ;"
        print(id)
        results = connectToMySQL('recipes_schema').query_db(query,data)
        return cls(results[0])
        
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email_address = %(email_address)s;"
        result = connectToMySQL('recipes_schema').query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])
