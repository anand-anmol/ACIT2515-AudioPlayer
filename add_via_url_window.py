import tkinter as tk


class AddViaUrlWindow(tk.Frame):
    """ Layout for the Chooser Window """

    def __init__(self, parent, add_callback, close_callback):
        """ Initialize the popup listbox window """
        tk.Frame.__init__(self, parent)
        self._add_cb = add_callback
        self._close_cb = close_callback

        parent.title('Add Song using URL')

        # Frames
        self.top_frame = tk.Frame(self.master)
        self.top_frame.grid(row=0, padx=30, pady=0)

        self.bot_frame = tk.Frame(self.master)
        self.bot_frame.grid(row=1, padx=30, pady=0)

        # Labels and entries
        self._URL_label = tk.Label(self.top_frame, text='URL:')
        self._URL_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        self._URL_entry = tk.Entry(self.top_frame, width=20)
        self._URL_entry.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

        # Buttons
        self.save_button = tk.Button(self.bot_frame, text='Save', width=10)
        self.save_button.grid(row=10, padx=10, pady=5)
        self.save_button.bind("<Button-1>", self._add_cb)

        self.cancel_button = tk.Button(self.bot_frame, text='Close', width=10)
        self.cancel_button.grid(row=11, padx=10, pady=5)
        self.cancel_button.bind("<Button-1>", self._close_cb)

    def get_form_data(self):
        """ Returns dictionary with all entry fields """
        return {'URL': self._URL_entry.get()}
