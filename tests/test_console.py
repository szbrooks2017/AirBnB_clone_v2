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

fs = FileStorage()

args = {
    'user': os.getenv('HBNB_MYSQL_USER'),
    'passwd': os.getenv('HBNB_MYSQL_PWD'),
    'db': os.getenv('HBNB_MYSQL_DB'),
    'host': os.getenv('HBNB_MYSQL_HOST')
}

# make dictionary
# make a conncection
# make cursor object
# fetch one
# with patch create state
# name = state
# length 2 = length 1 + 1.


class TestConsoleClass(unittest.TestCase):

    """test for conosle"""
    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'file')
    def test_state(self):
        """test state"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State name='California'")
            s_id = f.getvalue()[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            name = 'name = "San Francisco"'
            command = 'create City {} "{}"'
            command = command.format(s_id, name)
            HBNBCommand().onecmd(command)
            c_id = f.getvalue()
            self.assertTrue(len(c_id) > 0)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'file')
    def test_single_state(self):
        """test regular case"""
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            st_id = f.getvalue()[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            command = 'State.show({})'
            command = command.format(st_id)
            HBNBCommand().onecmd(command)
            state_id = f.getvalue()
            self.assertIn(st_id, state_id)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
            m = f.getvalue()
        with open(fs._FileStorage__file_path, 'r') as fd:
            self.assertIn(st_id, fd.read())

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'file')
    def test_DB_create(self):
        """test state for DB"""
        self.db_connection = MySQLdb.connect(**args)
        self.cursor = self.db_connection.cursor()
        self.cursor.execute('SELECT count(*) FROM states')
        length1 = self.cursor.fetchone()[0]
        self.cursor.close()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State name='Montana'")
        self.db_connection = MySQLdb.connect(**args)
        self.cursor = self.db_connection.cursor()
        self.cursor.execute('SELECT count(*) FROM states')
        length2 = self.cursor.fetchone()[0]
        self.assertEqual(length2, length1 + 1)

if __name__ == '__main__':
    unittest.main()
