from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # Have the /play route render a template with 3 blue boxes
def checkerboard1():
    return render_template("index.html", x=8, y=8, color1="red", color2="bisque") 
@app.route('/<int:rows>')          
def checkerboard2(rows):
    return render_template("index.html", x=rows, y=4, color1="green", color2="brown") 
@app.route('/<int:rows>/<int:cols>/<colorone>/<colortwo>')          
def checkerboard3(rows, cols, colorone, colortwo):
    return render_template("index.html", x=rows, y=cols, color1=colorone, color2=colortwo) 
if __name__=="__main__":
    app.run(debug=True)
