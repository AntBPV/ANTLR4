from antlr4 import *
from SumaLexer import SumaLexer
from SumaParser import SumaParser

entradas = ["3+4", "5+10"]

for entrada in entradas:

    print(f"\nEntrada: {entrada}")

    input_stream = InputStream(entrada)

    lexer = SumaLexer(input_stream)

    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    print("TOKENS:")

    for token in token_stream.tokens:
        if token.type != Token.EOF:

            if token.type - 1 < len(lexer.ruleNames):
                token_name = lexer.ruleNames[token.type - 1]
            else:
                token_name = str(token.type)

            print(f"Texto: {token.text}  Tipo: {token_name}")

    parser = SumaParser(token_stream)

    tree = parser.expr()

    print("ÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))