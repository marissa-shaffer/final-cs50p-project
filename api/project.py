from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField, Recaptcha
from wtforms import StringField, validators, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap
import email_validator
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from google_recaptcha import ReCaptcha

appSecretKey = os.environ.get('APP_KEY')

RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_SITE_KEY')
RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_SECRET_KEY')

app = Flask(__name__)
app.config.from_object(__name__)
Bootstrap(app)
app.secret_key = appSecretKey

class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired(message="Please enter your name.")])
    email = StringField(label='Email', validators=[DataRequired(message="Please enter your email address."), Email(granular_message=True)])
    subject = StringField(label='Subject', validators=[DataRequired(message="Please enter a subject.")])
    message = TextAreaField(label='Message', validators=[DataRequired(message="Please enter a Message.")])
    grecaptcha = RecaptchaField()
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
            grecaptcha = request.json["g-recaptcha-repsonse"]

            print(f"Name:{form_name}, E-mail:{form_email}, subject:{form_subject} message:{form_message}")
            print('Recaptcha has succeeded')
            print(grecaptcha)

            api_key = os.environ.get('SG_API_KEY')

            message = Mail(
                from_email='marissashaffer.dev@gmail.com',
                to_emails='marissashaffer.dev@gmail.com',
                subject=form_subject,
                html_content=f'{form_message}<br><p>from {form_name} at {form_email}</p>')
            
            try:
                sg = SendGridAPIClient(api_key)
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e.message)

            return render_template("contact.html", success=True)
        elif cform.validate_on_submit() == False:
            flash('All fields are required.')
            return render_template("contact.html", form=cform)
    elif request.method == 'GET':
        return render_template("contact.html", form=cform)
    
    return render_template("contact.html", form=cform)

if __name__ == "__main__":
    main()
