'''
    TABLE OF CONTENTS

#---Logistical Function---#
    L26 --> __init__(self, db_name)

#---Games Ops Functions---#
    L34 --> show_games(self)
    L42 --> find_games(self, email)
    L50 --> add_game(self, gScore, gDate, gLoc, pEmail)
    L57 --> show_unique_locs(self)
    L65 --> add_player_score(self, pEmail, pScore, gID)
    L72 --> show_player_game_info(self, email)
'''

# Import
from database_conn import DatabaseOps

# CLASS: Contains various operations for getting and changing data in the games table.
class GameOps(DatabaseOps):
    #===============================================#
    #------------------Logistical-------------------#
    #===============================================#

    # FUNCTION: Initialize the Database.
    def __init__(self, db_name):
        super().__init__(db_name)

    #===============================================#
    #---------------Games Operations----------------#
    #===============================================#

    # FUNCTION: Displays all game records along with the player email they're associated with.
    def show_games(self):
        # Call procedure.
        self.cursor.callproc("display_games")

        return self.get_results() # Return the results.
        
        
    # FUNCTION: Displays all game records associated with a specific player email.
    def find_games(self, email):
        # Call procedure.
        self.cursor.callproc("find_games", (email,))
        
        return self.get_results() # Return the results.
    

    # FUNCTION: Add a bowling game record to the DB given the inputs.
    def add_game(self, gScore, gDate, gLoc, pEmail):
        # Call procedure.
        self.cursor.callproc("add_game", (gScore, gDate, gLoc, pEmail))
        self.conn.commit()


    # FUNCTION: Displays all unique locations in the games table.
    def show_unique_locs(self):
        # Call procedure.
        self.cursor.callproc("show_game_locations")
        
        return self.get_results() # Return the results.


    # FUNCTION: Adds a player's score (given a specific game) to the player + game join table.
    def add_player_score(self, pEmail, pScore, gID):
        # Call procedure.
        self.cursor.callproc("add_final_score", (pEmail, pScore, gID))
        self.conn.commit()


    # FUNCTION: Displays every game played by a player as well as specific personal information.
    def show_player_game_info(self, email):
        # Call procedure.
        self.cursor.callproc("show_player_games_info", (email,))
        
        return self.get_results() # Return the results.
    