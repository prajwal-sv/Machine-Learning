from flask import Flask
# Create a instance of the flask  Class 
#  which will be  your  WSGI Application 
app = Flask(__name__)
@app.route("/")
def welcome():
    return "Welcome to this best flask tutorial. this should be a"

@app.route("/lec1")
def Lec1():
    return "this is the lec1"

if __name__ == "__main__":
    app.run(debug=True)
