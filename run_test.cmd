
rem Run unit tests from the command line.

cls
echo off

rem Env stuff.
set ST_PACKAGES_PATH=%APPDATA%\Sublime Text\Packages
set PYTHONPATH=%ST_PACKAGES_PATH%\Notr;%ST_PACKAGES_PATH%\StPluginTester\st_emul
echo %PYTHONPATH%

rem Different ways of executing:::



rem Direct - requires that test_* have if __name__ == '__main__':     unittest.main()
python test_notr.py



rem Run explicit tests specified in script.
python run_test.py



rem pause
