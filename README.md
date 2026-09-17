# Actividad - Análisis Sintáctico (ANTLR)

**Grupo 1**
Ángel Arcos, Yeimy Beltrán, Nicolas Gutierrez, Samuel Lagos Prado

## Punto 1: Gramática de la diapositiva 11

Carpeta `Punto 1`. Implementa la gramática de expresiones (E → E+T | T, T → T*F | F, F → id | num | (E)) tal cual aparece en la diapositiva.

Generar el parser:
```
java -jar antlr-4.7-complete.jar -Dlanguage=Python3 Expresiones.g4
```

Ejecutar pruebas:
```
python3 main.py
```

`2 + 3 * 4` es válida. `2 + 3 - 4` y `2 + 3 * (4 - 5)` son inválidas porque la gramática no define el operador `-` (aunque la diapositiva los menciona como ejemplo, la regla formal solo tiene `+` y `*`).

## Punto 2: AST de la diapositiva 12/13

Carpeta `Punto 2`. Usa la misma gramática del punto 1 pero generada con `-visitor`:
```
java -jar antlr-4.7-complete.jar -Dlanguage=Python3 -visitor Expresiones.g4
```

`ast_visitor.py` recorre el parse tree y arma un AST más compacto (solo operadores y operandos, sin los nodos intermedios `e`/`t`/`f`), igual al de la diapositiva 13.

Ejecutar:
```
python3 test_ast.py
```

Para `3 + 4 * 5` el AST queda `(+ 3 (* 4 5))`, exactamente como en la diapositiva.

## Punto 3: Gramática ambigua de la diapositiva 15

Carpeta `Punto 3`. Implementa la gramática ambigua (E → E+E | E*E | num).

Generar y probar:
```
java -jar antlr-4.7-complete.jar -Dlanguage=Python3 ExpAmbig.g4
python3 main.py
```

Con `2 + 3 * 4`, ANTLR arma `(2+3)*4 = 20` en vez de `2+(3*4) = 14`. Si se invierte el orden de las alternativas en la gramática (`*` antes que `+`), el árbol para la misma entrada cambia. Esto confirma que la gramática es ambigua: existe más de un árbol de derivación válido para la misma cadena, y ANTLR resuelve la ambigüedad según el orden de las reglas, no según precedencia real.
