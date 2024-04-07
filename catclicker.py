from random import choice, randint
import winsound
from winsound import Beep, PlaySound
from tkinter.messagebox import askretrycancel
from tkinter import messagebox

import customtkinter as ctk 
from PIL import Image
import pandas as pd

from VWidgets import *


class ClickerGUI(ctk.CTkToplevel):
    def __init__(self, master, image, data_to_load=None):
        super().__init__()

        height = 400
        width = 500
        center_x = (self.winfo_screenwidth() // 2) - (width // 2)
        center_y = (self.winfo_screenheight() // 2) - (height // 2)
        
        self.geometry("{}x{}+{}+{}".format(width, height, center_x, center_y))

        self.title("Cat Clicker")
        self.wm_protocol("WM_DELETE_WINDOW", self.on_closing)

        #usefull things
        global colors
        colors = ["green", "red", "orange", "blue", "purple", "cyan", "pink"]

        global funt
        funt = "Impact"
        global funt2
        funt2 = "Helvetica"
        global funt3
        funt3 = "Fixedsys"

        self.data_to_load = data_to_load
        if not data_to_load:
            #Frame del principio
            self.start_part = True

            self.start_frame = ctk.CTkFrame(self)
            self.start_frame.pack(pady=100)

            self.intro_label = ctk.CTkLabel(self.start_frame, text="Enter the cat's name :D",
                                            text_color=choice(colors), font=(funt, 28))
            self.intro_label.pack(pady=10, padx=20)

            self.name_entry = ctk.CTkEntry(self.start_frame, font=(funt2,24), width=250)
            self.name_entry.pack(pady=10)

            self.save_name_button = ctk.CTkButton(self.start_frame, text="Save Name",
                                                text_color="white", fg_color="green", font=(funt2,16),
                                                border_width=2, border_spacing=1, corner_radius=50,
                                                border_color="black", hover_color="orange",
                                                command=self.start_game)
            self.save_name_button.pack(pady=10)

            #Frame del gato e info
            self.load_images(image)

            self.cat_frame = ctk.CTkFrame(self)

            self.cat_image_label = ctk.CTkLabel(self.cat_frame, image=self.cat_image, text="")
            self.cat_image_label.pack()
            self.cat_image_label.bind("<Button-1>", self.click_on_cat)

            #Frame del nombre del gato
            self.cat_name_frame = ctk.CTkFrame(self)

            self.cat_name_label = ctk.CTkLabel(self.cat_frame, text="")
            self.cat_name_label.pack(pady=20)

            #Frame del score y datos
            self.score_frame = ctk.CTkFrame(self)

            self.score_count = 0
            self.score_label = ctk.CTkLabel(self.score_frame, font=(funt3, 22, "bold"),
                                            text=f"Score:\n{self.score_count}")
            self.score_label.pack(pady=10, padx=20)

            self.coins = 0
            self.coin_label = ctk.CTkLabel(self.score_frame, text=f"Coins:\n{self.coins}",
                                        font=(funt3, 16, "bold"))
            self.coin_label.pack(pady=5, padx=10)
        
        else:

            #Frame del gato e info
            self.load_images(image)

            self.cat_frame = ctk.CTkFrame(self)

            self.cat_image_label = ctk.CTkLabel(self.cat_frame, image=self.cat_image, text="")
            self.cat_image_label.pack()
            self.cat_image_label.bind("<Button-1>", self.click_on_cat)

            #Frame del nombre del gato
            self.cat_name_frame = ctk.CTkFrame(self)

            self.cat_name_label = ctk.CTkLabel(self.cat_frame, text="")
            self.cat_name_label.pack(pady=20)

            #Frame del score y datos
            self.score_frame = ctk.CTkFrame(self)

            self.score_count = int(self.data_to_load[1])
            self.score_label = ctk.CTkLabel(self.score_frame, font=(funt3, 22, "bold"),
                                            text=f"Score:\n{self.score_count}")
            self.score_label.pack(pady=10, padx=20)

            self.coins = int(self.data_to_load[2])
            self.coin_label = ctk.CTkLabel(self.score_frame, text=f"Coins:\n{self.coins}",
                                        font=(funt3, 16, "bold"))
            self.coin_label.pack(pady=5, padx=10)

            self.start_game()


    def start_game(self):
        if self.data_to_load:
            self.cat_name = self.data_to_load[0]
        else:
            self.cat_name = self.name_entry.get().capitalize()

        if self.cat_name == "":
            askretrycancel(title="Why none?!", message="Cat must have a name!!")
            return None #Needs to insert a name for the kitty

        self.cat_name_label.configure(text=self.cat_name, font=(funt3,22),
                                      text_color=choice(colors), fg_color="white",
                                      corner_radius=12)

        if not self.data_to_load:
            self.start_frame.after(200, self.start_frame.pack_forget)

        self.cat_frame.pack(pady=50,padx=30, side="left")
        self.score_frame.pack(pady=50, padx=30, side="right")

        self.start_part = False

    def click_on_cat(self, event):
        self.score_count += 1
        self.score_label.configure(text=f"Score:\n{self.score_count}")
        Beep(320, 50)

        probability = randint(1,120)
        change = lambda : self.coin_label.configure(text=f"Coins:\n{self.coins}")

        if probability == 55:
            PlaySound("assets//meow_sound.wav", winsound.SND_ASYNC)
            self.coins += 20
            self.coin_label.configure(text=f"Coins:\n{self.coins} + MEOW!")
            self.coin_label.after(300, change)

        if probability < 25:
            self.coins += 1
            self.coin_label.configure(text=f"Coins:\n{self.coins} +1")
            self.coin_label.after(300, change)
    
    def load_images(self, cat_image):
        self.cat_image = cat_image

    def save_data_to_csv(self):
        if self.start_part is False:
            df = pd.read_csv("saves//catos_logged.csv")
        
            # Verificar si ya existe una fila con el mismo "Cat Name"
            existing_row = df[df['Cat Name'] == self.cat_name]

            if not existing_row.empty:
                # Actualizar los valores "Score" y "Coins" en la fila existente
                df.loc[df['Cat Name'] == self.cat_name, ['Score', 'Coins']] = [self.score_count, self.coins]
            else:
                # Agregar una nueva fila con los datos del gato
                new_file = pd.DataFrame([[self.cat_name, self.score_count, self.coins]],
                                    columns=["Cat Name", "Score", "Coins"])
                df = pd.concat([df, new_file], ignore_index=True)

            df.to_csv("saves//catos_logged.csv", index=False)
        else:
            return

    def on_closing(self):
        self.save_data_to_csv()
        
        self.after(100, self.withdraw)
        exit()

