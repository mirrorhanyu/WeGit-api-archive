from sqlalchemy.orm import sessionmaker


class DatabaseInitializer(object):
    session = None

    @staticmethod
    def initialize_session(engine):
        DatabaseInitializer.engine = engine
        DatabaseInitializer.Session = sessionmaker(expire_on_commit=False, bind=engine)
        DatabaseInitializer.session = DatabaseInitializer.Session()

    @staticmethod
    def destroy_session():
        DatabaseInitializer.session.close() if DatabaseInitializer.session else None
