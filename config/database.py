"""This file is used to connect to the database and create a collection."""
from pymongo import MongoClient

client = MongoClient(
    "") #put your MongoDB URI

db = client.film_db

collection_name = db["films_collection"]
