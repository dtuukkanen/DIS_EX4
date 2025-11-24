import psycopg
import config

def postgres_connect():
    """
    Function to connect to Postgres database.
    :return:
    """
    try:
        conn = psycopg.connect("dbname=wine_db user=pguser password=pgpassword host=localhost port=5432")
        print("Connection to Postgres database established.")
        return conn
    except Exception as e:
        print(f"An error occurred while connecting to Postgres database: {e}")
        return None

def postgres_print(cursor):
    """
    Function to print data from Postgres database.
    :return:
    """

def postgres_insert(cursor):
    """
    Function to insert data into Postgres database.
    :return:
    """
    pass

def postgres_delete(cursor):
    """
    Function to delete data from Postgres database.
    :return:
    """
    pass

def postgres_modify(cursor):
    """
    Function to modify data in Postgres database.
    :return:
    """
    pass
