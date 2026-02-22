from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap5


myWebsite = Flask(__name__)
bootstrap = Bootstrap5(myWebsite)

# Load environment variables from .env
load_dotenv()

# Get values from .env file
myWebsite.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
myWebsite.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
myWebsite.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
myWebsite.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
myWebsite.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
myWebsite.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
myWebsite.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')


mail = Mail(myWebsite)


@myWebsite.route("/")
def home():
    return render_template('about.html')#remeber to correct the route to the actual 'home' route

@myWebsite.route("/skills")
def skills():
    return render_template('skills.html')

@myWebsite.route("/about")
def about():
    return render_template('about.html')

@myWebsite.route("/sendMessage", methods=['post'])
def sendMessage():
    if request.method == 'post':
        print("Form data received:", request.form)
        
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        print(f"Name: {name}, Email: {email}, Message: {message}")
        
        # if not name or not email or not message:
        #     flash('All fields are required!', 'error')
        #     return redirect(url_for('home') + '#contact')
        
        try:
            msg = Message(
                subject=f"New Contact from {name}",
                sender=myWebsite.config['MAIL_USERNAME'],
                recipients=myWebsite.config['MAIL_USERNAME']
            )
            msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
            mail.send(msg)
            flash('Message sent successfully!', 'success')
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
        
        return redirect('/'+ '#contact')
    
    return render_template('/')

if __name__ == "__main__":
    myWebsite.run(debug=True,host="0.0.0.0",port=8090)

    #host="0.0.0.0",port=8090