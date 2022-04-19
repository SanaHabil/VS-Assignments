from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import author
from flask_app.models import book


@app.route('/authors')
def index():
        authors = author.Author.get_all()
        return render_template("authors.html", all_authors = authors)

@app.route('/add_author', methods=['POST'])
def add_author():

    if not author.Author.validate_author(request.form):
        # redirect to the route where the author form is rendered.
        return redirect("/authors")
    # else no errors:
    author.Author.add_author(request.form)
    return redirect('/authors')

@app.route('/books')
def show_books():
    books = book.Book.books_all()
    print(books)
    return render_template("books.html", all_books = books)


@app.route('/add_book', methods=['POST'])
def new_book():
    book_id= book.Book.add_book(request.form)
    return redirect(f"/book/{book_id}")


@app.route('/show_author')
def show_author():
    return render_template("show_author.html")

@app.route('/authors/<id>')
def show_one(id):
    data={
            "id": id
    }
    print(data)
    return render_template("show_author.html",select_one= author.Author.show_one_author(data),unfavorited_books=book.Book.unfavorited_books(data))

@app.route('/book/<id>')
def show_one_book(id):
    data={
            "id": id
         }
    return render_template("show_book.html",select_one=book.Book.show_one_book(data),unfavorited_authors=author.Author.unfavorited_authors(data))


@app.route('/join/author',methods=['POST'])
def join_author():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    author.Author.add_favorite(data)
    return redirect(f"/book/{request.form['book_id']}")

@app.route('/join/book',methods=['POST'])
def join_book():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    author.Author.add_favorite(data)
    return redirect(f"/authors/{request.form['author_id']}")


if __name__ == "__main__":
    app.run(debug=True)
