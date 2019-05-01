import sys
import json
import glob as g

sys.path.insert(0,"../virkconfig")

from initdb import connect_db


def main():
    db = connect_db('virk')
    files = g.glob('./apidata/*.json')
    for file in files:
        print(file)
        with open(file) as json_file:
            data = json.load(json_file)
            
        try:       
            with db.cursor() as cur:
                cur.execute("INSERT INTO address (Street,city,postal_code) \
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