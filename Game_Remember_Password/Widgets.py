"""Widgets to be used in the APP"""

import tkinter as tk


class Entry(tk.Frame):
    """Widget for a Saved Password Entry"""

    def __init__(self, parent: tk.Frame, name: str, password: str) -> None:
        tk.Frame.__init__(self, parent, height=5, relief="groove", borderwidth=2)
        self._name = name
        self._password = password
        self.name: tk.Label = tk.Label(self, text=name, relief="groove")
        self.name.pack(fill="both", side="left", expand=True)
        self.password: tk.Label = tk.Label(self, text=password, relief="groove")
        self.password.pack(after=self.name, fill="both", side="right", expand=True)
