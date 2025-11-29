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
       SELECT * FROM {table_name}
       """
# table created
cur.execute(sql)

# Fetch all the results
myresult = cur.fetchall()

# Print the results
for row in myresult:
    print(row)
conn.commit()

# To close the connection
conn.close()