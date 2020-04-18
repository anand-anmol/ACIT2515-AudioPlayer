import csv
import tkinter as tk
from math import floor
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os
import requests
from player_window import PlayerWindow
from add_manually_window import AddManuallyWindow
import vlc
import eyed3
from add_via_url_window import AddViaUrlWindow


class MainAppController(tk.Frame):
    """ Main Application Window """

    def __init__(self, parent):
        """ Create the views """
        tk.Frame.__init__(self, parent)
        self._root_win = tk.Toplevel()
        self._player_window = PlayerWindow(self._root_win, self)
        self.listbox_callback()
        self._vlc_instance = vlc.Instance()
        self._player = self._vlc_instance.media_player_new()

    def play_callback(self):
        """ Play audio file. """

        song_name_dict = self._player_window.get_form_data()

        response = requests.get("http://localhost:5000/song/name/{}".format(song_name_dict['title']))

        media_file = response.json()['file_location']

        media = self._vlc_instance.media_new_path(media_file)
        self._player.set_media(media)
        self._player.play()
        self._player_window.state_value['text'] = "Playing"
        self._player_window.title_value['text'] = response.json()['title']

        play_response = requests.post("http://localhost:5000/play_song/{}".format(song_name_dict['index']))

    def pause_resume_callback(self):
        """ Pauses playing audio. """
        if self._player.get_state() == vlc.State.Playing:
            self._player.pause()
            self._player_window.state_value['text'] = "Paused"

        elif self._player.get_state() == vlc.State.Paused:
            self._player.pause()
            self._player_window.state_value['text'] = "Playing"

    def stop_callback(self):
        """ Stops playing audio. """
        self._player.stop()
        self._player_window.state_value['text'] = "Not Playing"

    def listbox_callback(self):
        """ List titles in listbox. """
        response = requests.get("http://localhost:5000/song/names")
        self.song_list = response.json()
        title_list = [f'{s["title"]}' for s in response.json()]
        self._player_window.set_titles(title_list)

    def add_from_file_callback(self):
        """ Loads file from local machine. """
        selected_file = askopenfilename(initialdir='.', defaultextension='.mp3')
        if not selected_file:
            return
        adjusted_path = selected_file.replace("/", os.sep)

        audio = eyed3.load(adjusted_path)

        title = audio.tag.title
        artist = audio.tag.artist
        album = audio.tag.album
        genre = audio.tag.genre._name

        runtime_secs = audio.info.time_secs
        runtime_mins = int(runtime_secs // 60)

        runtime = str(runtime_mins) + ':' + str(floor(runtime_secs) - (runtime_mins * 60))

        data = {'title': title,
                'artist': artist,
                'album': album,
                'runtime': runtime,
                'file_location': adjusted_path,
                'genre': genre}

        response = requests.post("http://localhost:5000/song", json=data)

        if response.status_code == 200:
            msg_str = f"Song added to the database."
            messagebox.showinfo(title='Add Song', message=msg_str)
            self.listbox_callback()
        else:
            messagebox.showerror(title='Error', message='Something went wrong, song not added.')

    def quit_callback(self):
        """ Exit the application. """
        self.master.quit()

    def clear_callback(self):
        pass

    def add_manually_callback(self, event):
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
            self._close_popup(event)
            self.listbox_callback()
        else:
            messagebox.showerror(title='Error', message='Something went wrong, song not added.')

    def delete_callback(self):
        """ Deletes selected song. """
        song_index_dict = self._player_window.get_form_data()

        response = requests.delete(f"http://localhost:5000/song/{song_index_dict['index']}")

        if response.status_code == 200:
            messagebox.showinfo(title='Delete Song', message='Song deleted.')
            self.listbox_callback()
        else:
            messagebox.showerror(title='Error', message='Something went wrong, song not deleted.')

    def add_manually_popup(self):
        """ Show add popup window """
        self._add_win = tk.Toplevel()
        self._add = AddManuallyWindow(self._add_win, self.add_manually_callback, self._close_popup)

    def add_via_url_popup(self):
        """ Show add via url popup window """
        self._add_via_url_win = tk.Toplevel()
        self._add_via_url = AddViaUrlWindow()

    def _close_popup(self, event):
        """ Close Add Popup """
        self._add_win.destroy()


if __name__ == "__main__":
    """ Create Tk window manager and a main window. Start the main loop """
    root = tk.Tk()
    MainAppController(root).pack()
    tk.mainloop()
