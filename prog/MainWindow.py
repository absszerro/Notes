import tkinter as tk
import random
from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
from functools import partial

HEIGHT = 700
WIDTH = 1200

COLORS = [('#ED8C8A', '#FF9494'),
          ('#EDE0A4', '#FFF2B0'),
          ('#DA95EB', '#ECA1FF'),
          ('#7CEBA1', '#87FFA9'),
          ('#8988EB', '#9A94FF')]

DARK_TEXT_COLOR = '#272138'

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class MainWindow(ctk.CTk):
    def __init__(self, ):
        super().__init__()

        # icons
        self.icon_home = ctk.CTkImage(Image.open('icons/home.png'), size=(20, 20))
        self.icon_archive = ctk.CTkImage(Image.open('icons/archive.png'), size=(20, 20))
        self.icon_statistics = ctk.CTkImage(Image.open('icons/statistics.png'), size=(20, 20))
        self.icon_settings = ctk.CTkImage(Image.open('icons/settings.png'), size=(20, 20))
        self.icon_save = ctk.CTkImage(Image.open('icons/save.png'), size=(30, 30))
        self.icon_edit = ctk.CTkImage(Image.open('icons/edit.png'), size=(30, 30))
        self.icon_search = ctk.CTkImage(Image.open('icons/search.png'), size=(20, 20))
        self.icon_sorted = ctk.CTkImage(Image.open('icons/sorted.png'), size=(20, 20))
        self.icon_add_note = ctk.CTkImage(Image.open('icons/add2.png'), size=(30, 30))

        self.check = True

        # create a window
        self.title('Planner')
        self.resizable(False, False)
        self.geometry(f"{WIDTH}x{HEIGHT}")
        # self.home_frame = None

        # left panel frame
        self.left_panel_frame = ctk.CTkFrame(self, width=WIDTH // 100 * 5, height=HEIGHT)
        self.left_panel_frame.pack(fill=tk.Y, side=tk.LEFT)
        self.home_button = ctk.CTkButton(self.left_panel_frame,
                                         text='Home',
                                         image=self.icon_home,
                                         fg_color='transparent',
                                         corner_radius=0,
                                         hover_color=("gray70", "gray30"),
                                         anchor="w",
                                         border_spacing=10,
                                         # compound='LEFT',
                                         command=self.clicked_home_button)
        self.home_button.pack(fill=tk.X, side=tk.TOP)
        self.archive_button = ctk.CTkButton(self.left_panel_frame,
                                            text='Archive',
                                            image=self.icon_archive,
                                            fg_color='transparent',
                                            corner_radius=0,
                                            anchor="w",
                                            border_spacing=10,
                                            hover_color=("gray70", "gray30"),
                                            command=self.clicked_archive_button)
        self.archive_button.pack(fill=tk.X, side=tk.TOP)
        self.statistics_button = ctk.CTkButton(self.left_panel_frame,
                                               text='Statistics',
                                               image=self.icon_statistics,
                                               fg_color='transparent',
                                               corner_radius=0,
                                               anchor="w",
                                               border_spacing=10,
                                               hover_color=("gray70", "gray30"),
                                               command=self.clicked_statistics_button)
        self.statistics_button.pack(fill=tk.X, side=tk.TOP)
        # self.events_button = ctk.CTkButton(self.left_panel_frame, text='events')
        # self.events_button.pack(fill=tk.X, side=tk.TOP)
        self.settings_button = ctk.CTkButton(self.left_panel_frame,
                                             text='Settings',
                                             image=self.icon_settings,
                                             fg_color='transparent',
                                             corner_radius=0,
                                             anchor="w",
                                             border_spacing=10,
                                             hover_color=("gray70", "gray30"),
                                             command=self.clicked_settings_button)
        self.settings_button.pack(fill=tk.X, side=tk.BOTTOM)

        # today frame
        self.home_frame = self.create_home_frame()

        # archive frame
        self.archive_frame = self.create_archive_frame()

        # statistics frame
        self.statistics_frame = self.create_statistics_frame()

        # settings frame
        self.settings_frame = self.create_settings_frame()

        # self.select_frame_by_name('home')

    def create_home_frame(self, ):

        frame = ctk.CTkFrame(self, width=WIDTH, height=HEIGHT, corner_radius=0, fg_color='transparent', )
        # frame.pack_configure(False)
        # frame.pack_propagate(False)
        # frame.grid_propagate(False)

        date_time = '12/12/2015'
        data = ''
        entry = ctk.CTkEntry(frame, placeholder_text=date_time, width=120, height=30, border_width=2, state=DISABLED)
        entry.place(relx=0.15, rely=0.03, anchor='ne')

        frame_tags = ctk.CTkFrame(frame,
                                  fg_color='gray15',
                                  corner_radius=10,
                                  width=850,
                                  height=45,
                                  border_color='red',
                                  )

        frame_tags.place(relx=0.57, rely=0.02, anchor='n')
        frame_tags.pack_propagate(False)
        frame_tags.grid_propagate(False)

        self.create_list_tags(frame_tags)

        frame_view = ctk.CTkFrame(frame,
                                  fg_color='gray15',
                                  corner_radius=10,
                                  width=1000,
                                  height=550,
                                  border_color='red',
                                  )
        frame_view.place(relx=0.5, rely=0.11, anchor='n')
        frame_view.pack_propagate(False)
        frame_view.grid_propagate(False)

        frame_edit = self.create_frame_edit(frame)

        button_edit_save_note = ctk.CTkButton(frame,
                                              text='',
                                              image=self.icon_edit,
                                              fg_color='transparent',
                                              # anchor="N",
                                              width=10,
                                              height=10,
                                              # border_spacing=10,
                                              # corner_radius=100,
                                              hover_color=("gray70", "gray30"),
                                              command=lambda: self.clicked_edit_save_note(frame_edit,
                                                                                          button_edit_save_note)
                                              )

        # button_create_note.pack()
        button_edit_save_note.place(relx=0.95, rely=0.97, anchor='s')
        return frame

    def create_archive_frame(self, ):
        frame = ctk.CTkFrame(self, width=WIDTH, height=HEIGHT, corner_radius=0, fg_color='transparent', )
        entry = ctk.CTkEntry(frame, placeholder_text='Поиск', width=600, height=30, border_width=2)
        # entry.pack(padx=20, pady=10)
        entry.place(relx=0.5, rely=0.02, anchor=tk.N)
        button_search = ctk.CTkButton(frame,
                                      text='',
                                      image=self.icon_search,
                                      fg_color='transparent',
                                      corner_radius=0,
                                      # anchor="N",
                                      width=30,
                                      height=30,
                                      border_spacing=10,
                                      hover_color=("gray70", "gray30"),
                                      command=self.clicked_search)
        # button_search.pack(side=tk.BOTTOM)
        button_search.place(relx=0.81, rely=0.01, anchor=tk.N)
        button_sorted = ctk.CTkButton(frame,
                                      text='Недавние',
                                      image=self.icon_sorted,
                                      fg_color='transparent',
                                      corner_radius=0,
                                      # anchor="N",
                                      width=30,
                                      height=30,
                                      border_spacing=10,
                                      hover_color=("gray70", "gray30"),
                                      command=self.clicked_sorted)
        button_sorted.place(relx=0.88, rely=0.01, anchor=tk.N)

        frame_tags = ctk.CTkFrame(frame,
                                  fg_color='gray15',
                                  corner_radius=10,
                                  width=1000,
                                  height=45,
                                  border_color='red',
                                  )

        frame_tags.place(relx=0.5, rely=0.13, anchor=tk.CENTER)
        frame_tags.pack_propagate(False)
        frame_tags.grid_propagate(False)

        self.create_list_tags(frame_tags)

        # frame_notes = tk.Frame(frame,
        #                        background='gray15',
        #                        # corner_radius=10,
        #                        width=1000,
        #                        height=500, )

        frame_notes = ctk.CTkFrame(frame,
                                   fg_color='gray15',
                                   corner_radius=10,
                                   width=1000,
                                   height=500,
                                   border_color='red',
                                   )
        frame_notes.place(relx=0.5, rely=0.20, anchor='n')
        frame_notes.pack_propagate(False)
        frame_notes.grid_propagate(False)

        # scroll = ctk.CTkScrollbar(frame_notes, orientation='vertical', command=frame_notes.yview)
        # scroll.grid(row=0, column=5, sticky='NS')
        # scroll.pack(side='right', fill=tk.Y)
        # frame_notes['yscrollcommand'] = scroll.set

        self.create_list_notes(frame_notes)

        # frame_notes.configure(yscrollcommand=scroll.set)

        button_create_note = ctk.CTkButton(frame,
                                           text='',
                                           image=self.icon_add_note,
                                           fg_color='transparent',
                                           # anchor="N",
                                           width=10,
                                           height=10,
                                           # border_spacing=10,
                                           # corner_radius=100,
                                           hover_color=("gray70", "gray30"),
                                           command=self.clicked_add_note)
        # button_create_note.pack()
        button_create_note.place(relx=0.95, rely=0.98, anchor='s')

        return frame

    def create_statistics_frame(self):
        return ctk.CTkFrame(self, width=WIDTH, height=HEIGHT, corner_radius=0, fg_color='green')

    def create_settings_frame(self):
        return ctk.CTkFrame(self, width=WIDTH, height=HEIGHT, corner_radius=0, fg_color='blue')

    def create_list_tags(self, frame):
        tags = ['#idea', '#food', '#school', ]
        index = 0
        for tag in tags:
            # color = random.choice(COLORS)
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
        notes = [0] * 5
        row = 0
        column = 0
        for i in range(len(notes)):
            if column == 4:
                column = 0
                row += 1
            self.create_note(frame, '12.12.12', '1/10', 'jffkefweflefj', row, column)
            column += 1

    def create_note(self, frame, date, check_tasks, data_preview, row, column):
        color = random.choice(COLORS)
        font = ('', 14, tk.font.BOLD)
        width = 200
        height = 200
        # date = '16.12.2023'
        # check_tasks = '1/10'
        # data_preview = 'today \nim so tired 123456' + ' . . . '
        text_format = '\n' + date + '\t' + check_tasks + '\n\n' + data_preview
        label = ctk.CTkLabel(frame,
                             text=text_format,
                             font=font,
                             text_color=DARK_TEXT_COLOR,
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
        label.grid(row=row, column=column, padx=25, pady=25)

    def create_frame_edit(self, frame):
        frame_edit = ctk.CTkFrame(frame,
                                  fg_color="gray20",
                                  corner_radius=10,
                                  width=955,
                                  height=50,
                                  )
        return frame_edit

    def config_widget(self, widget, color, event):
        widget.configure(fg_color=color)

    def select_frame_by_name(self, name):
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.archive_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.statistics_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.settings_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.pack(fill=tk.X, side=tk.RIGHT)
        else:
            self.home_frame.pack_forget()
        if name == "archive":
            self.archive_frame.pack(fill=tk.X, side=tk.RIGHT)
        else:
            self.archive_frame.pack_forget()
        if name == "statistics":
            self.statistics_frame.pack(fill=tk.X, side=tk.RIGHT)
        else:
            self.statistics_frame.pack_forget()
        if name == "settings":
            self.settings_frame.pack(fill=tk.X, side=tk.RIGHT)
        else:
            self.settings_frame.pack_forget()

    def delete_frame(self, frame):
        print('delete')
        frame.place_forget()

    def clicked_home_button(self):
        self.select_frame_by_name('home')

    def clicked_archive_button(self):
        self.select_frame_by_name('archive')

    def clicked_statistics_button(self):
        self.select_frame_by_name('statistics')

    def clicked_settings_button(self):
        self.select_frame_by_name('settings')

    def open_note(self, date):
        print('OPEEEEEENNN')

    def clicked_save_note(self, frame_edit, button_edit_save_note):
        self.check = True
        button_edit_save_note.configure(image=self.icon_edit)
        self.delete_frame(frame_edit)

    def clicked_edit_note(self, frame_edit, button_edit_save_note):
        self.check = False
        button_edit_save_note.configure(image=self.icon_save)
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
