from unicodedata import name
from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
@app.route('/dojo')
def dojo():
    return 'Dojo!'
@app.route('/say/<name>')
def say_hello(name):
    if name.isalpha():    # check if input is a string or not
        return 'Hello '+name +'!'
    else:
        return('Sorry! No response. Try again')    
@app.route('/repeat/<num>/<name>')
def repeate_hello(num,name):
        if (int(num)and name.isalpha()):
            result = str(name) * int(num)
            print(result)
            return result
        else:
            return ('Sorry! No response. Try again')    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
# import statements, maybe some other routes
    
