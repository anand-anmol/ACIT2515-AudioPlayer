import tkinter as tk


class UpdateWindow(tk.Frame):
    """ Layout for the Chooser Window """

    def __init__(self, parent, update_callback, close_callback, index):
        """ Initialize the popup listbox window """
        tk.Frame.__init__(self, parent)
        self._update_cb = update_callback
        self._close_cb = close_callback
        self._song_index = index
        parent.title('Update Song')

        # Frames
        self.top_frame = tk.Frame(self.master)
        self.top_frame.grid(row=0, padx=30, pady=0)

        self.bot_frame = tk.Frame(self.master)
        self.bot_frame.grid(row=1, padx=30, pady=0)

        # Labels and entries
        self._genre_label = tk.Label(self.top_frame, text='Genre:')
        self._genre_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        self._genre_entry = tk.Entry(self.top_frame, width=20)
        self._genre_entry.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

        self._rating_label = tk.Label(self.top_frame, text='Rating:')
        self._rating_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

        self._rating_entry = tk.Entry(self.top_frame, width=20)
        self._rating_entry.grid(row=3, column=0, sticky=tk.E, padx=5, pady=5)

        # Buttons
        self.save_button = tk.Button(self.bot_frame, text='Save', width=10)
        self.save_button.grid(row=10, padx=10, pady=5)
        self.save_button.bind("<Button-1>", self._update_cb)

        self.cancel_button = tk.Button(self.bot_frame, text='Close', width=10)
        self.cancel_button.grid(row=11, padx=10, pady=5)
        self.cancel_button.bind("<Button-1>", self._close_cb)

    def get_form_data(self):
        """ Returns dictionary with all entry fields """
        return {
                'genre': self._genre_entry.get(),
                'rating': self._rating_entry.get()
                }, self._song_index
