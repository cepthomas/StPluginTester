
import sys
import os
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
    def test_123(self):

        settings_file = os.path.join(sublime.packages_path(), 'StPluginTester', 'files', 'test_settings.sublime-settings')
        test_file1 = os.path.join(sublime.packages_path(), 'StPluginTester', 'files', 'ross.txt')
        test_file2 = os.path.join(sublime.packages_path(), 'StPluginTester', 'files', '5denselines.txt')

# sublime. :
# def packages_path():
# def set_clipboard(text):
# def get_clipboard():
# def set_timeout(f, timeout_ms=0):
# TODO:    
# def run_command(cmd, args=None):
        sublime.load_settings(settings_file)

        window = sublime.Window(202)
        view1 = window.open_file(test_file1)
        view2 = window.new_file()
        view3 = window.open_file(test_file2)
        view4 = window.new_file()

        self.assertEqual(len(view1), 7)
        self.assertEqual(view1.size(), 7)
        self.assertEqual(view1.id(), 7)
        self.assertTrue(view1)
        self.assertEqual(view1.window(), window)
        self.assertEqual(view1.file_name(), 'aaaa')

        self.assertEqual(len(view2), 7)
        self.assertEqual(view2.size(), 7)
        self.assertEqual(view2.id(), 7)
        self.assertEqual(view2.window(), window)
        self.assertEqual(view2.file_name(), 'aaaa')

        self.assertEqual(len(view3), 7)
        self.assertEqual(view3.size(), 7)
        self.assertEqual(view3.id(), 7)
        self.assertEqual(view3.window(), window)
        self.assertEqual(view3.file_name(), 'aaaa')

        self.assertEqual(len(view4), 7)
        self.assertEqual(view4.size(), 7)
        self.assertEqual(view4.id(), 7)
        self.assertEqual(view4.window(), window)
        self.assertEqual(view4.file_name(), 'aaaa')


# sublime.View:
#     def __eq__(self, other):
#     def settings(self):
#     def sel(self):
#     def rowcol(self, point):
#     def text_point(self, row, col):
#     def insert(self, edit, point, text):
#     def replace(self, edit, region, text):
#     def split_by_newlines(self, region):
#     def find(self, pattern, start_pt, flags=0):
#     def find_all(self, pattern, flags=0, fmt=None, extractions=None):
#     def substr(self, x):
#     def word(self, x):
#     def line(self, x):
#     def full_line(self, x):
# TODO:
#     def run_command(self, cmd, args=None):
#     def syntax(self):
#     def scope_name(self, point):
#     def style_for_scope(self, scope):
#     def add_regions(self, key, regions, scope="", icon="", flags=0):
#     def get_regions(self, key):
#     def erase_regions(self, key):
#
# 745 word unplanned
# 1190 line Let your heart be your guide.
# 440 line start Don't hurry. Take your time and enjoy.



# sublime.Window:
    # def settings(self):
    # def new_file(self, flags=0, syntax=""):
    # def open_file(self, fname, flags=0, group=-1):
    # def find_open_file(self, fname):
    # def focus_view(self, view):
    # def get_view_index(self, view):
    # def views(self):
# TODO:
    # def run_command(self, cmd, args=None):



#-----------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
