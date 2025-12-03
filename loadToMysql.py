import pymysql

# To connect MySQL database
# Enter your own values for the parameters
conn = pymysql.connect(
        host='localhost', # Your Mysql Server name
        user='root', # Your Mysql Username
        password="", # Your Mysql Password
        db='database_gfg',# Your Mysql database name
)

cur = conn.cursor()
table_name = "products"
# Create a table and adjust the Schema as needed
sql = f"""
       CREATE TABLE IF NOT EXISTS {table_name} (RowID INT PRIMARY KEY AUTO_INCREMENT,
       OrderID  VARCHAR(50) NOT NULL, OrderDate DATE, ShipDate DATE,
       ShipMode VARCHAR(50) NOT NULL,
       CustomerID VARCHAR(50) NOT NULL, CustomerName VARCHAR(50) NOT NULL,
       Segment VARCHAR(50) NOT NULL, Country VARCHAR(50) NOT NULL, City VARCHAR(50) NOT NULL,
       State VARCHAR(50) NOT NULL, PostalCode INT,Region VARCHAR(50) NOT NULL,
       ProductID VARCHAR(50) NOT NULL,Category VARCHAR(50) NOT NULL,
       SubCategory VARCHAR(50) NOT NULL,
       ProductName VARCHAR(50) NOT NULL, Sales DECIMAL(10,3)
       )
       """

# table created
cur.execute(sql)
conn.commit()

# To close the connection
conn.close()
