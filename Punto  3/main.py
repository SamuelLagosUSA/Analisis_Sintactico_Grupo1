from antlr4 import InputStream, CommonTokenStream
from ExpAmbigLexer import ExpAmbigLexer
from ExpAmbigParser import ExpAmbigParser


def probar_expresion(expr: str):
    print("----------------------------------------")
    print(f"Entrada: {expr}")

    input_stream = InputStream(expr)
    lexer = ExpAmbigLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExpAmbigParser(token_stream)

    tree = parser.prog()

    if parser.getNumberOfSyntaxErrors() == 0:
        print("Resultado: Sintaxis VÁLIDA")
        print("Parse Tree:", tree.toStringTree(recog=parser))
    else:
        print(f"Resultado: Sintaxis INVÁLIDA ({parser.getNumberOfSyntaxErrors()} error/es)")


def main():
    expresiones = [
        "2 + 3 * 4",
        "2 + 3 + 4",
        "2 * 3 * 4",
    ]
    for expr in expresiones:
        probar_expresion(expr)


if __name__ == "__main__":
    main()
