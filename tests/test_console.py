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

if __name__ == '__main__':
    unittest.main()
