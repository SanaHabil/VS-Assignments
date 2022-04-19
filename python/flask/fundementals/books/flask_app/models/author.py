from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author
from flask_app.models import book
from flask import flash

class Author:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # We create a list so that later we can add in all the ninjas that are associated with a dojo.
        self.books = []


    @classmethod
    def get_all(cls):
            query = "SELECT * FROM authors;"
            # make sure to call the connectToMySQL function with the schema you are targeting.
            results = connectToMySQL('books_schema').query_db(query)
            authors = []
            for author in results:
                authors.append( cls(author) )
            return authors

    @classmethod    
    def add_author(cls, data):
            query = "INSERT INTO authors ( name , created_at , updated_at ) VALUES (%(name)s,NOW(),NOW());"
            result = connectToMySQL('books_schema').query_db(query,data)
            return result  

    @classmethod    
    def show_one_author(cls, data):
            query ="SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"
            results = connectToMySQL('books_schema').query_db(query,data)

            author = cls(results[0])

            for row_from_db in results:
                if row_from_db['books.id'] == None:
                    break
                data = {
                        "id" : row_from_db['books.id'],
                        "title" : row_from_db['title'],
                        "pages" : row_from_db['pages'],
                        "created_at" : row_from_db['books.created_at'],
                        "updated_at" : row_from_db['books.updated_at']
                }
                author.books.append(book.Book(data))
            return author

    @classmethod
    def unfavorited_authors(cls,data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s );"
        authors = []
        results = connectToMySQL('books_schema').query_db(query,data)
        for x in results:
            authors.append(cls(x))
        return authors

    @classmethod
    def add_favorite(cls,data):
        query = "INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        return connectToMySQL('books_schema').query_db(query,data)
    
    @staticmethod
    def validate_author(author):
        is_valid = True # we assume this is true
        if len(author['name']) < 2:
            flash(" Author name must be at least 2 characters.")
            is_valid = False
        return is_valid