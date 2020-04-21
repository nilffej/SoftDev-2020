from pprint import pprint

f = open('nycdeaths.csv','r')
f = f.readlines()
data = []
for line in f:
    data.append(line[:-1].split(','))

pprint(data)