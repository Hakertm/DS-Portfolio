'''
    TABLE OF CONTENTS

#---Logistical Function---#
    L32 --> __init__(self, *args, **kwargs) | Initializes the team window and UI elements.

#---UI Creation Function---#
    L54 --> create_ui(self, font_info) | Creates + Aligns all UI elements.

#---UI Command Functions---#
    L166 --> show_teams(self) | Displays all teams in the teams table.
    L171 --> find_team(self) | Finds and displays the team of a specific name.
    L176 --> filter_by(self, choice) | Displays all teams of a specific team type.
    L181 --> create_team(self) | Adds a new team to the teams table. Displays confirmation.
    L194 --> update_attribute(self, choice) | Updates a specific attribute of a specified team.

#---Auxilary Function---#
    L215 --> output_results(self, results) | Displays DB operation results to the result box.
'''

# Imports
import customtkinter as cusTK
from team_ops import TeamOps

# CLASS: Team Window/Page, contains various operations to interact with the teams table.
class TeamWindow(cusTK.CTkToplevel):
    #===============================================#
    #------------------Logistical-------------------#
    #===============================================#
    
    # FUNCTION: Initialize the team window.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create team database operations object.
        self.db_ops = TeamOps("bowling")

        # Set the window size and title.
        self.geometry("1280x720")
        self.title("Teams")

        # Text box created here in order to allow for access by commands.
        self.result_box = cusTK.CTkTextbox(self, font = ("System", 20))

        # Create the rest of the UI.
        font_i = ("System", 30) # Used to adjust button fonts easily.
        self.create_ui(font_i)
    
    #===============================================#
    #-----------------UI Creation-------------------#
    #===============================================#

    # FUNCTION: Create all the UI elements for the team window.
    def create_ui(self, font_info):
        # Button for Displaying Current Records
        self.display_button = cusTK.CTkButton(self, text = "Show Teams", 
                                              command = self.show_teams,
                                              fg_color = "#CC5500",
                                              hover_color = "#F28C28", 
                                              font = font_info)
        
        self.display_button.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Results Label
        self.result_l = cusTK.CTkLabel(self, 
                                       text = "(:·)  (:·) ----------------Results---------------- (:·)  (:·)", 
                                       font = font_info)

        self.result_l.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "nsew")
        
        # Entry Box for Search by Team Name
        self.search_e = cusTK.CTkEntry(self, placeholder_text = "Search for a team (by name)")
        self.search_e.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Search for Team Button
        self.search_b = cusTK.CTkButton(self, text = "Find Team",
                                         command = self.find_team,
                                         fg_color = "#CC5500",
                                         hover_color = "#F28C28",
                                         font = font_info)
        
        self.search_b.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Filter Label
        self.filter_label = cusTK.CTkLabel(self, text = "☼------Filter by Team Type------☼",
                                            font = ("System", 20))

        self.filter_label.grid(row = 3, column = 0, padx = 5, sticky = "nsew")

        # Options Menu for Filtering by Specific Values
        self.filters = cusTK.CTkOptionMenu(self, values = ["Solo", "School", "Private", "Other"],
                                         command = self.filter_by,
                                         width = 200,
                                         anchor = "center",
                                         fg_color = "#CC5500",
                                         button_color = "#8B4000",
                                         button_hover_color = "#F28C28",
                                         font = font_info)
        
        self.filters.grid(row = 4, column = 0)

        # Create Team Label
        self.create_label = cusTK.CTkLabel(self, text = "☼------Add a New Team------☼",
                                            font = ("System", 20))
        
        self.create_label.grid(row = 5, column = 0, padx = 5, sticky = "nsew")

        # Entry Boxes for Creating a New Team
        self.create_e1 = cusTK.CTkEntry(self, placeholder_text = "Team Name...")
        self.create_e1.grid(row = 6, column = 0, padx = 5, pady = 5, sticky = "nsew")
        
        self.create_e2 = cusTK.CTkEntry(self, placeholder_text = "Team Size...")
        self.create_e2.grid(row = 7, column = 0, padx = 5, pady = 5, sticky = "nsew")
        
        # Option Menu for Third Entry
        self.create_e3 = cusTK.CTkSegmentedButton(self, values = ["Solo", "School", "Private", "Other"],
                                                    selected_color = "#CC5500",
                                                    selected_hover_color = "#F28C28",
                                                    font = ("System", 20))
        
        self.create_e3.grid(row = 8, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Create Team Record Button
        self.create_b = cusTK.CTkButton(self, text = "Add Team",
                                        command = self.create_team,
                                        fg_color = "#CC5500",
                                        hover_color = "#F28C28",
                                        font = font_info)
        
        self.create_b.grid(row = 9, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Update Team Label
        self.update_label = cusTK.CTkLabel(self, text = "☼------Update a Team's Info------☼",
                                           font = ("System", 20))
        
        self.update_label.grid(row = 10, column = 0, padx = 5, sticky = "nsew")

        # Entry Boxes for Updating Attributes
        self.update_e1 = cusTK.CTkEntry(self, placeholder_text= "Team Name to Update a Value For...")
        self.update_e1.grid(row = 11, column = 0, padx = 5, pady = 5, sticky = "nsew")

        self.update_e2 = cusTK.CTkEntry(self, placeholder_text = "New Value... (see below)")
        self.update_e2.grid(row = 12, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Segmented Button for Choosing What to Update
        self.update_b = cusTK.CTkSegmentedButton(self, values = ["Update Name", "Update Size", "Update Type"],
                                                 command = self.update_attribute,
                                                 dynamic_resizing = False,
                                                 selected_color = "#CC5500",
                                                 selected_hover_color = "#F28C28",
                                                 font = ("System", 20))
        
        self.update_b.grid(row = 13, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Align all UI elements
        self.result_box.grid(row = 1, column = 1, padx = 5, pady = 5, rowspan = 14, sticky = "nsew")
        self.grid_columnconfigure(0, weight = 1, uniform = "column")
        self.grid_columnconfigure(1, weight = 2, uniform = "column")
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), weight = 1)

    #===============================================#
    #-------------------Commands--------------------#
    #===============================================#

    # FUNCTION: Displays the teams in the DB table.
    def show_teams(self):
        self.output_results(self.db_ops.show_teams())  


    # FUNCTION: Displays the team of the input name from the entry box.
    def find_team(self):
        self.output_results(self.db_ops.find_team(self.search_e.get()))


    # FUNCTION: Displays teams only of a specific team type.
    def filter_by(self, choice):
        self.output_results(self.db_ops.filter_by_type(choice))


    # FUNCTION: Adds a new team to the database based on entered data.
    def create_team(self):
        self.result_box.delete("0.0", "end") # Clear text box contents.

        # Adds the team to the DB using input info.
        self.db_ops.add_team(self.create_e1.get(),      # Team Name
                             int(self.create_e2.get()), # Team Size
                             self.create_e3.get())      # Team Type
        
        # Confirmation.
        self.result_box.insert("0.0", "New Team Added Successfully.")


    # FUNCTION: Updates a team's specific attribute.
    def update_attribute(self, choice):
        self.result_box.delete("0.0", "end") # Clear text box contents.
        
        # Store user input.
        userVal = self.update_e2.get()

        # Ensure no ValueError is thrown for other options. NOT A PROPER ERROR CHECK.
        if(choice == "Update Size"):
            self.db_ops.update_attribute(self.update_e1.get(), userVal, int(userVal), userVal, choice)
        
        else:
            self.db_ops.update_attribute(self.update_e1.get(), userVal, 1, userVal, choice)

        # Confirmation
        self.result_box.insert("0.0", f"Successfully Updated {self.update_e1.get()}'s Information.")

    #===============================================#
    #-------------------Auxilary--------------------#
    #===============================================#

    # FUNCTION: Outputs the results from a query to the textbox.
    def output_results(self, results):
        # Clear text box and display attribute order.
        self.result_box.delete("0.0", "end")
        self.result_box.insert("end", "Team Name, Team Size, Team Type\n\n")
        
        # Iterate through the results and display their data on the textbox.
        for data in results:
            t_name, t_size, t_type = data
            self.result_box.insert("end", f"{t_name}, {t_size}, {t_type}\n")
