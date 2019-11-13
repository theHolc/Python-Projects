import psycopg2
# initialized to create a store table with rows consisting of
# item name, quantity of item in stock, and price of item

# enter your postgresSQL credentials to the parameters in the conn
# variable to create your own store!

def create_table():
    conn = psycopg2.connect(dbname='', user='', password='', host='', port='')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect(dbname='', user='', password='', host='', port='')
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect(dbname='', user='', password='', host='', port='')
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect(dbname='', user='', password='', host='', port='')
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = psycopg2.connect(dbname='', user='', password='', host='', port='')
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()