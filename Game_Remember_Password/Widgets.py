"""Widgets to be used in the APP"""

import tkinter as tk
from tkinter import Event


class Entry(tk.Frame):
    """Widget for a Saved Password Entry"""

    def __init__(self, parent: tk.Frame, name: str, password: str) -> None:
        tk.Frame.__init__(self, parent, height=5, relief="groove", borderwidth=2)
        self.pack(fill="x")
        self._name = name
        self._password = password
        self.name: tk.Label = tk.Label(self, text=name, relief="groove")
        self.name.grid(column=0, row=0, sticky="we")
        self.password: tk.Label = tk.Label(self, text=password, relief="groove")
        self.password.grid(column=1, row=0, sticky="we")

        left_button: str = "<Button-1>"
        for w in (self, self.name, self.password):
            w.bind(left_button, self._onClick)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def _onClick(self, _: Event) -> None:
        print(f"Clicked item {self}")
