import pymysql
import pandas as pd
from datetime import datetime

from decimal import Decimal
import csv


csv_date_format = '%d-%m-%Y'
mysql_date_format = '%Y-%m-%d %H:%M:%S'

# To connect MySQL database
# Enter your own values for the parameters
conn = pymysql.connect(
        host='localhost', # Your MySQL Server name
        user='root', # Your MySQL Username
        password="", # Your MySQL Password
        db='database_gfg',# Your MySQL database name
)

cur = conn.cursor()

csv_file_path = 'train.csv'
df = pd.read_csv(csv_file_path, dtype=str)

table_name = "products"
# Create a table and adjust the Schema as needed
for index, row in df.iterrows():
    date_str_order = row['Order Date']
    date_str_ship = row['Ship Date']

    dt_object_order = datetime.strptime(date_str_order,csv_date_format)
    #format for MySQL
    mysql_formatted_date_order = dt_object_order.strftime(mysql_date_format)
    dt_object_ship = datetime.strptime(date_str_ship, csv_date_format)
    # format for MySQL
    mysql_formatted_date_ship = dt_object_order.strftime(mysql_date_format)
    df['Sales'] = df['Sales'].astype(str)
    df['Sales'].str.lower()
    df['Sales'] = (
         df['Sales'].str.replace(",", ".", regex=False)
        .str.replace(r"[^0-9.]", "", regex=True)
        .str.strip())
    df['Sales'] = df['Sales'].apply(lambda x: Decimal(x))

    sql =  f"""
           INSERT INTO {table_name} (RowID, OrderID, OrderDate, ShipDate, ShipMode,
           CustomerID, CustomerName, Segment, Country, City, State, PostalCode, ProductID,
           Category, Region, Sales, SubCategory, ProductName )           
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    # Map CSV columns to table columns
    val = (row['Row ID'], row['Order ID'], mysql_formatted_date_order,
           mysql_formatted_date_ship, row['Ship Mode'],
           row['Customer ID'], row['Customer Name'], row['Segment'],
           row['Country'], row['City'],
           row['State'], row['Postal Code'], row['Product ID'],
           row['Category'], row['Region'], row['Sales'],
           row['Sub-Category'], row['Product Name'])
    conn.ping()  # reconnecting mysql
    with conn.cursor() as cur:
        cur.execute(sql,val)

    #commit changes to the database
    conn.commit()
    print(cur.rowcount, "record inserted.")
    # To close the connection
    conn.close()
