import tkinter as tk
from tkinter import Scrollbar


class QueueWindow(tk.Frame):
    """ Layout for the Chooser Window """

    def __init__(self, parent, play_queue_callback, play_previous, clear_callback, remove_callback, close_callback):
        """ Initialize the popup listbox window """
        tk.Frame.__init__(self, parent)
        self._play_queue_cb = play_queue_callback
        self._play_previous_cb = play_previous
        self._clear_cb = clear_callback
        self._remove_cb = remove_callback
        self._close_cb = close_callback

        parent.title('Song Queue')

        # Frames
        self.top_frame = tk.Frame(self.master)
        self.top_frame.grid(row=0, padx=30, pady=0)

        self.bot_frame = tk.Frame(self.master)
        self.bot_frame.grid(row=1, padx=30, pady=0)

        # Labels and entries
        # Listbox
        self.list_box = tk.Listbox(self.top_frame, width=20, height=10)
        self.list_box.grid(row=0, column=0)

        # Scrollbar
        scrollbar = Scrollbar(self.top_frame, orient="vertical", width=20)
        scrollbar.config(command=self.list_box.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")

        self.list_box.config(yscrollcommand=scrollbar.set)

        # Buttons
        self.next_button = tk.Button(self.bot_frame, text='Play Next', width=10)
        self.next_button.grid(row=10, column=1, padx=10, pady=5)
        self.next_button.bind("<Button-1>", self._play_queue_cb)

        self.previous_button = tk.Button(self.bot_frame, text='Play Previous', width=10)
        self.previous_button.grid(row=10, column=2, padx=10, pady=5)
        self.previous_button.bind("<Button-1>", self._play_previous_cb)

        self.clear_button = tk.Button(self.bot_frame, text='Reset Queue', width=10)
        self.clear_button.grid(row=11, column=1, padx=10, pady=5)
        self.clear_button.bind("<Button-1>", self._clear_cb)

        self.remove_button = tk.Button(self.bot_frame, text='Remove', width=10)
        self.remove_button.grid(row=11, column=2, padx=10, pady=5)
        self.remove_button.bind("<Button-1>", self._remove_cb)

        self.cancel_button = tk.Button(self.bot_frame, text='Close', width=10)
        self.cancel_button.grid(row=12, column=1, columnspan=2, sticky=tk.N, padx=10, pady=5)
        self.cancel_button.bind("<Button-1>", self._close_cb)

    def set_titles(self, titles):
        """ Update the listbox to display all names """
        self.list_box.delete(0, tk.END)
        for title in titles:
            self.list_box.insert(tk.END, title)

    def get_form_data(self):
        """ returns selected song from the listbox """
        return {"title": self.list_box.get('anchor'), "index": self.list_box.index('anchor')}
