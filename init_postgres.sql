-- PostgreSQL Database Initialization for Restaurant Management System
--
-- SIMILAR TABLES (exist in both PG and Mongo): orders, customers, menu_items
-- DIFFERENT TABLES (only in PG): restaurants, staff
--
-- Drop tables if they exist
DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS menu_items CASCADE;
DROP TABLE IF EXISTS restaurants CASCADE;
DROP TABLE IF EXISTS staff CASCADE;

-- Create Customers table (Similar to MongoDB customers but with different attributes)
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    customer_id VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20),
    address TEXT,
    registration_date DATE DEFAULT CURRENT_DATE
);

-- Create Restaurants table (Postgres only)
CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY,
    restaurant_id VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(200),
    cuisine_type VARCHAR(50),
    opening_hours VARCHAR(100),
    rating DECIMAL(3,2)
);

-- Create Menu Items table (Postgres only)
CREATE TABLE menu_items (
    id SERIAL PRIMARY KEY,
    item_id VARCHAR(50) UNIQUE NOT NULL,
    restaurant_id VARCHAR(50) REFERENCES restaurants(restaurant_id),
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2),
    description TEXT,
    available BOOLEAN DEFAULT TRUE
);

-- Create Staff table (Postgres only)
CREATE TABLE staff (
    id SERIAL PRIMARY KEY,
    staff_id VARCHAR(50) UNIQUE NOT NULL,
    restaurant_id VARCHAR(50) REFERENCES restaurants(restaurant_id),
    name VARCHAR(100) NOT NULL,
    position VARCHAR(50),
    hire_date DATE,
    salary DECIMAL(10,2)
);

-- Create Orders table (Similar to MongoDB orders but with different attributes)
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    order_id VARCHAR(50) UNIQUE NOT NULL,
    customer_id VARCHAR(50) REFERENCES customers(customer_id),
    restaurant_id VARCHAR(50) REFERENCES restaurants(restaurant_id),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10,2),
    status VARCHAR(20),
    delivery_address TEXT
);

-- Insert sample data
-- Restaurants
INSERT INTO restaurants (restaurant_id, name, location, cuisine_type, opening_hours, rating) VALUES
('R001', 'Italian Bistro', '123 Main St, Downtown', 'Italian', '11:00-22:00', 4.5),
('R002', 'Sushi Palace', '456 Oak Ave, Uptown', 'Japanese', '12:00-23:00', 4.8),
('R003', 'Burger Haven', '789 Pine Rd, Midtown', 'American', '10:00-21:00', 4.2),
('R004', 'Thai Spice', '321 Elm St, Eastside', 'Thai', '11:30-22:30', 4.6),
('R005', 'French Delight', '654 Maple Dr, Westside', 'French', '17:00-23:00', 4.9);

-- Customers
INSERT INTO customers (customer_id, name, email, phone, address, registration_date) VALUES
('C001', 'John Smith', 'john.smith@email.com', '555-0101', '100 First St, Apt 1A', '2024-01-15'),
('C002', 'Emma Johnson', 'emma.j@email.com', '555-0102', '200 Second Ave, Unit 2B', '2024-02-20'),
('C003', 'Michael Brown', 'mbrown@email.com', '555-0103', '300 Third Blvd, Suite 3C', '2024-03-10'),
('C004', 'Sarah Davis', 'sarah.d@email.com', '555-0104', '400 Fourth St, Room 4D', '2024-04-05'),
('C005', 'James Wilson', 'jwilson@email.com', '555-0105', '500 Fifth Ave, Floor 5E', '2024-05-12'),
('C006', 'Lisa Anderson', 'l.anderson@email.com', '555-0106', '600 Sixth Rd, Apt 6F', '2024-06-18');

