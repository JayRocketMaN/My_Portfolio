from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms import StringField, EmailField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
import requests

from dotenv import load_dotenv


myWebsite = Flask(__name__)
bootstrap = Bootstrap5(myWebsite)

# Load environment variables from .env
load_dotenv()

# Get values from .env file
myWebsite.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
myWebsite.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
myWebsite.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
myWebsite.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
myWebsite.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL') == 'True' 
myWebsite.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
myWebsite.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
myWebsite.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
myWebsite.config['BREVO_EMAIL_API_KEY'] = os.getenv('BREVO_EMAIL_API_KEY')



mail = Mail(myWebsite)


@myWebsite.route("/")
def home():
    form = ContactForm()
    return render_template('about.html', form=form)#remeber to correct the route to the actual 'home' route

@myWebsite.route("/skills")
def skills():
    return render_template('skills.html')

@myWebsite.route("/about")
def about():
    form = ContactForm()
    return render_template('about.html', form=form)


class ContactForm(FlaskForm):
        name = StringField('name', validators=[DataRequired()])
        email = EmailField('Email', validators=[DataRequired(), Email()])
        message = TextAreaField('message', validators=[DataRequired(), Length(min=-1, max=1000, message='check message again')])
        submit = SubmitField('Send Message')


@myWebsite.route('/sendMessage', methods=['GET','POST'])
def contactMe():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
   
       
    api_url = "https://api.brevo.com/v3/smtp/email"
    headers = {
            "accept": "application/json",
            "api-key": os.environ.get("BREVO_API_KEY"),
            "content-type": "application/json"
        }
        
    payload = {
            "sender": {"name": "My Portfolio Form", "email": "odidikaanthony02@gmail.com"},
            "to":[{"email": "odidikaanthony02@gmail.com", "name": "somto"}],
            "replyTo": {"email": email, "name": name}, # The visitor's email goes here!
            "subject": f"New Contact from {name}",
            "htmlContent": f"<p><strong>Name:</strong> {name}</p><p><strong>Email:</strong> {email}</p><p><strong>Message:</strong> {message}</p>"
        }
    
    try:
            # Send the API request
            response = requests.post(api_url, json=payload, headers=headers)
            
            print(f"--- BREVO STATUS: {response.status_code} ---", flush=True)
            print(f"--- BREVO RESPONSE: {response.text} ---", flush=True)
            
            if response.status_code in [200, 201]:
                flash('Message sent successfully!', 'success')
            else:
                print(f"BREVO ERROR: {response.status_code} - {response.text}") 
                flash('Email provider rejected the message.', 'error')
                
    except Exception as e:
            print(f"--- PYTHON ERROR: {str(e)} ---", flush=True)
            flash(f'Error: {str(e)}', 'error')
        
            return redirect(url_for('home') + '#contact')

    return render_template('about.html', form=form)

# try:
#             # Send the API request
#             response = requests.post(api_url, json=payload, headers=headers)
            
#             # FORCE RENDER TO PRINT THE EXACT ERROR:
#             print(f"--- BREVO STATUS: {response.status_code} ---", flush=True)
#             print(f"--- BREVO RESPONSE: {response.text} ---", flush=True)
            
#             if response.status_code in[200, 201]:
#                 flash('Message sent successfully!', 'success')
#             else:
#                 flash('Email provider rejected the message.', 'error')
                
#         except Exception as e:
#             print(f"--- PYTHON ERROR: {str(e)} ---", flush=True)
#             flash(f'Error: {str(e)}', 'error')
                 # try:
        #     msg = Message(
        #         subject=f"New Contact from {name}",
        #         sender=myWebsite.config['MAIL_USERNAME'],
        #         recipients=[myWebsite.config['MAIL_USERNAME']]
        #     )
        #     msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        #     mail.send(msg)
        #     flash('Message sent successfully!', 'success')
        # except Exception as e:
        #     flash(f'Error: {str(e)}', 'error')
        
        # return redirect('/' + '#contact')
    

# def sendMessage():
#     if request.method == 'POST':e
#         name = request.form.get('name')
#         email = request.form.get('email')
#         message = request.form.get('message')
        
#         # Check if data is None
#         if name is None or email is None or message is None:
#             print("ERROR: Form data is None!")
#             flash('Form data not received. Check console.', 'error')
#             return redirect('/' + '#contact')
        
        

if __name__ == "__main__":
    myWebsite.run(debug=True)

    #host="0.0.0.0",port=8090