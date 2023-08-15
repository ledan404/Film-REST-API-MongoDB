"""This module contains the routes of the API"""
from bson import ObjectId
from fastapi import APIRouter

from config.database import collection_name
from models.film import Film
from schema.schemas import indevidual_serial, serial_films

router = APIRouter()


@router.get("/")
async def get_films():
    """This function is used to get all the films from the database."""
    films = serial_films(collection_name.find())
    return films


@router.get("/{id}")
async def get_film(id: str):# pylint: disable=[invalid-name, redefined-builtin]
    """This function is used to get a film from the database."""
    film = indevidual_serial(collection_name.find_one({"_id": ObjectId(id)}))
    return film


@router.post("/")
async def post_film(film: Film):
    """This function is used to post a film to the database."""
    collection_name.insert_one(dict(film))


@router.put("/{id}")
async def update_film(id: str, film: Film):# pylint: disable=[invalid-name, redefined-builtin]
    """This function is used to update a film in the database."""
    collection_name.update_one({"_id": ObjectId(id)}, {"$set": dict(film)})


@router.delete("/{id}")
async def delete_film(id: str):# pylint: disable=[invalid-name, redefined-builtin]
    """This function is used to delete a film from the database."""
    collection_name.delete_one({"_id": ObjectId(id)})
