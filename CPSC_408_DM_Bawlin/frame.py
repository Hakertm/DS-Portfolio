'''
    TABLE OF CONTENTS

#---Logistical Function---#
    L32 --> __init__(self, *args, **kwargs)

#---UI Creation Function---#
    L54 --> create_ui(self, font_info)

#---UI Command Functions---#
    L210 --> show_frames(self)
    L215 --> find_frames(self)
    L222, 226, 230 
        --> Changes the value below the respective slider.
    L235 --> add_frame(self)

#---Auxilary Function---#
    L257 --> output_results(self, results)
'''

# Imports
import customtkinter as cusTK
from frame_ops import FrameOps

# CLASS: Bowling Frame Window/Page, contains various operations to interact with the frames table.
class FrameWindow(cusTK.CTkToplevel):
    #===============================================#
    #------------------Logistical-------------------#
    #===============================================#
    
    # FUNCTION: Initialize the bowling frames window.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create bowling frame database operations object.
        self.db_ops = FrameOps("bowling")

        # Set the window size and title.
        self.geometry("1280x720")
        self.title("Frames")

        # Text box created here in order to allow for access by commands.
        self.result_box = cusTK.CTkTextbox(self, font = ("System", 20))

        # Create the rest of the UI.
        font_i = ("System", 30) # Used to adjust button fonts easily.
        self.create_ui(font_i)

    #===============================================#
    #-----------------UI Creation-------------------#
    #===============================================#

    # FUNCTION: Create all the UI elements for the bowling frames window.
    def create_ui(self, font_info):
        # TODO (Functionality): Add frames given inputs
        # TODO (UI Elements): Pin Setup Legend Label
        
        # Button to Display Records
        self.display_b = cusTK.CTkButton(self, text = "Show Frames", 
                                              command = self.show_frames,
                                              fg_color = "#CC5500",
                                              hover_color = "#F28C28",
                                              font = font_info)
        
        self.display_b.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")
        
        # Results Label
        self.result_l = cusTK.CTkLabel(self, 
                                       text = "(:·)  (:·) ----------------Results---------------- (:·)  (:·)", 
                                       font = font_info)
        
        self.result_l.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "nsew")

        # Find Frames Label
        self.find_l = cusTK.CTkLabel(self, text = "☼------Find Frames of Game+Player------☼",
                                     font = ("System", 20))
        
        self.find_l.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Find Frames Initial Entry Boxes
        self.find_e1 = cusTK.CTkEntry(self, placeholder_text = "Game ID...")
        self.find_e1.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "nsew")

        self.find_e2 = cusTK.CTkEntry(self, placeholder_text = "Player Email...")
        self.find_e2.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Find Frames Button
        self.find_b = cusTK.CTkButton(self, text = "Find Frames",
                                      command = self.find_frames,
                                      fg_color = "#CC5500",
                                      hover_color = "#F28C28",
                                      font = font_info)
        
        self.find_b.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Add Frame Label
        self.add_l = cusTK.CTkLabel(self, text = "☼------Add Frames------☼",
                                    font = ("System", 20))
        
        self.add_l.grid(row = 5, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Add Frame Entry Boxes
        self.add_e1 = cusTK.CTkEntry(self, placeholder_text = "Game ID...")
        self.add_e1.grid(row = 6, column = 0, padx = 5, pady = 5, sticky = "nsew")

        self.add_e2 = cusTK.CTkEntry(self, placeholder_text = "Player Email...")
        self.add_e2.grid(row = 7, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Add Frame Sliders
        # Frame
        self.add_s1 = cusTK.CTkSlider(self, from_ = 1, to = 10, 
                                         button_color = "#CC5500", 
                                         button_hover_color = "#F28C28", 
                                         number_of_steps = 9,
                                         command = self.set_frame_val)
        
        self.add_s1_l = cusTK.CTkLabel(self, text = "Frame: 5") # Displays slider value.
        self.add_s1.grid(row = 8, column = 0)
        self.add_s1_l.grid(row = 9, column = 0)

        # Attempt
        self.add_s2 = cusTK.CTkSlider(self, from_ = 1, to = 3, 
                                         button_color = "#CC5500", 
                                         button_hover_color = "#F28C28", 
                                         number_of_steps = 2,
                                         command = self.set_attempt_val)
        
        self.add_s2_l = cusTK.CTkLabel(self, text = "Attempt: 2") # Displays slider value.
        self.add_s2.grid(row = 10, column = 0)
        self.add_s2_l.grid(row = 11, column = 0)

        # Score
        self.add_s3 = cusTK.CTkSlider(self, from_ = 0, to = 10, 
                                         button_color = "#CC5500", 
                                         button_hover_color = "#F28C28", 
                                         number_of_steps = 10,
                                         command = self.set_score_val)
        
        self.add_s3_l = cusTK.CTkLabel(self, text = "Score: 5") # Displays slider value.
        self.add_s3.grid(row = 12, column = 0)
        self.add_s3_l.grid(row = 13, column = 0)


        # Add Frame Dropdowns
        # Score Type
        self.add_d1 = cusTK.CTkOptionMenu(self, values = ["Leftover", "Spare", "Strike"],
                                         width = 200,
                                         anchor = "center",
                                         fg_color = "#CC5500",
                                         button_color = "#8B4000",
                                         button_hover_color = "#F28C28",
                                         font = ("System", 20))
        
        self.add_d1.grid(row = 14, column = 0)

        # Shot Type
        self.add_d2 = cusTK.CTkOptionMenu(self, values = ["Straight", "Curve", 
                                                         "Straight-Curve", "Hard-Curve"],
                                         width = 200,
                                         anchor = "center",
                                         fg_color = "#CC5500",
                                         button_color = "#8B4000",
                                         button_hover_color = "#F28C28",
                                         font = ("System", 20))
        
        self.add_d2.grid(row = 15, column = 0)

        # Pin Setup
        self.add_d3 = cusTK.CTkOptionMenu(self, values = ["FH", "M", "MP", "L", "DL", "R", "DR", "HS"],
                                         width = 200,
                                         anchor = "center",
                                         fg_color = "#CC5500",
                                         button_color = "#8B4000",
                                         button_hover_color = "#F28C28",
                                         font = ("System", 20))
        
        self.add_d3.grid(row = 16, column = 0)


        # Add Frame Final Entry Box
        self.add_e3 = cusTK.CTkEntry(self, placeholder_text = "Ball Speed...")
        self.add_e3.grid(row = 17, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Add Frame Button
        self.add_b = cusTK.CTkButton(self, text = "Add Frame",
                                     command = self.add_frame,
                                     fg_color = "#CC5500",
                                     hover_color = "#F28C28",
                                     font = font_info)
        
        self.add_b.grid(row = 18, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Pin Setup Legend Label
        legend_text = "Pin Setup Legend\n"
        legend_text += "FH: Full House | M: Middle | MP: Multi-Pin\n"
        legend_text += "L: Left | DL: Deep Left | R: Right | DR: Deep Right\n"
        legend_text += "HS: Hard Shot"

        self.pin_legend_l = cusTK.CTkLabel(self, text = legend_text,
                                           font = ("System", 15))
        
        self.pin_legend_l.grid(row = 19, column = 0, padx = 5, pady = 5, sticky = "nsew")

        # Align all UI elements
        self.result_box.grid(row = 1, column = 1, padx = 5, pady = 5, rowspan = 20, sticky = "nsew")
        self.grid_columnconfigure(0, weight = 1, uniform = "column")
        self.grid_columnconfigure(1, weight = 2, uniform = "column")
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19), weight = 1)

    #===============================================#
    #-------------------Commands--------------------#
    #===============================================#

    # FUNCTION: Displays all bowling game frames in the frames table.
    def show_frames(self):
        self.output_results(self.db_ops.show_frames())


    # FUNCTION: Displays all bowling game frames associated with a specifc player and game.
    def find_frames(self):
        self.output_results(self.db_ops.find_frames(int(self.find_e1.get()), # Game ID
                                                    self.find_e2.get()))     # Player Email


    #=====Slider Adjustment Functions=====#
    # FUNCTION: Adjusts the frame slider label's value.
    def set_frame_val(self, val):
        self.add_s1_l.configure(text = f"Frame: {int(val)}")

    # FUNCTION: Adjusts the attempt slider label's value.
    def set_attempt_val(self, val):
        self.add_s2_l.configure(text = f"Attempt: {int(val)}")

    # FUNCTION: Adjusts the score slider label's value.
    def set_score_val(self, val):
        self.add_s3_l.configure(text = f"Score: {int(val)}")


    # FUNCTION: Adds a new bowling game frame to the database based on input info.
    def add_frame(self):
        self.result_box.delete("0.0", "end") # Clear text box contents.

        # Adds the frame to the DB using the input info.
        self.db_ops.add_frame(int(self.add_s1.get()),   # Frame Number
                              int(self.add_e1.get()),   # Game ID
                              self.add_e2.get(),        # Player Email
                              int(self.add_s2.get()),   # Frame Attempt
                              int(self.add_s3.get()),   # Frame Score
                              self.add_d1.get(),        # Score Type
                              self.add_d2.get(),        # Shot Type
                              self.add_d3.get(),        # Pin Setup
                              float(self.add_e3.get())) # Ball Speed
        
        # Confirmation.
        self.result_box.insert("0.0", f"Frame: {self.add_s1.get()} Attempt: {self.add_s2.get()} Added.")

    #===============================================#
    #-------------------Auxilary--------------------#
    #===============================================#

    # FUNCTION: Outputs the results from a query to the textbox.
    def output_results(self, results):
        # Clear text box and display attribute order.
        self.result_box.delete("0.0", "end")
        self.result_box.insert("end", "Frame, Game ID, Attempt, Score, Score Type, Shot Type, ")
        self.result_box.insert("end", "Pin Setup, Ball Speed (MPH)\n\n")

        # Iterate through the results and display their data on the textbox.
        for data in results:
            f_Num, g_ID, f_Att, f_Score, f_ScType, f_ShType, f_PinSet, f_BallSp = data
            self.result_box.insert("end", f"{f_Num}, {g_ID}, {f_Att}, {f_Score}, {f_ScType}, ")
            self.result_box.insert("end", f"{f_ShType}, {f_PinSet}, {f_BallSp}\n")
