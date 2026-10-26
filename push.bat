@echo off
set "PATH=C:\Users\BRIJESH\AppData\Local\Programs\MinGit\cmd;C:\Users\BRIJESH\AppData\Local\Programs\MinGit\mingw64\bin;C:\Users\BRIJESH\AppData\Local\Programs\MinGit\usr\bin;%PATH%"
cd /d "e:\Venom\telepulse-360"
echo ====================================================
echo Pushing TELEPULSE 360 to GitHub...
echo ====================================================
git push -u origin main
echo ====================================================
pause
