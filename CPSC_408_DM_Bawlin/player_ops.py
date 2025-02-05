'''
    TABLE OF CONTENTS

#---Logistical Function---#
    L27 --> def __init__(self, db_name)

#---Players Ops Functions---#
    L35 --> show_players(self)
    L43 --> find_player(self, email)
    L51 --> delete_player(self, email)
    L58 --> add_player(self, pTeam, pFirstName, pLastName, pEmail)
    L65 --> update_attribute(self, searchEmail, pTeam, pFirstName, pLastName, pEmail, val) 
    L78 --> aggregate_op(self, email, val) 
'''

# Import
from database_conn import DatabaseOps

# CLASS: Contains various operations for getting and changing data in the players table.
# Additionally aggregates data from other tables.
class PlayerOps(DatabaseOps):
    #===============================================#
    #------------------Logistical-------------------#
    #===============================================#

    # FUNCTION: Initialize the Database.
    def __init__(self, db_name):
        super().__init__(db_name)

    #===============================================#
    #--------------Players Operations---------------#
    #===============================================#

    # FUNCTION: Return all player records.
    def show_players(self):
        # Call procedure.
        self.cursor.callproc("display_players")

        return self.get_results() # Return the results.
    

    # FUNCTION: Return the player of the input email.
    def find_player(self, email):
        # Call procedure.
        self.cursor.callproc("find_player", (email,))

        return self.get_results() # Return the results.


    # FUNCTION: Delete the player of the input email.
    def delete_player(self, email):
        # Call procedure.
        self.cursor.callproc("delete_player", (email,))
        # self.conn.commit() # Commented = Hard Delete, Uncommented = Soft Delete


    # FUNCTION: Add a new player record based on the input info.
    def add_player(self, pTeam, pFirstName, pLastName, pEmail):
        # Call procedure.
        self.cursor.callproc("add_player", (pTeam, pFirstName, pLastName, pEmail))
        self.conn.commit()


    # FUNCTION: Updates a specific players's attribute given the val parameter.
    def update_attribute(self, searchEmail, pTeam, pFirstName, pLastName, pEmail, val):
        # Call procedure.
        self.cursor.callproc("update_player_attribute", (searchEmail, 
                                                         pTeam, 
                                                         pFirstName, 
                                                         pLastName, 
                                                         pEmail, 
                                                         val))

        self.conn.commit()


    # FUNCTION: Either returns a count of each score or shot type for a player, or their average scores.
    def aggregate_op(self, email, val):
        # Determines which procedure to call.
        if(val == "Score Type Count"):
            self.cursor.callproc("count_player_score_type", (email,))

        elif(val == "Shot Type Count"):
            self.cursor.callproc("count_player_shot_type", (email,))

        elif(val == "Average Score"):
            self.cursor.callproc("average_player_score", (email,))
        
        return self.get_results() # Return the results.
    