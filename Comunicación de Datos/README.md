# README.md

Este repositorio contiene una API desarrollada con FastAPI en la ruta /API/ y una implementación de TCP/IP utilizando un servidor y cliente en Python en el directorio /TCP-IP/.

## Ambiente Virtual

Para utilizar este repositorio, se recomienda crear un ambiente virtual. Los siguientes pasos te guiarán para crear y activar un ambiente virtual llamado "env" en la carpeta local donde descargaste el repositorio:

### Linux

1. Abre una terminal y navega hasta la carpeta local del repositorio.
2. Instala virtualenv si no lo tienes instalado con el siguiente comando:
```
sudo apt-get install virtualenv
```
3. Crea el ambiente virtual con el siguiente comando:
```
virtualenv env
```
4. Activa el ambiente virtual con el siguiente comando:
```
source env/bin/activate
```
### Windows

1. Abre PowerShell y navega hasta la carpeta local del repositorio.
2. Instala virtualenv si no lo tienes instalado con el siguiente comando:
```
pip install virtualenv
```
3. Crea el ambiente virtual con el siguiente comando:
```
virtualenv env
```
4. Activa el ambiente virtual con el siguiente comando:
```
.\env\Scripts\Activate.ps1
```

Una vez que el ambiente virtual está activado, instala los paquetes necesarios utilizando el archivo requirements.txt del repositorio. Para hacer esto, ejecuta el siguiente comando en la terminal:
```
pip install -r requirements.txt
```

## Levantar API

Para levantar la API, debes seguir los siguientes pasos:

1. Cambiarse al directorio /API/ del repositorio.
2. Ejecuta el siguiente comando para levantar la API main.py con Uvicorn:
```
uvicorn main:app --reload
```
3. La API estará disponible en la dirección `http://localhost:8000/`. El endpoint de bienvenida estará disponible en la dirección `http://localhost:8000/home/`.

## Envío TCP-IP

Para enviar un mensaje mediante TCP/IP utilizando el servidor y cliente en Python, sigue los siguientes pasos:

1. Abre dos terminales/consolas y activa el ambiente virtual en ambas.
2. Cambiarse al directorio /TCP-IP/ del repositorio.
3. En la terminal 1, ejecuta el siguiente comando para levantar el servidor en escucha:
```
python server.py
```
4. En la terminal 2, ejecuta el siguiente comando para llamar al cliente y enviar el mensaje al servidor en escucha:
```
python cliente.py
```

¡Eso es todo! Si todo ha ido bien, el mensaje enviado desde el cliente debería aparecer en la terminal 1 donde se encuentra el servidor en escucha.
