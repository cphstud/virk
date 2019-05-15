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
    print("exep")
    print(sys.executable)
    print("ok")
    db = connect_db('virk')
    ssid = 1000
    files = g.glob('./dataimport/apidata/ok/*.json')

    for file in files:
        print(file)

        with open(file) as json_file:
            data = json.load(json_file)
            
            
              
        with db.cursor() as cur:
            cur.execute("INSERT INTO address (Street,city,postal_code) \
            VALUES ('{}','{}','{}') ".format(data['address'],data['city'],data['zipcode']))
            print("LAST: " + str(cur.lastrowid))
            cur.execute("INSERT INTO company (cvrnr, companyName,addressID) VALUES ({},'{}',{}) ".format(data['vat'],data['name'],cur.lastrowid))
            print("compid: " + str(cur.lastrowid))
            tmpCompid = cur.lastrowid
            if data['owners']:
                for person in data['owners']:
                    ssid = ssid + 1
                    cur.execute("INSERT INTO person (ssid, fullname, prole) VALUES ({},'{}','{}') ".format(ssid,person['name'],'owner'))
                    tmppersid = cur.lastrowid
                    cur.execute("INSERT INTO employment (personID, companyID) VALUES ({},{}) ".format(ssid,tmpCompid))

        
            #cur.execute('SELECT * FROM address where addressID = 180')

            for r in cur:
                print("--")
                print(r)
                print("DONE")
                    
        
        db.commit()
        print("done")


    #db.commit()

    db.close()

if __name__ == '__main__':
    main()