import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="flask"
)

datas = pd.read_csv("data/out/import.csv", sep=",", on_bad_lines='skip')

list_of_rows = [list(row) for row in datas.values]

count = 0
for data in list_of_rows:
    print(f"{data[0]}", f"{data[1]}", f"{data[2]}", f"{data[3]}")
    mycursor = mydb.cursor()
    sql = "INSERT INTO data (titre, ville, mot_cle, type_event) VALUES (%s, %s, %s, %s)"
    val = (f"{data[0]}", f"{data[1]}", f"{data[2]}", f"{data[3]}")
    mycursor.execute(sql, val)

    mydb.commit()
    count = count + 1
    print(count, "record inserted.")
