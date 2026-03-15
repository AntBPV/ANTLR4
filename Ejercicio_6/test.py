from antlr4 import *
from Saludo2Lexer import Saludo2Lexer
from Saludo2Parser import Saludo2Parser

entradas = ["hola Juan", "buenosdias Pedro"]

for entrada in entradas:

    print(f"\nEntrada: {entrada}")

    input_stream = InputStream(entrada)

    lexer = Saludo2Lexer(input_stream)

    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    print("TOKENS:")

    for token in token_stream.tokens:
        if token.type != Token.EOF:

            if token.type < len(lexer.symbolicNames):
                token_name = lexer.symbolicNames[token.type]
            else:
                token_name = lexer.literalNames[token.type]

            print(f"Texto: {token.text}  Tipo: {token_name}")

    parser = Saludo2Parser(token_stream)

    tree = parser.saludo()

    print("ÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))