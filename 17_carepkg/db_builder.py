# Jeff Lin
# SoftDev
# K17 :: SQLITE3 BASICS
# Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

with open('students.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    c.execute("CREATE TABLE students (name TEXT, age INTEGER, id INTEGER);")
    for row in reader:
        c.execute('INSERT INTO students VALUES ("' + row['name'] + '",' + row['age'] + ',' + row['id'] + ');')

with open('courses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    c.execute("CREATE TABLE courses (name TEXT, age INTEGER, id INTEGER);")
    for row in reader:
        c.execute('INSERT INTO students VALUES ("' + row['code'] + '",' + row['mark'] + ',' + row['id'] + ');')

db.commit() #save changes
db.close()  #close database
