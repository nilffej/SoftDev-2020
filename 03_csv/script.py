import csv
import random

file = open("occupations.csv","r")
readfile = file.readlines()
readfile.pop(0)

def sol():
    dictionary = {}
    total = 0;
    for line in readfile:
        idx = line.rfind(",")
        job = line[0:idx]
        percent = float(line[idx+1:-1])
        dictionary[job] = round(percent + total,1);
        total += percent
    del dictionary["Total"]
    rand = random.randint(1,998) * 0.1
    for key in dictionary.keys():
        if rand <= dictionary[key]:
            return key;

print(sol())
