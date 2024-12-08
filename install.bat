@echo off
setlocal

REM Define the target directory (ensure it's consistent with where you want the scripts)
set "TARGET_DIR=%USERPROFILE%\Scripts"

REM Create the target directory if it doesn't exist
if not exist "%TARGET_DIR%" (
    mkdir "%TARGET_DIR%"
)

REM Copy the brainrot.py script to the target directory
xcopy /Y /I "brainrot.py" "%TARGET_DIR%\brainrot.py"

REM Copy the commands directory to the target directory
xcopy /E /I /Y "commands" "%TARGET_DIR%\commands"

REM Create a wrapper batch file to run the Python script
(
    echo @echo off
    echo python "%~dp0brainrot.py" %%*
) > "%TARGET_DIR%\brainrot.bat"

REM Check if the target directory is in the PATH
echo %PATH% | find /I "%TARGET_DIR%" >nul
if errorlevel 1 (
    REM Add the target directory to the PATH for the current user
    setx PATH "%PATH%;%TARGET_DIR%"
    echo Added %TARGET_DIR% to PATH. You may need to restart your command prompt.
) else (
    echo %TARGET_DIR% is already in PATH
)

echo Installation complete. You can now run 'brainrot' from anywhere.
endlocal
pause