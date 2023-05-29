import sys
import traceback
import unittest
from unittest.mock import MagicMock
import sublime
import sublime_plugin
from SbotHighlight import sbot_highlight as hl
from SbotALogger import sbot_logger as slogger
from SbotALogger import sbot_common as sc

# Debugging of odds and ends that don't warrant their own file.


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

        view.window = MagicMock(return_value=window)
        view.file_name = MagicMock(return_value='file123.abc')

        # Do the test.
        hl_vals = hl._get_hl_vals(view, True)
        self.assertIsNotNone(hl_vals)


#-----------------------------------------------------------------------------------
class TestLogger(unittest.TestCase):

    def setUp(self):
        mock_settings = {
            "file_size": 5,
            "notify_cats": ["EXC", "ERR", "WRN"],
            "ignore_cats": [],
        }
        sublime.load_settings = MagicMock(return_value=mock_settings)
        slogger.plugin_loaded()

    def tearDown(self):
        slogger.plugin_unloaded()
        pass

    def test_log_exception(self):
        # Force an unhandled exception.
        def _force_exc(self):
            i = 222 / 0

        try:
            self._force_exc()
        except Exception as e:
            slogger._notify_exception(e, 'value', e.__traceback__)

    def test_simple(self):
        # Do the test.
        sc.slog('TST', 'dsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsds')


#-----------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
