from antlr4 import InputStream, CommonTokenStream
from ExpresionesLexer import ExpresionesLexer
from ExpresionesParser import ExpresionesParser


def probar_expresion(expr: str):
    print("----------------------------------------")
    print(f"Entrada: {expr}")

    input_stream = InputStream(expr)

    lexer = ExpresionesLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    parser = ExpresionesParser(token_stream)

    tree = parser.prog()

    if parser.getNumberOfSyntaxErrors() == 0:
        print("Resultado: Sintaxis VÁLIDA")
        print("Parse Tree:", tree.toStringTree(recog=parser))
    else:
        print(
            f"Resultado: Sintaxis INVÁLIDA ({parser.getNumberOfSyntaxErrors()} error/es)"
        )


def main():

    expresiones = [
        "2 + 3 * 4",
        "2 + 3 - 4",
        "2 + 3 * (4 - 5)",
    ]

    for expr in expresiones:
        probar_expresion(expr)


if __name__ == "__main__":
    main()
