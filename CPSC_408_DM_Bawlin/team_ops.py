'''
    TABLE OF CONTENTS

#---Logistical Function---#
    L25 --> __init__(self, db_name) | Connects to the database and intializes the class.

#---Teams Ops Functions---#
    L33 --> show_teams(self) | Returns all team records.
    L41 --> find_team(self, name) | Returns a team of a specific name.
    L49 --> filter_by_type(self, filter) | Returns teams of a specific type.
    L57 --> add_team(self, tName, tSize, tType) | Adds a new team to the teams table.
    L64 --> update_attribute(self, searchName, tName, tSize, tType, val) | Updates a specific attribute of a team.
'''

# Import
from database_conn import DatabaseOps

# CLASS: Contains various operations for getting and changing data in the teams table.
class TeamOps(DatabaseOps):
    #===============================================#
    #------------------Logistical-------------------#
    #===============================================#

    # FUNCTION: Initialize the Database.
    def __init__(self, db_name):
        super().__init__(db_name)
    
    #===============================================#
    #---------------Teams Operations----------------#
    #===============================================#

    # FUNCTION: Returns all team records.
    def show_teams(self):
        # Call procedure.
        self.cursor.callproc("display_teams")
        
        return self.get_results() # Return results.
        
    
    # FUNCTION: Returns the team record of the input name.
    def find_team(self, name):
        # Call procedure.
        self.cursor.callproc("find_team", (name,))

        return self.get_results() # Return results.


    # FUNCTION: Returns all team records of a specific team type.
    def filter_by_type(self, filter):
        # Call procedure.
        self.cursor.callproc("filter_by_type", (filter,))

        return self.get_results() # Return results.

    
    # FUNCTION: Adds a new team record given the inputs.
    def add_team(self, tName, tSize, tType):
        # Call procedure.
        self.cursor.callproc("create_team", (tName, tSize, tType))
        self.conn.commit()
    

    # FUNCTION: Updates a specific team's attribute given the val parameter.
    def update_attribute(self, searchName, tName, tSize, tType, val):
        # Call procedure.
        self.cursor.callproc("update_team_attribute", (searchName, tName, tSize, tType, val))
        self.conn.commit()
