
cls

echo off

set ST_PACKAGES_PATH=%APPDATA%\Sublime Text\Packages

set PYTHONPATH=%PYTHONPATH%;%ST_PACKAGES_PATH%\Notr;%ST_PACKAGES_PATH%\SbotDev\st_emul

rem set 

python run.py
