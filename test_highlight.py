import sys
import traceback
import unittest
from unittest.mock import MagicMock
import sublime
import sublime_plugin

from SbotHighlight import sbot_highlight


#-----------------------------------------------------------------------------------
class TestHighlight(unittest.TestCase):

    def setUp(self):
        mock_settings = {
            # List of up to 6 scope names for highlight commands.
            "highlight_scopes": [ "region.redish", "region.yellowish", "region.greenish", "region.cyanish", "region.bluish", "region.purplish" ],
        }
        sublime.load_settings = MagicMock(return_value=mock_settings)

    def tearDown(self):
        pass

    def test_simple(self):
        window = sublime.Window(900)
        view = sublime.View(901)

        view._window = MagicMock(return_value=window)
        view.file_name = MagicMock(return_value='file123.abc')

        # Do the test.
        hl_vals = sbot_highlight._get_hl_vals(view, True)
        self.assertIsNotNone(hl_vals)


#-----------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
