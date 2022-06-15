import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Thidwick108*",
    database="sql_workbench"
)
mycursor = db.cursor()

#mycursor.execute("CREATE TABLE life (id int, name varchar(20), age int)")

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

#mycursor.execute("SHOW TABLES")

#for x in mycursor:
#  print(x)

#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

db.commit()

print(mycursor.rowcount, "record inserted.")

mycursor = db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

db.commit()

print(mycursor.rowcount, "was inserted.")
