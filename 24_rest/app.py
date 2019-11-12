from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from urllib.request import urlopen
import json
app = Flask(__name__)

@app.route("/")
def root():
    u = urlopen("https://api.nasa.gov/planetary/apod?api_key=BOwVXb2R0DrNbY31DDje2WF6MeioEHI1m0Lx1IbB")
    response = u.read()
    data = json.loads(response)
    return render_template("index.html", title = data['title'],
        pic = data['url'], text = data['explanation'])

if __name__ == "__main__":
    app.debug = True
    app.run()
