from antlr4 import InputStream, CommonTokenStream
from ExpresionesLexer import ExpresionesLexer
from ExpresionesParser import ExpresionesParser
from ast_builder import AstBuilder


def construir_ast(expr: str):
    lexer = ExpresionesLexer(InputStream(expr))
    parser = ExpresionesParser(CommonTokenStream(lexer))
    parse_tree = parser.prog()
    ast = AstBuilder().visit(parse_tree.e())
    return parse_tree, ast


def probar(expr: str):
    print("----------------------------------------")
    print(f"Entrada: {expr}")
    parse_tree, ast = construir_ast(expr)
    print("Parse Tree (dp. 12):", parse_tree.toStringTree(recog=parse_tree.parser))
    print("AST infijo  (dp. 13):", ast.to_infix())
    print("AST (repr):", repr(ast))
    print("Evaluado:", ast.eval())


def main():
    expresiones = [
        "3 + 4 * 5",
        "2 + 3 * 4",
        "(2 + 3) * 4",
    ]
    for expr in expresiones:
        probar(expr)


if __name__ == "__main__":
    main()
