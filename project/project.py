from flask import Flask

app = Flask(__name__)

def main():
    hello_world()
    about()
    projects()
    contact()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/about")
def about():
    return "The about page."

@app.route("/projects/")
def projects():
    return "The project page."

@app.route("/contact")
def contact():
    return "The contact page."

if __name__ == "__main__":
    main()