from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.books import Book

@app.route('/books')
def books():
    books=Book.retrieve_all_books()
    return render_template('books.html', books=books)

@app.route('/add_book' , methods=["POST"])
def add_book():
    data={
        'title':request.form['title'],
        'num_of_pages':request.form['num_of_pages']
    }
    Book.add_book(data)
    return redirect('/books')

