import cgi

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
@app.route("/")
def occupyflaskst():
    return render_template(
    )

@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args)
    return render_template(
    )

if __name__ == "__main__":
  app.debug = True
  app.run()
