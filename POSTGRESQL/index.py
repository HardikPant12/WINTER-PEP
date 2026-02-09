import psycopg2
conn=psycopg2.connect(
    host="localhost",
    database="school",
    user="postgres",
    password="hardik@pant1"
)
print("Connection done")

cur=conn.cursor()
cur.execute("""DROP TABLE if exists employee """)
cur.execute("""CREATE TABLE IF NOT EXISTS employee(id INT,name VARCHAR(50),salary INT)""")

cur.execute("""INSERT INTO employee VALUES(1,'Hardik',50000),(2,'Rohit',78972),(3,'Rahul',67343 )""")
conn.commit()
cur.execute("""SELECT * from employee""")
rows=cur.fetchall()
for row in rows:
    print(row)
conn.close()