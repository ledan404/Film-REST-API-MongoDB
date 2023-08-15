"""Film model"""
from typing import List

from pydantic import BaseModel


class Film(BaseModel):
    """Film model"""
    title: str
    actors: List[str]
    rating: float
    description: str
    facts: List[str]
