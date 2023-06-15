
import sys
import os
import unittest
from unittest.mock import MagicMock
import sublime
import sublime_plugin

# TODO This supports execution in VS or from command line but doesn't support intellisense.
from Notr import notr, table


#-----------------------------------------------------------------------------------
class TestNotr(unittest.TestCase):

    view = None

    def setUp(self):
        # Mock settings.
        files_path = os.path.join(sublime.packages_path(), 'Notr', 'files')
        mock_settings = {
            "visual_line_length": 100,
            "user_hl": [["2DO", "things"], ["user"], ["dynamic"], ["and_a"], ["and_b"], ["and_c"]],
            "user_hl_whole_word": True,
        }
        mock_settings["notr_paths"] = [files_path]
        mock_settings["notr_index"] = os.path.join(files_path, 'test-index.ntr')
        sublime.load_settings = MagicMock(return_value=mock_settings)

        # Init internals.
        self.view = sublime.View(600)
        sel = sublime.Selection(self.view.id())
        sel.add(sublime.Region(10, 20, 101))
        self.view.sel = MagicMock(return_value=sel)

        # Mock syntax.
        syntax = sublime.Syntax('', 'Notr', False, '')
        syntax.name = MagicMock(return_value='Notr')
        self.view.syntax = MagicMock(return_value=syntax)

    def tearDown(self):
        pass

    #@unittest.skip
    def test_TableFit(self):

        test_text = [
            'not-table',
            'not-table',
            'not-table',
            '|State |    Size    |Color|',
            '|   ME   |34|   Red     |',
            '|  IA   |  31    |Blue     |',
            '| CO  | 15  | Brown    |',
            '| NY     | 4  | Yellow    |',
            '| TX| 2  | Green    |',
            '| WY   | 45        | White    |',
            'not-table',
            'not-table',
            'not-table',
            ]

        edit = sublime.Edit('test')
        cmd = table.TableFitCommand(self.view)
        cmd.run(edit)




    @unittest.skip
    def test_on_init(self):
        window = sublime.Window(500)
        self.view._window = MagicMock(return_value=window)

        vnew = sublime.View(501)
        window.new_file = MagicMock(return_value = vnew)

        evt = notr.NotrEvent()
        evt.on_init([self.view])

        self.assertEqual(len(notr._tags), 7)
        self.assertEqual(len(notr._links), 6)
        self.assertEqual(len(notr._refs), 6)
        self.assertEqual(len(notr._sections), 13)
        self.assertEqual(len(notr._parse_errors), 0)

    @unittest.skip
    def test_GotoRef(self):
        edit = sublime.Edit('test')
        cmd = notr.NotrGotoRefCommand(self.view)
        cmd.run(edit)

    @unittest.skip
    def test_GotoSection(self):
        edit = sublime.Edit('test')
        cmd = notr.NotrGotoSectionCommand(self.view)
        cmd.run(edit)

    @unittest.skip
    def test_InsertRef(self):
        edit = sublime.Edit('test')
        cmd = notr.NotrInsertRefCommand(self.view)
        cmd.run(edit)


#-----------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
