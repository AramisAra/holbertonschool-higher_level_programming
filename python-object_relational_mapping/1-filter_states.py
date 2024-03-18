#!/usr/bin/python3
""" Imports """
import sys
import MySQLdb

def fliter_states(User, passwd, database):
    """
    Connects to a MySQL database and retrieves all state names that start with the letter 'N'.

    Parameters:
    a (str): The username for the database connection.
    b (str): The password for the database connection.
    c (str): The database name to connect to.
    
    Returns:
    None: Prints out each state name that starts with 'N'.
    """
    db = MySQLdb.connect(host='localhost', port=3306, user=User, passwd=passwd, db=database)
    cur = db.cursor()
    cur.execute("SELECT name FROM states WHERE name LIKE 'N%'")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    data = sys.argv[3]

    fliter_states(username, password, data)
