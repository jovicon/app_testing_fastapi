from starlette.testclient import TestClient
from random import randint
import requests

from app.main import app
client = TestClient(app)


def test_get_pokemon_by_id ():
    random_pokemon_id = randint(0, 890)
    
    response = client.get("/pokemons/"+str(random_pokemon_id))

    assert response.status_code == 200
    assert response.json()


def test_get_pokemon_by_bad_id ():
    random_pokemon_id = randint(892, 1000)
    
    response = client.get("/pokemons/"+str(random_pokemon_id))

    assert response.status_code == 404
    assert response.json() == { "detail": "Pokemon not found" }


def test_get_pokemon_by_bad_string_id ():
    response = client.get("/pokemons/any_text_here")

    assert response.status_code == 422
    assert response.json() == { "detail": [ { "loc": [ "path", "pokemon_id" ], "msg": "value is not a valid integer", "type": "type_error.integer" } ] }