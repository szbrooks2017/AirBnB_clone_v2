#!/usr/bin/python3
""" test for console"""
import os
import sys
import unittest
from io import StringIO
from datetime import datetime
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'file')
class TestConsoleClass(unittest.TestCase):
    """test for conosle"""

    def test_state(self):
        """test state"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State name='California'")
            s_id = f.getvalue()
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
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            s_id = f.getvalue()
            command = 'State.show({})'
            command = command.format(s_id)
            HBNBCommand().onecmd(command)
            state_id = f.getvalue()
            self.assertIn(s_id, state_id)
            

if __name__ == '__main__':
    unittest.main()
