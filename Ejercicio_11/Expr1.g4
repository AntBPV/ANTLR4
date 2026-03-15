grammar Expr1;

expr: expr PLUS NUM
    | NUM
    ;

PLUS: '+' ;

NUM: [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;