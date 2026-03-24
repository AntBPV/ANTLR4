from antlr4 import *
from Expr2Lexer import Expr2Lexer
from Expr2Parser import Expr2Parser

# Entradas a probar
entradas = ["3+4*5", "2*3+4"]

for entrada in entradas:

    print(f"\nEntrada: {entrada}")

    input_stream = InputStream(entrada)

    lexer = Expr2Lexer(input_stream)

    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    print("TOKENS:")

    for token in token_stream.tokens:
        if token.type != Token.EOF:

            if token.type < len(lexer.literalNames) and lexer.literalNames[token.type] is not None:
                token_name = lexer.literalNames[token.type]
            elif token.type < len(lexer.symbolicNames):
                token_name = lexer.symbolicNames[token.type]
            else:
                token_name = str(token.type)

            print(f"Texto: {token.text}  Tipo: {token_name}")

    parser = Expr2Parser(token_stream)

    tree = parser.expr()

    print("ÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))