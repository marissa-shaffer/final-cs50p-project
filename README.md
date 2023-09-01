# Flask App Personal Website
#### URL: https://marissashaffer-dev.vercel.app/
#### Languages/Libraries Used:
* Python
  * Flask
  * Flask-WTF
  * WTF Forms
  * Flask Bootstrap
  * Pytest
* HTML
* CSS

#### Description:
This is a Flask Application for me to display my project portfolio, an about me page, and a contact form if the user wants to reach out. I chose a Flask app because I wanted to build a portfolio page for my web development work and use the page itself to show what I can do with Python with the application itself. This application was for my Harvard CS50P Final Project.

To see a deployed version on hosted on Vercel, click the link in the URL above.

The project.py file contains the routes for the application and the contact form functionality. If a user filled out the contact form, it is validated with Flask WTForms and then the submission is printed in the logs. If the form submission was successful a success flag is sent to the contact.html page and displays a message to the user.

Each route in the project.py file has a function to return a Flask render_template function with the corresponding html web page. For the home page, which routes with a "/" and is defined in the app.route decorator, it returns the index.html page. Using Jinja templates, I designed the navigation bar and footer to go around the content for each page in the base.html file. Jinja templates can extend or inherit from another template, so the index.html page extends the base.html file with the Jinja syntax. Then in the block content from Jinja, I added a card with Bootstrap styling to display a photo and heading text overlayed on it to welcome the user.

The about page is routed as "/about" in the project.py file with a function that retuns the Flask render_template function to display the about.html page. This page is also styled with Flask Bootstrap and the image is hosted on github for ease of use. The content is a back story about me.

The contact page is routed in project.py as "/contact" with a function that returns the Flask render_template function to display the contact.html page. This page is styled with a combination Flask Bootstrap and some internal CSS on the base.html file. I also used Flask-WTForms to build the ContactForm class and invoke it within the contact function. With Flask Forms, I used validators to require the fields and check the email field. As I mentioned above, if the form is successfully submitted, a flag is sent to the contact page that is was a success and to display a confirmation message. Submitting the form also triggers a POST method which also initiates the form validation and prints the submission into the logs.

The contact page was actually the most challenging of all pages. The routing part was not as difficult but when it came to the functions, I ran into a lot of set backs. Initially I wanted to use smtplib to have the form send me an email with the contact form submission with a gmail account. Through reading Google's Gmail API documentation and forums, I found that Gmail does not allow less secure apps to send through SMTP without an app password or OAuth 2.0. For this project, I did not want to pay for email services like Twilio SendGrid or MailTrap to have the ease of their APIs and security. In the near future, I will look at setting up these services for my personal flask web application.

As for my design choices, I took time to think about what I really wanted to do for my project. I considered buidling something fun like a game but It made more sense to me to create something useful, at least for myself. In using the Flask libarary, I kept the python scripting in one file since it was a small application. If I had a larger application, I would have put the routes in their own file. Same for the form classes and function, they would have been placed in thier own python file if it was a larger application or form. It made sense to me to keep each html page separate and then render them into the project.py file in each route function. I went with minimal styling to use the power of Flask Bootstrap. It was very easy to use and allowed me to spend more time on coding rather than custom styling everything. Jinja templates was also a powerful way to inject python programming into the html files. It made the physical design of the pages much faster since the files could extend or inherit from another. I chose not use SMTP for my contact form because I did not want to use something with low security just to make my project work and I did not want to pay for a premium email service yet. Flask-WTForms just made sense since there were a lot built in functions that worked well with Flask in general. I also chose to deploy my project in Vercel since they had a Flask app option that would directly deploy from a public Github repository. The images are linked from my public github repository for the vercel deployment.

The test_project.py file uses pytest to test the Flask Application and each route or page. Each test uses the test_client() method from Flask that contains the features needed to make HTTP requests to the application under test. Each route or endpoint is tested with a GET request and the code then asserts that the response recieved, which should be a 200 status code. Also checking in the response data that it contains the correct page title for each endpoint. I also tested that the contact form sends back a 200 status code when the form is filled out by provide data for each field in a dict.