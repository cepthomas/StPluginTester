
import sys
import os
import json
import unittest
from unittest.mock import MagicMock

import sublime
import sublime_plugin

# Tests for the sublime api emulation.


#-----------------------------------------------------------------------------------
class TestEmul(unittest.TestCase):

    view = None

    def setUp(self):
        pass

    def tearDown(self):
        pass

    #@unittest.skip
    def test_basic(self):

        settings_file = os.path.join(sublime.packages_path(), 'StPluginTester', 'files', 'test_settings.sublime-settings')
        test_file1 = os.path.join(sublime.packages_path(), 'StPluginTester', 'files', 'ross.txt')
        test_file2 = os.path.join(sublime.packages_path(), 'StPluginTester', 'files', '5denselines.txt')

        #jt = { 'v1': 111, 'v2': 'popo'}
        #s = json.dumps(jt)

        ##### sublime.module
        # self.assertEqual(sublime.packages_path(), 'aaaa')

        settings = sublime.load_settings(settings_file)
        self.assertEqual(len(settings), 3)

        sublime.set_clipboard('we need a little path')
        #clip = sublime.get_clipboard()
        self.assertEqual(sublime.get_clipboard(), 'we need a little path')

        sublime.set_timeout(lambda: settings.set('a_null', None))
        self.assertEqual(len(settings), 4)

        # TODO sublime.run_command(cmd, args=None):


        ##### sublime.Window
        # Make a window.
        window = sublime.Window(202)
        self.assertTrue(window.is_valid())
        self.assertEqual(len(window.settings()), 4)

        # Add some views.
        view1 = window.open_file(test_file1)
        view2 = window.new_file()
        view3 = window.open_file(test_file2)
        view4 = window.new_file()

        self.assertEqual(len(window.views()), 4)
        self.assertEqual(window.views()[0], view1)
        self.assertEqual(window.views()[3], view4)
        self.assertEqual(window.find_open_file(test_file2), view3)
        self.assertIsNone(window.find_open_file('Invalid filename'))
        self.assertEqual(window.get_view_index(view4), 3)

        # TODO focus_view(self, view):
        # TODO run_command(self, cmd, args=None):


        ##### sublime.View
        # view1 ross.txt 1583 chars total
        # 745 word unplanned
        # 1190 line Let your heart be your guide.
        # 440 line start Don't hurry. Take your time and enjoy.
        # view3 1052 chars

        self.assertTrue(view1 == view1)
        self.assertFalse(view2 == view3)

        self.assertEqual(len(view1), 1583)
        self.assertEqual(view1.size(), 1583)
        self.assertEqual(view1.id(), 1)
        self.assertTrue(view1)
        self.assertEqual(view1.window(), window)
        self.assertEqual(view1.file_name(), test_file1)

        self.assertEqual(len(view2), 0)
        self.assertEqual(view2.size(), 0)
        self.assertEqual(view2.id(), 2)
        self.assertEqual(view2.window(), window)
        self.assertEqual(view2.file_name(), '')

        self.assertEqual(len(view3), 1052)
        self.assertEqual(view3.size(), 1052)
        self.assertEqual(view3.id(), 3)
        self.assertEqual(view3.window(), window)
        self.assertEqual(view3.file_name(), test_file2)

        self.assertEqual(len(view4), 0)
        self.assertEqual(view4.size(), 0)
        self.assertEqual(view4.id(), 4)
        self.assertEqual(view4.window(), window)
        self.assertEqual(view4.file_name(), '')


        self.assertEqual(view1.rowcol(0), (0, 0))
        self.assertEqual(view1.rowcol(100), (2, 63))
        self.assertEqual(view1.rowcol(1000), (13, 47))
        self.assertEqual(view1.rowcol(1582), (22, 94))
        self.assertEqual(view1.rowcol(1583), (22, 95))
        #self.assertEqual(view1.rowcol(1584), (22, 96))
        # self.assertRaises(view1.rowcol(1581), (5, 5))
        self.assertRaises(ValueError, view1.rowcol, 1584)

        self.assertEqual(view1.text_point(0, 0), 0)
        self.assertEqual(view1.text_point(8, 29), 666)
        self.assertEqual(view1.text_point(20, 46), 1466)
        self.assertRaises(ValueError, view1.text_point, 23456, 34)


        # def insert(self, edit, point, text):
        # def replace(self, edit, region, text):
        # def split_by_newlines(self, region):
        # def find(self, pattern, start_pt, flags=0):
        # def find_all(self, pattern, flags=0, fmt=None, extractions=None):
        # def substr(self, x):
        # def word(self, x):
        # def line(self, x):
        # def full_line(self, x):
        # def sel(self):

        # TODO
        # def run_command(self, cmd, args=None):
        # def syntax(self):
        # def scope_name(self, point):
        # def style_for_scope(self, scope):
        # def add_regions(self, key, regions, scope="", icon="", flags=0):
        # def get_regions(self, key):
        # def erase_regions(self, key):


#-----------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
