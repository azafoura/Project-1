import pandas as pd
import numpy as np
import mysql.connector
import sqlalchemy

conn = mysql.connector.connect(
    host="sql7.freemysqlhosting.net",           # Replace with your MySQL server (usually localhost)
    user="sql7731574",       # Replace with your MySQL username (root or your own)
    password="eWDTurJ4v2",   # Replace with your MySQL password
    database="sql7731574"
)

if conn.is_connected():
    print("Successfully connected to the database")

products_df = pd.read_sql("SELECT * FROM products", conn)
products_df.set_index('product_id', inplace=True)
sales_df = pd.read_sql("SELECT * FROM sales", conn)
sales_df.set_index('sale_id', inplace=True)
Daily_Sales_Matrix=[]

def Purchase():
    print("choose products to purchase:\n\n", products_df["name"])
    x = 0
    y = 0
    prds=[]
    qt=[]
    cursor = conn.cursor()
    while True:
        try:
            x=input('Enter Product ID or if done leave field empty and press enter:')
            if x == '': break
            x = int(x)
            if x not in products_df.index:
                raise ValueError('Product ID not found')
        except Exception as e:
            print(f'invalid entry: {e}')
            continue
        prds.append(x)
        while True:
            try:
                y=int(input(f"Enter {products_df.loc[x, 'name']} quantity:"))
                if y not in range(1, products_df.loc[x, 'stock_level']+1):
                    raise ValueError('try ordering less you fat fuck')
                else: break
            except Exception as e:
                print(f'invalid entry: {e}')
        qt.append(y)
        products_df.loc[x, 'stock_level']-= y
        sales_df.loc[1000+x, 'quantity_sold']+= y
        sales_df.loc[1000+x, 'total_sale_value']+= y*products_df.loc[x, 'price']
    
        update_product_query = """
            UPDATE products
            SET stock_level = %s
            WHERE product_id = %s
            """
        cursor.execute(update_product_query, (int(products_df.loc[x, 'stock_level']), x))
        update_sales_query = """
                UPDATE sales
                SET quantity_sold = %s, total_sale_value = %s
                WHERE sale_id = %s
                """
        cursor.execute(update_sales_query, (int(sales_df.loc[1000+x, 'quantity_sold']), float(sales_df.loc[1000+x, 'total_sale_value']), 1000+x))
    Daily_Sales_Matrix.append(np.array([prds, qt]))
    conn.commit()
    cursor.close()            
       
Purchase()
conn.close()