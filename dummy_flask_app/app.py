import requests
from  flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/") 
def hello():
    return render_template("cover.html")

@app.route("/signup")
def signup():
    return render_template("sign_in.html")

@app.route("/register")
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run()
