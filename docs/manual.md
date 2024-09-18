# Manual

Este documento contiene información sobre el archivo lexer.py

## Tabla de Contenidos
- [Manual](#manual)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Información sobre los tokens](#información-sobre-los-tokens)
  - [Ejemplos de entradas](#ejemplos-de-entradas)


## Información sobre los tokens
Con este proyecto se trabajan cuatro tipos de tokens.

- Palabras reservadas: Estas son palabras con un significado concreto en el lenguaje, un ejempplo en Pascal puede ser `ABSOLUTE`

- Operadores: Como su nombre lo indica estos son las palabras con las cuales se realizan operaciones aritméticas, un ejemplo en Pascal puede ser `MINUS`

- Delimitadores: Son símbolos o caracteres especiales que se utilizan para marcar el inicio, fin o separación de diferentes elementos dentro del código, un ejemplo en pascal puede ser `LPAREN`

- Otros: Se usa como apartado de símbolos que no entran en ninguna de las categorias anteriores.

## Ejemplos de entradas
Una posible entrada es la siguiente:

````
program Example1;
var
  x, y: integer;
begin
  x := 10;
  y := x + 20;
  writeln(y);
end.
````
