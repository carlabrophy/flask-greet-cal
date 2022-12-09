from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return f"<h1>Welcome</h1>"

@app.route("/welcome/home")
def home():
    return f"<h1>Welcome home</h1>"

@app.route("/welcome/back")
def back():
    return f"<h1>Welcome back</h1>"
