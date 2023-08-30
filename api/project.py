from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap
import email_validator
import smtplib
import os

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "any-string-you-want-just-keep-it-secret"

class contactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email(granular_message=True)])
    subject = StringField(label='Subject')
    message = StringField(label='Message')
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
    cform = contactForm()
    if request.method == 'POST':
        if cform.validate_on_submit() == True:
            name = cform.name.data
            email = cform.email.data
            subject = cform.subject.data
            form_message = cform.message.data

            print(f"Name:{name}, E-mail:{email}, subject:{subject} message:{form_message}")

            username = os.environ.get('mailtrap_sandbox_username')
            password = os.environ.get('mailtrap_sandbox_pw')

            sender = "Private Person <from@example.com>"
            receiver = 'A Test User <to@example.com>'

            message = f"""\
            Subject: {subject}
            To: {receiver}
            From: {sender}

            {form_message}"""

            with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
                server.login(username, password)
                server.sendmail(sender, receiver, message)
                print('Email sent.')
            return render_template("contact.html", form=cform)
        else:
            print('Form was unsucessful')
            return render_template("contact.html", form=cform)
    elif request.method == 'GET':
        return render_template("contact.html", form=cform)
    
    return render_template("contact.html", form=cform)

if __name__ == "__main__":
    main()
