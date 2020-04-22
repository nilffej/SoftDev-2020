from pprint import pprint
from operator import itemgetter

# OPTION OUTPUT FUNCTION FOR ORGANIZATION
def output(data, head):
    output = [head]
    file = open('output.csv','w')
    for item in data:
        output.append(','.join(item) + '\n')
    file.writelines(output)

# DATA CLEANING
f = open('nycdeaths.csv','r')
f = f.readlines()
data = []
head = f[0]
for line in f[1:]:
    data.append(line[:-1].split(','))

# ORGANIZING DATA INTO NESTED DICT
datadict = {}
for item in data:
    item[1] = item[1].replace('"','')
    if item[0] not in datadict.keys():
        datadict[item[0]] = {}
    if item[1] not in datadict[item[0]].keys():
        datadict[item[0]][item[1]] = 1
    else:
        datadict[item[0]][item[1]] = 1 + datadict[item[0]][item[1]]

pprint(datadict)

# data = sorted(data, key = itemgetter(0))
# data = sorted(data, key = itemgetter(1))
# output(data, head)