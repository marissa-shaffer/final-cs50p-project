from flask import Flask, render_template

app = Flask(__name__)

#def main():
#    index()
#    about()
#    projects()
#    contact()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return "The about page."

@app.route("/projects/")
def projects():
    return "The project page."

@app.route("/contact")
def contact():
    return "The contact page."

#if __name__ == "__main__":
#    main()