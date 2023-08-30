from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap
import email_validator
from flask_mail import Mail, Message
import smtplib
import os

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "any-string-you-want-just-keep-it-secret"

username = os.environ.get('gusername')
password = os.environ.get('gpassword')

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = username
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

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
            form_name = cform.name.data
            form_email = cform.email.data
            form_subject = cform.subject.data
            form_message = cform.message.data

            print(f"Name:{form_name}, E-mail:{form_email}, subject:{form_subject} message:{form_message}")

            msg = Message(subject=form_subject, sender=username+'@gmail.com', recipients=['marissa.shaffer1@gmail.com'])
            msg.body = form_message
            mail.send(msg)
            print("Message sent!")
            
            return render_template("contact.html", success=True)
        else:
            print('Form was unsucessful')
            return render_template("contact.html", form=cform)
    elif request.method == 'GET':
        return render_template("contact.html", form=cform)
    
    return render_template("contact.html", form=cform)

if __name__ == "__main__":
    main()
