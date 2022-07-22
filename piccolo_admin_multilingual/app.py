from fastapi.applications import FastAPI
from piccolo.apps.user.tables import BaseUser
from piccolo.columns.column_types import Varchar
from piccolo.engine.sqlite import SQLiteEngine
from piccolo.table import create_db_tables_sync
from piccolo.table import Table
from piccolo_admin.endpoints import create_admin
from piccolo_api.session_auth.tables import SessionsBase

from fastapi import FastAPI


DB = SQLiteEngine(path="translation_demo.sqlite")


class User(BaseUser, db=DB, tablename="piccolo_user"):
    pass


class Sessions(SessionsBase, db=DB):
    pass


class ExampleTable(Table, db=DB):
    name = Varchar()


def setup():
    create_db_tables_sync(ExampleTable, User, Sessions, if_not_exists=True)

    if not User.exists().where(User.username == "piccolo").run_sync():
        User.create_user_sync(
            username="piccolo",
            password="piccolo123",
            admin=True,
            superuser=True,
            active=True,
        )


from piccolo_admin.translations.data import ENGLISH, WELSH

app = FastAPI(on_startup=[setup])
app.mount(
    "/",
    create_admin(
        tables=[ExampleTable],
        auth_table=User,
        session_table=Sessions,
        default_language_code="en",
        translations=[ENGLISH, WELSH],
    ),
)
