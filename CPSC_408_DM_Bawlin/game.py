'''
    TABLE OF CONTENTS

#---Logistical Function---#
    L34 --> __init__(self, *args, **kwargs)

#---UI Creation Function---#
    L56 --> create_ui(self, font_info)

#---UI Command Functions---#
    L198 --> show_games(self)
    L203 --> find_games(self)
    L208 --> add_game(self)
    L222 --> show_locs(self)
    L234 --> add_player_score(self)
    L247 --> show_or_gen(self, val)

#---Auxilary Function---#
    L289 --> output_results(self, results)
'''

# Imports
import customtkinter as cusTK
from game_ops import GameOps
import csv

# CLASS: Bowling Game Window/Page, contains various operations to interact with the games table.
class GameWindow(cusTK.CTkToplevel):
    #===============================================#
    #------------------Logistical-------------------#
    #===============================================#
    
    # FUNCTION: Initialize the bowling game window.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create bowling game database operations object.
        self.db_ops = GameOps("bowling")

        # Set the window size and title.
        self.geometry("1280x720")
        self.title("Games")

        # Text box created here in order to allow for access by commands.
        self.result_box = cusTK.CTkTextbox(self, font = ("System", 20))

        # Create the rest of the UI.
        font_i = ("System", 30) # Used to adjust button fonts easily.
        self.create_ui(font_i)

    #===============================================#
    #-----------------UI Creation-------------------#
    #===============================================#

    # FUNCTION: Create all the UI elements for the game window.
    def create_ui(self, font_info):  
        # Button to Display Records
        self.display_b = cusTK.CTkButton(self, text = "Show Games", 
                                              command = self.show_games,
                                              fg_color = "#CC5500",
                                              hover_color = "#F28C28",
                                              font = font_info)
        
        self.display_b.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")
        
        # Results Label
        self.result_l = cusTK.CTkLabel(self, 
                                       text = "(:·)  (:·) ----------------Results---------------- (:·)  (:·)", 
                                       font = font_info)
        
        self.result_l.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "nsew")

        # Find Label
        self.find_l = cusTK.CTkLabel(self, text = "☼------Find Games of Specific Player------☼",
                                     font = ("System", 20))
        
        self.find_l.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Find Entry
        self.find_e = cusTK.CTkEntry(self, placeholder_text = "Player Email...")
        self.find_e.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Find Button
        self.find_b = cusTK.CTkButton(self, text = "Find Games",
                                      command = self.find_games,
                                      fg_color = "#CC5500",
                                      hover_color = "#F28C28",
                                      font = font_info)
        
        self.find_b.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Create Game Record Label
        self.create_l = cusTK.CTkLabel(self, text = "☼------Add New Game Record------☼",
                                       font = ("System", 20))
        
        self.create_l.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Create Game Entry Boxes
        # Final Score
        self.create_e1 = cusTK.CTkEntry(self, placeholder_text = "Final Score...")
        self.create_e1.grid(row = 5, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Date (YYYY-MM-DD)
        self.create_e2 = cusTK.CTkEntry(self, placeholder_text = "Date Played(YYYY-MM-DD)...")
        self.create_e2.grid(row = 6, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Location
        self.create_e3 = cusTK.CTkEntry(self, placeholder_text = "Location Game Played...")
        self.create_e3.grid(row = 7, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Player Email
        self.create_e4 = cusTK.CTkEntry(self, placeholder_text = "Player Email...")
        self.create_e4.grid(row = 8, column = 0, padx = 5, pady = 5, sticky = "nsew")


        # Create Game Button
        self.create_b = cusTK.CTkButton(self, text = "Add Game Record",
                                        command = self.add_game,
                                        fg_color = "#CC5500",
                                        hover_color = "#F28C28",
                                        font = font_info)

        self.create_b.grid(row = 9, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Add Player Score Label
        self.add_score_l = cusTK.CTkLabel(self, text = "☼------Add Player Score------☼",
                                        font = ("System", 20))
        
        self.add_score_l.grid(row = 10, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Add Player Score Entry Boxes
        self.add_score_e1 = cusTK.CTkEntry(self, placeholder_text = "Player Email...")
        self.add_score_e1.grid(row = 11, column = 0, padx = 5, pady = 5, sticky = "nsew")

        self.add_score_e2 = cusTK.CTkEntry(self, placeholder_text = "Player Score...")
        self.add_score_e2.grid(row = 12, column = 0, padx = 5, pady = 5, sticky = "nsew")

        self.add_score_e3 = cusTK.CTkEntry(self, placeholder_text = "Game ID...")
        self.add_score_e3.grid(row = 13, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Add Player Score Button
        self.add_score_b = cusTK.CTkButton(self, text = "Add Player Score",
                                           command = self.add_player_score,
                                           fg_color = "#CC5500",
                                           hover_color = "#F28C28",
                                           font = font_info)

        self.add_score_b.grid(row = 14, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Unique Locations Label
        self.loc_l = cusTK.CTkLabel(self, text = "☼------Show all Unique Locations------☼",
                                    font = ("System", 20))
        
        self.loc_l.grid(row = 15, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Unique Locations Button
        self.loc_b = cusTK.CTkButton(self, text = "Unique Locations",
                                     command = self.show_locs,
                                     fg_color = "#CC5500",
                                     hover_color = "#F28C28",
                                     font = font_info)
        
        self.loc_b.grid(row = 16, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Show and Generate CSV Label
        self.gen_l = cusTK.CTkLabel(self, text = "☼------Show/Make CSV Player Games Info------☼",
                                    font = ("System", 20))

        self.gen_l.grid(row = 17, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Show and Generate CSV Entry Box
        self.gen_e = cusTK.CTkEntry(self, placeholder_text = "Player Email...")
        self.gen_e.grid(row = 18, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Show and Generate CSV Dropdown Menu
        self.gen_d = cusTK.CTkOptionMenu(self, values = ["Show Info", "Generate CSV"],
                                         command = self.show_or_gen,
                                         width = 200,
                                         anchor = "center",
                                         fg_color = "#CC5500",
                                         button_color = "#8B4000",
                                         button_hover_color = "#F28C28",
                                         font = ("System", 20))
        
        self.gen_d.grid(row = 19, pady = 5, column = 0)

        # Align all UI elements
        self.result_box.grid(row = 1, column = 1, padx = 5, pady = 5, rowspan = 20, sticky = "nsew")
        self.grid_columnconfigure(0, weight = 1, uniform = "column")
        self.grid_columnconfigure(1, weight = 2, uniform = "column")
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19), weight = 1)

    #===============================================#
    #-------------------Commands--------------------#
    #===============================================#

    # FUNCTION: Displays the bowling games in the bowling games table.
    def show_games(self):
        self.output_results(self.db_ops.show_games())


    # FUNCTION: Displays the game(s) associated with a specific player.
    def find_games(self):
        self.output_results(self.db_ops.find_games(self.find_e.get()))


    # FUNCTION: Adds a new game to the database based on input info.
    def add_game(self):
        self.result_box.delete("0.0", "end") # Clear text box contents.

        # Adds the game to the DB using the input info.
        self.db_ops.add_game(int(self.create_e1.get()), # Final Score
                             self.create_e2.get(),      # Date
                             self.create_e3.get(),      # Location
                             self.create_e4.get())      # Player Email

        # Confirmation.
        self.result_box.insert("0.0", "New Game Added Successfully.")


    # FUNCTION: Displays all unique locations games were played at.
    def show_locs(self):
        # Clear text box and display attribute name.
        self.result_box.delete("0.0", "end")
        self.result_box.insert("end", "Unique Locations\n\n")

        # Iterate through the results and display their data on the textbox.
        for data in self.db_ops.show_unique_locs():
            self.result_box.insert("end", data)
            self.result_box.insert("end", "\n")


    # FUNCTION: Adds a new player score to the player + game join table based on the input info.
    def add_player_score(self):
        self.result_box.delete("0.0", "end") # Clear text box contents.

        # Adds the player score to a specific game to the DB given the input info.
        self.db_ops.add_player_score(self.add_score_e1.get(),       # Email
                                     int(self.add_score_e2.get()),  # Final Score
                                     int(self.add_score_e3.get()))  # Game ID
        
        # Confirmation.
        self.result_box.insert("0.0", "New Player Score Added Successfully.")


    # FUNCTION: Displays every game played by a player and some of their personal information.
    def show_or_gen(self, val):
        self.result_box.delete("0.0", "end") # Clear text box contents.
        
        # Store the results.
        results = self.db_ops.show_player_game_info(self.gen_e.get())

        # Determine whether or not to generate a CSV file or only show the results.
        if(val == "Show Info"):
            # Display Headers/Attribute Order
            self.result_box.insert("end", "Email, First Name, Last Name, Team Name, Team Type, ")
            self.result_box.insert("end", "Game ID, Final Score, Date, Location\n\n")

            # Iterate through the results and display their data on the textbox.
            for data in results:
                p_Email, p_FName, p_LName, t_Name, t_Type, g_ID, g_Score, g_Date, g_Loc= data
                self.result_box.insert("end", f"{p_Email}, {p_FName}, {p_LName}, {t_Name}, {t_Type}, ")
                self.result_box.insert("end", f"{g_ID}, {g_Score}, {g_Date}, {g_Loc}\n")

        # Generate a CSV file given the results.
        else:
            # Headers for the CSV file.
            headers = ["Email", "First Name", "Last Name",           # Player Info
                       "Team Name", "Team Type",                     # Team Info
                       "Game ID", "Final Score", "Date", "Location"] # Game Info
            
            # Append all data from the operation results into one list. Will be inserted into the CSV.
            insert_data = [headers]
            for data in results:
                insert_data.append(data)

            # Create the CSV file and write the data to it.
            with open ("player_game_info.csv", "w", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(insert_data)

            self.result_box.insert("0.0", "Successfully generated a CSV file.")

    #===============================================#
    #-------------------Auxilary--------------------#
    #===============================================#

    # FUNCTION: Outputs the results from a query to the textbox.
    def output_results(self, results):
        # Clear text box and display attribute order.
        self.result_box.delete("0.0", "end")
        self.result_box.insert("end", "Game ID, Final Score, Date, Location, Email\n\n")
        
        # Iterate through the results and display their data on the textbox.
        for data in results:
            g_ID, g_Score, g_Date, g_Loc, p_Email = data
            self.result_box.insert("end", f"{g_ID}, {g_Score}, {g_Date}, {g_Loc}, {p_Email}\n")
