# Jeff Lin + Jackson Zou
# SoftDev PD 9
# K18 Come Up For Air
# 2020-04-21

from flask import Flask, render_template, request, redirect, url_for
from parse import *
app = Flask(__name__)

@app.route("/")
def homepage():
    info = parse()
    return render_template('index.html', info = info)

if __name__ == "__main__":
    app.debug = True
    app.run()
