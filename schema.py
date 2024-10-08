import sqlite3

conn = sqlite3.connect('ben_pizzaria.db')
cursor = conn.cursor()


def create_schema():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Orders(
        row_id INTEGER PRIMARY KEY NOT NULL,
        order_id VARCHAR(30) NOT NULL,
        order_time DATE,
        category VARHCAR (50),
        item_id INTEGER,
        quantity INTEGER,
        customer_id INTEGER,
        delivery_order BOOLEAN,
        address_id INTEGER,
        FOREIGN KEY (item_id) REFERENCES Items (item_id),
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
        FOREIGN KEY (address_id) REFERENCES Address(address_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INTEGER PRIMARY KEY NOT NULL,
        firstname VARCHAR(50),
        lastname VARCHAR(50)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Address (
        address_id INTEGER PRIMARY KEY NOT NULL,
        delivery_address varchar(50),
        delivery_address2 varchar(50),
        delivery_city varchar (50),
        delivery_zipcode varchar (50)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Items (
        item_id INTEGER PRIMARY KEY NOT NULL,
        sku varchar (20),
        item_name varchar(50),
        item_price decimal (5,2),
        item_size varchar (20)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Recipe (
        row_id INTEGER PRIMARY KEY NOT NULL,
        recipe_id varchar (20),
        ingredient_id varchar (20),
        quantity integer,
        FOREIGN KEY (recipe_id) REFERENCES Items(sku),
        FOREIGN KEY (ingredient_id) REFERENCES Ingredients(ingredient_id),
        FOREIGN KEY (ingredient_id) REFERENCES Inventory(ingredient_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Ingredients (
        ingredient_id INTEGER PRIMARY KEY NOT NULL,
        ingredient_name varchar(50),
        ingrediencrt_measure varchar(50),
        ingredient_weight integer,
        ingredient_price decimal(5,2)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Inventory (
        inventory_id INTEGER PRIMARY KEY NOT NULL,
        item_id integer,
        quantity integer
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Rota (
        row_id INTEGER PRIMARY KEY NOT NULL,
        rota_id INTEGER,
        date DATE, 
        shift_id INTEGER,
        staff_id INTEGER,
        FOREIGN KEY (date) REFERENCES Orders(order_time)
        FOREIGN KEY (staff_id) REFERENCES Staff(staff_id)
        FOREIGN KEY (shift_id) REFERENCES Shift(shift_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Staff(
        staff_id INTEGER PRIMARY KEY NOT NULL,
        first_name VARCHAR(30),
        last_name VARCHAR(30),
        position VARCHAR (30),
        hourly_rate DECIMAL (5,2)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Shift(
        shift_id INTEGER PRIMARY KEY NOT NULL,
        day_of_week VARCHAR (20),
        start_time TIMESTAMP,
        end_time TIMESTAMP
    )
    """)

    conn.close()


create_schema()