'''
    TABLE OF CONTENTS

#---Logistical Functions---#
    L22 --> __init__(self, db_name) | Establishes connection to DB.
    L35 --> close_connections(self) | Closes the DB connection.

#---Auxilary Function---#
    L45 --> get_results(self) | Returns the results from a procedure.
'''

# Import mySQL Package
import mysql.connector

# CLASS: Base parent class for all other operation classes. Establishes+Closes connection to the DB.
class DatabaseOps:
    #===============================================#
    #------------------Logistical-------------------#
    #===============================================#

    # FUNCTION: Create connection + cursor object.
    def __init__(self, db_name):
        self.conn = mysql.connector.connect(host = "localhost", # Always stays the same.
                                            user = "root",      # Always stays the same.
                                            password = "dolphinmuncha69$",
                                            auth_plugin = "mysql_native_password", # Always stays the same.
                                            database = db_name)
        
        # Create Cursor
        self.cursor = self.conn.cursor()
        print("Connection Established.") # Confirmation, for debugging/testing.


    # FUNCTION: Close the database connections.
    def close_connections(self):
        self.cursor.close()
        self.conn.close()
        print('Connection Closed.') # Confirmation, for debugging/testing.

    #===============================================#
    #-------------------Auxilary--------------------#
    #===============================================#

    # FUNCTION: Return stored results from a procedure.
    def get_results(self):
        # Get the results.
        for result in self.cursor.stored_results():
            return result.fetchall()
        