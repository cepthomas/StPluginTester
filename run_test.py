import os
import sys
import unittest

import test_notr

# print('sys.path:::')
# print(sys.path)

# Explicitly run specific tests. Requires PYTHONPATH to be set as in run_test.cmd.
runner = unittest.TextTestRunner()
runner.verbosity = 2

runner.run(test_notr.TestNotr('test_init'))
