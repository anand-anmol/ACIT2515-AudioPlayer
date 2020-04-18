import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os
from tkinter import Scrollbar


class PlayerWindow(tk.Frame):
    """ Layout for the Player Window """

    def __init__(self, parent, controller):
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
        file_menu.add_command(label='Load from file', command=controller.add_from_file_callback)
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
        tk.Label(top_frame, text='Song:').grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.title_value = tk.Label(top_frame, text='None')
        self.title_value.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(mid_frame, text='State:').grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.state_value = tk.Label(mid_frame, text='Not Playing')
        self.state_value.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

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
        tk.Button(bot_frame, text='Play ▶', width=10, command=controller.play_callback) \
            .grid(row=0, column=0, sticky=tk.E, padx=10, pady=5)

        tk.Button(bot_frame, text='Stop ⏹', width=10, command=controller.stop_callback) \
            .grid(row=0, column=2, sticky=tk.E, padx=10, pady=5)

        tk.Button(bot_frame, text='Pause/Resume ⏯', width=15, command=controller.pause_resume_callback) \
            .grid(row=0, column=1, sticky=tk.E, padx=10, pady=5)

        # Buttons under listbox
        tk.Button(bot_right_frame, text='Add Manually', width=10, command=controller.add_manually_popup) \
            .grid(row=2, column=1, sticky=tk.E, padx=10, pady=5)

        tk.Button(bot_right_frame, text='Add via URL', width=10, command=controller.add_via_url_popup) \
            .grid(row=2, column=2, sticky=tk.E, padx=10, pady=5)

        tk.Button(bot_right_frame, text='Delete', width=10, command=controller.delete_callback) \
            .grid(row=3, column=1, sticky=tk.N, padx=10, pady=5)

        tk.Button(bot_right_frame, text='Edit Song', width=10, command=controller.update_popup) \
            .grid(row=3, column=2, sticky=tk.N, padx=10, pady=5)

        tk.Button(bot_right_frame, text='View Queue', width=10, command=controller.queue_popup) \
            .grid(row=4, column=1, sticky=tk.N, padx=10, pady=5)

        tk.Button(bot_right_frame, text='Add to Queue', width=10, command=controller.add_to_queue_callback) \
            .grid(row=4, column=2, sticky=tk.N, padx=10, pady=5)

    def set_titles(self, titles):
        """ Update the listbox to display all names """
        self.list_box.delete(0, tk.END)
        for title in titles:
            self.list_box.insert(tk.END, title)

    def get_form_data(self):
        """ returns selected song from the listbox """
        return {"title": self.list_box.get('anchor'), "index": self.list_box.index('anchor')}
