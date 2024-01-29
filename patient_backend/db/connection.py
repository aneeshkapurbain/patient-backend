from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from patient_backend.core.config import PATIENT_DATABASE


# make db connection
class DBConnection:
    def __init__(self):
        """ Initialize db connection
        """
        # sql conn string
        self.sql_conn_url = self.get_sql_conn_str()

        # create engine
        self.engine = create_engine(self.sql_conn_url, connect_args={}, pool_size=50)

        # Initialize session
        self.SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )
        print(f"connection successful to database with url ${self.sql_conn_url} ")

    @staticmethod
    def get_sql_conn_str():
        """ class method to get conn string w/o db """
        HOST = PATIENT_DATABASE.DB_HOST
        print("@@@@@@", HOST)

        # handling local vs live connections
        if PATIENT_DATABASE.DB_HOST == 'postgres':
            return (f"postgresql://{PATIENT_DATABASE.DB_USER}:{PATIENT_DATABASE.DB_PASS}@{PATIENT_DATABASE.DB_HOST}"
                    f"/{PATIENT_DATABASE.DB_NAME}")
        return (f"postgresql://{PATIENT_DATABASE.DB_USER}:{PATIENT_DATABASE.DB_PASS}@{PATIENT_DATABASE.DB_HOST}"
                f":{PATIENT_DATABASE.DB_PORT}/{PATIENT_DATABASE.DB_NAME}")

    @classmethod
    def get_base(cls):
        """ class method to return declarative base """
        return declarative_base()

    def get_db(self):
        # yield db connection object
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()
