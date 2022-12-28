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
    def __init__(self, frame, width, height, check):
        super(FrameView, self).__init__()
        self.width = width
        self.height = height
        self.master = frame
        self.check = check
        self.second = None
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
        self.second = ctk.CTkFrame(self.canvas,
                              fg_color='gray15',
                              corner_radius=10)
        scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        # !!! заполнение second

        # self.text_1 = ctk.CTkTextbox(second, width=930, height=30,
        #                            border_width=2, font=('', 18))
        # self.text_1.insert('0.0', 'Сегодня нужно сделать много дел...')
        # self.text_1.grid(row=0, column=2, sticky='n', ipadx=10, ipady=10, padx=10, pady=10)
        #
        # self.num_list = ctk.CTkTextbox(second, width=930,
        #                              height=60, border_width=2, font=('', 18))
        # self.num_list.insert('0.0', '\n1. Погулять с собакой\n2. Убраться дома')
        # self.num_list.grid(row=1, column=2, sticky='n', ipadx=10, ipady=10, padx=10, pady=10)
        #
        # self.text = ctk.CTkTextbox(second, width=930, height=30,
        #                          border_width=2, font=('', 18))
        # self.num_list.insert('0.0', '...какие подарки подарить родным?')
        # self.text.grid(row=2, column=2, sticky='n', ipadx=10, ipady=10, padx=10, pady=10)
        #
        # self.mark_list = ctk.CTkTextbox(second, width=930,
        #                               height=40, border_width=2, font=('', 18))
        # self.mark_list.insert('0.0', '· Погулять с собакой\n· Убраться дома\n· ')
        # self.mark_list.grid(row=3, column=2, sticky='n', ipadx=10, ipady=10, padx=10, pady=10)
        #
        # # check_var = StringVar("on")
        # self.checkbox = ctk.CTkCheckBox(second, text="Сходить в магазин",  font=('', 18))
        # self.checkbox.grid(row=4, column=2, sticky='w', ipadx=10, ipady=10, padx=10, pady=10)

        # !!!
        self.second.update()
        if self.second.winfo_reqheight() > 624:
            scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.canvas.create_window((0, 0), window=self.second, anchor='nw')
        self.canvas.bind(
            '<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        #

        return frame

    def add_elem(self, elem):
        # self.check = self._master.check
        while self.check:
            index = 0
            # добавить текстовое поле
            if name == 'text':
                self.clicked_add_text_elem(index)
            elif name == 'num_list':
                print('num_list')
                self.clicked_add_num_list(index)
            elif name == 'mark_list':
                print('mark_list')
                self.clicked_mark_list_add(index)
            elif name == 'task':
                print('task')
                self.clicked_check_list(index)
            # print('errrrrrr')
