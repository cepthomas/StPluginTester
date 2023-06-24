
import sys
import os
import unittest
from unittest.mock import MagicMock
import sublime
import sublime_plugin

from Notr import notr, table


#-----------------------------------------------------------------------------------
class TestNotr(unittest.TestCase):

    # view = None

    test_text = '\n'.join([
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
        ])


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

        view = sublime.View(500)
        view.insert(None, 0, self.test_text)

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

        view = sublime.View(600)
        view.insert(None, 0, self.test_text)

        sel = sublime.Selection(view.id())
        sel.add(sublime.Region(73, 77)) # in table
        view.sel = MagicMock(return_value=sel)

        hdr_pos = (50, 77)
        body_pos = (78, 239)
        def scope_name(*args, **kwargs):
            pos = args[0]
            if pos >= hdr_pos[0] and pos <= hdr_pos[1]:
                return 'text.notr meta.table.header'
            elif pos >= body_pos[0] and pos <= body_pos[1]:
                return 'text.notr meta.table'
            else:
                return 'text.notr'
            pass

        view.scope_name = MagicMock(side_effect=scope_name)

        cmd = table.TableFitCommand(view)
        cmd.run(None)

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

        hdr_pos = (50, 75)
        body_pos = (76, 231)
        reg = cmd.get_table_region()
        newtext = view.substr(reg)
        self.assertEqual(newtext, text_out)


    # @unittest.skip
    def test_TableSortByCol(self):
        ''' TableSortByColCommand. '''

        view = sublime.View(601)
        view.insert(None, 0, self.test_text)

        cmd = table.TableSortByColCommand(view)
        cmd.run(None)



    @unittest.skip
    def test_TableInsertCol(self):
        ''' TableInsertColCommand. '''

        view = sublime.View(602)
        view.insert(None, 0, self.test_text)

        cmd = table.TableInsertColCommand(view)
        cmd.run(None)



    @unittest.skip
    def test_TableDeleteCol(self):
        ''' TableDeleteColCommand. '''

        view = sublime.View(603)
        view.insert(None, 0, self.test_text)

        cmd = table.TableDeleteColCommand(view)
        cmd.run(None)



    @unittest.skip
    def test_TableSelectCol(self):
        ''' TableSelectColCommand. '''

        view = sublime.View(604)
        view.insert(None, 0, self.test_text)

        cmd = table.TableSelectColCommand(view)
        cmd.run(None)


    #------------------------ notr ------------------------------------

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
