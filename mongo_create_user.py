import os
import pymongo

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv(".env"))

MONGO_INITDB_ROOT_USERNAME = os.environ.get("MONGO_INITDB_ROOT_USERNAME")
MONGO_INITDB_ROOT_PASSWORD = os.environ.get("MONGO_INITDB_ROOT_PASSWORD")
DB = 'admin'

def connect():
    try:
        conn = pymongo.MongoClient('mongodb://%s:%s@127.0.0.1/%s' % (MONGO_INITDB_ROOT_USERNAME, MONGO_INITDB_ROOT_PASSWORD, DB))
    except pymongo.errors.PyMongoError:
        log.error("Error connecting to database %s", database)
        return False

    return conn

def db_list():
    conn = connect()
    if not conn:
        return "Failed to connect to mongo database"

    try:
        return conn.list_database_names()
    except pymongo.errors.PyMongoError as err:
        print("Ooops")
        return str(err)

def user_create(database:str = DB, name: str = '', passwd:str = ''):

    roles=["read"]
    conn = connect()

    try:
        mdb = pymongo.database.Database(conn, database)
        mdb.command("createUser", name, pwd=passwd, roles=roles)
    except pymongo.errors.PyMongoError as err:
        log.error("Creating user %s failed with error: %s", name, err)
        return False

    return True

print(db_list())
#user_create(DB, 'abc', 'abc')