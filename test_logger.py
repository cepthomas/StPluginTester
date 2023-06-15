import sys
import traceback
import unittest
from unittest.mock import MagicMock
import sublime
import sublime_plugin
import sbot_common as sc

from SbotALogger import sbot_logger


#-----------------------------------------------------------------------------------
class TestLogger(unittest.TestCase):

    def setUp(self):
        mock_settings = {
            "file_size": 5,
            "notify_cats": ["EXC", "ERR", "WRN"],
            "ignore_cats": [],
        }
        sublime.load_settings = MagicMock(return_value=mock_settings)
        sbot_logger.plugin_loaded()

    def tearDown(self):
        sbot_logger.plugin_unloaded()
        pass

    def test_log_exception(self):
        # Force an unhandled exception.
        def _force_exc():
            i = 222 / 0

        try:
            _force_exc()
        except Exception as e:
            sbot_logger._notify_exception(e, 'value', e.__traceback__)

    def test_simple(self):
        # Do the test.
        sc.slog('TST', 'dsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsds')


#-----------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
