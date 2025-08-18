from flask import Flask,render_template
# Create a instance of the flask  Class 
#  which will be  your  WSGI Application 
app = Flask(__name__)
@app.route("/")
def welcome():
    return "Welcome to this best flask tutorial. this should be a "

@app.route("/Home")
def Home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
