import mysql.connector as connector
from mysql.connector import errorcode

# Singleton metaclass
class Singleton(object):
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls)     # create new object if not created
        return cls._instance

class Connector(Singleton):
    def __init__(self):
        # Input local connection details and leave database name as is
        self.config = {
            'user': 'root',         # CHANGE THIS WHEN TESTING
            'password': 'tpets',       # CHANGE THIS WHEN TESTING
            'host': 'localhost',
            'database': 'appDB',
            'raise_on_warnings': True,
        }
    
    def getConnection(self):
        '''Returns the connection if config parameters are good else None
        '''
        try:
            conn = connector.connect(**self.config)
            return conn

        # Various error handling (documentation for this can be found on MySQL website)
        except connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Invalid username and/or password, please check them again")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            
            return None
            