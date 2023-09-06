from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap
import email_validator
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

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

            api_key = os.environ.get('SG_API_KEY')

            message = Mail(
                from_email='marissashaffer.dev@gmail.com',
                to_emails='marissashaffer.dev@gmail.com',
                subject=form_subject,
                plain_text_content=f'{form_message} from {form_name} at {form_email}')
            
            try:
                sg = SendGridAPIClient(api_key)
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e.message)

            return render_template("contact.html", success=True)
        elif cform.validate() == False:
            flash('All fields are required.')
            return render_template("contact.html", form=cform)
    elif request.method == 'GET':
        return render_template("contact.html", form=cform)
    
    return render_template("contact.html", form=cform)

if __name__ == "__main__":
    main()
