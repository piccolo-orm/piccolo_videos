from piccolo.engine.postgres import PostgresEngine

from piccolo.conf.apps import AppRegistry


DB = PostgresEngine(
    config={
        "database": "m2m_demo",
        "user": "postgres",
        "password": "",
        "host": "localhost",
        "port": 5432,
    }
)

APP_REGISTRY = AppRegistry(
    apps=["music.piccolo_app", "piccolo_admin.piccolo_app"]
)
