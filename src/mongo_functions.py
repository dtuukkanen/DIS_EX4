import pymongo
import config

def mongo_connect():
    """
    Function to connect to MongoDB database.
    :return:
    """
    try:
        client = pymongo.MongoClient(config.MONGO_CLIENT_STRING)
        db = client[config.DB_NAME]
        print("Connection to MongoDB database established.")
        return db
    except Exception as e:
        print(f"An error occurred while connecting to MongoDB database: {e}")
        return None

def mongo_print(cursor):
    """
    Function to print data from MongoDB database.
    :return:
    """
    pass

def mongo_insert(cursor):
    """
    Function to insert data into MongoDB database.
    :return:
    """
    pass

def mongo_delete(cursor):
    """
    Function to delete data from MongoDB database.
    :return:
    """
    pass

def mongo_modify(cursor):
    """
    Function to modify data in MongoDB database.
    :return:
    """
    pass
