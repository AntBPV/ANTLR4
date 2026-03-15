grammar Expr3;

expr: term ((PLUS | MINUS) term)* ;

term: factor ((MULT | DIV) factor)* ;

factor: NUM ;

PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';

NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;