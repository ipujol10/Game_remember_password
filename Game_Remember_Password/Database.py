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
        self.cur: sqlite3.Cursor = self.con.cursor()
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        if ("entries",) not in self.cur.fetchall():
            self.cur.execute("CREATE TABLE entries(name TEXT PRIMARY KEY, password TEXT)")

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
        if self.con.execute(f"SELECT COUNT(1) FROM entries WHERE name='{name}'").fetchone()[0]:
            return
        statement: str = f"INSERT INTO entries (name, password) VALUES ('{name}', '{password}')"
        self.cur.execute(statement)

    def deleteEntry(self, name: str) -> None:
        """
        Delete a password entry

        Arguments:
            name (str): the name of the entry

        Returns:
            None
        """
        statement: str = f"DELETE FROM entries WHERE name='{name}'"
        self.cur.execute(statement)

    def getEntries(self) -> list[tuple[str, str]]:
        """
        Get all entries of saved entries

        Returns:
            out (list[tuple[str, str]]): a list of pairs [name, password]
        """
        statement: str = "SELECT name, password FROM entries"
        res: sqlite3.Cursor = self.cur.execute(statement)
        return res.fetchall()
