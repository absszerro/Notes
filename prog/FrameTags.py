import tkinter as tk
import random
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
from functools import partial
import Icons as icons
import Params as p


class FrameTags(tk.Frame):
    def __init__(self, frame, width, height):
        super(FrameTags, self).__init__()
        self.list = ['#idea', '#food', '#school', '#123']
        self._master = frame
        self.width = width
        self.height = height
        self.frame_tags = self.create_frame_tags()
        self.list_button = []

    def create_frame_tags(self):
        frame = ctk.CTkFrame(self._master,
                             fg_color='gray15',
                             corner_radius=10,
                             width=self.width,
                             height=self.height,
                             )
        frame.pack_propagate(False)
        frame.grid_propagate(False)
        self.create_list_tags(frame)
        return frame

    def create_list_tags(self, frame):
        index = 0
        for tag in self.list:
            tag_button = ctk.CTkButton(frame,
                                       text=tag,
                                       corner_radius=30,
                                       width=20,
                                       height=20,
                                       border_width=0,
                                       )
            tag_button.grid(row=0, column=index, padx=10, pady=10)
            index += 1
