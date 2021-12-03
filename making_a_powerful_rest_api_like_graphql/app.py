from fastapi import FastAPI
from piccolo_api.crud.endpoints import PiccoloCRUD
from piccolo_api.fastapi.endpoints import FastAPIWrapper

from movies.tables import Movie


app = FastAPI()


FastAPIWrapper(
    "/movies/",
    app,
    PiccoloCRUD(Movie, read_only=True, exclude_secrets=True, max_joins=1),
)
