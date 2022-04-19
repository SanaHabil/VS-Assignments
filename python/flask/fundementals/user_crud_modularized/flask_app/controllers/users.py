from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

@app.route('/users')
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users = users)

@app.route('/add_new_user')
def add_new_user():
    return render_template("add_new_user.html")

@app.route('/user/new', methods=['POST'])    
def create():
    User.create_user(request.form)
    return redirect('/users/')

@app.route('/show_user')
def show_user():
    return render_template("show_user.html")

@app.route('/users/<id>')
def show_one(id):
    user=User.show_one_user(id)
    print(user)
    return render_template("show_user.html",user=user)

@app.route('/edit_user/<int:id>')
def edit_user(id):
    user=User.show_one_user(id)
    return render_template("edit_user.html", user=user)

@app.route('/edit/<id>', methods=['POST'])    
def edit(id):
    data = {
        "id": id,
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    User.update(data,id)
    return redirect('/users')


@app.route('/delete_user/<int:id>')
def delete_user(id):
    User.delete(id)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)
