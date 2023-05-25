
rem Run unit tests from the command line.

cls
echo off

rem Env stuff.
set ST_PACKAGES_PATH=%APPDATA%\Sublime Text\Packages
rem set PYTHONPATH=%APPDATA%\Sublime Text\Packages;%APPDATA%\Sublime Text\Packages\StPluginTester\st_emul
echo %PYTHONPATH%

rem Different ways of executing:::

rem Direct - requires that test_* have if __name__ == '__main__':     unittest.main()
python test_notr.py

rem Run explicit tests specified in script - like cycler. Doesn't require if __name__ == '__main__':
python run_test.py

rem pause
