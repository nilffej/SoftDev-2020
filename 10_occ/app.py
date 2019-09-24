# Jeff Lin and Manfred Tan - Team Gold
# SoftDev1 pd9
# K #10: Jinja Tuning
# 2019-09-23

import csv
import random

from flask import Flask, render_template
app = Flask(__name__)

dictionary = {}

# makes dictionary and returns random job.
def makeDict():
    # open returns a file object, which is an iterator and iterable
    with open("occupations.csv","r") as oldcsv:
        # returns file object. Turns each row into a list, with
        # element 0 as the occupation and element 1 as percentage
        csvRead = csv.reader(oldcsv)
        # skips first row (title)
        next(csvRead)
        # adds each row into dictionary
        for row in csvRead:
            dictionary[row[0]] = float(row[1])

    del dictionary["Total"] # remove total percentage (final line)
    # chooses number from 1 to 998, then multiplies by 0.1 to get 0.1 to 99.8
    rand = random.randint(1,998) * 0.1
    # this sum represents what percent range we are at. Each job occupies a
    # range of numbers with the length being equal to the percentage. If the
    # random number falls within this range, the job is chosen.
    tempsum = 0
    # checks to see if the random number is within the job percentage range.
    for key in dictionary.keys():
        tempsum += dictionary[key]
        if rand <= tempsum:
            return key

@app.route("/")
def hello_world():
    # prints out something on load/reload in console
    print("Main page loaded")
    return "New test page!"

@app.route("/occupyflaskst")
def newpage():
    # declaration calls method to build dictionary and choose random occupation
    occupation = makeDict()
    # obtains percentage of occupation
    percentage = dictionary.get(occupation)
    # creates list of dictionary keys
    keys = list( dictionary.keys() )
    # passes variable names with stored values to Jinja template
    return render_template('site.html',
    titulo = "Occupations",
    job = occupation,
    percent = percentage,
    col1 = keys,
    col2 = list( dictionary.values() ),
    # length of list for loop to build table
    lengthNum = range( len(keys) )
    )

if __name__ == "__main__":
    # Automatically updates project with save file
    app.debug = True
    app.run()
