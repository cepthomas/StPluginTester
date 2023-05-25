
import sys
import os
import unittest
from unittest.mock import MagicMock
import sublime
import sublime_plugin



#PYTHONPATH=$(APPDATA)\Sublime Text\Packages;$(APPDATA)\Sublime Text\Packages\StPluginTester\st_emul

# This supports VS intellisense but doesn't run in VS or cli.
#from ..Notr import notr

# vice versa.
from Notr import notr


## Returns `None` if the key doesn't exist
#print(os.environ.get('KEY_THAT_MIGHT_EXIST'))
## Returns `default_value` if the key doesn't exist
#print(os.environ.get('KEY_THAT_MIGHT_EXIST', default_value))
## Returns `default_value` if the key doesn't exist
#print(os.getenv('KEY_THAT_MIGHT_EXIST', default_value))


print('sys.path:::')
print(sys.path)

print('os.environ:::')
print(os.environ)

#-----------------------------------------------------------------------------------
class TestNotr(unittest.TestCase):

    view = None

    def setUp(self):
        # Mock settings.
        mock_settings = {
            "notr_paths": ["C:\\Users\\cepth\\AppData\\Roaming\\Sublime Text\\Packages\\Notr\\files"],
            "visual_line_length": 100,
            "user_hl": [["2DO", "things"], ["user"], ["dynamic"], ["and_a"], ["and_b"], ["and_c"]],
            "user_hl_whole_word": True,
        }
        sublime.load_settings = MagicMock(return_value = mock_settings)

        # Init internals.
        self.view = sublime.View(600)
        sel = sublime.Selection(self.view.id())
        sel.add(sublime.Region(10, 20, 101))
        self.view.sel = MagicMock(return_value = sel)

        # Mock syntax.
        syntax = sublime.Syntax()
        syntax.name = MagicMock(return_value = 'Notr')
        self.view.syntax = MagicMock(return_value = syntax)

    def tearDown(self):
        pass

    def test_init(self):

        # slog('ooo', 'test_init()')
        evt = notr.NotrEvent()
        evt.on_init([self.view])

        self.assertEqual(len(notr._tags), 7)
        self.assertEqual(len(notr._links), 6)
        self.assertEqual(len(notr._refs), 8)
        self.assertEqual(len(notr._sections), 13)

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
