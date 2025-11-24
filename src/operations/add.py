"""Add Operations Module"""

from datetime import datetime


class AddOperations:
    """Handles adding/inserting data into databases"""
    
    def __init__(self, db_manager):
        self.db = db_manager

    def add_order(self):
        """Add order - asks which DB or both"""
        print("Note: Orders exist in both databases")
        print("1. Add to system (auto-select)")
        print("2. Add to both databases")
        choice = input("Select: ")

        order_id = input("Order ID (e.g., O009): ")
        customer_id = input("Customer ID (e.g., C001): ")
        restaurant_id = input("Restaurant ID (e.g., R001): ")
        while True:
            total_input = input("Total amount: ")
            try:
                total = float(total_input)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the total amount.")

        if choice == '1' or choice == '2':
            # Add to PostgreSQL
            try:
                cur = self.db.postgres_conn.cursor()
                status = input("Status (Pending/In Progress/Delivered): ")
                address = input("Delivery address: ")

                cur.execute("""
                    INSERT INTO orders (order_id, customer_id, restaurant_id, total_amount, status, delivery_address)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (order_id, customer_id, restaurant_id, total, status, address))
                self.db.postgres_conn.commit()
                print("✓ Order added to system")
                cur.close()
            except Exception as e:
                self.db.postgres_conn.rollback()
                print(f"Error: {e}")

        if choice == '2':
            # Add to MongoDB too
            try:
                payment = input("Payment method: ")
                while True:
                    tip_input = input("Tip amount: ")
                    try:
                        tip = float(tip_input)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a numeric value for the tip amount.")

                order_doc = {
                    "order_id": order_id,
                    "customer_id": customer_id,
                    "restaurant_id": restaurant_id,
                    "order_date": datetime.now(),
                    "items": [],  # Simplified
                    "total_amount": total,
                    "payment_method": payment,
                    "tip_amount": tip,
                    "status": "Pending",
                    "customer_rating": None
                }
                self.db.mongo_db.orders.insert_one(order_doc)
                print("✓ Order also added to analytics system")
            except Exception as e:
                print(f"Error: {e}")

    def add_customer(self):
        """Add customer - user doesn't know it goes to both DBs"""
        print("Adding new customer to system...")

        customer_id = input("Customer ID (e.g., C012): ")
        name = input("Customer name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        address = input("Address: ")

        # Add to PostgreSQL
        try:
            cur = self.db.postgres_conn.cursor()
            cur.execute("""
                INSERT INTO customers (customer_id, name, email, phone, address)
                VALUES (%s, %s, %s, %s, %s)
            """, (customer_id, name, email, phone, address))
            self.db.postgres_conn.commit()
            cur.close()
            print("✓ Customer registered in main system")
        except Exception as e:
            self.db.postgres_conn.rollback()
            print(f"Error: {e}")
            return

        # Automatically add to MongoDB too (same columns, user doesn't know)
        try:
            customer_doc = {
                "customer_id": customer_id,
                "name": name,
                "email": email,
                "phone": phone,
                "address": address,
                "registration_date": datetime.now()
            }
            self.db.mongo_db.customers.insert_one(customer_doc)
            print("✓ Customer also registered in backup system")
        except Exception as e:
            print(f"Note: {e}")

    def add_menu_item(self):
        """Add menu item - same columns in both databases"""
        print("Adding new menu item...")

        item_id = input("Item ID (e.g., M023): ")
        restaurant_id = input("Restaurant ID: ")
        name = input("Item name: ")
        category = input("Category: ")
        while True:
            price_input = input("Price: ")
            try:
                price = float(price_input)
                break
            except ValueError:
                print("Invalid price. Please enter a numeric value.")
        description = input("Description: ")
        available = input("Available? (yes/no): ").lower() == 'yes'

        # Add to PostgreSQL
        try:
            cur = self.db.postgres_conn.cursor()
            cur.execute("""
                INSERT INTO menu_items (item_id, restaurant_id, name, category, price, description, available)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (item_id, restaurant_id, name, category, price, description, available))
            self.db.postgres_conn.commit()
            print("✓ Menu item added to ordering system")
            cur.close()
        except Exception as e:
            self.db.postgres_conn.rollback()
            print(f"Error: {e}")
            return

        # Also add to MongoDB (user doesn't know)
        try:
            menu_doc = {
                "item_id": item_id,
                "restaurant_id": restaurant_id,
                "name": name,
                "category": category,
                "price": price,
                "description": description,
                "available": available
            }
            self.db.mongo_db.menu_items.insert_one(menu_doc)
            print("✓ Menu item also added to backup system")
        except Exception as e:
            print(f"Note: {e}")

    def add_review(self):
        """Add review (MongoDB only)"""
        print("Adding new review...")

        try:
            review_id = input("Review ID (e.g., REV006): ")
            customer_id = input("Customer ID: ")
            restaurant_id = input("Restaurant ID: ")
            order_id = input("Order ID: ")
            while True:
                rating_input = input("Rating (1-5): ")
                try:
                    rating = int(rating_input)
                    if 1 <= rating <= 5:
                        break
                    else:
                        print("Error: Rating must be an integer between 1 and 5.")
                except ValueError:
                    print("Error: Please enter a valid integer for the rating.")
            comment = input("Comment: ")

            review_doc = {
                "review_id": review_id,
                "customer_id": customer_id,
                "restaurant_id": restaurant_id,
                "order_id": order_id,
                "rating": rating,
                "comment": comment,
                "review_date": datetime.now(),
                "helpful_count": 0
            }
            self.db.mongo_db.reviews.insert_one(review_doc)
            print("✓ Review added")
        except Exception as e:
            print(f"Error: {e}")

    def add_promotion(self):
        """Add promotion (MongoDB only)"""
        print("Adding new promotion...")

        try:
            promo_id = input("Promotion ID (e.g., PROMO007): ")
            restaurant_id = input("Restaurant ID: ")
            name = input("Promotion name: ")
            description = input("Description: ")
            discount = int(input("Discount percentage: "))

            promo_doc = {
                "promotion_id": promo_id,
                "restaurant_id": restaurant_id,
                "name": name,
                "description": description,
                "discount_percentage": discount,
                "start_date": datetime.now(),
                "end_date": datetime(2024, 12, 31),
                "active": True,
                "usage_count": 0
            }
            self.db.mongo_db.promotions.insert_one(promo_doc)
            print("✓ Promotion added")
        except Exception as e:
            print(f"Error: {e}")
