from flask import Flask , render_template  # import render_template for rendering HTML templates

app = Flask(__name__)  # create an instance [Constructor] of the Flask class

@app.route("/")  # decorator to tell Flask what URL should call the function
def home():
    return  render_template('home.html',title="Home")# render the index.html template


@app.route("/about")  # decorator to tell Flask what URL should call the function
def about():
    return  render_template('about.html',title="Home")# render the about.html template


@app.route("/list")  # decorator to tell Flask what URL should call the function
def list_items():
    items = ["Item 1", "Item 2", "Item 3"]  
    return render_template('list.html', items=items, title="List")

if __name__ == "__main__":
    app.run(debug=True)  # run the app in debug mode


