'''
    TABLE OF CONTENTS

#---Logistical Function---#
    L38 --> __init__(self, *args, **kwargs) | Initializes the app and main menu.

#---UI Creation Function---#
    L68 --> main_menu(self, font_info) | Creates the main menu. font_info is used for buttons only.

#---Button Command Functions---#
    L149, 160, 171, 182, 193
        --> Each functions opens/creates the respective window for the specific entitiy.
    L206, 211
        --> Quit commands. One is for the button, the other overwrites the X quit button.
'''

# Import Packages
import customtkinter as cusTK # If only I could name it tiger_knee; too long though :[
import sys

# Import Window Classes
from team import TeamWindow
from player import PlayerWindow
from ball import BallWindow
from game import GameWindow
from frame import FrameWindow

# Import Base Database Class (used for closing connection)
from database_conn import DatabaseOps

# CLASS: Main Menu, provides navigation to the different menus for the respective entities.
class App(cusTK.CTk):
    #===============================================#
    #------------------Logistical-------------------#
    #===============================================#

    # FUNCTION: Initializes the application and main menu page.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set the window size, title, and theme.
        self.geometry("1280x720")
        self.title("Bawlin'")
        cusTK.set_default_color_theme("green")
        
        # Overwrite X quit button functionality.
        self.protocol("WM_DELETE_WINDOW", self.x_quit)

        # Create DB operations object.
        self.db_ops = DatabaseOps("bowling")
        
        # Create the Main Menu.
        font = ("System", 30) # Font parameters for all the buttons.
        self.main_menu(font)

        # Window objects. Initialized upon selecting their respective button.
        self.teams_window = None
        self.players_window = None
        self.balls_window = None
        self.games_window = None
        self.frames_window = None

    #===============================================#
    #-----------------UI Creation-------------------#
    #===============================================#

    # FUNCTION: Creates the Main Menu page.
    def main_menu(self, font_info):
        #=====Create Menu Title=====#
        self.menu_title = cusTK.CTkLabel(self, text = "Bawlin'",
                                    font = ("System", 100))
    
        self.menu_title.grid(row = 0, column = 0, pady = (75, 10)) # Set position and vertical padding.
        
        #=====Create Buttons=====#
        # Teams Button
        self.team_b = cusTK.CTkButton(self, text = "Teams", 
                                  command = self.open_teams_win,
                                  fg_color = "#CC5500",
                                  hover_color = "#F28C28",
                                  width = 235,
                                  font = font_info)
        
        self.team_b.grid(row = 1, column = 0, pady = 10) # Set position and vertical padding.


        # Players Button
        self.player_b = cusTK.CTkButton(self, text = "Players", 
                                  command = self.open_players_win,
                                  fg_color = "#CC5500",
                                  hover_color = "#F28C28",
                                  width = 235,
                                  font = font_info)
        
        self.player_b.grid(row = 2, column = 0, pady = 10) # Set position and vertical padding.


        # Bowling Balls Button
        self.ball_b = cusTK.CTkButton(self, text = "Bowling Balls", 
                                  command = self.open_balls_win, 
                                  fg_color = "#CC5500",
                                  hover_color = "#F28C28",
                                  width = 235,
                                  font = font_info)
        
        self.ball_b.grid(row = 3, column = 0, pady = 10) # Set position and vertical padding.


        # Games Button
        self.game_b = cusTK.CTkButton(self, text = "Games", 
                                  command = self.open_games_win, 
                                  fg_color = "#CC5500",
                                  hover_color = "#F28C28",
                                  width = 235,
                                  font = font_info)
        
        self.game_b.grid(row = 4, column = 0, pady = 10) # Set position and vertical padding.

        
        # Frames Button
        self.frame_b = cusTK.CTkButton(self, text = "Frames", 
                                  command = self.open_frames_win, 
                                  fg_color = "#CC5500",
                                  hover_color = "#F28C28",
                                  width = 235,
                                  font = font_info)

        self.frame_b.grid(row = 5, column = 0, pady = 10) # Set position and vertical padding.


        # Quit Button
        self.quit_b = cusTK.CTkButton(self, text = "Quit", 
                                  command = self.quit_app, 
                                  fg_color = "#D70040",
                                  hover_color = "#880808",
                                  width = 150,
                                  font = font_info)
        
        self.quit_b.grid(row = 6, column = 0, pady = 10) # Set position and vertical padding.
        
        # Center the buttons and label.
        self.grid_columnconfigure(0, weight = 1)

    #===============================================#
    #-------------------Commands--------------------#
    #===============================================#

    # FUNCTION: Creates the teams window if non-existent. Focuses on it otherwise.
    def open_teams_win(self):
        # Create the team window if its None or if it has been destroyed.
        if ((self.teams_window is None) or (not self.teams_window.winfo_exists())):
            self.teams_window = TeamWindow(self)
            self.teams_window.after(10, self.teams_window.lift) # Moves the window to the top.
        
        # Focus on the window if it already exists.
        else:
            self.teams_window.focus()

    # FUNCTION: Creates the players window if non-existent. Focuses on it otherwise.
    def open_players_win(self):
        # Create the player window if its None or if it has been destroyed.
        if ((self.players_window is None) or (not self.players_window.winfo_exists())):
            self.players_window = PlayerWindow(self)
            self.players_window.after(10, self.players_window.lift) # Moves the window to the top.
        
        # Focus on the window if it already exists.
        else:
            self.players_window.focus()

    # FUNCTION: Creates the bowling balls window if non-existent. Focuses on it otherwise.
    def open_balls_win(self):
        # Create the bowling ball window if its None or if it has been destroyed.
        if ((self.balls_window is None) or (not self.balls_window.winfo_exists())):
            self.balls_window = BallWindow(self)
            self.balls_window.after(10, self.balls_window.lift) # Moves the window to the top.
        
        # Focus on the window if it already exists.
        else:
            self.balls_window.focus()
    
    # FUNCTION: Creates the games window if non-existent. Focuses on it otherwise.
    def open_games_win(self):
        # Create the game window if its None or if it has been destroyed.
        if ((self.games_window is None) or (not self.games_window.winfo_exists())):
            self.games_window = GameWindow(self)
            self.games_window.after(10, self.games_window.lift) # Moves the window to the top.
        
        # Focus on the window if it already exists.
        else:
            self.games_window.focus()
    
    # FUNCTION: Creates the frames window if non-existent. Focuses on it otherwise.
    def open_frames_win(self):
        # Create the frame window if its None or if it has been destroyed.
        if ((self.frames_window is None) or (not self.frames_window.winfo_exists())):
            self.frames_window = FrameWindow(self)
            self.frames_window.after(10, self.frames_window.lift) # Moves the window to the top.
        
        # Focus on the window if it already exists.
        else:
            self.frames_window.focus()


    #=====Quit Commands=====#
    # FUNCTION: Quit button command. Closes DB conenctions and exits the program.
    def quit_app(self):
        self.db_ops.close_connections()
        sys.exit()

    # FUNCTION: X quit button command. Closes DB connections and exits the program.
    def x_quit(self):
        self.db_ops.close_connections()
        sys.exit()
