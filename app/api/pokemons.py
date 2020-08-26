import requests
from typing import List

from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

@router.get("/pokemons/{pokemon_id}")
def get_pokemon_by_id(pokemon_id: int):
    """
    Get pokemon data by id

    Read data for a specific pokemon consuming from pokeapi
    
    Doesn't require authentication
    """
    url = "https://pokeapi.co/api/v2/pokemon/" + str(pokemon_id)
    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Pokemon not found")

    return response.json()