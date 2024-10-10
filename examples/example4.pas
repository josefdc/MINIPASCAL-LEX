program Example3;
    var x, y: integer;
    const
        PI = 3.14;
        MAX = 100;
    type
        myArray = array [1..10] of integer;
        myRecord = record
            a: integer;
            b: real;
        end;
    begin
        x := 10;
        y := x + 20;
        if x > 5 then
            y := y + 1
        else
            y := y - 1;
        while y < 100 do
            y := y + 10;
        repeat
            y := y - 5;
        until y <= 50;
        for x := 1 to 10 do
            y := y + x;
end.