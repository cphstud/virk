import sys
import os
import json
import glob as g
import csv

sys.path.insert(0,"/Users/thw/Documents/visualcode/python")

from virkconfig.initdb import connect_db


def main():
    csvfile="./dataimport/RisikaAll.csv"
    print(os.getcwd())
    print("ok")
    db = connect_db('virk')

    #   handle csv
    #   cvrnr;start_date;end_date;bruttoresultat;aaretsresultat;aktiver;egenkapital;kortgaeld;langgaeld;hensaettelser
    #   sample line: 25789822;01/01/16;31/12/16;88.750;75.666;227.354;155.666;71.688;;
    #   TODO:
    #   convert date to year, eg 01/01/16 to 2016
    #   remove any dots, eg 75.666

    cvrlist = []
    with open(csvfile) as fp:
        csv_reader = csv.reader(fp, delimiter=';')
        print(csv_reader)
        for row in csv_reader:
            cvrlist.append(row[-1])

      
            with db.cursor() as cur:
                #cur.execute("REPLACE INTO address (Street,city,postal_code) \
                #VALUES ('{}','{}','{}') ".format(data['address'],data['city'],data['zipcode']))
                #print("LAST: " + str(cur.lastrowid))
                cur.execute("SELECT cvrnr, companyName, companyID FROM company WHERE cvrnr = {} ".format(row[0]))
                res = cur.fetchone()
                if (res is not None):
                    print("ok")
                    # THIS IS NOT DONE YET
                    tmpYear = '20' + row[1].split('/')[-1] 
                    try:

                        cur.execute("INSERT INTO audits (cvrnr,companyID, auditYear, GrossResult, Equity, LongTermDebt) \
                        VALUES ({},{},{},{},{},{})".format(row[0],res['companyID'],tmpYear, row[3].replace('.',''),row[5].replace('.',''),row[7].replace('.','')))
                        print(res)
                        print('; '.join(row))
                    except:
                        print("problem with row ")
                        print('; '.join(row))
                else:
                    print("basd")
                    print('; '.join(row))
                #cur.execute('SELECT * FROM address where addressID = 180')
                '''
                for r in cur:
                    print("--")
                    print(r)
                    print("DONE")
                '''
            print("doxxcne")


    db.commit()
    db.close()

if __name__ == '__main__':
    main()