#!/usr/bin/python3
"""
Displays all values in the states table where
 name matches the provided argument.
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states \
                   WHERE NAME LIKE BINARY '{}' \
                   ORDER BY id ASC;".format(argv[4]))

    rows = cursor.fetchall()

    for state in rows:
        print(state)

    cursor.close()
    db.close()
