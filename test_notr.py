
import sys
import os
import unittest
from unittest.mock import MagicMock
import sublime
import sublime_plugin

from Notr import notr, table


#-----------------------------------------------------------------------------------
class TestNotr(unittest.TestCase):

    view = None

    def setUp(self):
        # Mock settings.
        files_path = os.path.join(sublime.packages_path(), 'Notr', 'files')
        mock_settings = {
            "visual_line_length": 100,
            "user_hl": [["2DO", "things"], ["user", "dynamic"], ["and_a", "and_b", "and_c"]],
            "user_hl_whole_word": True,
        }
        mock_settings["notr_paths"] = [files_path]
        mock_settings["notr_index"] = os.path.join(files_path, 'test-index.ntr')
        sublime.load_settings = MagicMock(return_value=mock_settings)


    def tearDown(self):
        pass

    #@unittest.skip
    def test_TableFit(self):

        #'|State |    Size    |Color|',
        #'|   ME   |34|   Red     |',28
        #'|  IA   |  31    |Blue     |',54
        #'| CO  | 15  | Brown    |',83
        #'| NY     | 4  | Yellow    |',108
        #'| TX| 2  | Green    |',136
        #'| WY   | 45        | White    |',158-189
        #{ "scope": "meta.table", "background": "lightblue" },
        #{ "scope": "meta.table.header", "background": "deepskyblue" },


        test_text = [
            'notable 1',
            'notable 2',
            'notable 3',
            'notable 4',
            'notable 5',
            '|State |    Size    |Color|',
            '|   ME   |34|   Red     |',
            '|  IA   |  31    |Blue     |',
            '| CO  | 15  | Brown    |',
            '| NY     | 4  | Yellow    |',
            '| TX| 2  | Green    |',
            '| WY   | 45        | White    |',
            'notable 6',
            'notable 7',
            'notable 8',
            'notable 9',
            ]

        view = sublime.View(600)
        view.insert(None, 0, '\n'.join(test_text))
        sel = sublime.Selection(view.id())
        #sel.add(sublime.Region(25, 29)) # before table
        sel.add(sublime.Region(73, 77)) # in table
        view.sel = MagicMock(return_value=sel)

        def scope_name(*args, **kwargs):
            pos = args[0]
            if pos >= 28 and pos <= 53:
                return 'text.notr meta.table.header'
            elif pos >= 54 and pos <= 189:
                return 'text.notr meta.table'
            else:
                return 'text.notr'
            pass

        view.scope_name = MagicMock(side_effect=scope_name)

        #edit = sublime.Edit('test')
        cmd = table.TableFitCommand(view)
        cmd.run(None)



    #@unittest.skip
    def test_on_init(self):
        ''' Tests the ntr file parsing. '''

        view = sublime.View(601)
        sel = sublime.Selection(view.id())
        sel.add(sublime.Region(10, 20, 101))
        view.sel = MagicMock(return_value=sel)

        # Mock syntax.
        syntax = sublime.Syntax('', 'Notr', False, '')
        #syntax.name = MagicMock(return_value='Notr')
        view.syntax = MagicMock(return_value=syntax)

        window = sublime.Window(500)
        view._window = MagicMock(return_value=window)

        vnew = sublime.View(501)
        window.new_file = MagicMock(return_value = vnew)

        evt = notr.NotrEvent()
        evt.on_init([view])

        self.assertEqual(len(notr._tags), 7)
        self.assertEqual(len(notr._links), 6)
        self.assertEqual(len(notr._refs), 6)
        self.assertEqual(len(notr._sections), 13)
        self.assertEqual(len(notr._parse_errors), 0)

    @unittest.skip
    def test_GotoRef(self):
        edit = sublime.Edit('test')
        cmd = notr.NotrGotoRefCommand(view)
        cmd.run(edit)

    @unittest.skip
    def test_GotoSection(self):
        edit = sublime.Edit('test')
        cmd = notr.NotrGotoSectionCommand(view)
        cmd.run(edit)

    @unittest.skip
    def test_InsertRef(self):
        edit = sublime.Edit('test')
        cmd = notr.NotrInsertRefCommand(view)
        cmd.run(edit)


#-----------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
