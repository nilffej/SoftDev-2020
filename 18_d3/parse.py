from pprint import pprint
from operator import itemgetter

def output(data, head):
    output = [head]
    file = open('output.csv','w')
    for item in data:
        output.append(','.join(item) + '\n')
    file.writelines(output)

f = open('nycdeaths.csv','r')
f = f.readlines()
data = []
head = f[0]
for line in f[1:]:
    data.append(line[:-1].split(','))
data = sorted(data, key = itemgetter(0))
data = sorted(data, key = itemgetter(1))

output(data, head)