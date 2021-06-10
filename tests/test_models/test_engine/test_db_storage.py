#!/usr/bin/python3
""" test for console"""
import os
import sys
import unittest
import MySQLdb
from io import StringIO
from datetime import datetime
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

args = {
    'user': os.getenv('HBNB_MYSQL_USER'),
    'passwd': os.getenv('HBNB_MYSQL_PWD'),
    'db': os.getenv('HBNB_MYSQL_DB'),
    'host': os.getenv('HBNB_MYSQL_HOST')
}


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'file')
class TestDBStorage(unittest.TestCase):

    def setUp(self):
        self.db_connection = MySQLdb.connect(**self.args)
        self.cursor = self.db_connection.cursor()

    def tearDown(self):
        self.cursor.close()
        self.db_connection.close()

    def test_all(self):
        """tests if all works in File Storage"""
        storage = DBStorage()
        storage.reload()
        new_dict = len(storage.all())
        s = State(name="New_York")
        s.save()
        storage.save()
        self.assertIs(len(storage.all()), new_dict + 1)
