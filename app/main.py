from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

app = FastAPI()

@app.post("/test")
def test():
    """
    Testing post.
    """
    return {
        "test": "hello world"
    }