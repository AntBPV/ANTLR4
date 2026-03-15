from antlr4 import *
from SumaRestaLexer import SumaRestaLexer
from SumaRestaParser import SumaRestaParser

# Entradas a probar
entradas = ["5+3", "8-2"]

for entrada in entradas:

    print(f"\nEntrada: {entrada}")

    input_stream = InputStream(entrada)

    # Crear lexer
    lexer = SumaRestaLexer(input_stream)

    # Crear stream de tokens
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

    # Crear parser
    parser = SumaRestaParser(token_stream)

    # Regla inicial
    tree = parser.expr()

    print("ÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))