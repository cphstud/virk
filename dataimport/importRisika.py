import sys
import os
import json
import glob as g
import csv

sys.path.insert(0,"/Users/thw/Documents/visualcode/python")

from virkconfig.initdb import connect_db


def main():
    csvfile="./dataimport/Risika.csv"
    print(os.getcwd())
    print("ok")
    db = connect_db('virk')

    #handle csv
    cvrlist = []
    with open(csvfile) as fp:
        csv_reader = csv.reader(fp, delimiter=';')
        print(csv_reader)
        for row in csv_reader:
            cvrlist.append(row[0])

      
            with db.cursor() as cur:
                #cur.execute("REPLACE INTO address (Street,city,postal_code) \
                #VALUES ('{}','{}','{}') ".format(data['address'],data['city'],data['zipcode']))
                #print("LAST: " + str(cur.lastrowid))
                cur.execute("SELECT cvrnr, companyName, companyID FROM company WHERE cvrnr = {} ".format(row[0]))
                res = cur.fetchone()
                if (res is not None):
                    print("ok")
                    print(res)
                    print('; '.join(row))
                else:
                    print("basd")
                #cur.execute('SELECT * FROM address where addressID = 180')
                '''
                for r in cur:
                    print("--")
                    print(r)
                    print("DONE")
                '''
            print("doxxcne")


    #db.commit()
    db.close()

if __name__ == '__main__':
    main()