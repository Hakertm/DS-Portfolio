'''
    TABLE OF CONTENTS

#---Logistical Function---#
    L23 --> __init__(self, db_name)

#---Frame Ops Functions---#
    L31 --> show_frames(self)
    L39 --> find_frames(self, gID, email)
    L47 --> add_frame(self, fNum, gID, email, fAttempt, fScore, fScoreType, fShotType, fPinSet, fBSpeed)
'''

# Import
from database_conn import DatabaseOps

# CLASS: Contains various operations for getting and changing data in the frames table.
class FrameOps(DatabaseOps):
    #===============================================#
    #------------------Logistical-------------------#
    #===============================================#

    # FUNCTION: Initialize the Database.
    def __init__(self, db_name):
        super().__init__(db_name)

    #===============================================#
    #--------------Frames Operations----------------#
    #===============================================#

    # FUNCTION: Shows all bowling game frames in the frames table.
    def show_frames(self):
        # Call procedure.
        self.cursor.callproc("display_frames")

        return self.get_results() # Return the results.
    
    
    # FUNCTION: Finds frames associated with a specific player and game.
    def find_frames(self, gID, email):
        # Call procedure.
        self.cursor.callproc("find_frames", (gID, email))

        return self.get_results() # Return the results.
    

    # FUNCTION: Adds a frame to the frames table given the inputs.
    def add_frame(self, fNum, gID, email, fAttempt, fScore, fScoreType, fShotType, fPinSet, fBSpeed):
        self.cursor.callproc("add_frame", (fNum, gID, email, fAttempt, fScore, fScoreType, fShotType, 
                                           fPinSet, fBSpeed))
        self.conn.commit()
