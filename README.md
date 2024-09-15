# Documentación Analizador Léxico para Mini Pascal usando PLY

Este repositorio contiene la documentación para un analizador léxico de Mini Pascal utilizando PLY (Python Lex-Yacc). El proyecto es colaborativo y sigue una estructura organizada para asegurar un desarrollo eficiente y de alta calidad.

## Tabla de Contenidos
- [Documentación Analizador Léxico para Mini Pascal usando PLY](#documentación-analizador-léxico-para-mini-pascal-usando-ply)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Introducción](#introducción)
    - [¿Qué es un analizador léxico?](#qué-es-un-analizador-léxico)
    - [¿Qué es lo que pasa dentro de un analizador léxico?](#qué-es-lo-que-pasa-dentro-de-un-analizador-léxico)
    - [¿Por qué Pascal?](#por-qué-pascal)
  - [Propósito del Analizador Léxico](#propósito-del-analizador-léxico)
  - [Instrucciones de instalación y ejecución](#instrucciones-de-instalación-y-ejecución)
  - [Bibliografía](#bibliografía)

## Introducción
El proyecto vigente trata sobre un analizador léxico para mini Pascal usando PLY para la materia "compiladores" con el profesor Cesar Jaramillo, esto con el ideal de aplicar lo visto en la materia vigente y la materia "gramatica y lenguajes formales".

### ¿Qué es un analizador léxico?
Primero se hablará del obejtivo principal de un analizador léxico y este es el de "leer el flujo de caracteres de entrada y transformarlo en una secuencia de componentes léxicos que utilizará el analizador sintáctico" [1,p. 1].
¿Pero para qué se querría transformar una secuencia de componentes léxicos?
La respuesta está en una simple palabra, **precisión**. Describir algo en particular se vuelve sencillo de la mano de lenguajes formales y no deja espacio a ambiguedades. Al usar el castellano se puede incidir en errores de tipo lógico a la hora de describir procesos o características de procesos, al usar analizadores léxicos (que a su vez estos usan lenguajes formales) este problema se elimina de raíz.

### ¿Qué es lo que pasa dentro de un analizador léxico?
Se debe saber que el analizador divide la entrada en partes y este debe saber cuando las partes son un componente en conjunto o vienen totalmente separadas de algún contexto en específico, esto lo hace por medio de identificadores o palabras clave (tambien llamadas tokens). Existen distintas categorias de tokens:
- Palabras claves
- Identificadores
- Operadores
- Constantes numéricas
- Constantes de carácter o cadena
- Símbolos especiales

### ¿Por qué Pascal?
Pascal a día de hoy sigue siendo uno de los lenguajes más claros en el uso del lenguaje, con un tipado fuerte y estático, lo que significa que los errores relacionados con el tipo de datos se detectan en tiempo de compilación, relacionado a esto último, resulta ser un lenguaje eficiente en lo que a tiempos de ejecución se refiere y con una buena modularidad. Todas estas caracteristicas lo hacen el candidato perfecto para el área académica.

## Propósito del Analizador Léxico
El propósito no es más que el acádemico, poner en práctica los temas vistos en clase y demostrar el dominio que se poseen de estos.

## Instrucciones de instalación y ejecución
Instalación de Python
Descarga Python:

- Ve al sitio oficial de Python: [Python](python.org)

Descarga la última versión compatible con tu sistema operativo (Windows, macOS o Linux).

- Instala Python:
  
En Windows, asegúrate de marcar la opción "Add Python to PATH" durante la instalación.

Sigue las instrucciones del instalador.

En Mac, Usa el gestor de paquetes Homebrew (si no tienes Homebrew instalado, sigue las instrucciones en brew.sh)

En la mayoría de las distribuciones de Linux, Python ya está instalado. Si no es el caso, puedes instalarlo usando el gestor de paquetes adecuado según tu distribución.

Para Ubuntu:

```` markdown
sudo apt update
sudo apt install python3
````

Para fedora:

`sudo dnf install python3`

- Verifica la instalación:

Abre una terminal o consola (Command Prompt en Windows, Terminal en macOS/Linux).

Escribe python --version o python3 --version y presiona Enter.

Debería mostrarte la versión instalada de Python.

## Bibliografía
[1] Juan Vázquez. *Enseñanzas de la Implementación de un Analizador Léxico*. Disponible en: [https://www.researchgate.net/...](https://www.researchgate.net/profile/Juan-Vazquez-3/publication/302941976_Ensenanzas_de_la_Implementacion_de_un_Analizador_Lexico/links/5733db5308ae9f741b261a57/Ensenanzas-de-la-Implementacion-de-un-Analizador-Lexico.pdf)

[2][VILAR TORRES, Juan Miguel. *Analizador léxico (versión del curso 2008-2009)*. 2009.](https://repositori.uji.es/xmlui/bitstream/handle/10234/5877/lexico.apun.pdf?sequence=1)

