@echo vamos a realizar un arbol de carpetas, en donde vamos a copiar algunos archivos.
@echo off
pause
@echo creando carpetas estilo arbol
pause
md directorio_principal
cd directorio_principal

md documentos imagenes programas archivos_temporales

cd documentos
md informes propuestas cartas
cd informes
md 2023 2024
cd..
cd propuestas
type nul>sitioweb.txt
cd..
cd..
cd imagenes 
md vacaciones trabajo personales
cd..
cd programas 
md python  java javascript
cd javascript
type nul>react.txt 
type nul>angular.txt 
type nul>vue.txt
cd..
cd..
cd..

@echo copiando a angular a directorio cartas

set angularr=c:\parcial\directorio_principal\programas\javascript\angular.txt 
set carts=c:\parcial\directorio_principal\documentos\cartas\

@echo moviendo react a directorio personales

set reactt=c:\parcial\directorio_principal\programas\javascript\react.txt 
set personales=c:\parcial\directorio_principal\imagenes\personales\


pause

@echo  realizando procesos
@echo off
pause

copy "%angularr%" "%carts%"
move "%reactt%" "%personales%"


attrib +h "c:\parcial\directorio_principal\programas\javascript\vue.txt"
pause

tree c:\directorio_principal
dir c:\directorio_principal







