#!/usr/bin/python3
"""
Safe filter
"""
import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    myquery = "SELECT * FROM states WHERE name = %s"
    userInput =  sys.argv[4]
    parms = (userInput + '%',)

    cur.execute(myquery, parms)

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
