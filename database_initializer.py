from sqlalchemy.orm import sessionmaker


class DatabaseInitializer():
    def __init__(self, engine):
        self.engine = engine
        self.session = None

    def __enter__(self):
        self.session = sessionmaker(expire_on_commit=False, bind=self.engine)()
        return self.session

    def __exit__(self, type, value, traceback):
        self.session.close()
        self.engine.dispose()
