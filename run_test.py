import os
import sys
import unittest

# from tests import data_logger_tests
import test_notr


### Run specific tests.
runner = unittest.TextTestRunner()
runner.verbosity = 2
try:
   runner.run(test_notr.TestNotr('test_init'))
except Exception as e:
   print(e)


