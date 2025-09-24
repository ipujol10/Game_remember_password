"""Game class where the magic happens"""

import tkinter as tk
from types import TracebackType
from Game_Remember_Password.Utils import Screens
from Game_Remember_Password.Screens import MyScreen, InitialScreen, GameScreen


class Game(tk.Tk):
    """Class"""

    def __init__(self) -> None:
        tk.Tk.__init__(self)
        self.title("Password Game")
        self.main_frame: tk.Frame = tk.Frame(self)
        self.main_frame.grid(column=0, row=0, sticky="nswe")
        self._current_frame: MyScreen
        self._frames: dict[Screens, MyScreen] = {}
        for i, screen in enumerate((InitialScreen, GameScreen)):
            frame = screen(parent=self.main_frame, controller=self)
            self._frames[Screens(i)] = frame

            frame.grid(row=0, column=0, sticky="nswe")

        self.showScreen(Screens.INITIAL)

        self.password: str

    def showScreen(self, screen: Screens) -> None:
        """Display the selected screen"""
        self._current_frame = self._frames[screen]
        self._current_frame.setScreen()
        self._current_frame.keyboardBinding()
        self._current_frame.tkraise()  # type: ignore

    def __enter__(self) -> "Game":
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.quit()
