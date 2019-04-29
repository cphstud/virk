import pymysql
#import config

DATABASE_CONFIG = {
    'host': 'localhost',
    'dbname': 'virk',
    'user': 'twu',
    'password': 'twu123',
    'port': 3306
}

def connect_db(dbname):
    if dbname != DATABASE_CONFIG['dbname']:
        raise ValueError("Couldn't not find DB with given name")
    conn = pymysql.connect(host=DATABASE_CONFIG['host'],
                           user=DATABASE_CONFIG['user'],
                           password=DATABASE_CONFIG['password'],
                           db=DATABASE_CONFIG['dbname'],
                           cursorclass=pymysql.cursors.DictCursor)
    return conn