#Derek Leung + Jeff Lin [TEAM COCONUT WATER]
#SoftDev1 PD 9
#K12
#2019-09-21

import cgi

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
@app.route("/")
def occupyflaskst():
    return render_template(         # Renders new page template with name form
    'something.html'
    )

@app.route("/auth")
def authenticate():
    print(app)                      # Prints out Flask app name
    print(request)                  # Prints out Flask app web address
    print(request.args)             # Prints out dictionary with form information
    return render_template(
    'nothing.html',                 # Renders new page template
    myname = request.args["name"]   # Defines myname variable using form dictionary
    )

if __name__ == "__main__":
  app.debug = True
  app.run()
