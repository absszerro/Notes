import tkinter as tk
import random
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
from functools import partial
from NuT import NuT as nt
import Icons as icons
import Params as p
from datetime import datetime
from FrameTags import FrameTags as f_tags
from FrameView import FrameView as f_view
from FrameEdit import FrameEdit as f_edit


class HomePage(tk.Frame):
    def __init__(self, master):
        super(HomePage, self).__init__()
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Vertical.TScrollbar", background="gray15", bordercolor="gray15", arrowcolor="gray30",
                        troughcolor='gray15', elementborderwidth=3, activebackground='gray15', highlightthickness=0)
        self.check = True
        self.master = master
        self.frame_home = self.create_frame()

    def create_frame(self):
        frame = ctk.CTkFrame(self.master, width=p.WIDTH, height=p.HEIGHT, corner_radius=0, fg_color='transparent', )

        date_time = StringVar()
        date_time.set(datetime.now().strftime("%d.%m.%Y"))
        data = ''
        self.entry_data_time = ctk.CTkEntry(frame, textvariable=date_time, width=120, height=30, border_width=2,
                                            state=DISABLED)
        self.entry_data_time.place(relx=0.15, rely=0.03, anchor='ne')

        frame_tags = f_tags(frame, 850, 45)
        frame_tags.frame_tags.place(relx=0.57, rely=0.05, anchor=tk.CENTER)

        frame_view = f_view(frame, 1000, 550)
        frame_view.frame_view.place(relx=0.5, rely=0.11, anchor='n')

        frame_edit = f_edit(frame, 955, 50, self.check, frame_view)
        frame_edit.frame_edit.update()

        button_edit_save_note = ctk.CTkButton(frame,
                                              text='',
                                              image=icons.icon_edit,
                                              fg_color='transparent',
                                              width=10,
                                              height=10,
                                              hover_color=("gray70", "gray30"),
                                              command=lambda: self.clicked_edit_save_note(frame_edit.frame_edit,
                                                                                          button_edit_save_note)
                                              )
        #
        # # button_create_note.pack()
        button_edit_save_note.place(relx=0.95, rely=0.97, anchor='s')
        return frame

    def clicked_save_note(self, frame_edit, button_edit_save_note):
        self.check = True
        button_edit_save_note.configure(image=icons.icon_edit)
        frame_edit.place_forget()

    def clicked_edit_note(self, frame_edit, button_edit_save_note):
        self.check = False
        button_edit_save_note.configure(image=icons.icon_save)
        frame_edit.place(relx=0.479, rely=0.98, anchor='s')

    def clicked_edit_save_note(self, frame_edit, button_edit_save_note):
        if self.check:
            self.clicked_edit_note(frame_edit, button_edit_save_note)
        else:
            self.clicked_save_note(frame_edit, button_edit_save_note)
