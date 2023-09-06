from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap
import email_validator
import requests as req
import os

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "any-string-you-want-just-keep-it-secret"

class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired(message="Please enter your name.")])
    email = StringField(label='Email', validators=[DataRequired(message="Please enter your email address."), Email(granular_message=True)])
    subject = StringField(label='Subject', validators=[DataRequired(message="Please enter a subject.")])
    message = TextAreaField(label='Message', validators=[DataRequired(message="Please enter a Message.")])
    submit = SubmitField(label="Submit")

def main():
    index()
    about()
    projects()
    contact()
    app.run(debug=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    cform = ContactForm()
    if request.method == 'POST':
        if cform.validate() == True:
            form_name = cform.name.data
            form_email = cform.email.data
            form_subject = cform.subject.data
            form_message = cform.message.data

            print(f"Name:{form_name}, E-mail:{form_email}, subject:{form_subject} message:{form_message}")

            userId = os.environ.get('USER_ID')
            apiKey = os.environ.get('API_KEY')
            url = f'https://gmail.googleapis.com/upload/gmail/v1/users/{userId}/messages/send&key={apiKey}'
            body = {
                "raw": f'{form_message} from {form_name} {form_email}'
            }
    
            response = req.post(url=url, data=body)
            print(response)
            results = response.json()
            print(results)

            return render_template("contact.html", success=True)
        elif cform.validate() == False:
            flash('All fields are required.')
            return render_template("contact.html", form=cform)
    elif request.method == 'GET':
        return render_template("contact.html", form=cform)
    
    return render_template("contact.html", form=cform)

if __name__ == "__main__":
    main()
