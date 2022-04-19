from crypt import methods
from flask import Flask, render_template, request, redirect, session
import random 
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'click one more time' 

@app.route('/')
def index():
    if "num" not in session:
        session['num'] = random.randint(1,100)
    
        print(session['num'])

    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    session['numb'] = int(request.form['numb'])
    if "click" not in session:
        session['click'] = 1
    else:
        session['click'] += 1
    
    print(session['click'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('show.html')

@app.route('/show', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')   

if __name__=="__main__":
    app.run(debug=True)
