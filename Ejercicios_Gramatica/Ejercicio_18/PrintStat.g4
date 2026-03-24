grammar PrintStat;

stat: PRINT expr ;

expr
    : ID
    | NUM
    ;

PRINT: 'print';

ID: [a-zA-Z]+ ;
NUM: [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;