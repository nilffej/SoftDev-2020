from flask import Flask, render_template, request, redirect, url_for
import urllib.request, json
from parse import *
from pprint import pprint
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def root():
    parse()
    print(request.form)
    seasonlist = None
    yearlist = None
    season = None
    year = None
    if request.form:
        if request.form['season'] != '':
            season = int(request.form['season'][6:])
            seasonlist = getSeason(season)
        if request.form['year'] != '':
            year = int(request.form['year'])
            yearlist = getYear(year)
    return render_template("homepage.html", 
        season = season, year = year,
        seasonlist = seasonlist,
        yearlist = yearlist)

if __name__ == "__main__":
    app.debug = True
    app.run()