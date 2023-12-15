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
    state_name = argv[4]

    query = "SELECT cities.name FROM cities \
                   JOIN states \
                   ON cities.state_id = states.id \
                   WHERE states.name LIKE BINARY %s \
                   ORDER BY cities.id ASC;"

    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    if rows:
        flag = 0
        for row in rows:
            if flag == 1:
                print(", ", end="")
            print(row[0], end="")
            flag = 1
    print()

    cursor.close()
    db.close()
