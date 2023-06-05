# venv
FastAPI para crear web.

## Descripción

Este es un proyecto de ejemplo que utiliza FastAPI, un marco web rápido para crear API en Python. El proyecto muestra cómo servir archivos estáticos y utilizar plantillas Jinja2 para renderizar páginas HTML.

El archivo principal del proyecto es `main.py`, que contiene la configuración de la aplicación FastAPI y las rutas de manejo. Además, se incluyen archivos estáticos y plantillas en la carpeta `public`, que sigue una estructura de directorios típica.

El archivo `item.html` es una plantilla Jinja2 que muestra los detalles de un ítem. La plantilla utiliza archivos estáticos, como `style.css` y `script.js`, para dar estilo e interactividad a la página.

## Configuración y uso

1. Clona el repositorio.

2. Asegúrate de tener Python 3.7 o superior instalado.

3. Instala las dependencias utilizando el administrador de paquetes pip:

4. Ejecuta la aplicación con el siguiente comando:


5. Abre un navegador web y accede a `http://localhost:8000/template/1` para ver la página de detalles del ítem.

## Estructura de archivos
├── lib64 -> lib
├── main.py
├── pasos.txt
├── public
│ ├── css
│ ├── html
│ ├── js
│ ├── static
│ │ ├── index.html
│ │ ├── script.js
│ │ └── style.css
│ └── templates
│ └── item.html
├── pycache
│ └── main.cpython-310.pyc
└── pyvenv.cfg


- `lib64`, `__pycache__`, `pyvenv.cfg` y `pasos.txt` son archivos/directorios adicionales que pueden estar presentes en el proyecto, pero no están relacionados directamente con la funcionalidad de la aplicación FastAPI.

- `main.py` es el archivo principal de la aplicación FastAPI que configura la aplicación y define las rutas.

- `public` es la carpeta que contiene archivos estáticos y plantillas.

- `public/css`, `public/html` y `public/js` son carpetas para organizar archivos adicionales, pero actualmente están vacías según la estructura proporcionada.

- `public/static` es la carpeta donde se almacenan los archivos estáticos, como `index.html`, `script.js` y `style.css`.

- `public/templates` es la carpeta que contiene las plantillas Jinja2, en este caso, solo `item.html`.

## Contribuciones

Las contribuciones a este proyecto son bienvenidas. Siéntete libre de abrir un problema o enviar una solicitud de extracción con mejoras o correcciones.


