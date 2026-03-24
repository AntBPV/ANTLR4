grammar Programa;

prog: stat+ ;

stat: ID ASSIGN NUM ;

ASSIGN: '=';

ID: [a-zA-Z]+ ;
NUM: [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;