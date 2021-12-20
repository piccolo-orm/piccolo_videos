from piccolo_admin.endpoints import create_admin
from starlette.routing import Mount
from fastapi import FastAPI

from music.piccolo_app import APP_CONFIG
from music.tables import Band, Genre


app = FastAPI(
    routes=[
        Mount(
            "/admin/",
            create_admin(
                tables=APP_CONFIG.table_classes,
            ),
        ),
    ],
)


@app.get("/")
async def bands():
    return await Band.select(Band.name, Band.genres(Genre.name, as_list=True))
