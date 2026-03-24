grammar Expr2;

expr: expr PLUS expr
    | expr MULT expr
    | NUM
    ;

PLUS: '+';
MULT: '*';

NUM: [0-9]+;

WS: [ \t\r\n]+ -> skip;