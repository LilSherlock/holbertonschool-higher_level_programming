#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa
"""

import MySQLdb
import sys

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()

cur.execute("SELECT * FROM states WHERE name = '{}'".format(sys.argv[4]))

for state in cur.fetchall():
    print(state)
