import requests
from typing import List

from fastapi import APIRouter, Depends

router = APIRouter()

@router.get("/pokemons/{pokemon_id}")
def get_pokemon_by_id(pokemon_id: str):
    """
    Get pokemon data by id

    Read data for a specific pokemon consuming from pokeapi
    
    Doesn't require authentication
    """
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_id
    response = requests.get(url)

    return response.json()