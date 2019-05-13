import sys
import os
import json
import glob as g
import csv

sys.path.insert(0,"/Users/thw/Documents/visualcode/python")

from virkconfig.initdb import connect_db

''' Delete duplicates 
select street, count(street) from address group by street having count(street) > 1 order by 2;
delete t1 from address t1 inner join address t2 where t1.addressID < t2.addressID AND t1.street = t2.street;
'''

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
                cur.execute("REPLACE INTO address (Street,city,postal_code) \
                VALUES ('{}','{}','{}') ".format(data['address'],data['city'],data['zipcode']))
                print("LAST: " + str(cur.lastrowid))
                cur.execute("INSERT INTO company (cvrnr, companyName,addressID) VALUES ({},'{}',{}) ".format(data['vat'],data['name'],cur.lastrowid))
                
                #cur.execute('SELECT * FROM address where addressID = 180')

                for r in cur:
                    print("--")
                    print(r)
                    print("DONE")
                        
        finally:
            db.commit()
            print("done")


    #db.commit()

    db.close()

if __name__ == '__main__':
    main()