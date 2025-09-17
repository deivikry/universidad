@echo off
estamos realizando una copia
set origen=c:\ejercicio\*.*
set destino=c:\backups
pause
cd /
md backups
xcopy "%origen%" "%destino%" /y
tree c:\backups
dir c:\backups