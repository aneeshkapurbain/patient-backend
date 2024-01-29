import  json
from dotenv import load_dotenv
load_dotenv()

import os

try:
    # below condition is for remote databases
    DB_CREDENTIAL = os.environ.get('DB_CREDENTIALS')
    if DB_CREDENTIAL:
        database_environment = json.loads(os.environ['DB_CREDENTIALS'])
        DB_USER = database_environment.get("username")
        DB_PASS = database_environment.get("password")
        DB_PORT = database_environment.get("POSTGRES_PORT", "5432")
        DB_NAME = database_environment.get("POSTGRES_DB_NAME", "postgres")
        DB_HOST = database_environment.get("DB_HOSTNAME")
        if not DB_HOST:
            raise Exception("DB_HOST environment variable is mandatory")
    else:
        # below condition is for local databases
        ENVIRONMENT = os.environ
        DB_USER = ENVIRONMENT.get("POSTGRES_USER")
        DB_PASS = ENVIRONMENT.get("POSTGRES_PASSWORD")
        DB_PORT = ENVIRONMENT.get("POSTGRES_PORT", "5432")
        DB_NAME = ENVIRONMENT.get("POSTGRES_DB_NAME", "postgres")
        DB_HOST = ENVIRONMENT.get("DB_HOSTNAME")
except Exception as e:
    raise e

try:
    PATIENT_DATABASE = type(
        "PATIENT_DATABASE",
        (object,),
        {
            "DB_USER": DB_USER,
            "DB_PASS": DB_PASS,
            "DB_HOST": DB_HOST,
            "DB_PORT": DB_PORT,
            "DB_NAME": DB_NAME
        },
    )
    print("Current Env Variables are as follows:")
    print(f"DB_USER : {DB_USER}"),
    print(f"DB_HOST : {DB_HOST}"),
    print(f"DB_PORT : {DB_PORT}"),
    print(f"DB_NAME : {DB_NAME}")
except Exception as e:
    print("Required Environment variables not found")
    print(str(e))
    raise e
