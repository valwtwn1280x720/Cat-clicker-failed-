from typing import Any, Callable, Tuple
import customtkinter as ctk


class VLabel(ctk.CTkLabel):
    def __init__(self, master: Any, width: int = 0, height: int = 28, corner_radius: int | None = None,
                 bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None,
                 text_color: str | Tuple[str, str] | None = None, text_color_disabled: str | Tuple[str, str] | None = None,
                 text: str = "CTkLabel", font: tuple | ctk.CTkFont | None = None, image: ctk.CTkImage | None = None,
                 compound: str = "center", anchor: str = "center", wraplength: int = 0, **kwargs):
        
        super().__init__(master, width, height, corner_radius, bg_color, fg_color, text_color,
                         text_color_disabled, text, font, image, compound, anchor,
                         wraplength, **kwargs)
        
        self.Vmaster = master
        self.Vtext = text
        self.Vtext_color = text_color
        self.Vfont = font
        self.Vwidth = width
        self.Vimage = image
        self.Vcompound = compound
        self.Vfg_color = fg_color
        self.Vcorner_radius = corner_radius
    
    def multiply_itself (self, quantity:int):
        labels = []

        for i in range(quantity):
            label = VLabel(self.Vmaster, text=f"{self.Vtext} {i+1}", font=self.Vfont,
                           text_color=self.Vtext_color, width=self.Vwidth, image=self.Vimage,
                           compound=self.Vcompound, fg_color=self.Vfg_color, corner_radius=self.Vcorner_radius)
            labels.append(label)
        
        return labels
     
    def multiply_itself_with_masters(self, quantity:int, masters:list, widgets_per_master:int=1):
        labels = []

        for i in range(quantity):
            master_index = i // widgets_per_master

            master_index = min(master_index, len(masters) - 1)

            label = VLabel(masters[master_index], text=f"{self.Vtext} {i+1}", font=self.Vfont,
                           text_color=self.Vtext_color, width=self.Vwidth, image=self.Vimage,
                        compound=self.Vcompound, fg_color=self.Vfg_color, corner_radius=self.Vcorner_radius)
            labels.append(label)
        
        return labels


class VButton(ctk.CTkButton):
    def __init__(self, master: Any, width: int = 140, height: int = 28,
                 corner_radius: int | None = None, border_width: int | None = None,
                 border_spacing: int = 2, bg_color: str | Tuple[str] = "transparent",
                 fg_color: str | Tuple[str] | None = None, hover_color: str | Tuple[str] | None = None,
                 border_color: str | Tuple[str] | None = None, text_color: str | Tuple[str] | None = None,
                 text_color_disabled: str | Tuple[str] | None = None, background_corner_colors: Tuple[str | Tuple[str]] | None = None,
                 round_width_to_even_numbers: bool = True, round_height_to_even_numbers: bool = True,
                 text: str = "CTkButton", font: Tuple | ctk.CTkFont | None = None, textvariable: ctk.Variable | None = None,
                 image: ctk.CTkImage | Any | None = None, state: str = "normal", hover: bool = True,
                 command: Callable[[], Any] | None = None, compound: str = "left", anchor: str = "center", **kwargs):
        
        super().__init__(master, width, height, corner_radius, border_width, border_spacing,
                         bg_color, fg_color, hover_color, border_color, text_color,
                         text_color_disabled, background_corner_colors,
                         round_width_to_even_numbers, round_height_to_even_numbers, text, font,
                         textvariable, image, state, hover, command, compound, anchor, **kwargs)
        
        self.Vmaster = master
        self.Vwidth = width
        self.Vheight = height
        self.Vtext = text
        self.Vtext_color = text_color
        self.Vfont = font
        self.Vcorner_radius = corner_radius
        self.Vborder_width = border_width
        self.Vborder_color = border_color
        self.Vfg_color = fg_color
        self.Vhover = hover
        self.Vhover_color = hover_color
        self.Vimage = image
        self.Vcompound = compound
        self.Vcommand = command
        self.Vstate = state

    def multiply_itself (self, quantity:int):
        buttons = []

        for i in range(quantity):
            button = VButton(self.Vmaster, width=self.Vwidth, height=self.Vheight,
                             text=f"{self.Vtext} {i}", text_color=self.Vtext_color, font=self.Vfont,
                             corner_radius=self.Vcorner_radius, border_width=self.Vborder_width,
                             border_color=self.Vborder_color, fg_color=self.Vfg_color, hover=self.Vhover,
                             hover_color=self.Vhover_color, image=self.Vimage, compound=self.Vcompound,
                             command=self.Vcommand, state=self.Vstate)
            buttons.append(button)
        
        return buttons
    
    def multiply_itself_with_masters(self, quantity:int, masters:list, widgets_per_master:int=1):
        buttons = []

        for i in range(quantity):
            master_index = i // widgets_per_master

            master_index = min(master_index, len(masters) - 1)

            button = VButton(masters[master_index], width=self.Vwidth, height=self.Vheight,
                             text=f"{self.Vtext} {i}", text_color=self.Vtext_color, font=self.Vfont,
                             corner_radius=self.Vcorner_radius, border_width=self.Vborder_width,
                             border_color=self.Vborder_color, fg_color=self.Vfg_color, hover=self.Vhover,
                             hover_color=self.Vhover_color, image=self.Vimage, compound=self.Vcompound,
                             command=self.Vcommand, state=self.Vstate)
            buttons.append(button)
        
        return buttons


