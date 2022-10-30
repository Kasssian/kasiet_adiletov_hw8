import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)


def select_all_products(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM products''')

        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except Error as e:
        print(e)


def update_product(conn, product):
    try:
        sql = '''
        UPDATE products SET quantity=? ,price=? WHERE id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)


def search_by_word(conn, word):
    try:
        sql = '''SELECT * FROM products WHERE products_title LIKE ?'''
        cursor = conn.cursor()
        cursor.execute(sql, ('%' + word + '%',))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)


def create_products(conn, product):
    try:
        sql = '''
        INSERT INTO products(products_title, price, quantity) 
        VALUES (?, ?, ?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)

def create_many_products(conn):
    create_products(conn,('Танк "Merkava"',5000000,10))
    create_products(conn,('M14A1',3000,200))
    create_products(conn,('Desert Eagle',1000,20))
    create_products(conn,('Famous',2000,100))
    create_products(conn,('ПЗРК "Солнцепёк"',10000000,10))
    create_products(conn,('Javelin',10000,100))
    create_products(conn,('F-22',100000000,15))
    create_products(conn,('F-35',200000000,10))
    create_products(conn,('AK-12',1500,300))
    create_products(conn,('Су-35',50000000,20))
    create_products(conn,('МИ-8',10000000,30))
    create_products(conn,('МИ-24',20000000,40))
    create_products(conn,('Black Eagle',30000000,25))
    create_products(conn,('Soldier armour',1500,500))
    create_products(conn,('РПГ-7',1000,100))


def delete_product(conn, id):
    try:
        sql = '''
        DELETE FROM products WHERE id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error as e:
        print(e)


def select_product(conn):
    try:
        sql = '''SELECT * FROM products WHERE price < 100 and quantity > 5'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except Error as e:
        print(e)


sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
products_title VARCHAR(200) NOT NULL, 
price DOUBLE(10,2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0
)
'''

hw_db = "hw.db"
connection = create_connection(hw_db)

if connection is not None:
    # create_table(connection, sql_create_products_table)
    # create_products(connection, ('AK-74',99, 10))
    # update_product(connection, (50, 500, 1))
    # delete_product(connection, 2)
    # select_all_products(connection)
    # select_product(connection)
    # search_by_word(connection,'Танк')
    # create_many_products(connection)
    print('Successfully')
