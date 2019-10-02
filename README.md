# Introducción
Este repositorio continene los ficheros originales del [artículo del blog 'Contenedor Inseguro'](https://www.contenedorinseguro.net/) sobre la importancia de definir el usuario en los contenedores Docker. 


# Instalación
Para copiar el repositorio a local: 

```
git clone https://github.com/daviddetorres/jugandocontrivy
```

Para ejecutar en local la aplicación se requieren las siguientes librerías: 
* Flask
* waitress

Para la instalación de estos paquetes: 

```
pip3 install Flask waitress
```

Para crear las imágenes deberéis [tener instalado Docker](https://docs.docker.com/install/). 

# Preparando los directorios de pruebas de acceso
Crearemos primer un directorio con acceso al usuario con el que estamos trabajando (que no es root...) y un fichero con un texto dentro.

```
mkdir /tmp/directoriousuario 
echo "El secreto del usuario es que no tiene secretos." > /tmp/directoriousuario/secreto.txt 
chmod 700 /tmp/directoriousuario 
chmod 600 /tmp/directoriousuario/secreto.txt
```

También crearemos un directorio con un usuario root también con un archivo que contenga un secreto.

```
sudo mkdir /tmp/directorioroot
sudo echo "El secreto del superusuario es 42." > /tmp/directorioroot/secreto.txt
sudo chmod 700 /tmp/directorioroot
sudo chmod 600 /tmp/directorioroot/secreto.txt
```

# Creando las imágenes y los contenedores de Docker
A continuación se muestran los comandos para crear las diferentes imágenes y contenedores con diferentes configuraciones de usuarios.

Imagen con usuario por defecto (root):

```
docker build -f Dockerfile_usuariopordefecto -t app-usuario-root .
docker run -p 5000:5000 -v /tmp:/tmp/host -d --name contenedor-root app-usuario-root
```


# Probando los accesos con los diferentes contenedores

```
docker exec contenedor-root cat /tmp/host/directorioroot/secreto.txt
```

