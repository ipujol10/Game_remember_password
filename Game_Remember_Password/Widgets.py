"""Widgets to be used in the APP"""

import tkinter as tk


class Entry(tk.Frame):
    """Widget for a Saved Password Entry"""

    def __init__(self, parent: tk.Frame, name: str, password: str) -> None:
        tk.Frame.__init__(self, parent, width=parent.winfo_width(), height=5)
        self._name = name
        self._password = password
        self.name: tk.Label = tk.Label(self, text=name, relief="groove")
        self.name.pack(side="left", fill="both")
        self.password: tk.Label = tk.Label(self, text=password, relief="groove")
        self.password.pack(side="right", fill="both")
