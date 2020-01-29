# Jackson Zou + Jeff Lin [RIP Jun Tao]
# SoftDev1 PD 9
# K15
# 2019-10-03

import cgi

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

username = "Jeff"
password = "pass"
current = {}
app = Flask(__name__)
@app.route("/")
def occupyflaskst():
    if "name" not in current.keys():
        return render_template(         # Renders new page template with name form
            'login.html'
        )
    return render_template("homepage.html",
                            user = current["name"])

@app.route("/auth")
def authenticate():
    print(app)                      # Prints out Flask app name
    print(request)                  # Prints out Flask app web address
    print(request.args)             # Prints out dictionary with form information
    if "name" not in request.args or "pass" not in request.args:
        return
    current["name"] = request.args["name"]
    current["pass"] = request.args["pass"]
    if request.args["name"] == username and request.args["pass"] == password:
        return redirect(url_for("homepage"))
    else:
        return redirect(url_for("error"))

@app.route("/homepage")
def homepage():
    print(current)
    print(request.args)
    return render_template("homepage.html",
                            user = current["name"])

@app.route("/error")
def error():
    print(current)
    if current["name"] != username:
        return render_template("error.html",
                                user = current["name"])
    return render_template("error.html",
                            user = current["name"],
                            userp = current["pass"])

@app.route("/red")
def red():
    print(current)
    current.clear()
    return redirect(url_for("occupyflaskst"))

if __name__ == "__main__":
  app.debug = True
  app.run()
