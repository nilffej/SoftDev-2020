import pymongo

from pymongo import MongoClient
from bson.json_util import loads

client = MongoClient()
db = client.restaurants

file = open("primer-dataset.json","r")
insertstring = "["
for line in file:
	line = line.strip()
	insertstring += line + ","
final = insertstring[:len(insertstring)-1] + "]"
final = loads(final)
db.restaurants.insert(final)

def getRestaurantsByBorough( db, boro ):
	print("Restaurants in the borough of:", boro)
	info = db.restaurants.find( {"borough": boro} )
	print(info)
	for stuff in info:
		print(stuff)

def getRestaurantsByZip( db, zip ):
	print("Restaurants with the zipcode of:", zip)
	info = db.restaurants.find( {"address.zipcode": zip})
	print(info)
	for stuff in info:
		print(stuff)

def getRestaurantsByZipandGrade( db, zip, grade ):
	print("Restaurants with the zipcode and grade:", zip, grade)
	info = db.restaurants.find( {"address.zipcode": zip, "grades.0.grade": grade})
	print(info)
	for stuff in info:
		print(stuff)

def getRestaurantsByZipandScore( db, zip, score ):
	print("Restaurants with the zipcode and less score than:", zip, score)
	info = db.restaurants.find( {"address.zipcode": zip, "grades.0.score": {"$lt": int(score)}})
	print(info)
	for stuff in info:
		print(stuff)

#getRestaurantsByZipandScore(db, "10024", "3")
#getRestaurantsByZipandGrade(db, "10024", "B")
#getRestaurantsByZip(db, "10024")
getRestaurantsByBorough(db, "Brooklyn")
