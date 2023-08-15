"""This file is used to connect to the database and create a collection."""
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://admin:test1234@film.ld35bwf.mongodb.net/?retryWrites=true&w=majority")

db = client.film_db

collection_name = db["films_collection"]
