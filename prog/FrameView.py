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
        return frame
