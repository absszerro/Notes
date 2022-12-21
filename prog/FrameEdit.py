import tkinter as tk
import random
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
from functools import partial
import Icons as icons
import Params as p


class FrameEdit(tk.Frame):
    def __init__(self, frame, width, height):
        super(FrameEdit, self).__init__()
        self._master = frame
        self.width = width
        self.height = height
        self.frame_edit = self.create_frame()
        self.frame_edit.update()
        print('12121', self.frame_edit.winfo_reqwidth(), self.frame_edit.winfo_reqheight())
        print(self.width, self.height)

    def create_frame(self):
        width = 20
        height = 20
        radius = 10
        frame = ctk.CTkFrame(self._master,
                             fg_color="gray20",
                             corner_radius=10,
                             width=self.width,
                             height=self.height,
                             )
        frame.pack_propagate(False)
        frame.grid_propagate(False)
        frame.update()
        print('!edit', frame.winfo_reqwidth(), frame.winfo_reqheight())

        button_text_add = ctk.CTkButton(frame,
                                        text='',
                                        image=icons.icon_add_text,
                                        fg_color='transparent',
                                        width=width,
                                        height=height,
                                        corner_radius=radius,
                                        hover_color=("gray70", "gray30"),
                                        # command=self.clicked_add_text_elem(self.master)
                                        )
        button_num_list = ctk.CTkButton(frame,
                                        text='',
                                        image=icons.icon_add_num_list,
                                        fg_color='transparent',
                                        width=width,
                                        height=height,
                                        corner_radius=radius,
                                        hover_color=("gray70", "gray30"),
                                        # command=self.clicked_add_num_list
                                        )
        button_mark_list_add = ctk.CTkButton(frame,
                                             text='',
                                             image=icons.icon_add_mark_list,
                                             fg_color='transparent',
                                             width=width,
                                             height=height,
                                             corner_radius=radius,
                                             hover_color=("gray70", "gray30"),
                                             # command=self.clicked_mark_list_add
                                             )
        button_check_list_add = ctk.CTkButton(frame,
                                              text='',
                                              image=icons.icon_add_check_list,
                                              fg_color='transparent',
                                              width=width,
                                              height=height,
                                              corner_radius=radius,
                                              hover_color=("gray70", "gray30"),
                                              # command=self.clicked_check_list
                                              )
        button_text_add.grid(row=0, column=0, padx=5, pady=5)
        button_num_list.grid(row=0, column=1, padx=5, pady=5)
        button_mark_list_add.grid(row=0, column=2, padx=5, pady=5)
        button_check_list_add.grid(row=0, column=3, padx=5, pady=5)
        return frame
