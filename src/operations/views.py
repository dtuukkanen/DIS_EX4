"""
View Operations Module
Handles all data viewing/reading operations
"""


class ViewOperations:
    """Handles viewing data from databases"""
    
    def __init__(self, db_manager):
        self.db = db_manager

    def view_orders_joined(self):
        """View orders from BOTH databases combined (same columns)"""
        print("\n" + "="*80)
        print("COMBINED ORDERS FROM BOTH DATABASES (Same Schema)")
        print("="*80)

        try:
            # Collect all orders with source tags
            all_orders = []
            
            # PostgreSQL orders
            cur = self.db.postgres_conn.cursor()
            cur.execute("SELECT order_id, customer_id, restaurant_id, order_date, total_amount, status FROM orders;")
            pg_rows = cur.fetchall()
            
            for row in pg_rows:
                all_orders.append({
                    'source': 'PG',
                    'order_id': row[0],
                    'customer_id': row[1],
                    'restaurant_id': row[2],
                    'order_date': str(row[3]),
                    'total_amount': row[4],
                    'status': row[5]
                })

            # MongoDB orders
            mongo_orders = list(self.db.mongo_db.orders.find())
            
            for order in mongo_orders:
                all_orders.append({
                    'source': 'MG',
                    'order_id': order['order_id'],
                    'customer_id': order['customer_id'],
                    'restaurant_id': order['restaurant_id'],
                    'order_date': order['order_date'].strftime('%Y-%m-%d %H:%M'),
                    'total_amount': order['total_amount'],
                    'status': order['status']
                })

            # Display all orders in unified format
            print(f"\n--- All Orders (Combined from both databases) ---")
            for order in all_orders:
                print(f"[{order['source']}] Order: {order['order_id']} | Customer: {order['customer_id']} | "
                      f"Restaurant: {order['restaurant_id']} | Date: {order['order_date']} | "
                      f"Total: ${order['total_amount']} | Status: {order['status']}")

            print(f"\n✓ Total combined orders: {len(all_orders)} ({len(pg_rows)} from PostgreSQL, {len(mongo_orders)} from MongoDB)")
            print("✓ Both databases have SAME columns, different data!")
            cur.close()
        except Exception as e:
            print(f"Error joining data: {e}")

    def view_customers_joined(self):
        """View customers from BOTH databases combined (same columns)"""
        print("\n" + "="*80)
        print("COMBINED CUSTOMERS FROM BOTH DATABASES (Same Schema)")
        print("="*80)

        try:
            # Collect all customers with source tags
            all_customers = []
            
            # PostgreSQL customers
            cur = self.db.postgres_conn.cursor()
            cur.execute("SELECT customer_id, name, email, phone, registration_date FROM customers;")
            pg_rows = cur.fetchall()
            
            for row in pg_rows:
                all_customers.append({
                    'source': 'PG',
                    'customer_id': row[0],
                    'name': row[1],
                    'email': row[2],
                    'phone': row[3],
                    'registration_date': str(row[4])
                })

            # MongoDB customers
            mongo_customers = list(self.db.mongo_db.customers.find())
            
            for cust in mongo_customers:
                all_customers.append({
                    'source': 'MG',
                    'customer_id': cust['customer_id'],
                    'name': cust['name'],
                    'email': cust['email'],
                    'phone': cust['phone'],
                    'registration_date': cust['registration_date'].strftime('%Y-%m-%d')
                })

            # Display all customers in unified format
            print(f"\n--- All Customers (Combined from both databases) ---")
            for cust in all_customers:
                print(f"[{cust['source']}] ID: {cust['customer_id']} | Name: {cust['name']} | "
                      f"Email: {cust['email']} | Phone: {cust['phone']} | Reg: {cust['registration_date']}")

            print(f"\n✓ Total combined customers: {len(all_customers)} ({len(pg_rows)} from PostgreSQL, {len(mongo_customers)} from MongoDB)")
            print("✓ Both databases have SAME columns, different data!")
            cur.close()
        except Exception as e:
            print(f"Error joining data: {e}")

    def view_menu_items_joined(self):
        """View menu items from BOTH databases combined (same columns)"""
        print("\n" + "="*80)
        print("COMBINED MENU ITEMS FROM BOTH DATABASES (Same Schema)")
        print("="*80)

        try:
            # Collect all menu items with source tags
            all_items = []
            
            # PostgreSQL menu items
            cur = self.db.postgres_conn.cursor()
            cur.execute("SELECT item_id, name, category, price, available FROM menu_items;")
            pg_rows = cur.fetchall()
            
            for row in pg_rows:
                all_items.append({
                    'source': 'PG',
                    'item_id': row[0],
                    'name': row[1],
                    'category': row[2],
                    'price': row[3],
                    'available': 'Available' if row[4] else 'Not Available'
                })

            # MongoDB menu items
            mongo_items = list(self.db.mongo_db.menu_items.find())
            
            for item in mongo_items:
                all_items.append({
                    'source': 'MG',
                    'item_id': item['item_id'],
                    'name': item['name'],
                    'category': item['category'],
                    'price': item['price'],
                    'available': 'Available' if item.get('available') else 'Not Available'
                })

            # Display all items in unified format
            print(f"\n--- All Menu Items (Combined from both databases) ---")
            for item in all_items:
                print(f"[{item['source']}] {item['item_id']} | {item['name']} | {item['category']} | "
                      f"${item['price']} | {item['available']}")

            print(f"\n✓ Total combined menu items: {len(all_items)} ({len(pg_rows)} from PostgreSQL, {len(mongo_items)} from MongoDB)")
            print("✓ Both databases have SAME columns, different data!")
            cur.close()
        except Exception as e:
            print(f"Error joining data: {e}")

    def view_restaurants(self):
        """View restaurants (PostgreSQL only)"""
        try:
            cur = self.db.postgres_conn.cursor()
            cur.execute("SELECT restaurant_id, name, location, cuisine_type, rating FROM restaurants;")
            rows = cur.fetchall()
            print(f"\n--- Restaurants ({len(rows)} restaurants) ---")
            for row in rows:
                print(f"ID: {row[0]} | {row[1]} | Location: {row[2]} | Type: {row[3]} | Rating: {row[4]}")
            cur.close()
        except Exception as e:
            print(f"Error: {e}")

    def view_staff(self):
        """View staff (PostgreSQL only)"""
        try:
            cur = self.db.postgres_conn.cursor()
            cur.execute("SELECT staff_id, name, position, restaurant_id FROM staff;")
            rows = cur.fetchall()
            print(f"\n--- Staff Members ({len(rows)} members) ---")
            for row in rows:
                print(f"ID: {row[0]} | Name: {row[1]} | Position: {row[2]} | Restaurant: {row[3]}")
            cur.close()
        except Exception as e:
            print(f"Error: {e}")

    def view_reviews(self):
        """View reviews (MongoDB only)"""
        try:
            reviews = self.db.mongo_db.reviews.find()
            print(f"\n--- Reviews ---")
            for review in reviews:
                print(f"ID: {review['review_id']} | Customer: {review['customer_id']} | "
                      f"Restaurant: {review['restaurant_id']} | Rating: {review['rating']}/5 | "
                      f"Comment: {review['comment'][:50]}...")
        except Exception as e:
            print(f"Error: {e}")

    def view_promotions(self):
        """View promotions (MongoDB only)"""
        try:
            promos = self.db.mongo_db.promotions.find()
            print(f"\n--- Promotions ---")
            for promo in promos:
                status = "Active" if promo['active'] else "Inactive"
                print(f"ID: {promo['promotion_id']} | {promo['name']} | "
                      f"Discount: {promo['discount_percentage']}% | "
                      f"Restaurant: {promo['restaurant_id']} | Status: {status}")
        except Exception as e:
            print(f"Error: {e}")
