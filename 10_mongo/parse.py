import pymongo

from pymongo import MongoClient
from bson.json_util import loads
from pprint import pprint

client = MongoClient()
db = client["jishwaa"]

def parse():
	if db.jishwaa.count_documents({}) == 0:
		file = open("big-bang-theory.json","r")
		dictionary = loads(file.read())
		db.jishwaa.insert(dictionary['_embedded']["episodes"])

def getSeason( db, season ):
	print("Episodes in Season {}:".format(season))
	info = db.jishwaa.find( {"season": season} )
	increment = 0
	for stuff in info:
		increment += 1
		print(str(increment) + " - " + stuff["name"])

parse()
getSeason(db,1)

# def getRestaurantsByZip( db, zip ):
# 	print("Restaurants with the zipcode of:", zip)
# 	info = db.restaurants.find( {"address.zipcode": zip})
# 	print(info)
# 	for stuff in info:
# 		print(stuff)
#
# def getRestaurantsByZipandGrade( db, zip, grade ):
# 	print("Restaurants with the zipcode and grade:", zip, grade)
# 	info = db.restaurants.find( {"address.zipcode": zip, "grades.0.grade": grade})
# 	print(info)
# 	for stuff in info:
# 		print(stuff)
#
# def getRestaurantsByZipandScore( db, zip, score ):
# 	print("Restaurants with the zipcode and less score than:", zip, score)
# 	info = db.restaurants.find( {"address.zipcode": zip, "grades.0.score": {"$lt": int(score)}})
# 	print(info)
# 	for stuff in info:
# 		print(stuff)
