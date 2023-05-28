
import sys
import os
import unittest
from unittest.mock import MagicMock

import sublime
import sublime_plugin

#print('sys.path')
#print(sys.path)

# This supports execution in VS or from command line but doesn't support intellisense.
from Notr import notr

# This (sometimes?) supports intellisense but fails to execute with "attempted relative import with no known parent package". It's a mystery.
#from ..Notr import notr


#-----------------------------------------------------------------------------------
class TestNotr(unittest.TestCase):

    view = None

    def setUp(self):
        # Mock settings.
        mock_settings = {
            "notr_paths": ["C:\\Users\\cepth\\AppData\\Roaming\\Sublime Text\\Packages\\Notr\\files"],
            "notr_index": "C:\\Users\\cepth\\AppData\\Roaming\\Sublime Text\\Packages\\Notr\\files\\index.ntr",
            "visual_line_length": 100,
            "user_hl": [["2DO", "things"], ["user"], ["dynamic"], ["and_a"], ["and_b"], ["and_c"]],
            "user_hl_whole_word": True,
        }
        sublime.load_settings = MagicMock(return_value=mock_settings)

        # Init internals.
        self.view = sublime.View(600)
        sel = sublime.Selection(self.view.id())
        sel.add(sublime.Region(10, 20, 101))
        self.view.sel = MagicMock(return_value=sel)

        # Mock syntax.
        syntax = sublime.Syntax()
        syntax.name = MagicMock(return_value='Notr')
        self.view.syntax = MagicMock(return_value=syntax)

    def tearDown(self):
        pass

    def test_on_init(self):

        window = sublime.Window(500)
        self.view.window = MagicMock(return_value=window)

        vnew = sublime.View(501)
        window.new_file = MagicMock(return_value = vnew)

        evt = notr.NotrEvent()
        evt.on_init([self.view])

        self.assertEqual(len(notr._tags), 8)
        self.assertEqual(len(notr._links), 6)
        self.assertEqual(len(notr._refs), 6)
        self.assertEqual(len(notr._sections), 14)
        self.assertEqual(len(notr._parse_errors), 0)

    def test_GotoRef(self):
        edit = sublime.Edit('token')
        cmd = notr.NotrGotoRefCommand(self.view)
        #cmd.run(edit)

    def test_GotoSection(self):
        edit = sublime.Edit('token')
        cmd = notr.NotrGotoSectionCommand(self.view)
        #cmd.run(edit)

    def test_InsertRef(self):
        edit = sublime.Edit('token')
        cmd = notr.NotrInsertRefCommand(self.view)
        #cmd.run(edit)


#-----------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
