#Derek Leung + Jeff Lin [TEAM COCONUT WATER]
#SoftDev1 pd9
#K11
#2019-09-21

import cgi

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
@app.route("/")
def occupyflaskst():
    return render_template(
    'something.html'
    )

@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args)
    return "HELLO"

if __name__ == "__main__": #RUNS THE APP AT THE END
  app.debug = True
  app.run()

# print(flaskapp)
