grammar Sample;

program: comparison;

expression: expression (Add | Sub) term | term;
comparison: expression (Less | LessEqual | Greater | GreaterEqual | Equal) expression | expression;

term: term (Mul | Div | Mod | Exp) factor | factor;

factor: Integer;

Add : '+';
Sub : '-';

Mul : '*';
Div : '/';
Mod : '%';
Exp: '^';

Less: '<';
Greater: '>';
LessEqual: '<=';
GreaterEqual: '>=';
Equal: '==';

Integer: [0-9]+ ;

WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
