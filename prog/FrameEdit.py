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
        # print(frame_view)
        self.check = check
        self._master = frame
        self.width = width
        self.height = height
        self.frame_edit = self.create_frame()

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
                                        command=self.add_elem('num_list')
                                        )
        button_mark_list_add = ctk.CTkButton(frame,
                                             text='',
                                             image=icons.icon_add_mark_list,
                                             fg_color='transparent',
                                             width=width,
                                             height=height,
                                             corner_radius=radius,
                                             hover_color=("gray70", "gray30"),
                                             command=self.add_elem('mark_list')
                                             )
        button_check_list_add = ctk.CTkButton(frame,
                                              text='',
                                              image=icons.icon_add_check_list,
                                              fg_color='transparent',
                                              width=width,
                                              height=height,
                                              corner_radius=radius,
                                              hover_color=("gray70", "gray30"),
                                              command=self.add_elem('tasks')
                                              )
        button_text_add.grid(row=0, column=0, padx=5, pady=5)
        button_num_list.grid(row=0, column=1, padx=5, pady=5)
        button_mark_list_add.grid(row=0, column=2, padx=5, pady=5)
        button_check_list_add.grid(row=0, column=3, padx=5, pady=5)
        return frame

    def add_elem(self, name):
        # self.check = self.frame_home.check
        # while not self.check:
        #     index = 0
        #     # добавить текстовое поле
        #     if name == 'text':
        #         print('text')
        #         self.clicked_add_text_elem(index)
        #     elif name == 'num_list':
        #         self.clicked_add_num_list(index)
        #     elif name == 'mark_list':
        #         self.clicked_mark_list_add(index)
        #     elif name == 'task':
        #         self.clicked_check_list(index)
        #     # print('errrrrrr')
        pass

    def clicked_add_text_elem(self, index):
        # new_text = ctk.CTkEntry(self.frame_view, placeholder_text='Поиск', width=600, height=30, border_width=2)
        # print('add')
        # new_text.grid(row=index, column=0,)
        pass

    def clicked_check_list(self, index):
        pass

    def clicked_mark_list_add(self, index):
        pass

    def clicked_add_num_list(self, index):
        pass
