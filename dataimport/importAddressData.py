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
    files = g.glob('H:/downloads/vardeadrr.csv')
    outputfile = 'H:/downloads/addrroutvarde.csv'
    fhout = open(outputfile,'w')
    out_writer = csv.writer(fhout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for file in files:
        #0a3f508e-17bc-32b8-e044-0003ba298018
        #0a3f508e-17ca-32b8-e044-0003ba298018

        with open(file, "r") as f:
            included_cols = [5, 6, 8, 9, 10, 11, 14, 15]
            reader = csv.reader(f, delimiter=",")
            header = next(reader)
            prevrowtmp = next(reader)
            prevrow = list(prevrowtmp[i] for i in included_cols)

            #previdArr = next(reader)[0].split("-")
            #previd = previdArr[0]

            print("CSV header: {}".format(header))
            for row in reader:
                content = list(row[i] for i in included_cols)
                print("Processing row: {}".format(content))
                if (content != prevrow):
                    prevrow = content
                    out_writer.writerow(content)
                    print("did this {}".format(content))

        '''
        with open(file) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                print("Line {}: {}".format(cnt, line.strip()))
                line = fp.readline()
                cnt += 1

                
            
              
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
                '''
        print("done")


    #db.commit()

    db.close()

if __name__ == '__main__':
    main()