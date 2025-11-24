"""Update Operations Module"""


class UpdateOperations:
    """Handles updating/modifying data in databases"""
    
    def __init__(self, db_manager):
        self.db = db_manager

    def update_order(self):
        """Update order status"""
        order_id = input("Enter Order ID to update: ")
        print("1. Update status")
        print("2. Update total amount")
        field_choice = input("Select: ")

        if field_choice == '1':
            new_status = input("New status (Pending/In Progress/Delivered): ")
            try:
                cur = self.db.postgres_conn.cursor()
                cur.execute("UPDATE orders SET status = %s WHERE order_id = %s",
                           (new_status, order_id))
                self.db.postgres_conn.commit()
                if cur.rowcount > 0:
                    print(f"✓ Order {order_id} status updated")
                cur.close()
            except Exception as e:
                self.db.postgres_conn.rollback()
                print(f"Error: {e}")

        elif field_choice == '2':
            while True:
                new_total_input = input("New total amount: ")
                try:
                    new_total = float(new_total_input)
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value for the total amount.")
            # Update in both databases
            try:
                cur = self.db.postgres_conn.cursor()
                cur.execute("UPDATE orders SET total_amount = %s WHERE order_id = %s",
                           (new_total, order_id))
                self.db.postgres_conn.commit()
                cur.close()
                print(f"✓ Order {order_id} total updated in main system")

                self.db.mongo_db.orders.update_one(
                    {"order_id": order_id},
                    {"$set": {"total_amount": new_total}}
                )
                print(f"✓ Order {order_id} total updated in analytics")
            except Exception as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error: {e}")

    def update_customer(self):
        """Update customer info"""
        customer_id = input("Enter Customer ID to update: ")
        print("1. Update email")
        print("2. Update phone")
        print("3. Update loyalty points")
        field_choice = input("Select: ")

        if field_choice == '1':
            new_email = input("New email: ")
            try:
                cur = self.db.postgres_conn.cursor()
                cur.execute("UPDATE customers SET email = %s WHERE customer_id = %s",
                           (new_email, customer_id))
                self.db.postgres_conn.commit()
                cur.close()

                self.db.mongo_db.customers.update_one(
                    {"customer_id": customer_id},
                    {"$set": {"email": new_email}}
                )
                print(f"✓ Customer {customer_id} email updated")
            except Exception as e:
                print(f"Error: {e}")


        elif field_choice == '2':
            new_phone = input("New phone: ")
            try:
                cur = self.db.postgres_conn.cursor()
                cur.execute("UPDATE customers SET phone = %s WHERE customer_id = %s",
                           (new_phone, customer_id))
                self.db.postgres_conn.commit()
                cur.close()

                self.db.mongo_db.customers.update_one(
                    {"customer_id": customer_id},
                    {"$set": {"phone": new_phone}}
                )
                print(f"✓ Customer {customer_id} phone updated")
            except Exception as e:
                print(f"Error: {e}")

        elif field_choice == '3':
            while True:
                points_input = input("New loyalty points: ")
                try:
                    points = int(points_input)
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value for loyalty points.")
            try:
                self.db.mongo_db.customers.update_one(
                    {"customer_id": customer_id},
                    {"$set": {"loyalty_points": points}}
                )
                print(f"✓ Customer {customer_id} loyalty points updated")
            except Exception as e:
                print(f"Error: {e}")

    def update_review(self):
        """Update review (MongoDB only)"""
        review_id = input("Enter Review ID to update: ")
        print("1. Update rating")
        print("2. Update comment")
        field_choice = input("Select: ")

        if field_choice == '1':
            while True:
                rating_input = input("New rating (1-5): ")
                try:
                    new_rating = int(rating_input)
                    if 1 <= new_rating <= 5:
                        break
                    else:
                        print("Error: Rating must be an integer between 1 and 5.")
                except ValueError:
                    print("Error: Please enter a valid integer between 1 and 5.")
            try:
                result = self.db.mongo_db.reviews.update_one(
                    {"review_id": review_id},
                    {"$set": {"rating": new_rating}}
                )
                if result.modified_count > 0:
                    print(f"✓ Review {review_id} rating updated")
            except Exception as e:
                print(f"Error: {e}")

        elif field_choice == '2':
            new_comment = input("New comment: ")
            try:
                result = self.db.mongo_db.reviews.update_one(
                    {"review_id": review_id},
                    {"$set": {"comment": new_comment}}
                )
                if result.modified_count > 0:
                    print(f"✓ Review {review_id} comment updated")
            except Exception as e:
                print(f"Error: {e}")

    def update_menu_item(self):
        """Update menu item in both databases (same columns)"""
        item_id = input("Enter Item ID to update: ")
        print("1. Update price (both databases)")
        print("2. Update availability (both databases)")
        field_choice = input("Select: ")

        if field_choice == '1':
            while True:
                new_price_input = input("New price: ")
                try:
                    new_price = float(new_price_input)
                    break
                except ValueError:
                    print("Invalid price. Please enter a numeric value.")
            # Update in both databases
            try:
                cur = self.db.postgres_conn.cursor()
                cur.execute("UPDATE menu_items SET price = %s WHERE item_id = %s",
                           (new_price, item_id))
                self.db.postgres_conn.commit()
                cur.close()

                self.db.mongo_db.menu_items.update_one(
                    {"item_id": item_id},
                    {"$set": {"price": new_price}}
                )
                print(f"✓ Menu item {item_id} price updated in both databases")
            except Exception as e:
                print(f"Error: {e}")

        elif field_choice == '2':
            available = input("Available? (yes/no): ").lower() == 'yes'
            try:
                cur = self.db.postgres_conn.cursor()
                cur.execute("UPDATE menu_items SET available = %s WHERE item_id = %s",
                           (available, item_id))
                self.db.postgres_conn.commit()
                cur.close()

                self.db.mongo_db.menu_items.update_one(
                    {"item_id": item_id},
                    {"$set": {"available": available}}
                )
                print(f"✓ Menu item {item_id} availability updated in both databases")
            except Exception as e:
                self.db.postgres_conn.rollback()
                print(f"Error: {e}")

    def update_promotion(self):
        """Update promotion (MongoDB only)"""
        promo_id = input("Enter Promotion ID to update: ")
        print("1. Update discount percentage")
        print("2. Activate/Deactivate")
        field_choice = input("Select: ")

        if field_choice == '1':
            while True:
                discount_input = input("New discount percentage: ")
                if discount_input.isdigit():
                    new_discount = int(discount_input)
                    break
                else:
                    print("Please enter a valid numeric discount percentage.")
            try:
                result = self.db.mongo_db.promotions.update_one(
                    {"promotion_id": promo_id},
                    {"$set": {"discount_percentage": new_discount}}
                )
                if result.modified_count > 0:
                    print(f"✓ Promotion {promo_id} discount updated")
            except Exception as e:
                print(f"Error: {e}")

        elif field_choice == '2':
            active = input("Activate? (yes/no): ").lower() == 'yes'
            try:
                result = self.db.mongo_db.promotions.update_one(
                    {"promotion_id": promo_id},
                    {"$set": {"active": active}}
                )
                if result.modified_count > 0:
                    status = "activated" if active else "deactivated"
                    print(f"✓ Promotion {promo_id} {status}")
            except Exception as e:
                print(f"Error: {e}")
