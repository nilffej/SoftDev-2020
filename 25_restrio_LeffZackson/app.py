# Jeff Lin & Jackson Zou
# SoftDev1 PD 9
# K25
# 11/13/2019

from flask import Flask, render_template, request, redirect, url_for
import urllib.request, json
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("tree.html")

@app.route("/metaweather")
def metaweather():
    u = urllib.request.urlopen("https://www.metaweather.com/api/location/44418/")
    response = u.read()
    data = json.loads(response)
    weather = data['consolidated_weather'][0]
    return render_template("metaweather.html",
                            place = data['title'],
                            latt_long = data['latt_long'],
                            applicable_date = weather['applicable_date'],
                            weather_state_name = weather['weather_state_name'],
                            image = "https://www.metaweather.com/static/img/weather/png/64/{}.png".format(weather['weather_state_abbr']))

@app.route("/itunes")
def itunes():
    u = urllib.request.urlopen("https://itunes.apple.com/search?term=linkin+park&limit=5")
    response = u.read()
    data = json.loads(response)
    songlist = []
    print(data)
    for item in data['results']:
        songlist.append(dict(name = item['trackName'],
            albumcover = item['artworkUrl100'], album = item['collectionName'], price = item['trackPrice']))
    return render_template("itunes.html", tracks = songlist)

if __name__ == "__main__":
    app.debug = True
    app.run()
