from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap5


myWebsite = Flask(__name__)
bootstrap = Bootstrap5(myWebsite)

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
    your_message = request.form.get("Your Message")
    if len(str('your_message')) <= 200:
     return redirect('/')
    else:
        return('Message is too long')

if __name__ == "__main__":
    myWebsite.run(debug=True,host="0.0.0.0",port=8090)

    #host="0.0.0.0",port=8090