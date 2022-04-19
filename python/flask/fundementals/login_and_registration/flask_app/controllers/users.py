from email import message
from flask_app import app
from flask import render_template,redirect,request,session,flash
import datetime
from flask_bcrypt import Bcrypt
from flask_app.models import user
from flask_app.models.message import Message

bcrypt = Bcrypt(app)

app.secret_key = 'login and register'

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/register', methods=['POST'])
def register():
    if not user.User.validate_user(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    # ... do other things
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # put the pw_hash into the data dictionary
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email_address": request.form['email_address'],
        "password" : pw_hash,
        "confirm_password" : pw_hash,
    }
    # Call the save @classmethod on User
    id = user.User.add_user(data)
    # store user id into session
    session['user_id'] = id
    return redirect("/results")

@app.route('/results')
def show_results():
    if 'user_id' not in session:
        return redirect('/reset')
    data ={
        'id': session['user_id']
    } 
    current_user = user.User.show_user(data)
    messages = Message.get_user_messages(data)
    count = len(messages)
    users = user.User.get_all()
    return render_template("results.html",current_user = current_user, messages=messages, users=users, count=count)

@app.route('/reset')
def reset():
    session.clear()
    return redirect("/")

@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email_address" : request.form["email_address"] }
    user_in_db = user.User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password", "login")
        return redirect("/")
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect('/results')


@app.route('/send_message', methods=['POST'])
def send_message():
    data = { 'content' : request.form['content'], 
            'sender_id': request.form['sender_id'],
            'receiver_id': request.form['receiver_id']
            }
    if 'user_id' not in session:
        return redirect('/reset')
    Message.save_message(data)
    return redirect('/results')

@app.route('/delete_message/<int:id>')    
def delete(id):
    data = {
        'id':id
    }
    Message.delete_message(data)
    return redirect('/results')


if __name__=="__main__":
    app.run(debug=True)
