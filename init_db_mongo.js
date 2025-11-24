// MongoDB initialization script for Restaurant Management System
//
// SIMILAR COLLECTIONS (exist in both PG and Mongo): orders, customers, menu_items
// DIFFERENT COLLECTIONS (only in Mongo): reviews, promotions
//

db = db.getSiblingDB('restaurant_db');

print("Initializing Restaurant Management Database...");

// Drop existing collections
db.orders.drop();
db.customers.drop();
db.menu_items.drop();
db.reviews.drop();
db.promotions.drop();

// Create Customers collection (Similar to PostgreSQL - SAME COLUMNS, different data)
db.customers.insertMany([
    {
        customer_id: "C007",
        name: "Robert Taylor",
        email: "r.taylor@email.com",
        phone: "555-0107",
        address: "700 Seventh St, Apt 7G",
        registration_date: new Date("2024-07-20")
    },
    {
        customer_id: "C008",
        name: "Jennifer White",
        email: "j.white@email.com",
        phone: "555-0108",
        address: "800 Eighth Ave, Unit 8H",
        registration_date: new Date("2024-08-15")
    },
    {
        customer_id: "C009",
        name: "David Martinez",
        email: "d.martinez@email.com",
        phone: "555-0109",
        address: "900 Ninth Blvd, Suite 9I",
        registration_date: new Date("2024-09-10")
    },
    {
        customer_id: "C010",
        name: "Maria Garcia",
        email: "m.garcia@email.com",
        phone: "555-0110",
        address: "1000 Tenth St, Room 10J",
        registration_date: new Date("2024-10-05")
    },
    {
        customer_id: "C011",
        name: "William Lee",
        email: "w.lee@email.com",
        phone: "555-0111",
        address: "1100 Eleventh Ave, Floor 11K",
        registration_date: new Date("2024-11-01")
    }
]);

// Create Orders collection (Similar to PostgreSQL - SAME COLUMNS, different data)
db.orders.insertMany([
    {
        order_id: "O009",
        customer_id: "C002",
        restaurant_id: "R002",
        order_date: new Date("2024-11-09T13:30:00"),
        total_amount: 45.50,
        status: "Delivered",
        delivery_address: "200 Second Ave, Unit 2B"
    },
    {
        order_id: "O010",
        customer_id: "C003",
        restaurant_id: "R004",
        order_date: new Date("2024-11-10T18:00:00"),
        total_amount: 32.75,
        status: "Delivered",
        delivery_address: "300 Third Blvd, Suite 3C"
    },
    {
        order_id: "O011",
        customer_id: "C005",
        restaurant_id: "R001",
        order_date: new Date("2024-11-11T12:15:00"),
        total_amount: 28.99,
        status: "In Progress",
        delivery_address: "500 Fifth Ave, Floor 5E"
    },
    {
        order_id: "O012",
        customer_id: "C006",
        restaurant_id: "R003",
        order_date: new Date("2024-11-12T19:45:00"),
        total_amount: 41.20,
        status: "Pending",
        delivery_address: "600 Sixth Rd, Apt 6F"
    },
    {
        order_id: "O013",
        customer_id: "C001",
        restaurant_id: "R005",
        order_date: new Date("2024-11-13T20:00:00"),
        total_amount: 55.00,
        status: "Delivered",
        delivery_address: "100 First St, Apt 1A"
    },
    {
        order_id: "O014",
        customer_id: "C004",
        restaurant_id: "R002",
        order_date: new Date("2024-11-14T14:30:00"),
        total_amount: 38.95,
        status: "Delivered",
        delivery_address: "400 Fourth St, Room 4D"
    }
]);

// Create Menu Items collection (Similar to PostgreSQL - SAME COLUMNS, different data)
db.menu_items.insertMany([
    {
        item_id: "M013",
        restaurant_id: "R001",
        name: "Lasagna",
        category: "Main Course",
        price: 16.99,
        description: "Layered pasta with meat sauce",
        available: true
    },
    {
        item_id: "M014",
        restaurant_id: "R001",
        name: "Caprese Salad",
        category: "Appetizer",
        price: 9.99,
        description: "Fresh mozzarella and tomatoes",
        available: true
    },
    {
        item_id: "M015",
        restaurant_id: "R002",
        name: "Spicy Tuna Roll",
        category: "Sushi",
        price: 12.99,
        description: "Tuna with spicy mayo",
        available: true
    },
    {
        item_id: "M016",
        restaurant_id: "R002",
        name: "Tempura",
        category: "Appetizer",
        price: 10.99,
        description: "Lightly battered and fried",
        available: true
    },
    {
        item_id: "M017",
        restaurant_id: "R003",
        name: "Chicken Sandwich",
        category: "Main Course",
        price: 11.99,
        description: "Grilled chicken with special sauce",
        available: true
    },
    {
        item_id: "M018",
        restaurant_id: "R003",
        name: "Onion Rings",
        category: "Side",
        price: 5.99,
        description: "Crispy fried onion rings",
        available: true
    },
    {
        item_id: "M019",
        restaurant_id: "R004",
        name: "Tom Yum Soup",
        category: "Soup",
        price: 8.99,
        description: "Spicy and sour Thai soup",
        available: true
    },
    {
        item_id: "M020",
        restaurant_id: "R004",
        name: "Massaman Curry",
        category: "Main Course",
        price: 15.99,
        description: "Rich peanut curry",
        available: true
    },
    {
        item_id: "M021",
        restaurant_id: "R005",
        name: "Beef Bourguignon",
        category: "Main Course",
        price: 24.99,
        description: "Beef stewed in red wine",
        available: true
    },
    {
        item_id: "M022",
        restaurant_id: "R005",
        name: "Crème Brûlée",
        category: "Dessert",
        price: 8.99,
        description: "Custard with caramelized sugar",
        available: true
    }
]);

