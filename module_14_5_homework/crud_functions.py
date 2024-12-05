import sqlite3


def initiate_db():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products


def add_user(username, email, age):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (username, email, age, 1000))
    connection.commit()


def is_included(username):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    check_user = cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))

    if check_user.fetchone() is None:
        return False
    else:
        return True


products = [
    (1, 'Котик 1', 'Черный', 100),
    (2, 'Котик 2', 'Осторожный', 200),
    (3, 'Котик 3', 'Рыжий-лентяй', 300),
    (4, 'Котик 4', 'Красивый', 400),
]


# def add_product(product_id, title, description, price):
#     connection = sqlite3.connect('Products.db')
#     cursor = connection.cursor()
#     cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
#                    (product_id, title, description, price))
#     connection.commit()
#     connection.close()


initiate_db()

# for product in products:
#     add_product(*product)
