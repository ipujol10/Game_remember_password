"""Widgets to be used in the APP"""

import tkinter as tk
from tkinter import Event
from typing import TYPE_CHECKING
from Game_Remember_Password.Screens import Screens

if TYPE_CHECKING:
    from Game import Game


class Entry(tk.Frame):
    """Widget for a Saved Password Entry"""

    def __init__(self, parent: tk.Frame, controller: "Game", name: str, password: str) -> None:
        tk.Frame.__init__(self, parent, height=5, relief="groove", borderwidth=2)
        self.controller = controller
        self.pack(fill="x")
        self._name = name
        self._password = password
        name_label: tk.Label = tk.Label(self, text=name, relief="groove")
        name_label.grid(column=0, row=0, sticky="we")
        password_label: tk.Label = tk.Label(self, text=password, relief="groove")
        password_label.grid(column=1, row=0, sticky="we")

        left_button: str = "<Button-1>"
        for w in (self, name_label, password_label):
            w.bind(left_button, self._onClick)

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

    def _onClick(self, _: Event) -> None:
        self.controller.password = self._password
        self.controller.showScreen(Screens.GAME)