class VFrame(ctk.CTkFrame):
    def __init__(self, master: Any, width: int = 200, height: int = 200,
                 corner_radius: int | str | None = None, border_width: int | str | None = None,
                 bg_color: str | Tuple[str] = "transparent", fg_color: str | Tuple[str] | None = None,
                 border_color: str | Tuple[str] | None = None, background_corner_colors: Tuple[str | Tuple[str]] | None = None,
                 overwrite_preferred_drawing_method: str | None = None, **kwargs):
        
        super().__init__(master, width, height, corner_radius, border_width, bg_color,
                         fg_color, border_color, background_corner_colors,
                         overwrite_preferred_drawing_method, **kwargs)
        
        self.Vmaster = master
        self.Vheight = height
        self.Vwidth = width
        self.Vfg_color = fg_color
        self.Vborder_width = border_width
        self.Vborder_color = border_color

    def multiply_itself (self, quantity:int):
        frames = []

        for i in range(quantity):
            frame = VFrame(self.Vmaster, width=self.Vwidth, height=self.Vheight,
                           fg_color=self.Vfg_color, border_width=self.Vborder_width, border_color=self.Vborder_color)
            frames.append(frame)
        
        return frames


def multi_grid(list_widgets:list, command:str, PadX:int=0, PadY:int=0,
               Sticky:str="w", grid_propagate:bool=True, specific_col:int=0, specific_row:int=0,
               count_specific:int=1):
    match command:
        case "grid-horizontal":
            for i, widget in enumerate(list_widgets):
                widget.grid(row=0, column=i, padx=PadX, pady=PadY, sticky=Sticky)
                if grid_propagate is False:
                    widget.grid_propagate(False)
        
        case "grid-horizontal-specific": #For multiply_itself_with_master
            columnCount = 0
            for widget in list_widgets:
                widget.grid(row=0, column=columnCount, padx=PadX, pady=PadY, sticky=Sticky)

                columnCount += 1
                if columnCount == count_specific:
                    columnCount = 0
                
                if grid_propagate is False:
                    widget.grid_propagate(False)
        
        case "grid-vertical":
            for i, widget in enumerate(list_widgets):
                widget.grid(row=i, column=0, padx=PadX, pady=PadY, sticky=Sticky)
                if grid_propagate is False:
                    widget.grid_propagate(False)
        
        case "grid-column": #For multiply_itself_with_master
            for widget in list_widgets:
                widget.grid(row=0, column=specific_col, padx=PadX, pady=PadY, sticky=Sticky)
                if grid_propagate is False:
                    widget.grid_propagate(False)
        
        case "grid-row": #For multiply_itself_with_master
            for widget in list_widgets:
                widget.grid(row=specific_row, column=0, padx=PadX, pady=PadY, sticky=Sticky)
                if grid_propagate is False:
                    widget.grid_propagate(False)
        
        case "grid-row-column": #For multiply_itself_with_master
            for widget in list_widgets:
                widget.grid(row=specific_row, column=specific_col, padx=PadX, pady=PadY, sticky=Sticky)
                if grid_propagate is False:
                    widget.grid_propagate(False)

def multi_pack(list_widgets:list, PadX:int=0, PadY:int=0, Fill:str="none",
               Expand:bool=False, pack_propagate:bool=True):

    for widget in list_widgets:
        widget.pack(padx=PadX, pady=PadY, fill=Fill, expand=Expand)
        if not pack_propagate:
            widget.pack_propagate(False)

def multi_widget_forget(list_widgets:list, command:str):
    match command:
        case "pack":
            for widget in list_widgets:
                widget.pack_forget()

        case "grid":
            for widget in list_widgets:
                widget.grid_forget()

def truncate_text(text, max_length):
    if len(text) > max_length:
        return text[:max_length - 3] + "..."
    else:
        return text 

def add_values_on_command(func, list_buttons:list):
    for i in range(len(list_buttons)):
        list_buttons[i].configure(command = lambda c=i : func(number=c))
