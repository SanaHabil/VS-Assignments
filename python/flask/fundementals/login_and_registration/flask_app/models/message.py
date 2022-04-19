from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
from flask_app.models import message
import re
from flask_bcrypt import Bcrypt
from datetime import datetime

class Message:
    def __init__( self , data ):
        self.id = data['id']
        self.sender = data['sender']
        self.sender_id = data['sender_id']
        self.receiver = data['receiver']
        self.receiver_id = data['receiver_id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def sending_time(self): 
        now =datetime.now()
        delta= now-self.created_at
        return delta       
    
    @classmethod
    def save_message(cls, data):
        query = "INSERT INTO messages (sender_id, receiver_id, content) VALUES (%(sender_id)s,%(receiver_id)s,%(content)s);"
        results = connectToMySQL('login_schema').query_db(query,data)
        return results

    @classmethod
    def get_user_messages(cls, data):
        query = "SELECT users.first_name as sender, users2.first_name as receiver, messages.* FROM users LEFT JOIN messages ON users.id = messages.sender_id LEFT JOIN users as users2 ON users2.id = messages.receiver_id WHERE users2.id= %(id)s;"  
        results = connectToMySQL('login_schema').query_db(query,data)
        messages = []
        for x in results:
            messages.append( cls(x) )
        return messages

    @classmethod
    def delete_message(cls, data):
        query = "DELETE FROM messages WHERE messages.id= %(id)s;"
        results = connectToMySQL('login_schema').query_db(query,data)
        return results