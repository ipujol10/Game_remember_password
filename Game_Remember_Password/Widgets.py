"""Widgets to be used in the APP"""

import tkinter as tk
from tkinter import Event
from typing import TYPE_CHECKING
from Game_Remember_Password.Screens import Screens

if TYPE_CHECKING:
    from Game import Game
    from Screens import AllPasswords


class Entry(tk.Frame):
    """Widget for a Saved Password Entry"""

    def __init__(
        self, parent: tk.Frame, controller: "Game", all_passwords: "AllPasswords", name: str, password: str
    ) -> None:
        tk.Frame.__init__(self, parent, height=5, relief="groove", borderwidth=2)
        self.controller = controller
        self._parent = all_passwords
        self.pack(fill="x")
        self._name = name
        self._password = password
        name_label: tk.Label = tk.Label(self, text=name, relief="groove")
        name_label.grid(column=0, row=0, sticky="we")
        self._pass_variable: tk.StringVar = tk.StringVar(self)
        password_label: tk.Label = tk.Label(self, textvariable=self._pass_variable, relief="groove")
        password_label.grid(column=1, row=0, sticky="we")
        self._showing: bool = True
        self._showing_texts: tuple[tuple[str, str], tuple[str, str]] = (("********", "Show"), (self._password, "Hide"))
        self._show_variable: tk.StringVar = tk.StringVar(self)
        tk.Button(self, textvariable=self._show_variable, command=self._show).grid(column=2, row=0)
        tk.Button(self, text="X", command=self._delete).grid(column=3, row=0)

        left_button: str = "<Button-1>"
        for w in (self, name_label, password_label):
            w.bind(left_button, self._onClick)

        self.grid_columnconfigure(0, weight=8)
        self.grid_columnconfigure(1, weight=8)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._show()

    def _onClick(self, _: Event) -> None:
        self.controller.password = self._password
        self.controller.showScreen(Screens.GAME)

    def _show(self) -> None:
        self._showing = not self._showing
        password, button = self._showing_texts[self._showing]
        self._show_variable.set(button)
        self._pass_variable.set(password)

    def _delete(self) -> None:
        self._parent.deleteEntry(self)
