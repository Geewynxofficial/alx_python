import MySQLdb

database = MySQLdb.connect(host="localhost", port = 3306, user="Godwin", passwd="Geezee3200_", db="hbtn_0e_0_usa")

cursor = database.cursor()
cursor.execute ("SELECT * FROM states ORDER BY id ASC")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
database.close()
