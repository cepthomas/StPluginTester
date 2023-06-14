
import sys
import os
import json
import unittest
from unittest.mock import MagicMock
import sublime
import sublime_plugin

# Tests for the sublime api emulation non-trivial parts.


#-----------------------------------------------------------------------------------
class TestStEmul(unittest.TestCase):
    ''' Test the sublime api emulation. '''

    _settings_file = os.path.join(sublime.packages_path(), 'StPluginTester', 'files', 'test_settings.sublime-settings')
    _test_file1 = os.path.join(sublime.packages_path(), 'StPluginTester', 'files', 'ross.txt')
    _test_file2 = os.path.join(sublime.packages_path(), 'StPluginTester', 'files', 'messy.cs')

    def setUp(self):
        sublime._reset()

    def tearDown(self):
        pass

    #@unittest.skip
    def test_module(self):
        ''' sublime.module '''

        settings = sublime.load_settings(self._settings_file)
        self.assertEqual(len(settings), 3)

        sublime.set_clipboard('we need a little path')
        self.assertEqual(sublime.get_clipboard(), 'we need a little path')

        sublime.set_timeout(lambda: settings.set('a_null', None), 100)
        self.assertEqual(len(settings), 4)

        ## Not implemented.
        #view = sublime.View(-1)
        #self.assertRaises(NotImplementedError, view.run_command, 'a_command')


    #@unittest.skip
    def test_window(self):
        ''' sublime.Window() '''

        settings = sublime.load_settings(self._settings_file)

        # Make a window.
        window = sublime.Window(202)
        self.assertTrue(window.is_valid())
        self.assertEqual(len(window.settings()), 3)

        # Add some views.
        view1 = window.open_file(self._test_file1)
        view2 = window.new_file()
        view3 = window.open_file(self._test_file2)
        view4 = window.new_file()

        self.assertEqual(len(window.views()), 4)
        self.assertEqual(window.views()[0], view1)
        self.assertEqual(window.views()[3], view4)
        self.assertEqual(window.find_open_file(self._test_file2), view3)
        self.assertIsNone(window.find_open_file('Invalid filename'))
        self.assertEqual(window.get_view_index(view4), 3)

        ## Not implemented.
        #self.assertRaises(NotImplementedError, window.focus_view, view1)
        #self.assertRaises(NotImplementedError, window.run_command, 'a_command')


    #@unittest.skip
    def test_view(self):
        ''' sublime.View() '''
        window = sublime.Window(303)

        view1 = window.open_file(self._test_file1)
        view2 = window.new_file()
        view3 = window.open_file(self._test_file2)
        view4 = window.new_file()

        self.assertTrue(view1 == view1) # __eq__
        self.assertFalse(view2 == view3)

        self.assertEqual(len(view1), 1583) # __len__
        self.assertEqual(view1.size(), 1583)
        self.assertEqual(view1.id(), 1)
        self.assertTrue(view1) # __bool__
        self.assertEqual(view1.window(), window)
        self.assertEqual(view1.file_name(), self._test_file1)

        self.assertEqual(len(view2), 0)
        self.assertEqual(view2.size(), 0)
        self.assertEqual(view2.id(), 2)
        self.assertEqual(view2.window(), window)
        self.assertEqual(view2.file_name(), '')

        self.assertEqual(len(view3), 1327)
        self.assertEqual(view3.size(), 1327)
        self.assertEqual(view3.id(), 3)
        self.assertEqual(view3.window(), window)
        self.assertEqual(view3.file_name(), self._test_file2)

        self.assertEqual(len(view4), 0)
        self.assertEqual(view4.size(), 0)
        self.assertEqual(view4.id(), 4)
        self.assertEqual(view4.window(), window)
        self.assertEqual(view4.file_name(), '')

        # rowcol()
        self.assertEqual(view1.rowcol(0), (0, 0))
        self.assertEqual(view1.rowcol(100), (2, 57))
        self.assertEqual(view1.rowcol(1000), (13, 47))
        self.assertEqual(view1.rowcol(1582), (22, 94))
        self.assertEqual(view1.rowcol(1583), (22, 95))
        #self.assertRaises(ValueError, view1.rowcol, 1584)

        # text_point()
        self.assertEqual(view1.text_point(0, 0), 0)
        self.assertEqual(view1.text_point(8, 29), 666)
        self.assertEqual(view1.text_point(20, 46), 1466)
        #self.assertRaises(ValueError, view1.text_point, 23456, 34)

        # utilities
        lines = view1.split_by_newlines(sublime.Region(309, 1075))
        self.assertEqual(len(lines), 12)
        self.assertTrue(lines[0].startswith('I don\'t'))
        self.assertTrue(lines[11].endswith('the wo'))

        # find
        ss = view1.substr(17)
        self.assertEqual(ss, ':')
        ss = view1.substr(sublime.Region(373, 394))
        self.assertEqual(ss, 'ake these big decisio')

        reg = view1.word(0)
        self.assertEqual(view1.substr(reg), 'line-1')
        reg = view1.word(913)
        self.assertEqual(view1.substr(reg), 'fairytale')
        reg = view1.word(sublime.Region(1125, 1137))
        self.assertEqual(view1.substr(reg), 'everything can be happy.')
        reg = view1.word(sublime.Region(699, 720)) # has line end in middle
        self.assertEqual(view1.substr(reg), 'in the world.\nI like to')

        reg = view1.line(1140)
        self.assertEqual(view1.substr(reg), 'In this world, everything can be happy. If you hypnotize it, it will go away.')
        reg = view1.line(sublime.Region(1186, 1193))
        self.assertEqual(view1.substr(reg), 'Let your heart be your guide.')

        reg = view1.full_line(1194)
        self.assertEqual(view1.substr(reg), 'Let your heart be your guide.\n')
        reg = view1.full_line(sublime.Region(455, 470))
        self.assertEqual(view1.substr(reg), 'Don\'t hurry. Take your time and enjoy.\n')

        reg = view1.find('it really just happens', 100)
        self.assertIsNotNone(reg)
        self.assertEqual(view1.substr(reg), 'it really just happens')
        reg = view1.find('this is no good', 0)
        self.assertIsNone(reg)

        regs = view1.find_all('have')
        self.assertIsNotNone(regs)
        self.assertEqual(len(regs), 4)
        self.assertEqual(view1.substr(regs[1]), 'have')

        # edit
        num = view1.insert(None, 753, 'zzzzzzzzzz')
        self.assertEqual(num, 10)
        self.assertEqual(len(view1), 1593)

        num = view1.replace(None, sublime.Region(245, 265), '-----')
        self.assertEqual(num, 5)
        self.assertEqual(len(view1), 1578)

        # Not implemented. So far.
        #view = sublime.View(-1)
        #self.assertRaises(NotImplementedError, view.sel)
        #self.assertRaises(NotImplementedError, view.syntax)
        #self.assertRaises(NotImplementedError, view.scope_name, 0)
        #self.assertRaises(NotImplementedError, view.style_for_scope, '')
        #self.assertRaises(NotImplementedError, view.add_regions, '', []) #, scope="", icon="", flags=0)
        #self.assertRaises(NotImplementedError, view.get_regions, '')
        #self.assertRaises(NotImplementedError, view.erase_regions, '')
        #self.assertRaises(NotImplementedError, view.run_command, '')


#-----------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
