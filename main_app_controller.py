import csv
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os
import requests
from player_window import PlayerWindow
from add_window import AddWindow


class MainAppController(tk.Frame):
    """ Main Application Window """

    def __init__(self, parent):
        """ Create the views """
        tk.Frame.__init__(self, parent)
        self._root_win = tk.Toplevel()
        self._player = PlayerWindow(self._root_win, self, self.listbox_callback)
        self.listbox_callback()

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

    def listbox_callback(self):
        """ List titles in listbox. """
        response = requests.get("http://localhost:5000/song/names")
        title_list = [f'{s["title"]}' for s in response.json()]
        self._player.set_titles(title_list)  # <--- Error happens here

    def openfile(self):
        pass
    
    def quit_callback(self):
        """ Exit the application. """
        self.master.quit()

    def clear_callback(self):
        pass
    
    def add_callback(self, event):
        """ Add audio file. """
        form_data = self._add.get_form_data()

        data = {'title': form_data.get('title'),
                'artist': form_data.get('artist'),
                'album': form_data.get('album'),
                'runtime': form_data.get('runtime'),
                'file_location': form_data.get('file_location'),
                'genre': form_data.get('genre')}

        response = requests.post("http://localhost:5000/song", json=data)
        if response.status_code == 200:
            msg_str = f"{form_data.get('title')} added to the database"
            messagebox.showinfo(title='Add Song', message=msg_str)

    def delete_callback(self):
        """ Deletes selected song. """
        selected_title = self._player.get_selection()
        response = requests.get("http://localhost:5000/song/names")
        for title in response.json():
            if title["title"] == selected_title:
                response = requests.delete("http://localhost:5000/song/names" + title["title"])
        if response.status_code == 200:
            msg_str = f'{selected_title} has been deleted'
            messagebox.showinfo(title='Delete Song', message=msg_str)

    def add_popup(self):
        """ Show add popup window """
        self._add_win = tk.Toplevel()
        self._add = AddWindow(self._add_win, self.add_callback, self._close_add_popup)

    def _close_add_popup(self, event):
        """ Close Add Popup """
        self._add_win.destroy()


if __name__ == "__main__":
    """ Create Tk window manager and a main window. Start the main loop """
    root = tk.Tk()
    MainAppController(root).pack()
    tk.mainloop()
