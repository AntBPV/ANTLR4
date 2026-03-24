from antlr4 import *
from SaludoLexer import SaludoLexer
from SaludoParser import SaludoParser

# Entradas a probar
entradas = ["hola Juan", "hola Maria"]

for entrada in entradas:

    print(f"\nEntrada: {entrada}")

    input_stream = InputStream(entrada)

    # Crear lexer
    lexer = SaludoLexer(input_stream)

    # Crear stream de tokens
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

    # Crear parser
    parser = SaludoParser(token_stream)

    # Regla inicial
    tree = parser.saludo()

    print("ÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))