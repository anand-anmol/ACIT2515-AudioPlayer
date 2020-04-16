import tkinter as tk


class AddWindow(tk.Frame):
    """ Layout for the Chooser Window """

    def __init__(self, parent, add_callback, close_callback):
        """ Initialize the popup listbox window """
        tk.Frame.__init__(self, parent)
        self._add_cb = add_callback
        self._close_cb = close_callback

        parent.title('Add Song')

        # Frames
        self.top_frame = tk.Frame(self.master)
        self.top_frame.grid(row=0, padx=30, pady=0)

        self.bot_frame = tk.Frame(self.master)
        self.bot_frame.grid(row=1, padx=30, pady=0)

        # Labels and entries
        self._title_label = tk.Label(self.top_frame, text='Title:')
        self._title_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        self._title_entry = tk.Entry(self.top_frame, width=20)
        self._title_entry.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

        self._artist_label = tk.Label(self.bot_frame, text='Artist:')
        self._artist_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        self._artist_entry = tk.Entry(self.bot_frame, width=20)
        self._artist_entry.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

        self._album_label = tk.Label(self.bot_frame, text='Album:')
        self._album_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

        self._album_entry = tk.Entry(self.bot_frame, width=20)
        self._album_entry.grid(row=3, column=0, sticky=tk.E, padx=5, pady=5)

        self._runtime_label = tk.Label(self.bot_frame, text='Runtime:')
        self._runtime_label.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)

        self._runtime_entry = tk.Entry(self.bot_frame, width=20)
        self._runtime_entry.grid(row=5, column=0, sticky=tk.E, padx=5, pady=5)

        self._file_location_label = tk.Label(self.bot_frame, text='File location:')
        self._file_location_label.grid(row=6, column=0, sticky=tk.W, padx=5, pady=5)

        self._file_location_entry = tk.Entry(self.bot_frame, width=20)
        self._file_location_entry.grid(row=7, column=0, sticky=tk.E, padx=5, pady=5)

        self._genre_label = tk.Label(self.bot_frame, text='Genre (optional):')
        self._genre_label.grid(row=8, column=0, sticky=tk.W, padx=5, pady=5)

        self._genre_entry = tk.Entry(self.bot_frame, width=20)
        self._genre_entry.grid(row=9, column=0, sticky=tk.E, padx=5, pady=5)

        # Buttons
        self.save_button = tk.Button(self.bot_frame, text='Save', width=10)
        self.save_button.grid(row=10, padx=10, pady=5)
        self.save_button.bind("<Button-1>", self._add_cb)

        self.cancel_button = tk.Button(self.bot_frame, text='Close', width=10)
        self.cancel_button.grid(row=11, padx=10, pady=5)
        self.cancel_button.bind("<Button-1>", self._close_cb)

    def get_form_data(self):
        """ Returns dictionary with all entry fields """
        return {'title': self._title_entry.get(),
                'artist': self._artist_entry.get(),
                'album': self._album_entry.get(),
                'runtime': self._runtime_entry.get(),
                'file_location': self._file_location_entry.get(),
                'genre': self._genre_entry.get()}
