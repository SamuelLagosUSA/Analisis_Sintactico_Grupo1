grammar ExpAmbig;

prog
    : e EOF
    ;

// Estrictamente como está en la diapositiva 15 (deliberadamente ambigua):
e
    : e '+' e
    | e '*' e
    | NUM
    ;

NUM  : [0-9]+ ;
WS   : [ \t\r\n]+ -> skip ;
