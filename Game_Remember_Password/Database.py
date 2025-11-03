"""DataBase module"""

import sqlite3
import os

from types import TracebackType


class DataBase:
    """Class to manage the DataBase"""

    def __init__(self, file: str) -> None:
        if not os.path.exists(file):
            open(file, "a", encoding="utf_8").close()
        self.con = sqlite3.connect(file)

    def __enter__(self) -> "DataBase":
        return self

    def __exit__(
        self, type_: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
    ) -> None:
        self.con.close()

    def createEntry(self, name: str, password: str) -> None:
        """
        Create a password entry

        Arguments:
            name (str): name to be displayed in the GUI
            password (str): the related password

        Returns:
            None
        """
        raise NotImplementedError

    def deleteEntry(self, name: str) -> None:
        """
        Delete a password entry

        Arguments:
            name (str): the name of the entry

        Returns:
            None
        """
        raise NotImplementedError

    def getEntries(self) -> list[tuple[str, str]]:
        """
        Get all entries of saved entries

        Returns:
            out (list[tuple[str, str]]): a list of pairs [name, password]
        """
        raise NotImplementedError
