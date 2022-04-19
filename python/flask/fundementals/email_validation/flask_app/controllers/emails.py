from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import email

app.secret_key = 'hi this is Dojo Survey'

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/register', methods=['POST'])
def register():
    if not email.Email.validate_email(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    # ... do other things
    email_id=email.Email.add_email(request.form)
    return redirect('/results')

@app.route('/email/<int:id>')
def delete(id):
    email.Email.delete_email(id)
    return redirect('/results')

@app.route('/results')
def results():
    all_emails = email.Email.get_all()
    print(all_emails)
    return render_template("results.html", all_emails = all_emails)


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)






