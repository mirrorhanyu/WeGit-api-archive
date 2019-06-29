from sqlalchemy import create_engine, pool

from database.database_helper import get_database_url


class DatabaseEngine:
    instance = None

    @staticmethod
    def fetch():
        if not DatabaseEngine.instance:
            DatabaseEngine.instance = _create_database_engine()
        return DatabaseEngine.instance


def create_database_engine():
    return DatabaseEngine.fetch()


def _create_database_engine():
    engine = create_engine(get_database_url(), echo=False, pool_size=0, poolclass=pool.QueuePool)
    return engine
