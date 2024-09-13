program TestLexer;
var
  x, y: integer;   { Declaración de variables }
  z: real;
begin
  x := 10;          { Asignación de un número entero }
  y := x + 20;      { Operación aritmética con números enteros }
  z := 5.5;         { Asignación de un número real }
  if x > 0 then     { Uso de una estructura de control }
    writeln('x es positivo');
  while y < 100 do  { Bucle con condición }
  begin
    y := y + 1;
  end;
end.
