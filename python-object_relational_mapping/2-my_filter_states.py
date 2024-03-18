#!/usr/bin/python3
"""
This allow filtering with user input
"""
import sys
import MySQLdb


if __name__ == '__main__':

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    sqlQuery = "SELECT * FROM states WHERE name LIKE %s"
    userInput = sys.argv[4]
    params = (userInput + '%',)

    cur.execute(sqlQuery, params)

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
