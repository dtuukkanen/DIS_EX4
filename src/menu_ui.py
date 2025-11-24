"""
Menu/UI Module
Handles user interface and menu displays
"""

from src import config


class MenuUI:
    """Handles menu display and user interaction"""
    
    def show_main_menu(self):
        """Display main menu"""
        print("\n" + "="*60)
        print("      RESTAURANT MANAGEMENT SYSTEM")
        print("="*60)
        print("1. View Data")
        print("2. Add New Entry")
        print("3. Delete Entry")
        print("4. Update Entry")
        print("0. Exit")
        print("="*60)

    def show_view_menu(self):
        """Display view data menu"""
        print("\n--- VIEW DATA ---")
        print("1. View Orders")
        print("2. View Customers")
        print("3. View Menu Items")
        print("4. View Restaurants")
        print("5. View Staff")
        print("6. View Reviews")
        print("7. View Promotions")

    def show_categories(self):
        """Show available categories"""
        print("\nAvailable Categories:")
        for key, info in config.ALL_CATEGORIES.items():
            print(f"{key}. {info['name']}")
