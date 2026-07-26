@echo off

set esc=
set "CMD=py Password_Generator.py"

echo Generating Password...
timeout /t 3
echo.
echo.
echo %esc%[32mPassword Generated Successfully!%esc%[0m
echo Password is saved in Password.txt
echo AlphaNumeric Password:
echo.
%CMD%
echo.

pause