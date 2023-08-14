from typing import Union
from fastapi import FastAPI
from .routers import routers
from dotenv import dotenv_values
from pymongo import MongoClient

config = dotenv_values(".env")
app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGODB_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

for router in routers:
    app.include_router(
        router=router['router'],
        prefix=router['prefix'],
        tags=router['tags']
    )

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
