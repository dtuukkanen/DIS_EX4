"""
Database Connection Manager
Handles connections to PostgreSQL and MongoDB
"""

from pymongo import MongoClient
import psycopg
from src import config


class DatabaseManager:
    """Manages database connections"""
    
    def __init__(self):
        self.mongo_db = None
        self.postgres_conn = None
        self.connect_databases()

    def connect_databases(self):
        """Connect to both databases"""
        try:
            client = MongoClient(config.MONGO_CLIENT_STRING)
            self.mongo_db = client[config.DB_NAME]
            print("✓ MongoDB connected")
        except Exception as e:
            print(f"✗ MongoDB connection failed: {e}")

        try:
            self.postgres_conn = psycopg.connect(config.POSTGRES_CONN_STRING)
            print("✓ PostgreSQL connected")
        except Exception as e:
            print(f"✗ PostgreSQL connection failed: {e}")

    def close_connections(self):
        """Close database connections"""
        if self.postgres_conn is not None:
            self.postgres_conn.close()
        print("Database connections closed.")

    def is_connected(self):
        """Check if both databases are connected"""
        return self.mongo_db is not None and self.postgres_conn is not None
