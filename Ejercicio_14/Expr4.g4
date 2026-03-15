grammar Expr4;

expr: term ((PLUS | MINUS) term)* ;

term: factor ((MULT | DIV) factor)* ;

factor
    : NUM
    | LPAREN expr RPAREN
    ;

PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';

LPAREN: '(';
RPAREN: ')';

NUM: [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;