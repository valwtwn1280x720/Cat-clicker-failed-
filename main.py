from catclicker import ClickerGUI
from login import LoginGUI
import time
from PIL import Image
import customtkinter as ctk


def load_images():
    TrashCan = Image.open(r"assets\trash.png")
    DeleteImage = ctk.CTkImage(TrashCan, size=(20,25))

    Img_cat = Image.open(r"assets\elgato.png")
    CatImage = ctk.CTkImage(Img_cat, size=(200,200))
    
    return [DeleteImage, CatImage]

Images = load_images()

def main(data_load=None):
    root = ctk.CTk()
    if data_load is None:
        game = ClickerGUI(root, Images[1])
        game.mainloop()
    else:
        game = ClickerGUI(root, Images[1], data_load)
        game.mainloop()

if __name__ == "__main__":
    login = LoginGUI(Images[0])
    
    start = login.is_dataframe_empty()
    if start:
        main()
    else:
        login.mainloop()
        if login.newcat_pressed is True:
            main()
        
        if login.logincat_pressed is True and login.data_logged != None:
            main(data_load=login.data_logged)