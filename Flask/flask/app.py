from flask import Flask
# Create a instance of the flask  Class 
#  which will be  your  WSGI Application 
app = Flask(__name__)
@app.route("/")
def welcome():
    return "Welcome to this flask tutorial"


if __name__ == "__main__":
    app.run()
