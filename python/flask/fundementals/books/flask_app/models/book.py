from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book
from flask_app.models import author

class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.pages = data['pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors_who_favoraited=[]

    @classmethod
    def books_all(cls):
            query = "SELECT * FROM books;"
            results = connectToMySQL('books_schema').query_db(query)
            books = []
            for book in results:
                books.append( cls(book) )
            return books

    @classmethod    
    def add_book(cls, data):
            query = "INSERT INTO books (title, pages, created_at, updated_at) VALUES (%(title)s, %(pages)s,NOW(),NOW());"
            result = connectToMySQL('books_schema').query_db(query,data)
            return result

    @classmethod    
    def show_one_book (cls, data):
        query ="SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        result = connectToMySQL('books_schema').query_db(query,data)
        book = cls(result[0])

        for row_from_db in result:
            if row_from_db['authors.id']  == None:
                break 
            book_data = {
                        "id" : row_from_db["authors.id"],
                        "name" : row_from_db["name"],
                        "created_at" : row_from_db["authors.created_at"],
                        "updated_at" : row_from_db["authors.updated_at"]
                        
            }
            book.authors_who_favoraited.append(author.Author(book_data))
        return book

    @classmethod
    def unfavorited_books(cls,data):
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favorites WHERE author_id = %(id)s );"
        results = connectToMySQL('books_schema').query_db(query,data)
        books = []
        for row in results:
            books.append(cls(row))
        print(books)
        return books


    @classmethod
    def add_favorite(cls,data):
        query = "INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        return connectToMySQL('books_schema').query_db(query,data)
