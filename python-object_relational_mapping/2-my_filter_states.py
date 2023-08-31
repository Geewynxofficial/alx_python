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

    name = sys.argv[4]
    query = ("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC")
    cursor.execute(query, (name))
    
    rows = cursor.fectall()

    for row in rows:
        print(rows)

    cursor.close()
    database.close()

