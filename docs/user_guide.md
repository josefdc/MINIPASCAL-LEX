# Guía de usuario

Este documento contiene información relevante sobre el uso del programa, con este se pretende facilitar/mejorar la experiencia de usuario

## Tabla de Contenidos
- [Guía de usuario](#guía-de-usuario)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [¿Cómo usar lexer para Mini-Pascal?](#cómo-usar-lexer-para-mini-pascal)
  - [Ejemplos de código de Mini Pascal que pueden ser analizados.](#ejemplos-de-código-de-mini-pascal-que-pueden-ser-analizados)
  - [Explicación de los tokens reconocidos por el lexer.](#explicación-de-los-tokens-reconocidos-por-el-lexer)

## ¿Cómo usar lexer para Mini-Pascal?

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
Con esto ya se ejecutaría el programa de forma correcta.

## Ejemplos de código de Mini Pascal que pueden ser analizados.

Entrada:
```
program Example1;
var
  x, y: integer;
begin
  x := 10;
  y := x + 20;
  writeln(y);
end.
```
Con esta entrada se va analizando símbolo por símbolo.

Observemos la linea:
```
end.
```

El resultado esperado sería el siguiente:

```
LexToken (END, 'end', 61,1023)
LexToken(DOT, '.', 61,1028)
```

## Explicación de los tokens reconocidos por el lexer.
- Palabras reservadas: Estas son palabras con un significado concreto en el lenguaje, un ejempplo en Pascal puede ser `ABSOLUTE`

- Operadores: Como su nombre lo indica estos son las palabras con las cuales se realizan operaciones aritméticas, un ejemplo en Pascal puede ser `MINUS`

- Delimitadores: Son símbolos o caracteres especiales que se utilizan para marcar el inicio, fin o separación de diferentes elementos dentro del código, un ejemplo en pascal puede ser `LPAREN`

- Otros: Se usa como apartado de símbolos que no entran en ninguna de las categorias anteriores.