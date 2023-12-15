#!/usr/bin/python3
"""
Lists all states with a name starting with N from
 the database hbtn_0e_0_usa
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
                   WHERE NAME LIKE BINARY 'N%' \
                   ORDER BY id ASC")

    rows = cursor.fetchall()

    for state in rows:
        print(state)

    cursor.close()
    db.close()
