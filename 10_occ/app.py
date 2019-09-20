import csv
import random

from flask import Flask, render_template
app = Flask(__name__)


# Reading in occupations file
file = open("occupations.csv","r")
readfile = file.readlines()
readfile.pop(0)
dictionary = {}
percentages = []
def sol():
    total = 0;
    for line in readfile:
        idx = line.rfind(",")
        job = line[0:idx]
        percent = float(line[idx+1:-1])
        percentages.append(percent)
        dictionary[job] = round(percent + total,1);
        total += percent
    del dictionary["Total"]
    rand = random.randint(1,998) * 0.1
    for key in dictionary.keys():
        if rand <= dictionary[key]:
            return key

@app.route("/")
def hello_world():
    print("Main page loaded") # Prints out something on load/reload in console
    return "New test page!"

@app.route("/my_foist_template")
def newpage():
    name = sol()
    return render_template('site.html',
    titulo = "Team Gold Introduction",
    job = name,
    col1 = dictionary.keys(),
    col2 = percentages
    )

if __name__ == "__main__":
    app.debug = True # Automatically updates project with save file
    app.run()
