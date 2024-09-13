# Analizador Léxico para Mini Pascal usando PLY

Este repositorio contiene el código fuente para un analizador léxico de Mini Pascal utilizando PLY (Python Lex-Yacc). El proyecto es colaborativo y sigue una estructura organizada para asegurar un desarrollo eficiente y de alta calidad.

## Tabla de Contenidos
1. [Requisitos Previos](#requisitos-previos)
2. [Configuración del Entorno](#configuración-del-entorno)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Flujo de Trabajo](#flujo-de-trabajo)
5. [Guía de Contribución](#guía-de-contribución)
6. [Pruebas](#pruebas)
7. [Licencia](#licencia)

## Requisitos Previos
- Python 3.8 o superior.
- PLY: Se puede instalar ejecutando `pip install ply`.
- Git: Para el control de versiones.

## Configuración del Entorno
1. Clona el repositorio:
   ```bash
   git clone https://github.com/josefdc/MINIPASCAL-LEX.git
   ```
2. Crea un entorno virtual y activa el entorno:
   ```bash
   python -m venv venv
   source venv/bin/activate   # En Windows: venv\Scripts\activate
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Estructura del Proyecto
- `src/`: Contiene el código fuente del analizador léxico.
- `tests/`: Contiene los casos de prueba para el analizador.
- `docs/`: Contiene la documentación detallada del proyecto.
- `README.md`: Documentación general del proyecto.
- `requirements.txt`: Lista de dependencias necesarias.

## Flujo de Trabajo
1. **Crear una rama para tu tarea:**
   ```bash
   git checkout -b nombre_de_la_rama
   ```
2. **Realiza cambios y realiza commits regularmente:**
   ```bash
   git add .
   git commit -m "Descripción de los cambios"
   ```
3. **Sincroniza tu rama con `develop`:**
   ```bash
   git checkout develop
   git pull origin develop
   git checkout nombre_de_la_rama
   git merge develop
   ```
4. **Envía tu rama a GitHub y crea un Pull Request (PR):**
   ```bash
   git push origin nombre_de_la_rama
   ```
   Luego, crea un PR desde la interfaz de GitHub y solicita revisiones de tus compañeros.

## Guía de Contribución
- Sigue la convención de nombres de ramas: `feature/nueva_caracteristica`, `fix/correccion_de_error`.
- Asegúrate de que todos los cambios se prueben antes de enviar un PR.
- Participa en las revisiones de código para mejorar la calidad del proyecto.

## Pruebas
- Para ejecutar las pruebas, utiliza:
   ```bash
   pytest tests/
   ```
- Asegúrate de que todas las pruebas pasen antes de enviar tu PR.

## Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
