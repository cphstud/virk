import sys
import os
import json
import glob as g

sys.path.insert(0,"C:/Users/twu/Documents/projects/virk/")

from virkconfig.initdb import connect_db


def main():
    print(os.getcwd())
    print("ok")
    db = connect_db('virk')
    files = g.glob('./dataimport/apidata/*.json')
    for file in files:
        print(file)
        with open(file) as json_file:
            data = json.load(json_file)
            
        try:       
            with db.cursor() as cur:
                cur.execute("INSERT IGNORE INTO address (Street,city,postal_code) \
                    VALUES ('{}','{}','{}') ".format(data['address'],data['city'],data['zipcode']))
                print("LAST: " + str(cur.lastrowid))
                cur.execute("INSERT INTO company (cvrnr, companyName,addressID) VALUES ({},'{}',{}) ".format(data['vat'],data['name'],cur.lastrowid))
                
                #cur.execute('SELECT * FROM company')

                for r in cur:
                    print(r)
                        
        finally:
            db.commit()
            print("done")

    #db.commit()
    db.close()

if __name__ == '__main__':
    main()