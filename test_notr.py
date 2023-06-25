
import sys
import os
import unittest
from unittest.mock import MagicMock
import sublime
import sublime_plugin

from Notr import notr, table


#-----------------------------------------------------------------------------------
class TestNotr(unittest.TestCase):

    print('TestNotr')

    # GP test text.
    test_text = [
        'notable 0',
        'notable 1',
        'notable 2',
        'notable 3',
        'notable 4',
        '|State |    Size    |Color|',
        '|   ME   |34|   Red     |',
        '|  IA   |  31    |Blue     |',
        '| CO  | 15  | Brown    |',
        '| NY     | 4  | Yellow    |',
        '| TX| 2  | Green    |',
        '| WY   | 45        | White    |',
        'notable 12',
        'notable 13',
        'notable 14',
        'notable 15',
        ]

    test_text_str = '\n'.join(test_text)

    print('TestNotr2')

    def setUp(self):
        # Mock settings.
        print('setUp')
        files_path = os.path.join(sublime.packages_path(), 'Notr', 'files')
        mock_settings = {
            "visual_line_length": 100,
            "fixed_hl": [["2DO", "things"], ["user", "dynamic"], ["and_a", "and_b", "and_c"]],
            "fixed_hl_whole_word": True,
        }
        mock_settings["notr_paths"] = [files_path]
        mock_settings["notr_index"] = os.path.join(files_path, 'test-index.ntr')
        sublime.load_settings = MagicMock(return_value=mock_settings)


    def tearDown(self):
        pass


    #------------------------ plugin ------------------------------------

    @unittest.skip
    def test_on_init(self):
        ''' Tests the ntr file parsing. '''

        view = sublime.View(400)
        sel = sublime.Selection(view.id())
        sel.add(sublime.Region(10, 20, 101))
        view.sel = MagicMock(return_value=sel)

        # Mock syntax.
        syntax = sublime.Syntax('', 'Notr', False, '')
        #syntax.name = MagicMock(return_value='Notr')
        view.syntax = MagicMock(return_value=syntax)

        window = sublime.Window(100)
        view._window = MagicMock(return_value=window)

        vnew = sublime.View(401)
        window.new_file = MagicMock(return_value = vnew)

        evt = notr.NotrEvent()
        evt.on_init([view])

        self.assertEqual(len(notr._tags), 7)
        self.assertEqual(len(notr._links), 6)
        self.assertEqual(len(notr._refs), 6)
        self.assertEqual(len(notr._sections), 13)
        self.assertEqual(len(notr._parse_errors), 0)


    #------------------------ table ------------------------------------

    # @unittest.skip
    def test_table_internal(self):
        ''' Some basic tests. '''
        print('test_table_internal')

        view = sublime.View(500)
        view.insert(None, 0, self.test_text_str)

        # Test rowcol() and text_point().
        self.assertEqual(view.rowcol(24), (2, 4))
        self.assertEqual(view.rowcol(148), (8,15))
        self.assertEqual(view.rowcol(239), (11, 31))
        self.assertEqual(view.rowcol(240), (12, 0))
        self.assertEqual(view.text_point(2, 4), 24)
        self.assertEqual(view.text_point(8,15), 148)
        self.assertEqual(view.text_point(11, 31), 239)
        self.assertEqual(view.text_point(12, 0), 240)


    # @unittest.skip
    def test_TableFit(self):
        ''' TableFitCommand. Fitting column widths. '''
        print('test_TableFit')

        # Create test view.
        view = sublime.View(600)
        view.insert(None, 0, self.test_text_str)

        # Mock view selection.
        sel = sublime.Selection(view.id())
        sel.add(sublime.Region(73, 77)) # somewhere in table
        view.sel = MagicMock(return_value=sel)

        # Mock scope interrogation.
        def scope_name(*args, **kwargs):
            rc = view.rowcol(args[0])
            if rc[0] == 5:
                return 'text.notr meta.table.header'
            elif rc[0] >= 6 and rc[0] <= 11:
                return 'text.notr meta.table'
            else:
                return 'text.notr'
        view.scope_name = MagicMock(side_effect=scope_name)

        # Run the command.
        cmd = table.TableFitCommand(view)
        cmd.run(None)

        # Should look like this now.
        text_out = '\n'.join([
            '| State | Size | Color  |',
            '| ME    | 34   | Red    |',
            '| IA    | 31   | Blue   |',
            '| CO    | 15   | Brown  |',
            '| NY    | 4    | Yellow |',
            '| TX    | 2    | Green  |',
            '| WY    | 45   | White  |',
            ''
            ])

        reg = cmd.get_table_region()
        newtext = view.substr(reg)
        self.assertEqual(newtext, text_out)


    #@unittest.skip
    def test_TableSortByCol(self):
        ''' TableSortByColCommand. '''

        # Create test view.
        view = sublime.View(601)
        view.insert(None, 0, self.test_text_str)

        # Run the command.
        cmd = table.TableSortByColCommand(view)
        cmd.run(None)


    @unittest.skip
    def test_TableInsertCol(self):
        ''' TableInsertColCommand. '''

        # Create test view.
        view = sublime.View(602)
        view.insert(None, 0, self.test_text_str)

        # Run the command.
        cmd = table.TableInsertColCommand(view)
        cmd.run(None)


    @unittest.skip
    def test_TableDeleteCol(self):
        ''' TableDeleteColCommand. '''

        # Create test view.
        view = sublime.View(603)
        view.insert(None, 0, self.test_text_str)

        # Run the command.
        cmd = table.TableDeleteColCommand(view)
        cmd.run(None)


    @unittest.skip
    def test_TableSelectCol(self):
        ''' TableSelectColCommand. '''

        # Create test view.
        view = sublime.View(604)
        view.insert(None, 0, self.test_text_str)

        # Run the command.
        cmd = table.TableSelectColCommand(view)
        cmd.run(None)


    #------------------------ notr ------------------------------------

    @unittest.skip
    def test_GotoRef(self):
        view = sublime.View(701)
        cmd = notr.NotrGotoRefCommand(view)
        cmd.run(None)


    @unittest.skip
    def test_GotoSection(self):
        view = sublime.View(702)
        cmd = notr.NotrGotoSectionCommand(view)
        cmd.run(None)


    @unittest.skip
    def test_InsertRef(self):
        view = sublime.View(703)
        cmd = notr.NotrInsertRefCommand(view)
        cmd.run(None)


#-----------------------------------------------------------------------------------
if __name__ == '__main__':
    print('__main__')
    unittest.main()
    print('__main__2')
