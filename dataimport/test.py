import sys

sys.path.insert(0,"C:/Users/twu/Documents/projects/virk/")
print(sys.path)
from virkconfig.initdb import connect_db

print(sys.executable)

conn = connect_db('virk')
cur = conn.cursor()

cur.execute("SHOW DATABASES")
print(cur.fetchall())
conn.close()
