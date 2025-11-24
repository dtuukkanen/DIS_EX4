"""Delete Operations Module"""


class DeleteOperations:
    """Handles deleting data from databases"""
    
    def __init__(self, db_manager):
        self.db = db_manager

    def delete_order(self):
        """Delete order - handles both DBs"""
        order_id = input("Enter Order ID to delete: ")

        confirm = input(f"Delete order {order_id}? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Cancelled.")
            return

        # Delete from PostgreSQL
        try:
            cur = self.db.postgres_conn.cursor()
            cur.execute("DELETE FROM orders WHERE order_id = %s", (order_id,))
            pg_deleted = cur.rowcount
            self.db.postgres_conn.commit()
            cur.close()
            if pg_deleted > 0:
                print(f"✓ Order {order_id} deleted from main system")
        except Exception as e:
            self.db.postgres_conn.rollback()
            print(f"Error: {e}")

        # Delete from MongoDB
        try:
            result = self.db.mongo_db.orders.delete_one({"order_id": order_id})
            if result.deleted_count > 0:
                print(f"✓ Order {order_id} deleted from analytics")
        except Exception as e:
            print(f"Note: {e}")

    def delete_customer(self):
        """Delete customer from both DBs"""
        customer_id = input("Enter Customer ID to delete: ")

        confirm = input(f"Delete customer {customer_id}? This will remove all their data. (yes/no): ")
        if confirm.lower() != 'yes':
            print("Cancelled.")
            return

        # Delete from PostgreSQL
        try:
            cur = self.db.postgres_conn.cursor()
            cur.execute("DELETE FROM customers WHERE customer_id = %s", (customer_id,))
            pg_deleted = cur.rowcount
            self.db.postgres_conn.commit()
            cur.close()
            if pg_deleted > 0:
                print(f"✓ Customer {customer_id} deleted from main system")
        except Exception as e:
            self.db.postgres_conn.rollback()
            print(f"Error: {e}")

        # Delete from MongoDB
        try:
            result = self.db.mongo_db.customers.delete_one({"customer_id": customer_id})
            if result.deleted_count > 0:
                print(f"✓ Customer {customer_id} loyalty data removed")
        except Exception as e:
            print(f"Note: {e}")

    def delete_review(self):
        """Delete review (MongoDB only)"""
        review_id = input("Enter Review ID to delete: ")

        confirm = input(f"Delete review {review_id}? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Cancelled.")
            return

        try:
            result = self.db.mongo_db.reviews.delete_one({"review_id": review_id})
            if result.deleted_count > 0:
                print(f"✓ Review {review_id} deleted")
            else:
                print("Review not found")
        except Exception as e:
            print(f"Error: {e}")

    def delete_menu_item(self):
        """Delete menu item from both databases"""
        item_id = input("Enter Item ID to delete: ")

        confirm = input(f"Delete menu item {item_id}? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Cancelled.")
            return

        # Delete from PostgreSQL
        try:
            cur = self.db.postgres_conn.cursor()
            cur.execute("DELETE FROM menu_items WHERE item_id = %s", (item_id,))
            pg_deleted = cur.rowcount
            self.db.postgres_conn.commit()
            cur.close()
            if pg_deleted > 0:
                print(f"✓ Menu item {item_id} deleted from ordering system")
        except Exception as e:
            self.db.postgres_conn.rollback()
            print(f"Error: {e}")

        # Delete from MongoDB
        try:
            result = self.db.mongo_db.menu_items.delete_one({"item_id": item_id})
            if result.deleted_count > 0:
                print(f"✓ Menu item {item_id} nutritional data removed")
        except Exception as e:
            print(f"Note: {e}")
