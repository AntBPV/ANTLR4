grammar SumaResta;

expr: NUM op NUM ;

op: PLUS | MINUS ;

PLUS: '+' ;
MINUS: '-' ;

NUM: [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;