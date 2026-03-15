grammar Calc;

prog: stat+ ;

stat
    : ID ASSIGN expr
    | PRINT expr
    ;

expr: term ((PLUS | MINUS) term)* ;

term: factor ((MULT | DIV) factor)* ;

factor
    : NUM
    | ID
    | LPAREN expr RPAREN
    ;

PRINT: 'print';

ASSIGN: '=';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';

LPAREN: '(';
RPAREN: ')';

ID: [a-zA-Z]+ ;
NUM: [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;