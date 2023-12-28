# Proyecto de Tercera Pre-Entrega - CoderHouse

Este es un proyecto Django que incluye tres clases en el modelo (Estudiante, Profesor, Curso) y una aplicación llamada `appcoder`.

## Estructura del Proyecto

- `modelos/`: Contiene la configuración principal del proyecto.
- `modelos/appcoder/`: Aplicación Django con las clases del modelo y las vistas.
- `modelos/modelos/urls.py`: Archivo de configuración de URL principal.
- `modelos/modelos/settings.py`: Configuración general del proyecto.

## Instrucciones de Ejecución

1. Clona el repositorio:

   ```bash
   git clone https://github.com/TomyRedondo/Tercera-pre-entrega-Redondo.git

# Crea y activa un entorno virtual:
python -m venv .coderenv
.\.coderenv\Scripts\activate



# Instala las dependencias:
pip install -r requirements.txt


# Aplica las migraciones:
python manage.py migrate


# Ejecuta el servidor de desarrollo:
python manage.py runserver


# Visita http://localhost:8000/curso/ en tu navegador para interactuar con la aplicación.

# Funcionalidades
# Guardado de Curso: La aplicación incluye una vista para guardar un curso.

# Notas
# Asegúrate de tener Python y Django instalados en tu entorno.







