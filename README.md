# Introducción
Este repositorio continene los ficheros originales del [artículo del blog 'Contenedor Inseguro'](https://www.contenedorinseguro.net/2019/09/como-de-inseguro-es-contenedor-docker-trivy.html) sobre la herramienta [trivy de Aquasec](https://github.com/aquasecurity/trivy). Esta herramienta permite auditar la seguridad de imágenes de Docker. 

En el artículo se utiliza una aplicación sencilla en python y varios ejemplos de imágenes con diferentes configuraciones e imágenes base para ver las vulnerabilidades que detecta Trivy en cada una de ellas.

En el directorio `/informes` se pueden encontrar los informes generados por trivy de cada una de las imágenes.    

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

