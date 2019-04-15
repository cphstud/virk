from virkconfig.initdb import connect_db

db = connect_db('virk')


    #db = pymysql.connect(user='twu', passwd='twu123', host='127.0.0.1',
                       #port=tunnel.local_bind_port) #Your TCP IP and port (your end of the tunnel)

    # Run sample query in the database to validate connection
try:
    # Print all the databases
    with db.cursor() as cur:
        cur.execute('SHOW DATABASES')
        for r in cur:
            print(r)
finally:
    db.close()

print("YAYY!!")