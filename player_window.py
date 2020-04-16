import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os
from tkinter import Scrollbar


class PlayerWindow(tk.Frame):
    """ Layout for the Player Window """

    def __init__(self, parent, controller, list_box_callback):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        # 1: create any instances of other support classes that are needed

        # Window attributes
        parent.title('Player')

        # Menus
        main_menu = tk.Menu(master=parent)
        parent.config(menu=main_menu)
        file_menu = tk.Menu(main_menu)
        main_menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Open File', command="")
        file_menu.add_command(label='Open Folder', command="")
        file_menu.add_command(label='Quit', command=controller.quit_callback)

        # Defining frames
        top_frame = tk.Frame(master=parent)
        top_frame.grid(row=0, padx=30, pady=10)
        mid_frame = tk.Frame(master=parent)
        mid_frame.grid(row=1, padx=30, pady=10)
        bot_frame = tk.Frame(master=parent)
        bot_frame.grid(row=2, padx=30, pady=10)
        right_frame = tk.Frame(master=parent)
        right_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10)
        bot_right_frame = tk.Frame(master=parent)
        bot_right_frame.grid(row=2, column=1, padx=10, pady=10)

        # Labels
        tk.Label(top_frame, text='File:').grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self._file_value = tk.Label(top_frame, text='Test')
        self._file_value.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(mid_frame, text='State:').grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self._file_value = tk.Label(mid_frame, text='Not Playing')
        self._file_value.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        # Listbox
        self.list_box = tk.Listbox(right_frame, width=20, height=10)
        self.list_box.grid(row=0, column=0)
        # Might want to call listbox here

        # Scrollbar
        scrollbar = Scrollbar(right_frame, orient="vertical", width=20)
        scrollbar.config(command=self.list_box.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")

        self.list_box.config(yscrollcommand=scrollbar.set)

        # Main buttons
        tk.Button(bot_frame, text='Play', width=10, command="") \
            .grid(row=0, column=0, sticky=tk.E, padx=10, pady=5)

        tk.Button(bot_frame, text='Pause', width=10, command="") \
            .grid(row=0, column=1, sticky=tk.E, padx=10, pady=5)

        tk.Button(bot_frame, text='Stop', width=10, command="") \
            .grid(row=0, column=2, sticky=tk.E, padx=10, pady=5)

        tk.Button(bot_frame, text='Resume', width=10, command="") \
            .grid(row=0, column=3, sticky=tk.E, padx=10, pady=5)

        # Buttons under listbox
        tk.Button(bot_right_frame, text='Add', width=10, command="") \
            .grid(row=2, column=1, sticky=tk.E, padx=20, pady=5)

        tk.Button(bot_right_frame, text='Delete', width=10, command="") \
            .grid(row=3, column=1, sticky=tk.E, padx=20, pady=5)

        # Initial controller calls

    def set_titles(self, titles):
        """ Update the listbox to display all names """
        self.list_box.delete(0, tk.END)
        for title in titles:
            self.list_box.insert(tk.END, title)

    def __repr__(self):
        """ Replacement repr function """
        return {
        'listbox': self.list_box
        }