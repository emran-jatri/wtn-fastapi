from typing import Union
from fastapi import FastAPI
from .routers import routers

app = FastAPI()

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
