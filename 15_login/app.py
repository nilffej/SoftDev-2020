# Jackson Zou + Jeff Lin [RIP Jun Tao]
# SoftDev1 PD 9
# K12
# 2019-09-21

import cgi

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

username = "Jeff Lin"
password = "password"
current = {}
app = Flask(__name__)
@app.route("/")
def occupyflaskst():
    return render_template(         # Renders new page template with name form
    'login.html'
    )

@app.route("/auth")
def authenticate():
    print(app)                      # Prints out Flask app name
    print(request)                  # Prints out Flask app web address
    print(request.args)             # Prints out dictionary with form information
    current["name"] = request.args["name"]
    if request.args["name"] == username and request.args["pass"] == password:
        return redirect(url_for("homepage"))
    else:
        return redirect(url_for("error"))

@app.route("/homepage")
def homepage():
    print(current)
    return render_template("homepage.html",
                            user = current["name"])

@app.route("/error")
def error():
    print(current)
    return render_template("error.html",
                            user = current["name"])

@app.route("/red")
def red():
    print(current)
    return redirect(url_for("occupyflaskst"))

if __name__ == "__main__":
  app.debug = True
  app.run()
