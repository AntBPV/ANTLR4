grammar ExprVar;

expr: expr PLUS expr
    | ID
    | NUM
    ;

PLUS: '+';

ID: [a-zA-Z]+ ;
NUM: [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;