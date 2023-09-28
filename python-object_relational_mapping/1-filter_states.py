#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # if len(sys.argv) != 4:
    #     print("Usage: python script.py <username> <password> <database>")
    #     sys.exit(1)
    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
        )
    # except MySQLdb.Error as e:
    #     print(f"Error connecting to the database: {e}")
    #     sys.exit(1)

    cursor = database.cursor()
    cursor.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%'
                   ORDER BY states.id """)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    database.close()