from flask import Flask, render_template


#create flask instance
app = Flask(__name__)

#create a route decorator
@app.route('/')
#create a function to return html in local host
def index():
    first_name="John"
    stuff="This is <strong>Bold</strong>Text"
    favorite_pizza=["pepperonix", "salami", "meat", "ham", 542]
    return render_template("index.html", 
        first_name=first_name,
        stuff=stuff,
        favorite_pizza=favorite_pizza)

#localhost:5000/user/jhon
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)

#create custom error pages
#invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500



