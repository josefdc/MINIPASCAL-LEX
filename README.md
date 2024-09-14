# Documentación Analizador Léxico para Mini Pascal usando PLY

Este repositorio contiene la documentación para un analizador léxico de Mini Pascal utilizando PLY (Python Lex-Yacc). El proyecto es colaborativo y sigue una estructura organizada para asegurar un desarrollo eficiente y de alta calidad.

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Propósito del Analizador Léxico](#propósito-del-analizador-léxico)
3. [Instrucciones de instalación y ejecución](#instrucciones-de-instalación-y-ejecución)
4. [Bibliografía](#bibliografía)

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

## Bibliografía
[1]: https://www.researchgate.net/profile/Juan-Vazquez-3/publication/302941976_Ensenanzas_de_la_Implementacion_de_un_Analizador_Lexico/links/5733db5308ae9f741b261a57/Ensenanzas-de-la-Implementacion-de-un-Analizador-Lexico.pdf (Enseñanzas de la Implementación de un Analizador Léxico)
