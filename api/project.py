from flask import Flask, render_template

app = Flask(__name__)

def main():
    index()
    about()
    projects()
    contact()
    app.run(debug=True)

@app.route("/")
def index():
    return render_template("index.html")
    #return "The home page"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects/")
def projects():
    return "The project page."

@app.route("/contact")
def contact():
    return "The contact page."

if __name__ == "__main__":
    main()   