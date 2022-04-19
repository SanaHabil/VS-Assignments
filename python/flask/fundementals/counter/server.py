from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'click one more time' 

@app.route('/')
def index():
    if "click" not in session:
        session['click'] = 0
    else:
        session['click'] += 1
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/plus2')
def plus2():
    if "click" not in session:
        session['click'] = 0
    else:
        session['click'] += 2
    return render_template("plus2.html")

@app.route('/increment', methods=['POST'])
def submit():
    print(request.form)
    inc = request.form['increment']
    session['click'] += int(inc)- 1
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
