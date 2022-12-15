import tkinter as tk
from tkinter import *
import customtkinter
import customtkinter as ctk
from PIL import Image, ImageTk

HEIGHT = 700
WIDTH = 1200

COLORS = ['', '', '']

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class MainWindow(ctk.CTk):
    def __init__(self, ):
        super().__init__()

        # icons
        icon_home = ctk.CTkImage(Image.open('icons/home.png'), size=(20, 20))
        icon_archive = ctk.CTkImage(Image.open('icons/archive.png'), size=(20, 20))
        icon_statistics = ctk.CTkImage(Image.open('icons/statistics.png'), size=(20, 20))
        icon_settings = ctk.CTkImage(Image.open('icons/settings.png'), size=(20, 20))

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
                                         image=icon_home,
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
                                            image=icon_archive,
                                            fg_color='transparent',
                                            corner_radius=0,
                                            anchor="w",
                                            border_spacing=10,
                                            hover_color=("gray70", "gray30"),
                                            command=self.clicked_archive_button)
        self.archive_button.pack(fill=tk.X, side=tk.TOP)
        self.statistics_button = ctk.CTkButton(self.left_panel_frame,
                                               text='Statistics',
                                               image=icon_statistics,
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
                                             image=icon_settings,
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

        self.select_frame_by_name('home')

    def create_home_frame(self, ):
        frame = ctk.CTkFrame(self, width=WIDTH, height=HEIGHT, corner_radius=0, fg_color='transparent', )

        return frame

    def create_archive_frame(self, ):
        icon_search = ctk.CTkImage(Image.open('icons/search.png'), size=(20, 20))
        icon_sorted = ctk.CTkImage(Image.open('icons/sorted.png'), size=(20, 20))

        frame = ctk.CTkFrame(self, width=WIDTH, height=HEIGHT, corner_radius=0, fg_color='transparent', )
        entry = ctk.CTkEntry(frame, placeholder_text='Поиск', width=600, height=30, border_width=2)
        # entry.pack(padx=20, pady=10)
        entry.place(relx=0.5, rely=0.02, anchor=tk.N)
        button_search = ctk.CTkButton(frame,
                                      text='',
                                      image=icon_search,
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
                                      image=icon_sorted,
                                      fg_color='transparent',
                                      corner_radius=0,
                                      # anchor="N",
                                      width=30,
                                      height=30,
                                      border_spacing=10,
                                      hover_color=("gray70", "gray30"),
                                      command=self.clicked_sorted)
        button_sorted.place(relx=0.88, rely=0.01, anchor=tk.N)
        self.create_note(frame)
        return frame

    def create_statistics_frame(self):
        return ctk.CTkFrame(self, width=WIDTH, height=HEIGHT, corner_radius=0, fg_color='green')

    def create_settings_frame(self):
        return ctk.CTkFrame(self, width=WIDTH, height=HEIGHT, corner_radius=0, fg_color='blue')

    def create_list_tags(self):
        pass

    def create_list_notes(self):
        pass

    def create_note(self, frame):
        light_color = ''
        dark_color = ''
        note = ctk.CTkButton(frame, fg_color=('#abbbbb', '#ababba'))
        note.place(relx=0.5, rely=0.5)

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

    def clicked_home_button(self):
        self.select_frame_by_name('home')

    def clicked_archive_button(self):
        self.select_frame_by_name('archive')

    def clicked_statistics_button(self):
        self.select_frame_by_name('statistics')

    def clicked_settings_button(self):
        self.select_frame_by_name('settings')

    def clicked_search(self):
        pass

    def clicked_sorted(self):
        pass
