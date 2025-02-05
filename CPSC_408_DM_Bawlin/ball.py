'''
    TABLE OF CONTENTS

#---Logistical Function---#
    L34 --> __init__(self, *args, **kwargs)

#---UI Creation Function---#
    L56 --> create_ui(self, font_info)

#---UI Command Functions---#
    L216 --> show_balls(self)
    L221 --> find_ball(self)
    L226 --> filter_by_cover(self, choice)
    L231 --> filter_by_core(self, choice)
    L236 --> set_val(self, val)
    L241 --> create_bowling_ball(self)
    L256 --> sort_by_weight(self, choice)

#---Auxilary Function---#
    L264 --> output_results(self, results)
'''

# Imports
import customtkinter as cusTK
from ball_ops import BallOps

# CLASS: Bowling Ball Window/Page, contains various operations to interact with the bowling balls table.
class BallWindow(cusTK.CTkToplevel):
    #===============================================#
    #------------------Logistical-------------------#
    #===============================================#
    
    # FUNCTION: Initialize the bowling ball window.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create bowling ball database operations object.
        self.db_ops = BallOps("bowling")

        # Set the window size and title.
        self.geometry("1280x720")
        self.title("Bowling Balls")

        # Text box created here in order to allow for access by commands.
        self.result_box = cusTK.CTkTextbox(self, font = ("System", 20))

        # Create the rest of the UI.
        font_i = ("System", 30) # Used to adjust button fonts easily.
        self.create_ui(font_i)

    #===============================================#
    #-----------------UI Creation-------------------#
    #===============================================#

    # FUNCTION: Create all the UI elements for the bowling ball window.
    def create_ui(self, font_info):
        # Button to Display Records
        self.display_b = cusTK.CTkButton(self, text = "Show Bowling Balls", 
                                              command = self.show_balls,
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
        self.find_l = cusTK.CTkLabel(self, text = "☼------Find Owned Bowling Balls------☼",
                                     font = ("System", 20))
        
        self.find_l.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Find Entry Box
        self.find_e = cusTK.CTkEntry(self, placeholder_text = "Player Email to Search By...")
        self.find_e.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Find Button
        self.find_b = cusTK.CTkButton(self, text = "Find Bowling Ball(s)",
                                      command = self.find_ball,
                                      fg_color = "#CC5500",
                                      hover_color = "#F28C28",
                                      font = font_info)
        
        self.find_b.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Filter Label
        self.filter_l = cusTK.CTkLabel(self, text = "☼------Filter By Coverstock or Core------☼",
                                       font = ("System", 20))
        
        self.filter_l.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Filter Dropdown/Option Menus
        # Coverstocks
        self.filter_d1 = cusTK.CTkOptionMenu(self, values = ["Plastic",
                                                             "Urethane",
                                                             "Reactive"],
                                             command = self.filter_by_cover,
                                             width = 200,
                                             anchor = "center",
                                             fg_color = "#CC5500",
                                             button_color = "#8B4000",
                                             button_hover_color = "#F28C28",
                                             font = ("System", 20))
        
        self.filter_d1.grid(row = 5, column = 0)

        # Cores
        self.filter_d2 = cusTK.CTkOptionMenu(self, values = ["Symmetrical",
                                                             "Asymmetrical",
                                                             "Pancake"],
                                             command = self.filter_by_core,
                                             width = 200,
                                             anchor = "center",
                                             fg_color = "#CC5500",
                                             button_color = "#8B4000",
                                             button_hover_color = "#F28C28",
                                             font = ("System", 20))
        
        self.filter_d2.grid(row = 6, column = 0)

        # Create Ball Label
        self.create_l = cusTK.CTkLabel(self, text = "☼------Add a Bowling Ball------☼",
                                       font = ("System", 20))
        
        self.create_l.grid(row = 7, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Create Ball Entry Boxes
        # Color
        self.create_e1 = cusTK.CTkEntry(self, placeholder_text = "Ball Color...")
        self.create_e1.grid(row = 8, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Weight
        self.create_e2 = cusTK.CTkSlider(self, button_color = "#CC5500", button_hover_color = "#F28C28", 
                                         from_ = 6, to = 16, 
                                         number_of_steps = 10,
                                         command = self.set_val)
        
        self.create_e2_l = cusTK.CTkLabel(self, text = "Weight: 11") # Displays slider value.

        self.create_e2.grid(row = 9, column = 0)
        self.create_e2_l.grid(row = 10, column = 0)

        # Coverstock
        self.create_e3 = cusTK.CTkOptionMenu(self, values = ["Plastic",
                                                             "Urethane",
                                                             "Reactive"],
                                             width = 200,
                                             anchor = "center",
                                             fg_color = "#CC5500",
                                             button_color = "#8B4000",
                                             button_hover_color = "#F28C28",
                                             font = ("System", 20))
        
        self.create_e3.grid(row = 11, column = 0)

        # Core
        self.create_e4 = cusTK.CTkOptionMenu(self, values = ["Symmetrical",
                                                             "Asymmetrical",
                                                             "Pancake"],
                                             width = 200,
                                             anchor = "center",
                                             fg_color = "#CC5500",
                                             button_color = "#8B4000",
                                             button_hover_color = "#F28C28",
                                             font = ("System", 20))
        
        self.create_e4.grid(row = 12, column = 0)

        # Email
        self.create_e5 = cusTK.CTkEntry(self, placeholder_text = "Player Email...")
        self.create_e5.grid(row = 13, column = 0, padx = 5, pady = 5, sticky = "nsew")


        # Create Ball Button
        self.create_b = cusTK.CTkButton(self, text = "Add Bowling Ball",
                                        command = self.create_bowling_ball,
                                        fg_color = "#CC5500",
                                        hover_color = "#F28C28",
                                        font = font_info)
        
        self.create_b.grid(row = 14, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Sort by Label
        self.sort_l = cusTK.CTkLabel(self, 
                                     text = "☼------Sort by Weight------☼",
                                     font = ("System", 20))
        
        self.sort_l.grid(row = 15, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Sort by Segemented Button
        self.sort_b = cusTK.CTkSegmentedButton(self, values = ["Ascending", "Descending"],
                                               command = self.sort_by_weight,
                                               selected_color = "#CC5500",
                                               selected_hover_color = "#F28C28",
                                               font = ("System", 20))
        
        self.sort_b.grid(row = 16, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Align all UI elements
        self.result_box.grid(row = 1, column = 1, padx = 5, pady = 5, rowspan = 17, sticky = "nsew")
        self.grid_columnconfigure(0, weight = 1, uniform = "column")
        self.grid_columnconfigure(1, weight = 2, uniform = "column")
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16), weight = 1)

    #===============================================#
    #-------------------Commands--------------------#
    #===============================================#

    # FUNCTION: Displays the bowling balls in the bowling balls table.
    def show_balls(self):
        self.output_results(self.db_ops.show_balls())


    # FUNCTION: Displays the bowling ball(s) associated with a specific player.
    def find_ball(self):
        self.output_results(self.db_ops.find_ball(self.find_e.get()))


    # FUNCTION: Displays bowling balls of a specific coverstock.
    def filter_by_cover(self, choice):
        self.output_results(self.db_ops.filter_by_cover(choice))


    # FUNCTION: Displays bowling balls of a specific core type.
    def filter_by_core(self, choice):
        self.output_results(self.db_ops.filter_by_core(choice))


    # FUNCTION: Adjusts the slider label's value.
    def set_val(self, val):
        self.create_e2_l.configure(text = f"Weight: {int(val)}")


    # FUNCTION: Adds a new bowling to the database based on input info.
    def create_bowling_ball(self):
        self.result_box.delete("0.0", "end") # Clear text box contents.

        # Adds the bowling ball to the DB using the input info.
        self.db_ops.add_ball(self.create_e1.get(),      # Color
                             int(self.create_e2.get()), # Weight
                             self.create_e3.get(),      # Coverstock
                             self.create_e4.get(),      # Core
                             self.create_e5.get())      # Player Email
        
        # Confirmation.
        self.result_box.insert("0.0", "New Bowling Ball Added Successfully.")


    # FUNCTION: Displays records sorted by weight ascending or descending.
    def sort_by_weight(self, choice):
        self.output_results(self.db_ops.sort_by_weight(choice))

    #===============================================#
    #-------------------Auxilary--------------------#
    #===============================================#

    # FUNCTION: Outputs the results from a query to the textbox.
    def output_results(self, results):
        # Clear text box and display attribute order.
        self.result_box.delete("0.0", "end")
        self.result_box.insert("end", "Color, Weight, Coverstock, Core, Email\n\n")

        # Iterate through the results and display their data on the textbox.
        for data in results:
            b_color, b_weight, b_cover, b_core, p_email = data
            self.result_box.insert("end", f"{b_color}, {b_weight}, {b_cover}, {b_core}, {p_email}\n")
