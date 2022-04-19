from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import survey

app.secret_key = 'hi this is Dojo Survey'

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    session['favlang'] = request.form['favlang']
    session['cohort'] = request.form.getlist('cohort')
    print(session['cohort'])
    if not survey.Survey.validate_survey(request.form):
        # redirect to the route where the author form is rendered.
        return redirect("/")
    # else no errors:
    survey.Survey.add_survey(request.form)
    return redirect('/results') 

@app.route('/results')
def results():
    return render_template('results.html') 

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
