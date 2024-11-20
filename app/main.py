""" HTTP REST API """
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_x():
    return {"Hello": "Mr. X"}
