"""The Screens to be used in the Game"""

import tkinter as tk
from tkinter import Event
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from Game_Remember_Password.Utils import Screens


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

    def keyboardBinding(self) -> None:
        """Bind the current screen keys"""
        self.unbind_all("<Key>")
        self.bind_all("<Key>", self._key)

    @abstractmethod
    def _key(self, event: Event) -> None:
        """Set the key bindings"""


class InitialScreen(MyScreen):
    """The initial screen where you will include in the game"""

    def __init__(self, parent: tk.Frame, controller: "Game") -> None:
        MyScreen.__init__(self, parent, controller)
        self._password: str = ""

        tk.Label(self, text="Enter the password to train").grid(column=0, row=0, pady=20, sticky="nwe")
        self._password_entry: tk.Entry = tk.Entry(self, width=40, show="*")
        self._password_entry.grid(column=0, row=1, pady=20)
        tk.Button(self, text="Train", command=self._trainCallback).grid(column=0, row=2, pady=20)
        tk.Button(self, text="Saved", command=self._toTrain).grid(column=0, row=3, pady=20)
        tk.Button(self, text="Exit", command=self.quit).grid(column=0, row=4, pady=20)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

    def _trainCallback(self) -> None:
        self._password = self._password_entry.get()
        self.controller.password = self._password
        self.controller.showScreen(Screens.GAME)

    def _toTrain(self) -> None:
        self.controller.showScreen(Screens.ALL_PASSWORDS)

    def setScreen(self) -> None:
        self._password_entry.delete(0, tk.END)
        self._password_entry.insert(0, self._password)
        self._password_entry.focus_set()

    def _key(self, event: Event) -> None:
        key: str = event.keysym
        match key:
            case "Return":
                self._trainCallback()
                return
            case "Escape":
                self.quit()
                return
            case _:
                pass


class GameScreen(MyScreen):
    """The game to learn the password"""

    def __init__(self, parent: tk.Frame, controller: "Game") -> None:
        MyScreen.__init__(self, parent, controller)
        self._correct_password: str

        self._entry: tk.Entry = tk.Entry(self, width=40)
        self._entry.grid(column=0, row=0, pady=20)
        tk.Button(self, text="Check", command=self._checkCallback).grid(column=0, row=1, pady=20)
        self._display: tk.Text = tk.Text(self, width=40, height=1, state="disabled")
        self._display.grid(column=0, row=2, pady=20)
        tk.Button(self, text="Start again", command=self._backCallback).grid(column=0, row=3, pady=20, ipady=5)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self._fonts: list[tuple[str, int, str]] = [
            ("Arial", 12, ""),
            ("Arial", 12, "underline"),
        ]

    def _backCallback(self) -> None:
        self.controller.showScreen(Screens.INITIAL)

    def _checkCallback(self) -> None:
        current_password: str = self._entry.get()
        if current_password == self._correct_password:
            self.controller.showScreen(Screens.INITIAL)
        length: int = max(len(current_password), len(self._correct_password))
        text: str = ""
        formatting: list[tuple[str, tuple[str, int, str]]] = []
        yellow: str = "#f0a71f"
        for i in range(length):
            color: str
            f: tuple[str, int, str]
            char: str
            if i >= len(self._correct_password):
                color = yellow
                f = self._fonts[1]
                char = "x"
            elif i >= len(current_password):
                color = yellow
                f = self._fonts[1]
                char = "?"
            else:
                f = self._fonts[0]
                char = current_password[i]
                if self._correct_password[i] == current_password[i]:
                    color = "green"
                else:
                    color = "red"
            text += char
            formatting.append((color, f))
        self._display.config(state="normal")
        self._display.delete("1.0", tk.END)
        self._display.insert("1.0", text)
        self._entry.delete(0, tk.END)
        for i, (color, f) in enumerate(formatting):
            tag_name: str = f"char_{i}"
            start_idx: str = f"1.{i}"
            end_idx: str = f"1.{i+1}"
            self._display.tag_add(tag_name, start_idx, end_idx)
            self._display.tag_config(
                tagName=tag_name,
                foreground=color,
                font=f,
            )
        self._display.config(state="disabled")

    def setScreen(self) -> None:
        self._entry.delete(0, tk.END)
        self._display.config(state="normal")
        self._display.delete("1.0", tk.END)
        self._display.config(state="disabled")
        self._correct_password = self.controller.password
        self._entry.focus_set()

    def _key(self, event: Event) -> None:
        key: str = event.keysym
        match key:
            case "Return":
                self._checkCallback()
                return
            case "Escape":
                self._backCallback()
                return
            case _:
                pass


class AllPasswords(MyScreen):
    """Screen to have saved passwords and be able to train on them"""

    def __init__(self, parent: tk.Frame, controller: "Game") -> None:
        MyScreen.__init__(self, parent, controller)

        self._canvas: tk.Canvas = tk.Canvas(self)
        self._scrollbar: tk.Scrollbar = tk.Scrollbar(
            self,
            orient="vertical",
            command=self._canvas.yview,  # type:ignore
        )

        self._inner_frame: tk.Frame = tk.Frame(self._canvas)

        self._inner_frame.bind(
            "<Configure>",
            lambda _: self._canvas.configure(scrollregion=self._canvas.bbox("all")),
        )
        self._canvas.bind("<MouseWheel>", self._onMousewheel)

        self._canvas.create_window((0, 0), window=self._inner_frame, anchor="nw")
        self._canvas.configure(yscrollcommand=self._scrollbar.set)

        self._canvas.pack(side="left", fill="both", expand=True)
        self._scrollbar.pack(side="right", fill="y")

    def setScreen(self) -> None:
        pass

    def _key(self, event: Event) -> None:
        key: str = event.keysym
        match key:
            case "Escape":
                self.controller.showScreen(Screens.INITIAL)
            case "Return":
                self._addEntry()
            case _:
                pass

    def _onMousewheel(self, event: Event) -> None:
        self._canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _addEntry(self) -> None:
        tk.Label(self._inner_frame, text="Test_i").pack(pady=5)
