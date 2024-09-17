import pandas as pd
import numpy as np
import mysql.connector

conn = mysql.connector.connect(
    host="sql7.freemysqlhosting.net",           # Replace with your MySQL server (usually localhost)
    user="sql7731574",       # Replace with your MySQL username (root or your own)
    password="eWDTurJ4v2",   # Replace with your MySQL password
    database="sql7731574"
)
products_df = pd.read_sql("SELECT * FROM products", conn)
products_df.set_index('product_id', inplace=True)
max=products_df.index.max()
print(products_df.index.max())
if conn.is_connected():
    print("Successfully connected to the database")
    cursor = conn.cursor()
def additem(name,id=None,category=None, stock=0,price=0.0,stockthreshold=10,supplier_id=None):
    maxq=cursor.execute("""SELECT COUNT(*) FROM products""")
    max=cursor.fetchone()[0]
    if id==None: id=max+1


    query="""
    INSERT  INTO products
    VALUES  (%s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(query,(id,name,category,stock,price,stockthreshold,supplier_id))
    conn.commit()
    cursor.close()
additem('MAMADOU',99,'male',22,89.9,7,66)