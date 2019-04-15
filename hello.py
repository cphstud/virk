from sshtunnel import SSHTunnelForwarder
from virkconfig import config
import pymysql

with SSHTunnelForwarder(
    ('18.184.198.179', 22), #The server's IP and SSH port
    ssh_username="ubuntu",
    ssh_pkey="~/Downloads/test.pem",
    remote_bind_address=('127.0.0.1', 3306)) as tunnel: #The server's TCP IP and port, you're tunneling

    db = pymysql.connect(host=config.DATABASE_CONFIG['host'],
                           user=config.DATABASE_CONFIG['user'],
                           password=config.DATABASE_CONFIG['password'],
                           db=config.DATABASE_CONFIG['dbname'],
                           port=tunnel.local_bind_port)


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
