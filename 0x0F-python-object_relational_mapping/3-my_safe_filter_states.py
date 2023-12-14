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

    """ cursor.execute(query, (state_name,)) """
    cursor.execute("SELECT * FROM states \
                   WHERE NAME LIKE BINARY %s \
                   ORDER BY id ASC;", (argv[4],))

    rows = cursor.fetchall()

    for state in rows:
        print(state)

    cursor.close()
    db.close()
