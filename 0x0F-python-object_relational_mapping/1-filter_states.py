#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa with a name
starting with N
"""

import MySQLdb
import sys

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cursor = db.cursor()
 cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
  rows = cursor.fetchall()
   for row in rows:
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    db.close()
