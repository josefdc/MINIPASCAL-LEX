program TestProgram;
uses
  crt, sysutils;

const
  PI = 3.1415;
  MAX_VALUE = 100;

type
  TIntegerArray = array[1..10] of integer;

var
  i, j: integer;
  k: real;
  str: string;
  arr: TIntegerArray;

function Add(a, b: integer): integer;
begin
  Add := a + b;
end;

procedure PrintMessage(msg: string);
begin
  writeln(msg);
end;

begin
  { Comentario de una línea }
  (* Comentario
     de múltiples líneas *)
  i := 10;
  j := 20;
  k := 15.5;
  str := '¡Hola, Pascal!';
  arr[1] := i * j div 2;
  arr[2] := i mod j;
  if (i < j) and (k > 10.0) then
    PrintMessage(str)
  else
    PrintMessage('Condición no cumplida');
  for i := 1 to 10 do
  begin
    arr[i] := i shl 1;
    writeln('Elemento del array ', i, ': ', arr[i]);
  end;
  while i > 0 do
  begin
    i := i - 1;
    arr[i] := arr[i] shr 1;
  end;
  repeat
    i := i + 1;
  until i = 10;
  case i of
    1: writeln('Uno');
    2: writeln('Dos');
    else writeln('Otro');
  end;
  str := concat('El valor de PI es ', FloatToStr(PI));
  PrintMessage(str);
end.
