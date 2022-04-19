from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/play')          # Have the /play route render a template with 3 blue boxes
def level1():
    return render_template("index.html", x=3, color="blue") # Return the string 'Hello World!' as a response

@app.route('/play/<int:x>')          
def level2(x):
    return render_template("index.html", x=x, color="blue")  

@app.route('/play/<int:x>/<string:color>')          
def level3(x, color):
    return render_template("index.html", x=x, color=color)    
if __name__=="__main__":
    app.run(debug=True)
