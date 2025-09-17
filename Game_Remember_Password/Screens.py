"""The Screens to be used in the Game"""

import tkinter as tk
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from Utils import Screens


if TYPE_CHECKING:
    from Game import Game


class MyScreen(tk.Frame, ABC):
    """Screen base for the rest of screens"""

    def __init__(self, parent: tk.Frame, controller: "Game") -> None:
        tk.Frame.__init__(self, master=parent)
        self.controller: "Game" = controller

    @abstractmethod
    def setScreen(self) -> None:
        """Set the screen settings"""


class InitialScreen(MyScreen):
    """The initial screen where you will include in the game"""

    def __init__(self, parent: tk.Frame, controller: "Game") -> None:
        MyScreen.__init__(self, parent, controller)
        self._password: str = ""

        tk.Label(self, text="Enter the password to train").grid(column=0, row=0, pady=20, sticky="nwe")
        self._password_entry: tk.Entry = tk.Entry(self, width=40, show="*")
        self._password_entry.grid(column=0, row=1, pady=20)
        tk.Button(self, text="Train", command=self._trainCallback).grid(column=0, row=2, pady=20)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

    def _trainCallback(self) -> None:
        self._password = self._password_entry.get()
        self.controller.showScreen(Screens.GAME)

    def setScreen(self) -> None:
        self._password_entry.delete(0, tk.END)
        self._password_entry.insert(0, self._password)


class GameScreen(MyScreen):
    """The game to learn the password"""

    def __init__(self, parent: tk.Frame, controller: "Game") -> None:
        MyScreen.__init__(self, parent, controller)

        self._entry: tk.Entry = tk.Entry(self, width=40)
        self._entry.grid(column=0, row=0, pady=20)
        tk.Button(self, text="Check", command=self._checkCallback).grid(column=0, row=1, pady=20)
        self._display: tk.Text = tk.Text(self, width=40, height=1, state="disabled")
        self._display.grid(column=0, row=2, pady=20)
        tk.Button(self, text="Start again", command=self._backCallback).grid(column=0, row=3, pady=20)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

    def _backCallback(self) -> None:
        self.controller.showScreen(Screens.INITIAL)

    def _checkCallback(self) -> None:
        raise NotImplementedError

    def setScreen(self) -> None:
        self._entry.delete(0, tk.END)
        self._display.delete("1.0", tk.END)
