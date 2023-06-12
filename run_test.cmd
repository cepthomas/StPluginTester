
:: Run unit tests from the command line.

cls
echo off

:: Set up environment.
set ST_PACKAGES_PATH=%APPDATA%\Sublime Text\Packages
set PYTHONPATH=%ST_PACKAGES_PATH%
:: echo %PYTHONPATH%

:: Two options for running tests:
:: 1) Direct execution of all tests in a suite.
python test_tester.py

:: 2) Run tests explicitly specified in a script. Like:
::# Explicitly run specific tests. Requires PYTHONPATH to be set as in run_test.cmd.
::runner = unittest.TextTestRunner()
::runner.verbosity = 2
::runner.run(test_tester.TestStEmul('test_module'))

:: pause
