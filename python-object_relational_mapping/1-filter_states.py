#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )

    cursor = database.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(rows)

    cursor.close()
    database.close()