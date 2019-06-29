import os

from migrate.versioning import api

from database.database_helper import get_database_url
from settings import settings


def migrate():
    if not os.path.exists(settings.DATABASE_MIGRATION):
        api.create(settings.DATABASE_MIGRATION, settings.DATABASE_MIGRATION_NAME)
        api.version_control(get_database_url(), settings.DATABASE_MIGRATION)

    api.upgrade(get_database_url(), settings.DATABASE_MIGRATION)
