from flask import Flask, render_template
from flask_bootstrap import Bootstrap5


myWebsite = Flask(__name__)
bootstrap = Bootstrap5(myWebsite)

@myWebsite.route("/")
def home():
    return render_template('home.html')

@myWebsite.route("/skills")
def skills():
    return render_template('skills.html')

@myWebsite.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    myWebsite.run(debug=True,host="0.0.0.0",port=8090)