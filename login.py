from tkinter import messagebox
from random import choice

import customtkinter as ctk
from PIL import Image
import pandas as pd

from VWidgets import *
from catclicker import ClickerGUI

ctk.set_appearance_mode("dark")

class LoginGUI(ctk.CTk):
    def __init__(self, image):
        super().__init__()

        height = 500
        width = 730
        center_x = (self.winfo_screenwidth() // 2) - (width // 2)
        center_y = (self.winfo_screenheight() // 2) - (height // 2)
        
        self.geometry("{}x{}+{}+{}".format(width, height, center_x, center_y))
        self.title("Login Catos")
        self.resizable(True, True)
        self.wm_protocol("WM_DELETE_WINDOW", self.on_closing)

        self.load_data_csv()
        self.load_images(image)

        self.newcat_pressed = False
        
        self.logincat_pressed = False
        self.data_logged = None

        global colours
        colours = ["red", "Blue", "green", "Purple", "orange"]

        #HEADERS
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(fill="x", padx=20, pady=10)

        self.head_frame = ctk.CTkFrame(self.top_frame, fg_color="white")
        self.head_frame.pack(fill="x", padx=10, pady=5)

        self.columns = self.df.columns.to_list()

        self.headers = VLabel(self.head_frame, text=".",
                              font=("Fixedsys", 24, "bold"), width=140).multiply_itself(3)
        
        for i, header in enumerate(self.columns):
            self.headers[i].configure(text=header, text_color=choice(colours))
        
        multi_grid(self.headers, "grid-horizontal", 10, 10, grid_propagate=False, Sticky="w")

        self.NewCat_Button = ctk.CTkButton(self.head_frame, width=140, text="New Cat",
        font=("Fixedsys", 18, "bold"), border_width=2, border_color="black", command=self.new_cat)
        self.NewCat_Button.grid(row=0, column=3, padx=10, pady=10, sticky="w")
        self.NewCat_Button.grid_propagate(False)

        #HEADERS

        #DATAS FRAMES
        self.datas = self.df.values.tolist()
        
        if len(self.datas) < 4:
            self.data_frame = ctk.CTkFrame(self, fg_color="white")
            self.data_frame.pack(fill="both", expand=True, padx=20, pady=10)
        else:
            self.data_frame = ctk.CTkScrollableFrame(self, fg_color="white")
            self.data_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        self.frames_of_data = VFrame(self.data_frame, fg_color="gray").multiply_itself(len(self.datas))
        multi_pack(self.frames_of_data, Fill="x", PadX=10, PadY=10, pack_propagate=False)
        #DATAS FRAMES

        #DATAS LABELS
        quanty = len(self.columns) * len(self.datas)

        self.data_labels = VLabel(self, font=("Fixedsys",22,"underline"),
                                  width=140).multiply_itself_with_masters(quanty, self.frames_of_data, 3)

        IndexLabelCount = 0
        for row in self.datas:
            for item in row:
                self.data_labels[IndexLabelCount].configure(text=truncate_text(item, 9),
                text_color="black")
                IndexLabelCount += 1
        
        multi_grid(self.data_labels, "grid-horizontal-specific", 10, 40, Sticky="w", grid_propagate=False, count_specific=3)
        #DATA LABELS

        #OPTIONS BUTTONS
        NumberOfButtons = len(self.frames_of_data)

        self.enterButtons = VButton(self, width=40, text_color="white", border_width=2, border_color="black",
         font=("Fixedsys",10)).multiply_itself_with_masters(NumberOfButtons, self.frames_of_data)

        for index in range(len(self.enterButtons)):
            self.enterButtons[index].configure(text="Cat login")

        add_values_on_command(self.login_cat, self.enterButtons)

        multi_grid(self.enterButtons, "grid-column", PadX=10, PadY=10, specific_col=3)


        self.deleteButtons = VButton(self, width=20, height=30, text_color="black", border_width=2,
        border_color="black", fg_color="red", font=("Fixedsys",10), hover_color="orange",
        image=self.DeleteImage).multiply_itself_with_masters(NumberOfButtons, self.frames_of_data)

        for index in range(len(self.deleteButtons)):
            self.deleteButtons[index].configure(text="")
        
        add_values_on_command(self.delete_cat_data, list_buttons=self.deleteButtons)

        multi_grid(self.deleteButtons, "grid-column", PadY=10, specific_col=4)

    def login_cat(self, number):
        self.logincat_pressed = True
        self.data_logged = [label.cget("text") for label in self.data_labels if label.Vmaster == self.frames_of_data[number]]
        self.on_closing()

    def delete_cat_data(self, number):
        sure = messagebox.askyesno(title="Delete Data", message="Are you sure?")

        delete = lambda : self.frames_of_data[number].destroy()
        if sure:
            self.df.drop(number, inplace=True)
            self.df.to_csv("saves//catos_logged.csv", index=False)
            
            self.after(200, delete)
        else:
            return None
    
    def new_cat(self):
        self.newcat_pressed = True
        self.on_closing()
    
    def load_data_csv(self):
        try:
            self.df = pd.read_csv("saves//catos_logged.csv").astype("str") 
        except FileNotFoundError:
            columns = ["Cat Name", "Score", "Coins"]
            df = pd.DataFrame(columns=columns)

            df.to_csv("saves//catos_logged.csv", index=False)
            self.load_data_csv()

    def is_dataframe_empty(self):
        if self.df.empty:
            messagebox.askokcancel(title="Everything Good!", message="No Data to load.")
            return True
        else:
            return False
    
    def load_images(self, trash):
        self.DeleteImage = trash
    
    def on_closing(self):
        self.withdraw()
        self.after(100, self.destroy)

if __name__ == "__main__":
    login = LoginGUI()

    if login.is_dataframe_empty() is False:
        login.mainloop()