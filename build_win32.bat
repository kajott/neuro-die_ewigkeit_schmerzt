cd /d "%~dp0"
rmdir /s /q dist
py -2 -m PyInstaller --noconfirm --onedir --console ^
    --exclude-module Tkinter ^
    --exclude-module OpenGL.arrays.numpymodule ^
    demo.py
if errorlevel 1 exit /b 1

rmdir /s /q dist\demo\Include

copy /b *.py dist\demo
copy /b *.dll dist\demo

mkdir dist\demo\lib
mkdir dist\demo\lib\nedu
copy /b lib\nedu\*.py dist\demo\lib\nedu\

mkdir dist\demo\lib\nedu\res
copy /b lib\nedu\res\* dist\demo\lib\nedu\res\

mkdir dist\demo\res
copy /b res\* dist\demo\res\

mkdir dist\demo\res\shaders
copy /b res\shaders\* dist\demo\res\shaders\

copy special\*.bat dist\
copy special\*.sh dist\
copy README dist\README.txt

cd dist
zip -rv9 ..\neuro-die_ewigkeit_schmerzt-2022update.zip .
cd ..
