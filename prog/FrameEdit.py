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
from List_of_NuT import List_of_NuT as list_of_NuT


class FrameEdit(tk.Frame):
    def __init__(self, frame, width, height, check, frame_view):
        super(FrameEdit, self).__init__()
        frame_view.update()
        self.check = check
        self._master = frame
        self.width = width
        self.height = height
        self.frame_view = frame_view
        self.frame_edit = self.create_frame()
        # self.save_text = ''
        # self.save_list_num = ''
        # self.save_list_mark = ''
        # self.save_task = ''
        self.list_of_nut = list_of_NuT()
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
        self.mark_list.update()
        self.mark_list.configure(height=self.mark_list.winfo_reqheight() + 1)
        return 'break'  # отменяем перевод строки от клавиши Enter

    def insert_num(self, event, num):
        # self.num_list.insert(END, '\n1.\t')  # добавляем пробелы на следующей строке
        self.num_list.insert(END, '\n' + str(num) + '.\t')  # добавляем пробелы на следующей строке
        self.num_list.configure(height=self.num_list.winfo_reqheight() + 1)
        # self.num_list.configure(height=self.num_list.get(1.0).count('\n')*30)
        self.num += 1
        return 'break'  # отменяем перевод строки от клавиши Enter

    def clicked_add_text_elem(self, index):
        text = ctk.CTkTextbox(self.frame_view, width=960, height=30, border_width=2, font=('', 18))
        print('add')
        text.grid(row=index, column=0, sticky='n', ipadx=10, ipady=10, padx=10, pady=10, columnspan=2)
        self.index += 1
        # self.check = False
        # index += 1

    def clicked_check_list(self, index):
        checkbox = ctk.CTkCheckBox(self.frame_view, text="", font=('', 18))
        task = ctk.CTkEntry(self.frame_view, width=850, height=30, border_width=2, font=('', 18))
        checkbox.grid(row=index, column=0, sticky='w', ipadx=0, ipady=10, padx=10, pady=10)
        task.grid(row=index, column=1, ipadx=0, ipady=10, padx=0, pady=10)
        self.index += 1

    def clicked_mark_list_add(self, index):
        self.mark_list = ctk.CTkTextbox(self.frame_view, width=960, height=10, border_width=2, font=('', 18))
        self.mark_list.insert('0.0', '•\t')
        print('add')
        self.mark_list.grid(row=index, column=0, sticky='n', ipadx=10, ipady=10, padx=10, pady=10, columnspan=2)
        self.mark_list.bind('<Return>', self.insert_mark)
        self.index += 1

    def clicked_add_num_list(self, index):
        self.num = 2
        self.num_list = ctk.CTkTextbox(self.frame_view, width=960, height=10, border_width=2, font=('', 18))
        self.num_list.insert('0.0', '1.\t')
        # self.text_num['']
        print('add')
        self.num_list.grid(row=index, column=0, sticky='n', ipadx=10, ipady=10, padx=10, pady=10, columnspan=2)
        self.num_list.bind('<Return>', lambda event: self.insert_num(event, self.num))
        self.index += 1
