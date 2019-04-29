import sys
import json
import glob as g

sys.path.append("..")

from virkconfig.initdb import connect_db
db = connect_db('virk')

try:
    # Print all the databases
    with db.cursor() as cur:
        cur.execute('SHOW DATABASES')
        #cur.execute('INSERT INTO company (companyName,  cvrnr) VALUES ("test",123123123)')
        print(cur.lastrowid)
        cur.execute('SELECT * FROM company')

        for r in cur:
            print(r)
finally:
    db.commit()
    db.close()

print("YAYY!!")

files = g.glob('./apidata/*json')


for file in files:
    with open(file) as json_file:
        try:
            data = json.load(json_file)
            #print(data['name'])
        except:
            print("error")
        else:
            continue


#cursor.lastrowid