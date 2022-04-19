from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import dojo, ninja




@app.route('/ninjas')
def home():
    return render_template("ninjas.html", all_dojos= dojo.Dojo.get_all())

@app.route('/add_ninja', methods=['POST'])
def add_ninja():
    ninja.Ninja.add_ninja(request.form)
    id = request.form["id"]
    return redirect('/dojos')


if __name__ == "__main__":
    app.run(debug=True)