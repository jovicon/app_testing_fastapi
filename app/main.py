from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
# from sqlalchemy.orm import Session

from .api import pokemons

app = FastAPI()

app.include_router(pokemons.router, tags=["pokemons"])

# testing fast api
@app.post("/hello_world")
def hello_world():
    """
    hello world! post.
    """
    return {
        "message": "hello world!"
    }