"""Test DataBase module"""

import os
import unittest

from Game_Remember_Password.Database import DataBase


class DataBaseTest(unittest.TestCase):
    """Test Case for DataBase"""

    def tearDown(self) -> None:
        folder: str = "test/data/"
        files: list[str] = ["create_file.db", "createDB.db", "create_delete.db"]
        for file in files:
            path: str = folder + file
            if os.path.exists(path):
                os.remove(path)

        open(folder + "createDB.db", "w", encoding="utf_8").close()

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

    def testCreateNewDB(self) -> None:
        """Test the creation of a database"""
        file: str = "test/data/createDB.db"
        with DataBase(file) as db:
            self.assertFalse(db.getEntries())

    def testGetEntries(self) -> None:
        """Test DB get entries"""
        file: str = "test/data/get.db"
        with DataBase(file) as db:
            entries: list[tuple[str, str]] = db.getEntries()
            self.assertEqual(entries, [("test", "password"), ("test2", "password2")])

    def testCreateAndDelete(self) -> None:
        """Test that the DataBase can create and delete entries"""
        file: str = "test/data/create_delete.db"
        with DataBase(file) as db:
            self.assertFalse(db.getEntries())
            db.createEntry("test", "password")
            db.createEntry("test2", "password2")
            self.assertEqual(db.getEntries(), [("test", "password"), ("test2", "password2")])
            db.createEntry("test2", "password2")
            self.assertEqual(db.getEntries(), [("test", "password"), ("test2", "password2")])
            db.deleteEntry("test")
            self.assertEqual(db.getEntries(), [("test2", "password2")])
            db.deleteEntry("test")
            self.assertEqual(db.getEntries(), [("test2", "password2")])
