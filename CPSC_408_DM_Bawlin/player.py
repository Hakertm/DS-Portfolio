'''
    TABLE OF CONTENTS

#---Logistical Function---#
    L33 --> __init__(self, *args, **kwargs)

#---UI Creation Function---#
    L55 --> create_ui(self, font_info)

#---UI Command Functions---#
    L187 --> show_players(self)
    L192 --> switch_button_text(self)
    L197 --> find_or_delete(self)
    L212 --> create_player(self)
    L226 --> update_attribute(self, choice)
    L245 --> aggregate_operation(self, choice)

#---Auxilary Function---#
    L261 --> output_results(self, results)
'''

# Imports
import customtkinter as cusTK
from player_ops import PlayerOps

# CLASS: Player Window/Page, contains various operations to interact with the players table.
class PlayerWindow(cusTK.CTkToplevel):
    #===============================================#
    #------------------Logistical-------------------#
    #===============================================#
    
    # FUNCTION: Initialize the player window.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create player database operations object.
        self.db_ops = PlayerOps("bowling")

        # Set the window size and title.
        self.geometry("1280x720")
        self.title("Players")

        # Text box created here in order to allow for access by commands.
        self.result_box = cusTK.CTkTextbox(self, font = ("System", 20))

        # Create the rest of the UI.
        font_i = ("System", 30) # Used to adjust button fonts easily.
        self.create_ui(font_i)

    #===============================================#
    #-----------------UI Creation-------------------#
    #===============================================#

    # FUNCTION: Create all the UI elements for the player window.
    def create_ui(self, font_info):
        # Button for Displaying Records
        self.display_button = cusTK.CTkButton(self, text = "Show Players", 
                                              command = self.show_players,
                                              fg_color = "#CC5500",
                                              hover_color = "#F28C28",
                                              font = font_info)
        
        self.display_button.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Results Label
        self.result_l = cusTK.CTkLabel(self, 
                                       text = "(:·)  (:·) ----------------Results---------------- (:·)  (:·)", 
                                       font = font_info)

        self.result_l.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "nsew")

        # Search/Delete Label
        self.find_del_l = cusTK.CTkLabel(self, text = "☼------Find/Delete a Player Record------☼",
                                         font = ("System", 20))

        self.find_del_l.grid(row = 1, column = 0, padx = 5, sticky = "nsew")

        # Entry Box for Search/Delete by Player Email
        self.find_del_e = cusTK.CTkEntry(self, placeholder_text = "Player Email to Find/Delete...")
        self.find_del_e.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Switch For Deciding to Search or Delete
        self.find_del_switch = cusTK.CTkSwitch(self, text = "Delete", 
                                                 offvalue = "Find", 
                                                 onvalue = "Delete",
                                                 command = self.switch_button_text,
                                                 font = font_info)
        
        self.find_del_switch.grid(row = 3, column = 0, padx = 5, pady = 5)

        # Button to Search or Delete (Based on Switch Above)
        self.find_del_b = cusTK.CTkButton(self, text = "Find Player",
                                            command = self.find_or_delete,
                                            fg_color = "#CC5500",
                                            hover_color = "#F28C28",
                                            font = font_info)
        
        self.find_del_b.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Create Player Label
        self.create_l = cusTK.CTkLabel(self, text = "☼------Add a New Player------☼",
                                       font = ("System", 20))

        self.create_l.grid(row = 5, column = 0, padx = 5, sticky = "nsew")

        # Entry Boxes for Creating a New Player
        self.create_e1 = cusTK.CTkEntry(self, placeholder_text = "Player Team...")
        self.create_e1.grid(row = 6, column = 0, padx = 5, pady = 5, sticky = "nsew")

        self.create_e2 = cusTK.CTkEntry(self, placeholder_text = "Player First Name...")
        self.create_e2.grid(row = 7, column = 0, padx = 5, pady = 5, sticky = "nsew")

        self.create_e3 = cusTK.CTkEntry(self, placeholder_text = "Player Last Name...")
        self.create_e3.grid(row = 8, column = 0, padx = 5, pady = 5, sticky = "nsew")

        self.create_e4 = cusTK.CTkEntry(self, placeholder_text = "Player Email...")
        self.create_e4.grid(row = 9, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Button to Create a New Player Record
        self.create_b = cusTK.CTkButton(self, text = "Add Player",
                                        command = self.create_player,
                                        fg_color = "#CC5500",
                                        hover_color = "#F28C28",
                                        font = font_info)
        
        self.create_b.grid(row = 10, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Update Player Label
        self.update_l = cusTK.CTkLabel(self, text = "☼------Update a Player's Info------☼",
                                       font = ("System", 20))
        
        self.update_l.grid(row = 11, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Update Entry Boxes
        self.update_e1 = cusTK.CTkEntry(self, placeholder_text = "Player Email to Update Value For...")
        self.update_e1.grid(row = 12, column = 0, padx = 5, pady = 5, sticky = "nsew")

        self.update_e2 = cusTK.CTkEntry(self, placeholder_text = "New Value... (see below)")
        self.update_e2.grid(row = 13, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Option Menu for Which Attribute to Update
        self.update_m = cusTK.CTkOptionMenu(self, values = ["Update Team Name", 
                                                            "Update First Name", 
                                                            "Update Last Name", 
                                                            "Update Email"],
                                            command = self.update_attribute,
                                            fg_color = "#CC5500",
                                            button_color = "#8B4000",
                                            button_hover_color = "#F28C28",
                                            font = ("System", 20))

        self.update_m.grid(row = 14, column = 0)

        # Label for Aggregate Operations
        self.aggregate_l = cusTK.CTkLabel(self, text = "☼------Aggregate Operations------☼",
                                          font = ("System", 20))
        
        self.aggregate_l.grid(row = 15, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Entry Box for Aggregate Operations
        self.aggregate_e = cusTK.CTkEntry(self, placeholder_text = "Player Email for Stats...")
        self.aggregate_e.grid(row = 16, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Segmented Button for Aggregate Operations
        self.aggregate_b = cusTK.CTkSegmentedButton(self, values = ["Score Type Count",
                                                                    "Shot Type Count",
                                                                    "Average Score"],
                                                    command = self.aggregate_operation,
                                                    dynamic_resizing = False,
                                                    selected_color = "#CC5500",
                                                    selected_hover_color = "#F28C28",
                                                    font = ("System", 20))

        self.aggregate_b.grid(row = 17, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Align all UI elements
        self.result_box.grid(row = 1, column = 1, padx = 5, pady = 5, rowspan = 18, sticky = "nsew")
        self.grid_columnconfigure(0, weight = 1) # Not uniformed due to ag ops text being too long.
        self.grid_columnconfigure(1, weight = 2) # Not uniformed due to ag ops text being too long.
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17), weight = 1)
    
    #===============================================#
    #-------------------Commands--------------------#
    #===============================================#

    # FUNCTION: Displays the players in the players table.
    def show_players(self):
        self.output_results(self.db_ops.show_players())


    # FUNCTION: Switch the text in the find/delete button.
    def switch_button_text(self):
        self.find_del_b.configure(text = f"{self.find_del_switch.get()} Player")


    # FUNCTION: Finds or deletes a player based on the previous swtich.
    def find_or_delete(self):
        self.result_box.delete("0.0", "end") # Clear text box contents.

        # Determines which operation to trigger based on the previous switch.
        # Find a player.
        if (self.find_del_switch.get() == "Find"):
            self.output_results(self.db_ops.find_player(self.find_del_e.get()))
        
        # Delete a player.
        else:
            self.db_ops.delete_player(self.find_del_e.get())
            self.result_box.insert("0.0", "Player Removed Successfully.")


    # FUNCTION: Adds a new player to the database based on input info.
    def create_player(self):
        self.result_box.delete("0.0", "end") # Clear text box contents.

        # Adds the player to the DB using input info.
        self.db_ops.add_player(self.create_e1.get(), # Team Name
                               self.create_e2.get(), # First Name
                               self.create_e3.get(), # Last Name
                               self.create_e4.get()) # Email

        # Confirmation.
        self.result_box.insert("0.0", "New Player Added Successfully.")


    # FUNCTION: Update a specific player's attribute.
    def update_attribute(self, choice):
        self.result_box.delete("0.0", "end") # Clear text box contents.

        # Store user input.
        userVal = self.update_e2.get()

        # Call the operation.
        self.db_ops.update_attribute(self.update_e1.get(), 
                                     userVal, # Team Name
                                     userVal, # First Name
                                     userVal, # Last Name
                                     userVal, # Email
                                     choice) # Which attribute to update.

        # Confirmation.
        self.result_box.insert("0.0", " Player Updated Successfully.")


    # FUNCTION: Returns specific stats of a player.
    def aggregate_operation(self, choice):
        self.result_box.delete("0.0", "end") # Clear text box contents.
        
        # Store the results.
        results = self.db_ops.aggregate_op(self.aggregate_e.get(), choice)

        # Output to the results text box.
        for data in results:
            self.result_box.insert("end", data)
            self.result_box.insert("end", "\n")

    #===============================================#
    #-------------------Auxilary--------------------#
    #===============================================#

    # FUNCTION: Outputs the results from a query to the textbox.
    def output_results(self, results):
        # Clear text box and display attribute order.
        self.result_box.delete("0.0", "end")
        self.result_box.insert("end", "Team Name, First Name, Last Name, Email\n\n")

        # Iterate through the results and display their data on the textbox.
        for data in results:
            p_team, p_firstName, p_lastName, p_email = data
            self.result_box.insert("end", f"{p_team}, {p_firstName}, {p_lastName}, {p_email}\n")
