from pprint import pprint
from operator import itemgetter
import json

# OPTION OUTPUT FUNCTION FOR ORGANIZATION
def output(data, head):
    output = [head]
    file = open('output.csv','w')
    for item in data:
        output.append(','.join(item) + '\n')
    file.writelines(output)

def parse():
    # DATA CLEANING
    f = open('leadingcauses.csv','r')
    f = f.readlines()
    data = []
    for line in f[1:]:
        if 'New York' in line and 'All Causes' not in line:
            t = line[:-1].split(',')
            entry = [t[0],t[-5],int(''.join(t[-3:][:-1]).strip('"'))]
            data.append(entry)

    # ORGANIZING DATA INTO NESTED DICT
    datadict = {}
    for item in data:
        if item[0] not in datadict.keys():
            datadict[item[0]] = {}
        if item[1] not in datadict[item[0]].keys():
            datadict[item[0]][item[1]] = item[2]
    
    datadict = json.dumps(datadict)
    return datadict
