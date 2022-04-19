from crypt import methods
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import user
from flask_app.models import recipe
from flask_bcrypt import Bcrypt


@app.route('/new_recipe')
def new_recipe():
    return render_template("add_recipe.html")    

@app.route('/recipes/new', methods=['POST'])
def all_recipe():
    if 'user_id' not in session:
        return redirect('/reset')
    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "made_at" : request.form['made_at'],
        "under_30_min" : request.form['under_30_min'],
        "user_id" : request.form['user_id'],
        }
    if not recipe.Recipe.validate_recipe_on_submit(data):
        # we redirect to the template with the form.
        return redirect('/new_recipe')        
    recipe.Recipe.add_recipe(data)
    return redirect('/results')

@app.route('/recipes/<int:id>')
def view_instructions_page(id):
    if 'user_id' not in session:
        return redirect('/reset')
    recipe_data={
            'id': id
    }
    data ={
        'id': session['user_id']
    } 
    print(data)
    return render_template("view_instructions.html",current_user = user.User.show_user(data), one_recipe = recipe.Recipe.show_one_recipe(recipe_data))


@app.route('/user_recipes')
def recipes_show():
    
    return render_template("add_recipe.html")

@app.route('/edit_recipe/<int:id>')
def edit_recipe(id):    
    if 'user_id' not in session:
        return redirect('/reset')
    recipe_data={
            'id': id
    }
    data ={
        'id': session['user_id']
    } 
    
    return render_template("edit_recipe.html",current_user = user.User.show_user(data), one_recipe = recipe.Recipe.show_one_recipe(recipe_data))


@app.route("/recipes/edit/<int:id>", methods=['POST'])
def edit_one_recipe(id):
    if 'user_id' not in session:
        return redirect('/reset')
    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "made_at" : request.form['made_at'],
        "under_30_min" : request.form.get('under_30_min'),
        "user_id" : request.form['user_id'],
        "id" : request.form['id'],

        }
    if not recipe.Recipe.validate_recipe_on_update(data):
        # we redirect to the template with the form.
        return redirect(f'/edit_recipe/{id}')       
    print(data)    
    recipe.Recipe.update_one_recipe(data)
    return redirect('/results')

@app.route('/delete/<int:id>')
def delete_recipe(id):
    recipe.Recipe.delete(id)
    return redirect('/results')

if __name__=="__main__":
    app.run(debug=True)
