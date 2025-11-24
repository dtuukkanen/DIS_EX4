"""
Restaurant Management System - Unified Frontend
This system seamlessly integrates PostgreSQL and MongoDB databases
User doesn't know which database they're interacting with
"""

from src import config
from src.database import DatabaseManager
from src.operations.views import ViewOperations
from src.operations import AddOperations, DeleteOperations, UpdateOperations
from src.menu_ui import MenuUI


class RestaurantSystem:
    def __init__(self):
        self.db = DatabaseManager()
        self.views = ViewOperations(self.db)
        self.add_ops = AddOperations(self.db)
        self.delete_ops = DeleteOperations(self.db)
        self.update_ops = UpdateOperations(self.db)
        self.menu = MenuUI()

    def close_connections(self):
        """Close database connections"""
        self.db.close_connections()

    # ==================== VIEW DATA ====================

    def view_data(self):
        """View data from databases - user sees unified view"""
        self.menu.show_view_menu()
        choice = input("\nSelect option: ")

        if choice == '1':
            self.views.view_orders_joined()
        elif choice == '2':
            self.views.view_customers_joined()
        elif choice == '3':
            self.views.view_menu_items_joined()
        elif choice == '4':
            self.views.view_restaurants()
        elif choice == '5':
            self.views.view_staff()
        elif choice == '6':
            self.views.view_reviews()
        elif choice == '7':
            self.views.view_promotions()

    # ==================== INSERT DATA ====================

    def add_entry(self):
        """Add new entry - user doesn't know which DB"""
        self.menu.show_categories()
        choice = input("\nSelect category to add to: ")

        if choice not in config.ALL_CATEGORIES:
            print("Invalid choice!")
            return

        category_info = config.ALL_CATEGORIES[choice]
        category_name = category_info['name']

        print(f"\n--- Adding to {category_name} ---")

        if category_name == "Orders":
            self.add_ops.add_order()
        elif category_name == "Customers":
            self.add_ops.add_customer()
        elif category_name == "Menu Items":
            self.add_ops.add_menu_item()
        elif category_name == "Reviews":
            self.add_ops.add_review()
        elif category_name == "Promotions":
            self.add_ops.add_promotion()
        else:
            print("Adding to this category not implemented in demo.")

    # ==================== DELETE DATA ====================

    def delete_entry(self):
        """Delete entry - user doesn't know which DB"""
        self.menu.show_categories()
        choice = input("\nSelect category to delete from: ")

        if choice not in config.ALL_CATEGORIES:
            print("Invalid choice!")
            return

        category_info = config.ALL_CATEGORIES[choice]
        category_name = category_info['name']

        print(f"\n--- Deleting from {category_name} ---")

        if category_name == "Orders":
            self.delete_ops.delete_order()
        elif category_name == "Customers":
            self.delete_ops.delete_customer()
        elif category_name == "Menu Items":
            self.delete_ops.delete_menu_item()
        elif category_name == "Reviews":
            self.delete_ops.delete_review()
        else:
            print("Delete for this category not implemented in demo.")

    # ==================== UPDATE DATA ====================

    def update_entry(self):
        """Update entry - user doesn't know which DB"""
        self.menu.show_categories()
        choice = input("\nSelect category to update: ")

        if choice not in config.ALL_CATEGORIES:
            print("Invalid choice!")
            return

        category_info = config.ALL_CATEGORIES[choice]
        category_name = category_info['name']

        print(f"\n--- Updating {category_name} ---")

        if category_name == "Orders":
            self.update_ops.update_order()
        elif category_name == "Customers":
            self.update_ops.update_customer()
        elif category_name == "Reviews":
            self.update_ops.update_review()
        elif category_name == "Menu Items":
            self.update_ops.update_menu_item()
        elif category_name == "Promotions":
            self.update_ops.update_promotion()
        else:
            print("Update for this category not implemented in demo.")

    def run(self):
        """Main program loop"""
        if not self.db.is_connected():
            print("Failed to connect to databases. Exiting...")
            return

        print("\nWelcome to the Restaurant Management System!")
        print("Managing data seamlessly across the system...")

        while True:
            self.menu.show_main_menu()
            choice = input("\nSelect option: ")

            if choice == '1':
                self.view_data()
            elif choice == '2':
                self.add_entry()
            elif choice == '3':
                self.delete_entry()
            elif choice == '4':
                self.update_entry()
            elif choice == '0':
                print("\nExiting system...")
                self.close_connections()
                print("Goodbye!")
                break
            else:
                print("Invalid option!")


def main():
    """Entry point for the application"""
    system = RestaurantSystem()
    system.run()


if __name__ == "__main__":
    main()


