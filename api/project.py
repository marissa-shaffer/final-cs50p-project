from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap
import email_validator
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "any-string-you-want-just-keep-it-secret"

class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired(message="Please enter your name.")])
    email = StringField(label='Email', validators=[DataRequired(message="Please enter your email address."), Email(granular_message=True)])
    subject = StringField(label='Subject', validators=[DataRequired(message="Please enter a subject.")])
    message = StringField(label='Message', validators=[DataRequired(message="Please enter a Message.")])
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
        if cform.validate_on_submit() == True:
            form_name = cform.name.data
            form_email = cform.email.data
            form_subject = cform.subject.data
            form_message = cform.message.data

            print(f"Name:{form_name}, E-mail:{form_email}, subject:{form_subject} message:{form_message}")

            return render_template("contact.html", success=True)
        else:
            flash('All fields are required.')
            return render_template("contact.html", form=cform)
    elif request.method == 'GET':
        return render_template("contact.html", form=cform)
    
    return render_template("contact.html", form=cform)

if __name__ == "__main__":
    main()
