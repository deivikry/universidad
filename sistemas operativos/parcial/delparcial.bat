@echo vamos a eliminar el arbol y algunos archivos.
@echo off
pause
cd directorio_principal

cd documentos
cd cartas
del angular.txt
cd..

cd informes
rd 2024 2023
cd..
cd propuestas
del sitioweb.txt
cd..
rd propuestas informes cartas
cd..
cd imagenes 
cd personales
del react.txt
cd..
rd vacaciones trabajo personales
cd..
cd programas 
cd javascript
del angular.txt
attrib -h "vue.txt"
del vue.txt
cd..
rd python  java javascript


cd..
rd documentos imagenes programas archivos_temporales
cd..
rd directorio_principal 
cd..
@echo  realizando procesos de eliminacion de subcarpetas
pause
@echo  realizando proceso de eliminacion carpeta principal
pause
@echo  COMPLETADO
@echo off
pause

