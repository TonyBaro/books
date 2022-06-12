from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []
    
    @classmethod
    def retrieve_all_authors(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books').query_db(query)
        authors = []
        for author in results:
            authors.append( cls(author) )
        return authors

    @classmethod
    def add_author(cls,data):
        query="INSERT INTO authors(name) VALUES (%(name)s)"
        return connectToMySQL('books').query_db( query, data )
# 0
    @classmethod
    def retrieve_author(cls,data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = (%(author_id)s)"
        results = connectToMySQL('books').query_db(query , data)
        print(results)
        dojo = cls(results[0])
        return