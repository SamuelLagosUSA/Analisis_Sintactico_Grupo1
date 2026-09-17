grammar Expresiones;

prog
    : e EOF
    ;

// Estrictamente como está en la diapositiva:
e
    : e '+' t
    | t
    ;

t
    : t '*' f
    | f
    ;

f
    : ID
    | NUM
    | '(' e ')'
    ;

ID   : [a-z]+ ;
NUM  : [0-9]+ ;
WS   : [ \t\r\n]+ -> skip ;
