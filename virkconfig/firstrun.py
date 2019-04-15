import sys
import os
import pymysql
from initdb import connect_db

def executeScriptsFromFile(filename):
    
    fd = open(filename, 'r')
    sqlfile = fd.read()
    fd.close()
    conn = connect_db('virk')
    c = conn.cursor()
    sqlCommands = sqlfile.split(';')

    for command in sqlCommands:
        try:
            if command.strip() != '':
                c.execute(command)
                rows = c.fetchall()
                for row in rows:
                    print("got this " + str(row) + " from " + command)

        except pymysql.OperationalError as msg:
            print("Command skipped: ", msg)

cwd = os.getcwd()
print(cwd)
executeScriptsFromFile('./virkconfig/virkcr5.sql')