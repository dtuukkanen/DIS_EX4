# Database connection strings
MONGO_CLIENT_STRING = "mongodb://localhost:27017/"
POSTGRES_CONN_STRING = "dbname=restaurant_db user=pguser password=pgpassword host=localhost port=5432"

DB_NAME = "restaurant_db"

# PostgreSQL Tables (3 similar + 2 different)
# SIMILAR: orders, customers, menu_items (SAME COLUMNS, different data)
# DIFFERENT: restaurants, staff (only in PostgreSQL)
POSTGRES_TABLES = {
    "1": "orders",
    "2": "customers",
    "3": "menu_items",
    "4": "restaurants",
    "5": "staff"
}

# MongoDB Collections (3 similar + 2 different)
# SIMILAR: orders, customers, menu_items (SAME COLUMNS, different data)
# DIFFERENT: reviews, promotions (only in MongoDB)
MONGO_COLLECTIONS = {
    "1": "orders",
    "2": "customers",
    "3": "menu_items",
    "4": "reviews",
    "5": "promotions"
}

# Unified categories for user interface (user doesn't know about databases)
ALL_CATEGORIES = {
    "1": {"name": "Orders", "type": "both"},
    "2": {"name": "Customers", "type": "both"},
    "3": {"name": "Menu Items", "type": "both"},
    "4": {"name": "Restaurants", "type": "postgres"},
    "5": {"name": "Staff", "type": "postgres"},
    "6": {"name": "Reviews", "type": "mongo"},
    "7": {"name": "Promotions", "type": "mongo"}
}

