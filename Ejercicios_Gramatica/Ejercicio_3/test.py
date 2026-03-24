from antlr4 import *
from KeywordsLexer import KeywordsLexer
from KeywordsParser import KeywordsParser

# Entradas a probar
entradas = ["if", "while", "print"]

for entrada in entradas:

    print(f"\nEntrada: {entrada}")

    input_stream = InputStream(entrada)

    # Crear lexer
    lexer = KeywordsLexer(input_stream)

    # Crear stream de tokens
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    print("TOKENS:")

    for token in token_stream.tokens:
        if token.type != Token.EOF:

            token_name = lexer.symbolicNames[token.type]

            if token_name is None:
                token_name = lexer.literalNames[token.type]

            print(f"Texto: {token.text}  Tipo: {token_name}")

    # Crear parser
    parser = KeywordsParser(token_stream)

    # Regla inicial
    tree = parser.stat()

    print("ÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))