"""Test DataBase module"""

import os
import unittest

from Game_Remember_Password.Database import DataBase


class DataBaseTest(unittest.TestCase):
    """Test Case for DataBase"""

    def testCreateFile(self) -> None:
        """Test the creation of the database file"""
        file: str = "test/data/create_file.db"
        self.assertFalse(os.path.exists(file))
        with DataBase(file):
            pass
        self.assertTrue(os.path.exists(file))

        with DataBase(file):
            pass
        self.assertTrue(os.path.exists(file))

        os.remove(file)
        self.assertFalse(os.path.exists(file))

    def testCreateNewDB(self) -> None:
        """Test the creation of a database"""
        file: str = "test/data/createDB.db"
        with DataBase(file) as db:
            self.assertFalse(db.getEntries())

        os.remove(file)
        open(file, "w", encoding="utf_8").close()
