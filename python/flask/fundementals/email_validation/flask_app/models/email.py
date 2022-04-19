from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email_address = data['email_address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']        


    @staticmethod
    def validate_email(data):
        query=query = "SELECT * FROM emails WHERE email_address=%(email_address)s;"
        result = connectToMySQL('emails_schema').query_db(query,data)
        is_valid = True
        if len(result) >= 1:
            flash("Email Address is in use!")
            is_valid = False
        elif not EMAIL_REGEX.match(data['email_address']): 
            flash("Invalid email address!")
            is_valid = False 
        else:
            flash(f"The Email Address you entered {data['email_address']} is a valid Email Address")    
        return is_valid


    @classmethod
    def add_email(cls, data):
        query = "INSERT INTO emails (email_address , created_at , updated_at) VALUES (%(email_address)s,NOW(),NOW());"
        result = connectToMySQL('emails_schema').query_db(query,data)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL('emails_schema').query_db(query)
        emails = []
        for email in results:
            emails.append(cls(email) )
        return emails

    @classmethod
    def delete_email(cls, id):
        query  = f"DELETE FROM emails WHERE id = {id};"
        return connectToMySQL('emails_schema').query_db(query)