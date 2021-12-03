"""
Import all of the Tables subclasses in your app here, and register them with
the APP_CONFIG.
"""

import os

from piccolo.conf.apps import AppConfig, table_finder

from movies.commands.generate_data import generate_data


CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


APP_CONFIG = AppConfig(
    app_name="movies",
    migrations_folder_path=os.path.join(CURRENT_DIRECTORY, "piccolo_migrations"),
    table_classes=table_finder(modules=["movies.tables"]),
    migration_dependencies=[],
    commands=[generate_data],
)
