from crypt import methods
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import user
from flask_app.models import painting
from flask_bcrypt import Bcrypt


@app.route('/new_painting')
def new_painting():
    return render_template("add_painting.html")
    
@app.route('/paintings/new', methods=['POST'])
def all_painting():
    if 'user_id' not in session:
        return redirect('/reset')
    data = {
        "title": request.form['title'],
        "description": request.form['description'],
        "price": int(request.form['price']),
        "user_id" : request.form['user_id'],
        }
    if not painting.Painting.validate_painting_on_submit(data):
        # we redirect to the template with the form.
        return redirect('/new_painting')        
    painting.Painting.add_painting(data)
    return redirect('/results')

@app.route('/paintings/<int:id>')
def view_details_page(id):
    if 'user_id' not in session:
        return redirect('/reset')
    painting_data={
            'id': id
    }
    data ={
        'id': session['user_id']
    } 
    print(data)

    return render_template("view_details.html",current_user = user.User.show_user(data), one_painting = painting.Painting.show_one_painting(painting_data))


@app.route('/user_painting')
def paintings_show():
    
    return render_template("add_painting.html")

@app.route('/edit_painting/<int:id>')
def edit_painting(id):    
    if 'user_id' not in session:
        return redirect('/reset')
    painting_data={
            'id': id
    }
    data ={
        'id': session['user_id']
    } 
    
    return render_template("edit_painting.html",current_user = user.User.show_user(data), one_painting = painting.Painting.show_one_painting(painting_data))


@app.route("/paintings/edit/<int:id>", methods=['POST'])
def edit_one_painting(id):
    if 'user_id' not in session:
        return redirect('/reset')
    data = {
        "title": request.form['title'],
        "description": request.form['description'],
        "price": request.form['price'],
        "user_id" : request.form['user_id'],
        "id" : request.form['id'],

        }
    if not painting.Painting.validate_painting_on_update(data):
        # we redirect to the template with the form.
        return redirect(f'/edit_painting/{id}')       
    print(data)    
    painting.Painting.update_one_painting(data)
    return redirect('/results')

@app.route('/delete/<int:id>')
def delete_painting(id):
    painting.Painting.delete(id)
    return redirect('/results')

if __name__=="__main__":
    app.run(debug=True)
