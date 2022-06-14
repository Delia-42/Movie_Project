import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Thidwick108*",
    database="sql_workbench"
)
mycursor = db.cursor()

mycursor.execute("CREATE TABLE life (id int, name varchar(20), age int)")
