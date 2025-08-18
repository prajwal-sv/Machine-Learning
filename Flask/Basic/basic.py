## creating the flask app
#import thr flask module
from flask import Flask 
from flask import render_template  # import render_template for rendering HTML templates
from flask import request  # import request for accessing request data
from flask import url_for  # import url_for for building URLs dynamically
from flask import redirect  # import redirect for redirecting to a different route
app =  Flask(__name__)  # create an instance [Construtor] of the Flask class

@app.route("/")  # decorator to tell Flask what URL should call the function
def hello_world():
    return "Hello, World!"




# To run this app, save it as basic.py and run the command:
# python basic.py

# createing a new route
@app.route("/hello")
def new_route():                           #this is first type of creating a route  
    return "This is a new route!"

#another way to create a route
def another_route():
    return "This is another route!"
app.add_url_rule("/another_route", "another_route", another_route)  # this is second type of creating a route


#creating a route with a variable
@app.route("/user/<username>")  # <username> is a variable part of the URL
def show_user_profile(username):
    return f"User: {username}"

#creating a route with a variable with a converter
@app.route("/post/<int:post_id>")  # <int:post_id>
def show_post(post_id):
    return f"Post ID: {post_id}"    



#tamplate variables jnja2
@app.route("/variable/jnja2/<name>")
def jinja_variable(name):
    return render_template("variable.html", name=name)

# request variables

@app.route("/search")
def search():
    query = request.args.get('query')  # get the 'query' parameter from the URL
    return f"You searched for: {query}"

#/search?query=flask


app.route("/login", methods=["POST"])  # route for handling form submission
def login():
    username =  request.form.get('username')  # get the 'username' from the form data
    password = request.form.get('password')  # get the 'password' from the form data
    return f"Username: {username}, Password: {password} "  # return the username
   

#Bulding  a url dynamically in flask
@app.route("/link")
def link():
   return redirect(url_for('new_route')) # dynamically build the URL for the 'hello_world' function

if __name__ == "__main__":
    app.run(debug=True)  # run the app in debug mode


# Note: The debug mode allows you to see errors in the browser and automatically reloads the server when you make changes to the code.
# You can access the app by going to http://