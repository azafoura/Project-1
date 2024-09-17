import pandas as pd
import numpy as np
import mysql.connector

conn = mysql.connector.connect(
    host="sql7.freemysqlhosting.net",
    user="sql7731574",
    password="eWDTurJ4v2",
    database="sql7731574"
)

if conn.is_connected():
    print("Successfully connected to the database")

products_df = pd.read_sql("SELECT * FROM products", conn)
products_df.set_index('product_id', inplace=True)

def Restock():
    print('Enter product name to restock: \n', products_df["name"])
    x = 0
    y = 0
    cursor = conn.cursor()
    while True:
        try:
            x=input('Enter Product ID or if done leave field empty and press enter: ')
            if x == '': break
            x = int(x)
            if x not in products_df.index:
                raise ValueError('Product ID not found')
        except Exception as e:
            print(f'invalid entry: {e}')
            continue
        while True:
            try:
                y=int(input(f"Enter {products_df.loc[x, 'name']} added stock: "))
                if y < 0:
                    raise ValueError("Stock level must be a positive number")
            except Exception as e:
                print(f'invalid entry: {e}')
                continue
            break
        products_df.loc[x, 'stock_level']+= y
        update_product_stock_query = """
            UPDATE products
            SET stock_level = %s
            WHERE product_id = %s
            """
        try:
            cursor.execute(update_product_stock_query, (int(products_df.loc[x, 'stock_level']), x))
        except mysql.connector.Error as err:
            print(f"Error updating the database: {err}")
            conn.rollback()
    conn.commit()
    cursor.close() 

Restock()
conn.close()
