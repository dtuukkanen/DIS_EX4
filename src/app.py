import mongo_functions as mongo
import postgres_functions as postgres

def menu():
    """
    Display the main menu and get user choice.
    :return: User's menu choice
    """
    print("1. Print data")
    print("2. Insert data")
    print("3. Delete data")
    print("4. Modify data")
    print("0. Exit")
    choice = input("Select an option: ")
    return choice

def database_menu():
    """
    Display the database selection menu and get user choice.
    :return: User's database choice
    """
    print("Select Database:")
    print("1. Database1 (Mongo)")
    print("2. Database2 (Postgres)")
    db_choice = input("Select a database: ")
    return db_choice

def main():
    """
    Main function to run the application.
    """
    # Initialize database connections
    mongo_cursor, postgres_cursor = initialize_databases()

    while True:
        choice = menu()

        # Print data
        if choice == '1':
            print("Printing data...")
            # Add logic to print data
            print_data()

        # Insert data
        elif choice == '2':
            print("Inserting data...")
            # Add logic to insert data
            insert_data()

        # Delete data
        elif choice == '3':
            print("Deleting data...")
            # Add logic to delete data
            delete_data()

        # Modify data
        elif choice == '4':
            print("Modifying data...")
            # Add logic to modify data
            modify_data()

        # Exit
        elif choice == '0':
            print("Exiting...")
            break

        # Invalid option
        else:
            print("Invalid option. Please try again.")

        print() # Print a newline for better readability

def initialize_databases():
    mongo_cursor = mongo.mongo_connect()
    postgres_cursor = postgres.postgres_connect()
    return mongo_cursor, postgres_cursor

def print_data():
    db_choice = database_menu()
    if db_choice == '1':
        mongo.print_data()
    elif db_choice == '2':
        postgres.print_data()
    else:
        print("Invalid database option.")

def insert_data():
    db_choice = database_menu()
    if db_choice == '1':
        mongo.insert_data()
    elif db_choice == '2':
        postgres.insert_data()
    else:
        print("Invalid database option.")

def delete_data():
    pass

def modify_data():
    pass

if __name__ == "__main__":
    main()
