# The Big Bang Theory Episodes

# This dataset contains information about the TV show The Big Bang Theory
# and a list of every episode and their names, broadcasting dates, runtime,
# plot summaries, and more.

# Our import mechanism reads in the json file containing the dataset and
# specifically targets where the list of episodes are located in the dataset
# to insert into the collection.

import pymongo
from __init__ import *
from pymongo import MongoClient
from bson.json_util import loads
from pprint import pprint

client = MongoClient()
db = client["jishwaa"]

DIR = os.path.dirname(__file__) or "."
DIR += "/"
JSON_FILE = DIR + "big-bang-theory.json"

def parse():
	if db.jishwaa.count_documents({}) == 0:
		file = open(JSON_FILE,"r")
		dictionary = loads(file.read())
		db.jishwaa.insert(dictionary['_embedded']["episodes"])

def getSeason( season ):
	# print("Episodes in Season {}:".format(season))
	temp = []
	info = db.jishwaa.find( {"season": season} )
	for stuff in info:
		temp.append((str(stuff["number"]), stuff["name"]))
	return temp

def getYear( year ):
	# print("Episodes from {}:".format(year))
	temp = []
	info = db.jishwaa.find( {"airdate": {"$regex": str(year)}} )
	for stuff in info:
		temp.append((stuff["season"],stuff["number"],stuff["name"]))
	return temp

# pprint(getSeason(db,7))
# print("")
# pprint(getYear(db,2012))
