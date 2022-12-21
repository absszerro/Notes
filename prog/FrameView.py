import tkinter as tk
import random
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
from functools import partial
import Icons as icons
import Params as p


class FrameView(tk.Frame):
    def __init__(self, frame, width, height):
        super(FrameView, self).__init__()
        self.width = width
        self.height = height
        self.master = frame
        self.frame_view = self.create_frame()

    def create_frame(self):
        frame = ctk.CTkFrame(self.master,
                             fg_color='gray15',
                             corner_radius=10,
                             width=self.width,
                             height=self.height,
                             border_color='red',
                             )
        frame.pack_propagate(False)
        frame.grid_propagate(False)

        # scrolling frame
        self.canvas = Canvas(frame, bg='gray15', bd=0, highlightthickness=0)
        second = ctk.CTkFrame(self.canvas,
                              fg_color='gray15',
                              corner_radius=10)
        scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        # !!! заполнение second
        second.update()
        if second.winfo_reqheight() > 624:
            scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.canvas.create_window((0, 0), window=second, anchor='nw')
        self.canvas.bind(
            '<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        #
        return frame