-- Menu Items
INSERT INTO menu_items (item_id, restaurant_id, name, category, price, description, available) VALUES
('M001', 'R001', 'Margherita Pizza', 'Main Course', 12.99, 'Classic pizza with tomato and mozzarella', TRUE),
('M002', 'R001', 'Spaghetti Carbonara', 'Main Course', 14.99, 'Creamy pasta with bacon', TRUE),
('M003', 'R001', 'Tiramisu', 'Dessert', 6.99, 'Italian coffee-flavored dessert', TRUE),
('M004', 'R002', 'California Roll', 'Sushi', 8.99, 'Crab, avocado, cucumber roll', TRUE),
('M005', 'R002', 'Salmon Sashimi', 'Sashimi', 15.99, 'Fresh salmon slices', TRUE),
('M006', 'R002', 'Miso Soup', 'Appetizer', 3.99, 'Traditional Japanese soup', TRUE),
('M007', 'R003', 'Classic Burger', 'Main Course', 10.99, 'Beef patty with lettuce and tomato', TRUE),
('M008', 'R003', 'French Fries', 'Side', 4.99, 'Crispy golden fries', TRUE),
('M009', 'R003', 'Milkshake', 'Beverage', 5.99, 'Vanilla, chocolate, or strawberry', TRUE),
('M010', 'R004', 'Pad Thai', 'Main Course', 13.99, 'Stir-fried rice noodles', TRUE),
('M011', 'R004', 'Green Curry', 'Main Course', 14.99, 'Spicy coconut curry', TRUE),
('M012', 'R005', 'Coq au Vin', 'Main Course', 22.99, 'Chicken braised in wine', TRUE);

-- Staff
INSERT INTO staff (staff_id, restaurant_id, name, position, hire_date, salary) VALUES
('S001', 'R001', 'Mario Rossi', 'Head Chef', '2020-03-15', 55000.00),
('S002', 'R001', 'Anna Bianchi', 'Waiter', '2021-06-20', 32000.00),
('S003', 'R002', 'Yuki Tanaka', 'Sushi Chef', '2019-08-10', 60000.00),
('S004', 'R002', 'Hiro Nakamura', 'Manager', '2020-01-05', 50000.00),
('S005', 'R003', 'Bob Miller', 'Cook', '2021-11-12', 35000.00),
('S006', 'R003', 'Alice Cooper', 'Cashier', '2022-02-28', 28000.00),
('S007', 'R004', 'Som Chai', 'Head Chef', '2019-05-20', 52000.00),
('S008', 'R005', 'Pierre Dubois', 'Executive Chef', '2018-04-15', 70000.00);

-- Orders
INSERT INTO orders (order_id, customer_id, restaurant_id, order_date, total_amount, status, delivery_address) VALUES
('O001', 'C001', 'R001', '2024-11-01 12:30:00', 34.97, 'Delivered', '100 First St, Apt 1A'),
('O002', 'C002', 'R002', '2024-11-02 18:45:00', 28.97, 'Delivered', '200 Second Ave, Unit 2B'),
('O003', 'C003', 'R003', '2024-11-03 13:15:00', 21.97, 'Delivered', '300 Third Blvd, Suite 3C'),
('O004', 'C001', 'R004', '2024-11-04 19:20:00', 28.98, 'Delivered', '100 First St, Apt 1A'),
('O005', 'C004', 'R001', '2024-11-05 12:00:00', 27.98, 'In Progress', '400 Fourth St, Room 4D'),
('O006', 'C005', 'R002', '2024-11-06 20:30:00', 24.98, 'Pending', '500 Fifth Ave, Floor 5E'),
('O007', 'C002', 'R005', '2024-11-07 19:00:00', 22.99, 'Delivered', '200 Second Ave, Unit 2B'),
('O008', 'C006', 'R003', '2024-11-08 14:30:00', 16.98, 'Delivered', '600 Sixth Rd, Apt 6F');

-- Create indexes for better performance
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_orders_restaurant ON orders(restaurant_id);
CREATE INDEX idx_menu_restaurant ON menu_items(restaurant_id);
CREATE INDEX idx_staff_restaurant ON staff(restaurant_id);

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO pguser;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO pguser;

