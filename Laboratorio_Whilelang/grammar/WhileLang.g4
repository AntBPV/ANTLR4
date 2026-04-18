grammar WhileLang;

program: statement+ EOF;

statement
    : declaration
    | assignment
    | whileStatement
    | ifStatement
    | breakStatement
    | continueStatement
    ;

declaration: TYPE ID ASSIGN expr SEMI;

assignment: ID ASSIGN expr SEMI;

whileStatement: WHILE LPAREN condition RPAREN LBRACE statement* RBRACE;

ifStatement
    : IF LPAREN condition RPAREN LBRACE thenBlock=statement* RBRACE
      (ELSE LBRACE elseBlock=statement* RBRACE)?
    ;
    
breakStatement: BREAK SEMI;

continueStatement: CONTINUE SEMI;

condition: expr;

expr
    : ID                             # IdExpr
    | NUMBER                         # NumberExpr
    | STRING                         # StringExpr
    | expr OP expr                   # ArithmeticExpr
    | expr operator expr             # ComparisonExpr
    ;

operator: GT | LT | EQ |  NE;

OP: PLUS | MINUS | MULT | DIV;

WHILE: 'while';
IF: 'if';
ELSE: 'else';
BREAK: 'break';
CONTINUE: 'continue';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
ASSIGN: '=';
GT: '>';
LT: '<';
EQ: '==';
NE: '!=';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';

TYPE: 'int' | 'string';

STRING: '"' (~["\r\n])* '"';

ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
WS: [ \t\r\n]+ -> skip;