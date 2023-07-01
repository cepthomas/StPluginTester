
import sys
import os
import unittest
from unittest.mock import MagicMock
import sublime
import sublime_plugin
from Notr import notr, table


#-----------------------------------------------------------------------------------
class TestNotr(unittest.TestCase):

    #------------------------------------------------------------
    def setUp(self):

        notr_files_path = os.path.join(sublime.packages_path(), 'Notr', 'files')

        # Mock settings.
        mock_settings = {
            "visual_line_length": 100,
            "fixed_hl": [["2DO", "things"], ["user", "dynamic"], ["and_a", "and_b", "and_c"]],
            "fixed_hl_whole_word": True,
        }
        mock_settings["notr_paths"] = [notr_files_path]
        mock_settings["notr_index"] = os.path.join(notr_files_path, 'test-index.ntr')
        sublime.load_settings = MagicMock(return_value=mock_settings)

        # Mock top level entities.
        self.view = sublime.View(10)
        self.window = sublime.Window(20)
        self.view._window = MagicMock(return_value=self.window)

        # Mock syntax interrogation.
        self.syntax = sublime.Syntax('', 'Notr', False, '')
        self.view.syntax = MagicMock(return_value=self.syntax)


    #------------------------------------------------------------
    def tearDown(self):
        pass


    #------------------------------------------------------------
    @unittest.skip
    def test_parsing(self):
        ''' Tests the ntr file parsing. '''

        # notr._process_notr_files()
        # for e in notr._parse_errors:
        #     print(f'parse error:{e}')

        evt = notr.NotrEvent()
        evt.on_init([self.view])

        self.assertEqual(len(notr._tags), 7)
        self.assertEqual(len(notr._links), 6)
        self.assertEqual(len(notr._refs), 6)
        self.assertEqual(len(notr._sections), 13)
        self.assertEqual(len(notr._parse_errors), 0)


    #------------------------------------------------------------
    @unittest.skip
    def test_GotoRef(self):
        cmd = notr.NotrGotoRefCommand(self.view)
        cmd.run(None)


    #------------------------------------------------------------
    @unittest.skip
    def test_GotoSection(self):
        cmd = notr.NotrGotoSectionCommand(self.view)
        cmd.run(None)


    #------------------------------------------------------------
    @unittest.skip
    def test_InsertRef(self):
        cmd = notr.NotrInsertRefCommand(self.view)
        cmd.run(None)


#-----------------------------------------------------------------------------------
if __name__ == '__main__':
    # https://docs.python.org/3/library/unittest.html#unittest.main
    tp = unittest.main(verbosity=2, exit=False)
    print(tp.result)