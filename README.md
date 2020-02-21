# Compliance continuo de servidores
![technology Python](https://img.shields.io/badge/technology-python-blue.svg)

Aplicación para obtener y centralizar información de los servidores que se encuentran en la nube.


## Estructura del proyecto

* ```/Agente```: Contiene un script que se ejecuta en los servidores y envía información de estos a la API.
* ```/API```: Contiene el script inicializador y los archivos de configuración de la aplicación junto con los controllers/routers inherentes a la API.
* ```/CreateDB```: Contiene el script de creación de la base de datos normalizada.


## Funcionamiento

El programa agente obtiene información del servidor y la envía a la API. La información obtenida consta de los siguientes datos: arquitectura y marca del procesador, nombre y versión del sistema operativo, un listado de los procesos que están corriendo (nombre del proceso, id del proceso y usuario que lo ejecuta), listado de usuarios con una sesión abierta en el sistema (id del proceso y nombre del usuario), la fecha y hora en que fue obtenida la información y la dirección ip del servidor.

El agente envía esta información en formato JSON realizando un request POST.

La API recibe esta información y la almacena en un archivo de texto plano en formato JSON y también en una base de datos normalizada.

La base de datos cuenta con 3 tablas de almacenamiento:

* ```Servers```: contiene ip del servidor, fecha y hora en que se envió la información, arquitectura y marca del procesador, nombre y versión del sistema operativo.
* ```Procesos```: contiene ip del servidor,  fecha y hora en que se envió la información, id y nombre del procesos en ejecución, usuario que ejecutó el proceso e identificador del registro generado en la tabla Servers.
* ```Usuarios_activos```: contiene ip del servidor,  fecha y hora en que se envió la información, nombre del usuario activo, id de proceso e identificador del registro generado en la tabla Servers.

### Estructura general
La Base de datos SQLite, los agentes y la API
![](images/estructura.jpg)

### DER de la base de datos
![](images/DER.jpg)

# API Rest

## Endpoints

El método POST/servers recibe como parámetro un objeto json con el siguiente modelo:

![](images/model.jpg)

Devuelve como status el código 201 si pudo crear el servidor en la base de datos.
Si ocurre algún error, devuelve como status el código 400