// Create Reviews collection (MongoDB only)
db.reviews.insertMany([
    {
        review_id: "REV001",
        customer_id: "C001",
        restaurant_id: "R001",
        order_id: "O001",
        rating: 5,
        comment: "Amazing pizza and pasta! Will definitely come back.",
        review_date: new Date("2024-11-01T14:00:00"),
        helpful_count: 12
    },
    {
        review_id: "REV002",
        customer_id: "C002",
        restaurant_id: "R002",
        order_id: "O002",
        rating: 5,
        comment: "Fresh sushi, great atmosphere. Highly recommended!",
        review_date: new Date("2024-11-02T20:00:00"),
        helpful_count: 8
    },
    {
        review_id: "REV003",
        customer_id: "C003",
        restaurant_id: "R003",
        order_id: "O003",
        rating: 4,
        comment: "Good burger, could use more seasoning.",
        review_date: new Date("2024-11-03T15:30:00"),
        helpful_count: 5
    },
    {
        review_id: "REV004",
        customer_id: "C001",
        restaurant_id: "R004",
        order_id: "O004",
        rating: 5,
        comment: "Authentic Thai food! The green curry was perfect.",
        review_date: new Date("2024-11-04T21:00:00"),
        helpful_count: 15
    },
    {
        review_id: "REV005",
        customer_id: "C002",
        restaurant_id: "R005",
        order_id: "O007",
        rating: 5,
        comment: "Excellent French cuisine, worth the price!",
        review_date: new Date("2024-11-07T20:30:00"),
        helpful_count: 10
    }
]);


// Create Promotions collection (MongoDB only)
db.promotions.insertMany([
    {
        promotion_id: "PROMO001",
        restaurant_id: "R001",
        name: "Pizza Tuesday",
        description: "Get 20% off all pizzas every Tuesday",
        discount_percentage: 20,
        start_date: new Date("2024-11-01"),
        end_date: new Date("2024-12-31"),
        active: true,
        usage_count: 45
    },
    {
        promotion_id: "PROMO002",
        restaurant_id: "R002",
        name: "Sushi Happy Hour",
        description: "50% off sushi rolls from 5-7 PM",
        discount_percentage: 50,
        start_date: new Date("2024-11-01"),
        end_date: new Date("2024-11-30"),
        active: true,
        usage_count: 78
    },
    {
        promotion_id: "PROMO003",
        restaurant_id: "R003",
        name: "Family Combo Deal",
        description: "Buy 2 burgers, get fries free",
        discount_percentage: 0,
        start_date: new Date("2024-11-01"),
        end_date: new Date("2024-11-15"),
        active: true,
        usage_count: 32
    },
    {
        promotion_id: "PROMO004",
        restaurant_id: "R004",
        name: "Lunch Special",
        description: "15% off all orders before 3 PM",
        discount_percentage: 15,
        start_date: new Date("2024-11-01"),
        end_date: new Date("2024-12-31"),
        active: true,
        usage_count: 56
    },
    {
        promotion_id: "PROMO005",
        restaurant_id: "R005",
        name: "Date Night Package",
        description: "3-course meal for two at special price",
        discount_percentage: 25,
        start_date: new Date("2024-11-01"),
        end_date: new Date("2024-12-31"),
        active: true,
        usage_count: 23
    },
    {
        promotion_id: "PROMO006",
        restaurant_id: "R001",
        name: "Loyalty Bonus",
        description: "Earn double loyalty points this month",
        discount_percentage: 0,
        start_date: new Date("2024-11-01"),
        end_date: new Date("2024-11-30"),
        active: true,
        usage_count: 120
    }
]);

// Create indexes for better performance
db.customers.createIndex({ customer_id: 1 }, { unique: true });
db.customers.createIndex({ email: 1 });

db.orders.createIndex({ order_id: 1 }, { unique: true });
db.orders.createIndex({ customer_id: 1 });
db.orders.createIndex({ restaurant_id: 1 });

db.menu_items.createIndex({ item_id: 1 }, { unique: true });
db.menu_items.createIndex({ restaurant_id: 1 });
db.menu_items.createIndex({ category: 1 });

db.reviews.createIndex({ review_id: 1 }, { unique: true });
db.reviews.createIndex({ customer_id: 1 });
db.reviews.createIndex({ restaurant_id: 1 });
db.reviews.createIndex({ rating: -1 });

db.promotions.createIndex({ promotion_id: 1 }, { unique: true });
db.promotions.createIndex({ restaurant_id: 1 });
db.promotions.createIndex({ active: 1 });

print("MongoDB initialization complete!");
print("Collections created:");
print("- customers: " + db.customers.countDocuments() + " documents (SIMILAR - same columns as PG)");
print("- orders: " + db.orders.countDocuments() + " documents (SIMILAR - same columns as PG)");
print("- menu_items: " + db.menu_items.countDocuments() + " documents (SIMILAR - same columns as PG)");
print("- reviews: " + db.reviews.countDocuments() + " documents (DIFFERENT - MongoDB only)");
print("- promotions: " + db.promotions.countDocuments() + " documents (DIFFERENT - MongoDB only)");

