import csv
import sqlite3
conn = sqlite3.connect('database.sqlite3')
cur = conn.cursor()
# file_name = open("Test-Orders_DB", r)
max_product_len = []
with open("Test-Orders_DB.csv", "rU") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cost = row['cost_price']
        if cost:
            cost = cost * 66
        else:
            cost = 0
        date = row['order_date'].replace('/','-')
        cur.execute("""
        INSERT INTO orders values (?,?,?,?,?,?,?)
        """, (row['id'],row['order_id'], row['product_name'],row['order_status'], row['product_url'],cost,date))

conn.commit()
cur.close()

# order_id, product_name, order_status, product_url, cost_price , order_date
