import os
import sys
import unittest

# cycler: from tests import data_logger_tests
import test_notr


### Run specific tests.
runner = unittest.TextTestRunner()
runner.verbosity = 2

runner.run(test_notr.TestNotr('test_init'))

