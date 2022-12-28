import tkinter as tk
import random

import matplotlib
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from NuT import NuT as nt
from All_Nut import All_Nut as all_nt

from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from functools import partial
import Icons as icons
import Params as p
from FrameTags import FrameTags as f_tags
from HomePage import HomePage as home_page

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class MainWindow(ctk.CTk):
    def __init__(self, ):
        super().__init__()

        self.check = True

        # self.iconbitmap('icons/betel-nut.png')

        self.all_nut = all_nt()  # все заметки

        style = ttk.Style()
        style.theme_use('default')
        style.configure("Vertical.TScrollbar", background="gray15", bordercolor="gray15", arrowcolor="gray30",
                        troughcolor='gray15', elementborderwidth=3, activebackground='gray15', highlightthickness=0)

        # create a window
        self.title('NuT')
        self.resizable(False, False)
        self.geometry(f"{p.WIDTH}x{p.HEIGHT}")
        # self.home_frame = None

        # self.frame_icon = ctk.CTkFrame(self, width=p.WIDTH // 100 * 5, height=p.HEIGHT)
        # self.frame_icon.place(relx=0.5, rely=0.5, anchor='n')

        logo = ctk.CTkImage(Image.open('icons/betel-nut.png'), size=(250, 250))

        self.label_welcome = ctk.CTkLabel(self, image=logo, text='Добро пожаловать\n в приложение NuT!',
                                          compound='bottom', font=('Comic Sans MS', 36), text_color='#E0F5BC')
        self.label_welcome.place(relx=0.55, rely=0.5, anchor='center')

        # left panel frame
        self.left_panel_frame = ctk.CTkFrame(self, width=p.WIDTH // 100 * 5, height=p.HEIGHT)
        self.left_panel_frame.pack(fill=tk.Y, side=tk.LEFT)
        self.home_button = ctk.CTkButton(self.left_panel_frame,
                                         text='Главная',
                                         font=('Comic Sans MS', 18),
                                         image=icons.icon_home,
                                         fg_color='transparent',
                                         corner_radius=0,
                                         hover_color=("gray70", "gray30"),
                                         anchor="w",
                                         border_spacing=10,
                                         # compound='LEFT',
                                         command=self.clicked_home_button)
        self.home_button.pack(fill=tk.X, side=tk.TOP)
        self.archive_button = ctk.CTkButton(self.left_panel_frame,
                                            text='Архив',
                                            font=('Comic Sans MS', 18),
                                            image=icons.icon_archive,
                                            fg_color='transparent',
                                            corner_radius=0,
                                            anchor="w",
                                            border_spacing=10,
                                            hover_color=("gray70", "gray30"),
                                            command=self.clicked_archive_button)
        self.archive_button.pack(fill=tk.X, side=tk.TOP)
        self.statistics_button = ctk.CTkButton(self.left_panel_frame,
                                               text='Статистика',
                                               font=('Comic Sans MS', 18),
                                               image=icons.icon_statistics,
                                               fg_color='transparent',
                                               corner_radius=0,
                                               anchor="w",
                                               border_spacing=10,
                                               hover_color=("gray70", "gray30"),
                                               command=self.clicked_statistics_button)
        self.statistics_button.pack(fill=tk.X, side=tk.TOP)

        self.settings_button = ctk.CTkButton(self.left_panel_frame,
                                             text='Настройки',
                                             font=('Comic Sans MS', 18),
                                             image=icons.icon_settings,
                                             fg_color='transparent',
                                             corner_radius=0,
                                             anchor="w",
                                             border_spacing=10,
                                             hover_color=("gray70", "gray30"),
                                             command=self.clicked_settings_button)
        self.settings_button.pack(fill=tk.X, side=tk.BOTTOM)

        # today frame

        self.home_frame = home_page(self).frame_home
        # self.home_frame = self.create_home_frame()

        # archive frame
        self.archive_frame = self.create_archive_frame()

        # statistics frame
        self.statistics_frame = self.create_statistics_frame()

        # settings frame
        self.settings_frame = self.create_settings_frame()

        # self.select_frame_by_name('Главная')
        # self.button_welcome = ctk.CTkButton(self, text='Start!', font=('Comic Sans MS', 24),
        # hover_color=(random.choice(p.COLORS)[0], random.choice(p.COLORS)[1]),
        # corner_radius=10,
        # command=lambda e: self.select_frame_by_name('Главная')
        # )
        # self.button_welcome.place(relx=0.55, rely=0.8, anchor='center')

    def create_home_frame(self, ):
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Vertical.TScrollbar", background="gray15", bordercolor="gray15", arrowcolor="gray30",
                        troughcolor='gray15', elementborderwidth=3, activebackground='gray15', highlightthickness=0)

        frame = ctk.CTkFrame(self, width=p.WIDTH, height=p.HEIGHT, corner_radius=0, fg_color='transparent', )

        date_time = StringVar()
        # date_time.set('12/12/2015')
        data = ''
        self.entry_data_time = ctk.CTkEntry(frame, textvariable=date_time, width=120, height=30, border_width=2,
                                            state=DISABLED)
        self.entry_data_time.place(relx=0.15, rely=0.03, anchor='ne')

        frame_tags = f_tags(frame, 850, 45)
        frame_tags.frame_tags.place(relx=0.57, rely=0.02, anchor='n')

        self.create_list_tags(frame_tags)

        self.frame_view = ctk.CTkFrame(frame,
                                       fg_color='gray15',
                                       corner_radius=10,
                                       width=1000,
                                       height=550,
                                       border_color='red',
                                       )
        self.frame_view.place(relx=0.5, rely=0.11, anchor='n')
        self.frame_view.pack_propagate(False)
        self.frame_view.grid_propagate(False)

        frame_edit = self.create_frame_edit(frame)

        # scrolling frame
        self.canvas_edit = Canvas(self.frame_view, bg='gray15', bd=0, highlightthickness=0)
        second = ctk.CTkFrame(self.canvas_edit,
                              fg_color='gray15',
                              corner_radius=10)
        scrollbar = ttk.Scrollbar(self.frame_view, orient=VERTICAL, command=self.canvas_edit.yview)
        self.canvas_edit.configure(yscrollcommand=scrollbar.set)
        # !!! заполнение second
        second.update()
        if second.winfo_reqheight() > 624:
            scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas_edit.pack(side=LEFT, fill=BOTH, expand=1)
        self.canvas_edit.create_window((0, 0), window=second, anchor='nw')
        self.canvas_edit.bind(
            '<Configure>', lambda e: self.canvas_note_list.configure(scrollregion=self.canvas_note_list.bbox("all")))

        button_edit_save_note = ctk.CTkButton(frame,
                                              text='',
                                              image=icons.icon_edit,
                                              fg_color='transparent',
                                              width=10,
                                              height=10,
                                              hover_color=("gray70", "gray30"),
                                              command=lambda: self.clicked_edit_save_note(frame_edit,
                                                                                          button_edit_save_note)
                                              )

        # button_create_note.pack()
        button_edit_save_note.place(relx=0.95, rely=0.97, anchor='s')
        return frame

    def create_archive_frame(self, ):
        frame = ctk.CTkFrame(self, width=p.WIDTH, height=p.HEIGHT, corner_radius=0, fg_color='transparent', )
        entry_search = ctk.CTkEntry(frame, placeholder_text='Поиск', width=600, height=30, border_width=2,
                                    font=('', 18))
        # self.entry_search.pack(padx=20, pady=10)
        entry_search.place(relx=0.4, rely=0.02, anchor=tk.N)
        button_search = ctk.CTkButton(frame,
                                      text='',
                                      image=icons.icon_search,
                                      fg_color='transparent',
                                      corner_radius=0,
                                      width=30,
                                      height=30,
                                      border_spacing=10,
                                      hover_color=("gray70", "gray30"),
                                      command=self.clicked_search)
        # button_search.pack(side=tk.BOTTOM)
        button_search.place(relx=0.73, rely=0.01, anchor=tk.N)
        button_sorted = ctk.CTkButton(frame,
                                      text='Недавние',
                                      image=icons.icon_sorted,
                                      fg_color='transparent',
                                      corner_radius=0,
                                      width=30,
                                      height=30,
                                      border_spacing=10,
                                      hover_color=("gray70", "gray30"),
                                      font=('', 18),
                                      command=self.clicked_sorted)
        button_sorted.place(relx=0.83, rely=0.01, anchor=tk.N)

        frame_tags = f_tags(frame, 1000, 45)
        frame_tags.frame_tags.place(relx=0.5, rely=0.13, anchor=tk.CENTER)
        frame_tags.frame_tags.pack_propagate(False)
        frame_tags.frame_tags.grid_propagate(False)

        self.create_list_tags(frame_tags)

        frame_notes = ctk.CTkFrame(frame,
                                   fg_color='gray15',
                                   corner_radius=10,
                                   width=1000,
                                   height=500,
                                   border_color='red',
                                   )

        # frame_notes = Frame(frame, width=1000, height=500, )
        # frame_notes.pack(fill=BOTH, expand=1)
        frame_notes.place(relx=0.5, rely=0.20, anchor='n')
        frame_notes.pack_propagate(False)
        frame_notes.grid_propagate(False)

        # add scroll
        self.canvas_note_list = Canvas(frame_notes, bg='gray15', bd=0, highlightthickness=0)
        second = ctk.CTkFrame(self.canvas_note_list,
                              fg_color='gray15',
                              corner_radius=10,
                              )
        scrollbar = ttk.Scrollbar(frame_notes, orient=VERTICAL, command=self.canvas_note_list.yview)
        self.canvas_note_list.configure(yscrollcommand=scrollbar.set)
        self.create_list_notes(second)
        second.update()
        if second.winfo_reqheight() > 624:
            scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas_note_list.pack(side=LEFT, fill=BOTH, expand=1)
        self.canvas_note_list.create_window((0, 0), window=second, anchor='nw')

        self.canvas_note_list.bind(
            '<Configure>', lambda e: self.canvas_note_list.configure(scrollregion=self.canvas_note_list.bbox("all")))

        button_create_note = ctk.CTkButton(frame,
                                           text='',
                                           image=icons.icon_add_note,
                                           fg_color='transparent',
                                           width=10,
                                           height=10,
                                           hover_color=("gray70", "gray30"),
                                           command=self.clicked_add_note)
        button_create_note.place(relx=0.95, rely=0.98, anchor='s')

        return frame

    # matplotlib.use('TkAgg')

    from matplotlib.figure import Figure as fig
    from matplotlib.backends.backend_tkagg import (
        FigureCanvasTkAgg,
        NavigationToolbar2Tk
    )

    def create_statistics_frame(self):
        frame = ctk.CTkFrame(self, width=p.WIDTH, height=p.HEIGHT, corner_radius=0, fg_color='transparent')
        #
        # # button_update_statistics = ctk.CTkButton(text='Обновить статистику')
        #
        # # figure = Figure(figsize=(3, 2), dpi=50)
        #
        # # create FigureCanvasTkAgg object
        # figure_canvas = FigureCanvasTkAgg(figure, self)
        #
        # # create the toolbar
        # NavigationToolbar2Tk(figure_canvas, self)
        #
        # # create axes
        # axes = figure.add_subplot()
        #
        # data = {
        #     'Python': 11.27,
        #     'C': 11.16,
        #     'Java': 10.46,
        #     'C++': 7.5,
        #     'C#': 5.26
        # }
        # languages = data.keys()
        # popularity = data.values()
        #
        # # create the barchart
        # axes.bar(languages, popularity)
        # axes.set_title('Top 5 Programming Languages')
        # axes.set_ylabel('Popularity')
        #
        # figure_canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor='center')
        return frame

    def create_settings_frame(self):
        return ctk.CTkFrame(self, width=p.WIDTH, height=p.HEIGHT, corner_radius=0, fg_color='transparent')

    def create_list_tags(self, frame):
        tags = ['#idea', '#food', '#school', ]
        index = 0
        for tag in tags:
            # color = random.choice(p.COLORS)
            tag_button = ctk.CTkButton(frame,
                                       text=tag,
                                       # fg_color=color[0],
                                       # hover_color=(color[0], color[1]),
                                       corner_radius=30,
                                       width=20,
                                       height=20,
                                       border_width=0,
                                       )
            tag_button.grid(row=0, column=index, padx=10, pady=10)
            index += 1

    def create_list_notes(self, frame):
        notes = [0] * 10
        row = 0
        column = 0

        notes = [
            # ['19.12.2022', '2/5', 'Отличный день, чтобы \nкупить подарки:\n1. Плюшевый медведь\n\t...'],
            ['20.12.2022', '3/7', 'Лабораторные работы:\n☑. ЛР 1\n☑. ЛР 2\n\t...'],
            # ['21.12.2022', '2/6', '☑ Уборка\n☑ Магазин\n\t...'],
            # ['28.12.2022', '2/3', 'Сегодня прекрасная погода!\n1. Молоко\n2. Сыр\n3. Колбаса\n\t...'],
        ]

        for i in range(1):
            if column == 4:
                column = 0
                row += 1
            self.create_note(frame, notes[i][0], notes[i][1], notes[i][2], row, column)
            column += 1

    def create_note(self, frame, date, check_tasks, data_preview, row, column):
        color = random.choice(p.COLORS)
        font = ('', 18, tk.font.BOLD)
        width = 200
        height = 200
        # date = '16.12.2023'
        # check_tasks = '1/10'
        # data_preview = 'today \nim so tired 123456' + ' . . . '
        text_format = '\n' + date + '\t' + check_tasks + '\n\n' + data_preview
        label = ctk.CTkLabel(frame,
                             text=text_format,
                             font=font,
                             text_color=p.DARK_TEXT_COLOR,
                             justify='left',
                             fg_color=color[0],
                             width=width,
                             height=height,
                             anchor='n',
                             corner_radius=10,
                             )
        label.bind('<Button-1>', lambda e: self.open_note(date))
        label.bind('<Enter>', partial(self.config_widget, label, color[0]))
        label.bind('<Leave>', partial(self.config_widget, label, color[1]))
        # label.place(relx=0.5, rely=0.5, anchor=tk.N)
        label.grid(row=row, column=column, padx=10, pady=10)

    def create_frame_edit(self, frame):
        width = 20
        height = 20
        radius = 10
        print('create in main!!!')
        frame_edit = ctk.CTkFrame(frame,
                                  fg_color="gray20",
                                  corner_radius=10,
                                  width=955,
                                  height=50,
                                  )
        # frame.grid_propagate(False)
        frame_edit.grid_propagate(False)
        button_text_add = ctk.CTkButton(frame_edit,
                                        text='',
                                        image=icons.icon_add_text,
                                        fg_color='transparent',
                                        width=width,
                                        height=height,
                                        corner_radius=radius,
                                        hover_color=("gray70", "gray30"),
                                        command=self.clicked_add_text_elem(frame)
                                        )
        button_num_list = ctk.CTkButton(frame_edit,
                                        text='',
                                        image=icons.icon_add_num_list,
                                        fg_color='transparent',
                                        width=width,
                                        height=height,
                                        corner_radius=radius,
                                        hover_color=("gray70", "gray30"),
                                        # command=self.clicked_add_num_list
                                        )
        button_mark_list_add = ctk.CTkButton(frame_edit,
                                             text='',
                                             image=icons.icon_add_mark_list,
                                             fg_color='transparent',
                                             width=width,
                                             height=height,
                                             corner_radius=radius,
                                             hover_color=("gray70", "gray30"),
                                             # command=self.clicked_mark_list_add
                                             )
        button_check_list_add = ctk.CTkButton(frame_edit,
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
        return frame_edit

    def config_widget(self, widget, color, event):
        widget.configure(fg_color=color)

    def select_frame_by_name(self, name):
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "Главная" else "transparent")
        self.archive_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.statistics_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.settings_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "Главная":
            self.home_frame.pack(fill=tk.X, side=tk.RIGHT)
        else:
            self.home_frame.pack_forget()
        if name == "Архив":
            self.archive_frame.pack(fill=tk.X, side=tk.RIGHT)
        else:
            self.archive_frame.pack_forget()
        if name == "Статистика":
            self.statistics_frame.pack(fill=tk.X, side=tk.RIGHT)
        else:
            self.statistics_frame.pack_forget()
        if name == "Настройки":
            self.settings_frame.pack(fill=tk.X, side=tk.RIGHT)
        else:
            self.settings_frame.pack_forget()

    def delete_frame(self, frame):
        print('delete')
        frame.place_forget()

    def clicked_home_button(self):
        self.select_frame_by_name('Главная')

    def clicked_archive_button(self):
        self.select_frame_by_name('Архив')

    def clicked_statistics_button(self):
        self.select_frame_by_name('Статистика')

    def clicked_settings_button(self):
        self.select_frame_by_name('Настройки')

    def open_note(self, date):
        print('OPEEEEEENNN')

    def clicked_add_text_elem(self, frame):
        pass

    def clicked_save_note(self, frame_edit, button_edit_save_note):
        self.check = True
        button_edit_save_note.configure(image=icons.icon_edit)
        self.delete_frame(frame_edit)

    def clicked_edit_note(self, frame_edit, button_edit_save_note):
        self.check = False
        button_edit_save_note.configure(image=icons.icon_save)
        frame_edit.place(relx=0.479, rely=0.98, anchor='s')

    def clicked_edit_save_note(self, frame_edit, button_edit_save_note):
        if self.check:
            self.clicked_edit_note(frame_edit, button_edit_save_note)
        else:
            self.clicked_save_note(frame_edit, button_edit_save_note)

    def clicked_add_note(self):
        pass

    def clicked_search(self):
        pass

    def clicked_sorted(self):
        pass
