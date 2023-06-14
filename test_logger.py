import sys
import traceback
import unittest
from unittest.mock import MagicMock
import sublime
import sublime_plugin
from SbotALogger import sbot_logger as slogger
from SbotALogger import sbot_common as sc


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
        def _force_exc():
            i = 222 / 0

        try:
            _force_exc()
        except Exception as e:
            slogger._notify_exception(e, 'value', e.__traceback__)

    def test_simple(self):
        # Do the test.
        sc.slog('TST', 'dsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsds')


#-----------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
