from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# -----------------------------------
# CORS — required because 03_api.html is opened as a local file,
# not served from localhost:8000. Without this, the browser blocks
# the fetch() calls with a CORS error. allow_origins=["*"] is fine
# for this throwaway test; never use "*" in a real deployed app.
# -----------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------
# GET /hello — matches the fetch() in 03_api.html
# -----------------------------------

@app.get("/hello")
def hello():
    return {"message": "Hello"}

# -----------------------------------
# POST /users — matches the fetch() POST in 03_api.html
# -----------------------------------

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    return user