@echo vamos a realizar un arbol de carpetas, en donde vamos a copiar algunos archivos.
@echo off

md Latam
cd Latam
md colombia brasil argentina

cd colombia
md tolima atlantico valle
cd tolima
type nul>ibague.txt
type nul>venadillo.txt
cd..
cd atlantico
type nul>barranquilla.txt
cd..
cd valle
type nul>cali.txt
cd..
cd..

cd brasil
md brasilia amazonas
cd..
cd argentina
md bolivar bragado
cd..



set tolima=c:\latambat\latam\colombia\tolima\ibague.txt
set atlantic=c:\latambat\latam\colombia\atlantico\barranquilla.txt
set bras=c:\latambat\latam\brasil\brasilia\*.*
set argentina=c:\latambat\latam\argentina\bragado\

pause

@echo  realizando procesos
@echo off
pause


cd /
xcopy "%tolima%" "%bras%" /y
xcopy "%atlantic%" "%bras%" /y
xcopy "%bras%" "%argentina%" /y


attrib +h +r "%tolima%"
attrib +h +r "c:\latambat\latam\brasil\brasilia\ibague.txt"
attrib +h +r "c:\latambat\latam\argentina\bragado\ibague.txt"

pause


tree c:\latam
dir c:\latam
