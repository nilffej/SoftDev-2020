# Jeff Lin
# SoftDev1 PD9
# K18 -- Average
# 2019-10-14

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

with open('students.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    c.execute("CREATE TABLE students (name TEXT, age INTEGER, id INTEGER);")
    for row in reader:
        c.execute('INSERT INTO students VALUES ("{}",{},{})'.format(row['name'],row['age'],row['id']))

with open('courses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);")
    for row in reader:
        c.execute('INSERT INTO courses VALUES ("{}",{},{})'.format(row['code'],row['mark'],row['id']))

q = """
SELECT students.name, students.id, courses.mark
FROM students, courses
WHERE students.id = courses.id;
"""
foo = db.execute(q)
rows = foo.fetchall()

dict = {}
for item in rows:
    if item[0] not in dict.keys():
        dict[item[0]] = (item[1],[item[2]])
    else:
        dict[item[0]][1].append(item[2])

c.execute("CREATE TABLE stu_mean (name TEXT, id INTEGER, average NUMERIC)")
for item in dict.keys():
    average = round(sum(dict[item][1]) / len(dict[item][1]),1)
    c.execute('INSERT INTO stu_mean VALUES ("{}",{},{})'.format(item,dict[item][0],average))

show = db.execute("SELECT * FROM stu_mean")
rows = show.fetchall()
for row in rows:
    print(row)


db.commit() #save changes
db.close()  #close database
