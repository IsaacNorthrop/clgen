@echo off
cls
echo Welcome to clgen!
pause
:loop
python3 pdftest.py
set /P option=Do you want to generate another letter [y/n]? 
if %option%==y goto loop else goto end
:end
echo Thank you for using clgen!
pause


