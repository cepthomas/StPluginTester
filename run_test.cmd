
:: Run unit tests from the command line.

cls
echo off

:: Set up environment.
set ST_PACKAGES_PATH=%APPDATA%\Sublime Text\Packages
:: set PYTHONPATH=%ST_PACKAGES_PATH%;%ST_PACKAGES_PATH%\StPluginTester
set PYTHONPATH=%ST_PACKAGES_PATH%
:: echo %PYTHONPATH%

:: Two options for running tests:
:: 1) Direct execution of all tests in a suite.
python test_notr.py
:: 2) Run tests explicitly specified in a script.
python run_test.py

:: pause
