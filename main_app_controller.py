from time import sleep
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
from update_window import UpdateWindow
from queue_window import QueueWindow


class MainAppController(tk.Frame):
    """ Main Application Window

    Authors:
    Anmol Anand(A01174846),
    Nicholas Janus(A01179897)
    """

    def __init__(self, parent):
        """ Create the views """
        tk.Frame.__init__(self, parent)
        self._root_win = tk.Toplevel()
        self._player_window = PlayerWindow(self._root_win, self)
        self.listbox_callback()
        self._vlc_instance = vlc.Instance()
        self._player = self._vlc_instance.media_player_new()
        self.queue_pos = -1
        self._queue_list = []

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
        selected_file = askopenfilename(initialdir='.', filetypes=(("MP3 File", "*.mp3"),))  # Weird tkinter syntax
        if not selected_file:
            return
        adjusted_path = selected_file.replace("/", os.sep)

        data = MainAppController.__load_file(adjusted_path)

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

    @classmethod
    def __load_file(cls, selected_file):
        """ loads the mp3 file data using eyed3 tags. """
        audio = eyed3.load(selected_file)

        title = cls.get_tag(audio, "title")
        artist = cls.get_tag(audio, "artist")
        album = cls.get_tag(audio, "album")
        genre = cls.get_tag(audio, "genre._name")

        runtime_secs = audio.info.time_secs
        runtime_mins = int(runtime_secs // 60)

        runtime = str(runtime_mins) + ':' + str(floor(runtime_secs) - (runtime_mins * 60))

        data = {'title': title,
                'artist': artist,
                'album': album,
                'runtime': runtime,
                'file_location': selected_file,
                'genre': genre}
        return data

    @staticmethod
    def get_tag(file, tag):
        """ Static method to get eyed3 tags for mp3 files. """
        try:
            return str(getattr(file.tag, tag))
        except AttributeError:
            return "None"

    def add_manually_callback(self, event):
        """ Add audio file manually. """
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
            self._close_add_manually_popup(event)
            self.listbox_callback()
        else:
            messagebox.showerror(title='Error', message='Something went wrong, song not added.')

    def add_via_url_callback(self, event):
        """ Add audio file via URL """
        url = self._add_via_url.get_form_data()['URL']

        r = requests.get(url)

        if not os.path.exists('mp3'):
            os.makedirs('mp3')

        file_path = os.path.join('mp3', 'remote_audio.mp3').replace("/", os.sep)

        with open(file_path, "wb") as f:
            f.write(r.content)

        data = MainAppController.__load_file(file_path)

        new_file_path = os.path.join('mp3', f"{data['title']}.mp3")

        if not os.path.exists(new_file_path):
            os.rename(file_path, new_file_path)
        else:
            messagebox.showinfo(title='Add Song', message=f"{data['title']} already exists. Adding from "
                                                          f"local machine.")

        data['file_location'] = new_file_path

        response = requests.post("http://localhost:5000/song", json=data)
        if response.status_code == 200:
            msg_str = f"{data['title']} added to the database"
            messagebox.showinfo(title='Add Song', message=msg_str)
            self._close_add_via_url_popup(event)
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
        self._add = AddManuallyWindow(self._add_win, self.add_manually_callback, self._close_add_manually_popup)

    def add_via_url_popup(self):
        """ Show add via url popup window """
        self._add_via_url_win = tk.Toplevel()
        self._add_via_url = AddViaUrlWindow(self._add_via_url_win, self.add_via_url_callback,
                                            self._close_add_via_url_popup)

    def _close_add_manually_popup(self, event):
        """ Close Add Popup """
        self._add_win.destroy()

    def _close_add_via_url_popup(self, event):
        """ Close Add Popup """
        self._add_via_url_win.destroy()

    def update_popup(self):
        """ Show update popup window """
        song_data = self._player_window.get_form_data()
        song_index = song_data.get("index")

        self._update_win = tk.Toplevel()
        self._update = UpdateWindow(self._update_win, self.update_song_callback, self._close_update_popup,
                                    song_index)

    def _close_update_popup(self, event):
        """ Close update Popup """
        self._update_win.destroy()

    def update_song_callback(self, event):
        """ Update audio file. """
        form_data = self._update.get_form_data()

        data = {
            'genre': form_data[0].get('genre'),
            'rating': form_data[0].get('rating')
        }

        response = requests.put(f"http://localhost:5000/song/{form_data[1]}", json=data)
        if response.status_code == 200:
            messagebox.showinfo(title='Edit Song', message='Song updated!')
            self._close_update_popup(event)
            self.listbox_callback()
        else:
            messagebox.showerror(title='Error', message='Something went wrong, song has not updated.')

    def queue_popup(self):
        """ Show add popup window """
        self._queue_win = tk.Toplevel()
        self._queue = QueueWindow(self._queue_win, self.play_queue_callback, self.play_previous_callback,
                                  self.clear_queue_callback, self.remove_from_queue_callback, self._close_queue_popup)
        self.queue_list_box_callback()
        self._queue.position_value['text'] = self.queue_pos + 1

    def _close_queue_popup(self, event):
        """ Close update Popup """
        self._queue_win.destroy()

    def add_to_queue_callback(self):
        """ Adds song to queue. """
        song_name_dict = self._player_window.get_form_data()

        response = requests.get("http://localhost:5000/song/name/{}".format(song_name_dict['title']))
        if response.status_code == 200:
            self._queue_list.append(response.json())
            messagebox.showinfo(title='Add to Queue', message='Song added to queue!')

    def clear_queue_callback(self, event):
        """ Resets the queue position. """
        self.queue_pos = -1
        self._queue.position_value['text'] = self.queue_pos + 1

    def remove_from_queue_callback(self, event):
        """ Removes song from queue. """
        song_to_remove = self._queue.get_form_data()
        try:
            del self._queue_list[song_to_remove['index']]
            self.queue_list_box_callback()
            self.queue_pos = 0
            messagebox.showinfo(title='Queue', message='Song removed from queue.')
        except IndexError:
            messagebox.showerror(title='Error', message='No song selected.')

    def queue_list_box_callback(self):
        """ Sets queue's list box values. """
        title_list = [f'{s["title"]}' for s in self._queue_list]
        self._queue.set_titles(title_list)

    def play_queue_callback(self, event):
        """ Plays next song in queue (first if none already played). """
        try:
            if (len(self._queue_list) - 1) != self.queue_pos:
                self.queue_pos = self.queue_pos + 1
                self._queue.position_value['text'] = self.queue_pos + 1

                media_file = self._queue_list[self.queue_pos]['file_location']

                media = self._vlc_instance.media_new_path(media_file)

                self._player.set_media(media)
                self._player.play()
                self._player_window.state_value['text'] = "Playing"
                self._player_window.title_value['text'] = self._queue_list[self.queue_pos]['title']

                play_response = requests.post(f"http://localhost:5000/play_song/{self._queue_list[self.queue_pos]}")
            else:
                messagebox.showerror(title='Error', message='No songs left in queue!')
        except IndexError:
            messagebox.showerror(title='Error', message='No songs left in queue!')

    def play_previous_callback(self, event):
        """ Plays previous song in queue. """
        if self.queue_pos > 0:
            try:
                self.queue_pos = self.queue_pos - 1
                self._queue.position_value['text'] = self.queue_pos + 1

                media_file = self._queue_list[self.queue_pos]['file_location']

                media = self._vlc_instance.media_new_path(media_file)

                self._player.set_media(media)
                self._player.play()
                self._player_window.state_value['text'] = "Playing"
                self._player_window.title_value['text'] = self._queue_list[self.queue_pos]['title']

                play_response = requests.post(f"http://localhost:5000/play_song/{self._queue_list[self.queue_pos]}")
            except IndexError:
                messagebox.showerror(title='Error', message='No songs left in queue!')
        else:
            messagebox.showerror(title='Error', message='This is the first song!')


if __name__ == "__main__":
    """ Create Tk window manager and a main window. Start the main loop """
    root = tk.Tk()
    MainAppController(root).pack()
    tk.mainloop()
