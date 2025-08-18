from flask import Flask ,render_template,request
# Create a instance of the flask  Class 
#  which will be  your  WSGI Application 
app = Flask(__name__)
@app.route("/")
def welcome():
    return "Welcome to this best flask tutorial. this should be a"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')
@app.route("/about")
def about():
    return render_template('about.html')
@app.route('/form', methods=['GET','POST'])
def form():
    if request.method=='POST':
        name = request.form['name']
        return f'hellow {name}'
    return render_template('from.html')

if __name__ == "__main__":
    app.run(debug=True)
