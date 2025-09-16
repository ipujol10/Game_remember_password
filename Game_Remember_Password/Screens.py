"""The Screens to be used in the Game"""

import tkinter as tk
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from Game import Game


class MyScreen(tk.Frame):
    """Screen base for the rest of screens"""

    def __init__(self, parent: tk.Frame, controller: "Game") -> None:
        tk.Frame.__init__(self, master=parent)
        self.controller: "Game" = controller


class InitialScreen(MyScreen):
    """The initial screen where you will include in the game"""

    def __init__(self, parent: tk.Frame, controller: "Game") -> None:
        MyScreen.__init__(self, parent, controller)


class GameScreen(MyScreen):
    """The game to learn the password"""

    def __init__(self, parent: tk.Frame, controller: "Game") -> None:
        MyScreen.__init__(self, parent, controller)
