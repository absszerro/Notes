import tkinter as tk
import random
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
from functools import partial
import Icons as icons
import Params as p
from FrameView import FrameView as f_view


class FrameEdit(tk.Frame):
    def __init__(self, frame, width, height, check, frame_view):
        super(FrameEdit, self).__init__()
        print(frame_view)
        frame_view.update()
        print(frame_view.winfo_reqwidth())
        self.check = check
        self._master = frame
        self.width = width
        self.height = height
        self.frame_view = frame_view
        self.frame_edit = self.create_frame()
        self.index = 0

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

        button_text_add = ctk.CTkButton(frame,
                                        text='',
                                        image=icons.icon_add_text,
                                        fg_color='transparent',
                                        width=width,
                                        height=height,
                                        corner_radius=radius,
                                        hover_color=("gray70", "gray30"),
                                        command=lambda: self.add_elem('text')
                                        )
        button_num_list = ctk.CTkButton(frame,
                                        text='',
                                        image=icons.icon_add_num_list,
                                        fg_color='transparent',
                                        width=width,
                                        height=height,
                                        corner_radius=radius,
                                        hover_color=("gray70", "gray30"),
                                        command=lambda: self.add_elem('num_list')
                                        )
        button_mark_list_add = ctk.CTkButton(frame,
                                             text='',
                                             image=icons.icon_add_mark_list,
                                             fg_color='transparent',
                                             width=width,
                                             height=height,
                                             corner_radius=radius,
                                             hover_color=("gray70", "gray30"),
                                             command=lambda: self.add_elem('mark_list')
                                             )
        button_check_list_add = ctk.CTkButton(frame,
                                              text='',
                                              image=icons.icon_add_check_list,
                                              fg_color='transparent',
                                              width=width,
                                              height=height,
                                              corner_radius=radius,
                                              hover_color=("gray70", "gray30"),
                                              command=lambda: self.add_elem('task')
                                              )
        button_text_add.grid(row=0, column=0, padx=5, pady=5)
        button_num_list.grid(row=0, column=1, padx=5, pady=5)
        button_mark_list_add.grid(row=0, column=2, padx=5, pady=5)
        button_check_list_add.grid(row=0, column=3, padx=5, pady=5)
        return frame

    def add_elem(self, name):
        if name == 'text':
            self.clicked_add_text_elem(self.index)
            # self.check = self._master.check
            self.index += 1
        elif name == 'num_list':
            print('num_list')
            self.clicked_add_num_list(self.index)
        elif name == 'mark_list':
            print('mark_list')
            self.clicked_mark_list_add(self.index)
        elif name == 'task':
            print('task')
            self.clicked_check_list(self.index)

    def insert_mark(self, event):
        self.mark_list.insert(END, '\n•\t')  # добавляем пробелы на следующей строке
        return 'break'  # отменяем перевод строки от клавиши Enter

    def insert_num(self, event):
        self.text_num.insert(END, '\n1.\t')  # добавляем пробелы на следующей строке
        return 'break'  # отменяем перевод строки от клавиши Enter

    def clicked_add_text_elem(self, index):
        new_text = ctk.CTkTextbox(self.frame_view, width=960, height=50, border_width=2)
        print('add')
        new_text.grid(row=index, column=0, sticky='n', ipadx=10, ipady=10, padx=10, pady=10)
        # self.check = False
        # index += 1

    def clicked_check_list(self, index):
        new_text = ctk.CTkTextbox(self.frame_view, width=960, height=50, border_width=2)
        print('add')
        new_text.grid(row=index, column=0, sticky='n', ipadx=10, ipady=10, padx=10, pady=10)

    def clicked_mark_list_add(self, index):
        self.mark_list = ctk.CTkTextbox(self.frame_view, width=960, height=50, border_width=2)
        self.mark_list.insert('0', '1.')
        print('add')
        self.mark_list.grid(row=index, column=0, sticky='n', ipadx=10, ipady=10, padx=10, pady=10)
        self.mark_list.bind('<Return>', self.insert_mark)

    def clicked_add_num_list(self, index):
        self.text_num = ctk.CTkTextbox(self.frame_view, width=960, height=50, border_width=2)
        # self.text_num['']
        print('add')
        self.text_num.grid(row=index, column=0, sticky='n', ipadx=10, ipady=10, padx=10, pady=10)
        self.text_num.bind('<Return>', self.insert_num)
