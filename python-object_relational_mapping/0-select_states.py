import sys
import MySQLdb



def State_list(user, passwd, data):

    # Connection to database
    db = MySQLdb.connect(host='loaclhost', port='3306',
    user=user, passwd=passwd , db=data)

    # This is a cursor to be able to make query use python
    cur = db.cursor()

    # This is the query to get the table
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # This is to fetch the table to print it
    states = cur.fetchall()

    # This is to print the fetch
    for state in states:
        print(state)

    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    user = sys.argv[1]
    passwd = sys.argv[2]
    data = sys.argv[3]

    State_list(user, passwd, data)
