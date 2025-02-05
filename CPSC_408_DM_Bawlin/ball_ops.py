'''
    TABLE OF CONTENTS

#---Logistical Function---#
    L26 --> __init__(self, db_name)

#---Bowling Balls Ops Functions---#
    L34 --> show_balls(self)
    L42 --> find_ball(self, email)
    L50 --> filter_by_cover(self, cover)
    L58 --> filter_by_core(self, core)
    L66 --> add_ball(self, bColor, bWeight, bCover, bCore, pEmail)
    L29 --> sort_by_weight(self, val)
'''

# Import
from database_conn import DatabaseOps

# CLASS: Contains various operations for getting and changing data in the bowling balls table.
class BallOps(DatabaseOps):
    #===============================================#
    #------------------Logistical-------------------#
    #===============================================#

    # FUNCTION: Initialize the Database.
    def __init__(self, db_name):
        super().__init__(db_name)

    #===============================================#
    #-----------Bowling Balls Operations------------#
    #===============================================#

    # FUNCTION: Displays all bowling ball records along with player email they're associated with.
    def show_balls(self):
        # Call procedure.
        self.cursor.callproc("display_balls")

        return self.get_results() # Return the results.
    

    # FUNCTION: Find bowling ball(s) associated with a specific player.
    def find_ball(self, email):
        # Call procedure.
        self.cursor.callproc("find_bowling_ball", (email,))

        return self.get_results() # Return the results.


    # FUNCTION: Returns the records of a specific coverstock.
    def filter_by_cover(self, cover):
        # Call procedure.
        self.cursor.callproc("filter_ball_by_cover", (cover,))

        return self.get_results() # Return the results.
    

    # FUNCTION: Returns the records of a specific core type.
    def filter_by_core(self, core):
        # Call procedure.
        self.cursor.callproc("filter_ball_by_core", (core,))

        return self.get_results() # Return the results.
    

    # FUNCTION: Add a bowling ball record to the DB given the inputs.
    def add_ball(self, bColor, bWeight, bCover, bCore, pEmail):
        # Call procedure.
        self.cursor.callproc("add_ball", (bColor, bWeight, bCover, bCore, pEmail))
        self.conn.commit()


    # FUNCTION: Returns records sorted by ascending or descending weight.
    def sort_by_weight(self, val):
        # Call procedure.
        self.cursor.callproc("sort_by_ball_weight", (val,))

        return self.get_results() # Return the results.
    