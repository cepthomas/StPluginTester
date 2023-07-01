
:: Run unit tests from the command line.

cls
echo off

:: Set up environment.
set STPKGSPATH=%APPDATA%\Sublime Text\Packages
set PYTHONPATH=%STPKGSPATH%
set TSTRPATH=C:\Dev\repos\StPluginTester

rem echo %TSTRPATH%\test_notr.py

:: Two options for running tests:
:: 1) Direct execution of all tests in a suite.
rem python %TSTRPATH%\test_tester.py
rem python %TSTRPATH%\test_format.py
rem python %TSTRPATH%\test_highlight.py
rem python %TSTRPATH%\test_logger.py
rem python %TSTRPATH%\test_notr.py
python %TSTRPATH%\test_table.py

:: 2) Run tests explicitly specified in a script. Like:
::# Explicitly run specific tests. Requires PYTHONPATH to be set as in run_test.cmd.
::runner = unittest.TextTestRunner()
::runner.verbosity = 2
::runner.run(test_tester.TestStEmul('test_module'))

pause
