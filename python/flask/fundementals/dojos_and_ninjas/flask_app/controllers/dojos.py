from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import dojo, ninja

from flask_app.models.dojo import Dojo


@app.route('/dojos')
def index():
        dojos = Dojo.get_all()
        return render_template("dojos.html", all_dojos = dojos)

@app.route('/add_dojo', methods=['POST'])
def add_dojo():
        Dojo.add_dojo(request.form)
        return redirect('/dojos')

@app.route('/show_dojo')
def show_dojo():
    return render_template("show_dojo.html")

@app.route('/dojos/<id>')
def show_one(id):
    data={
            "id": id
    }
    return render_template("show_dojo.html", select_one= Dojo.show_one_dojo(data))   


@app.route('/ninjas')
def home():
    return render_template("ninjas.html", all_dojos= dojo.Dojo.get_all())

@app.route('/add_ninja', methods=['POST'])
def add_ninja():
    ninja.Ninja.add_ninja(request.form)
    return redirect('/dojos')


if __name__ == "__main__":
        app.run(debug=True)
