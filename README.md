# Modak web Front QA
Pruebas de front básico (UI)

## Requisitos
 - python >= 3.8
 - git Bash
 - Pycharm IDE
 - Crear un entorno virtual donde se instalarán las dependencias desde Pycharm
 - Instalar las dependencias del proyecto: `pip install -r requirements.txt`
 - Para actualizar las dependencias: `pip install -r requirements.txt -I`
 - Usuario de GITHUB con permisos
 
 

## Instalación
 - Instalar git bash para hacer uso de git
 - Instalar Pycharm desde el sitio oficial
 - Clonarse el repositorio `git clone https://github.com/oneksson/modakChallenge.git`.
 - Crear el ambiente virtual ejecutando: `python -m venv env`.
 - Activar su entorno virtual dentro de su proyecto `source env/bin/activate`.
 - Luego de instalar python y pip en caso de no tenerlo instalado, proceder a instalar las dependencias del proyecto dentro de su entorno virtual: `pip instasll -r requirements.txt`.
 - Instalar Pycharm y abrir el proyecto.
 - Activar el entorno virtual desde el IDE de Pycharm (esquina inferior derecha)
 

## Uso

Para correr los tests ejecute en la terminal el siguiente comando:
```sh
pytest -k test 
```

O ejecute mediante el IDE.
