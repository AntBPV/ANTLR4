grammar Suma;

expr: NUM PLUS NUM ;

PLUS: '+' ;

NUM: [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;