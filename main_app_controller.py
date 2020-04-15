import csv
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os
import requests
from player_window import PlayerWindow


class MainAppController(tk.Frame):
    """ Main Application Window """

    def __init__(self, parent):
        """ Create the views """
        tk.Frame.__init__(self, parent)
        self._root_win = tk.Toplevel()
        self._player = PlayerWindow(self._root_win, self)

    def play_callback(self):
        """ Play audio file. """
        pass

    def pause_callback(self):
        """ Pauses playing audio. """
        pass

    def stop_callback(self):
        """ Stops playing audio. """
        pass

    def resume_callback(self):
        """ Resumes playing stopped audio. """
        pass

    def openfile(self):
        pass
    
    def quit_callback(self):
        """ Exit the application. """
        self.master.quit()

    def clear_callback(self):
        pass
    
    def add_callback(self, event):
        pass

    def delete_callback(self):
        pass


if __name__ == "__main__":
    """ Create Tk window manager and a main window. Start the main loop """
    root = tk.Tk()
    MainAppController(root).pack()
    tk.mainloop()
