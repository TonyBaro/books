from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.authors import Author

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/authors')
def authors():
    authors=Author.retrieve_all_authors()
    print("authors are")
    print (authors)
    return render_template('authors.html', authors=authors)

@app.route('/add_author' , methods=["POST"])
def add_author():
    data={
        'name':request.form['name']
    }
    Author.add_author(data)
    return redirect('/authors')

@app.route('/author/<int:author_id>')
def show_one_author(author_id):
    data={
        'author_id':author_id
    }
    author = Author.retrieve_author(data)
    return render_template('author.html' , author = author)
