"""Game class where the magic happens"""

import tkinter as tk
from types import TracebackType


class Game(tk.Tk):
    """Class"""

    def __init__(self) -> None:
        tk.Tk.__init__(self)

    def __enter__(self) -> "Game":
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.quit()
