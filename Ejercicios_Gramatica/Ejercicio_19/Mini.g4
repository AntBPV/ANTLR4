grammar Mini;

prog: stat+ ;

stat
    : ID ASSIGN expr
    | PRINT expr
    ;

expr
    : expr PLUS expr
    | NUM
    | ID
    ;

PRINT: 'print';
ASSIGN: '=';
PLUS: '+';

ID: [a-zA-Z]+ ;
NUM: [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;