from antlr4 import *
from ProgramaLexer import ProgramaLexer
from ProgramaParser import ProgramaParser

entrada = """x=5
y=10
z=20"""

print("Entrada:")
print(entrada)

input_stream = InputStream(entrada)

lexer = ProgramaLexer(input_stream)

token_stream = CommonTokenStream(lexer)
token_stream.fill()

print("\nTOKENS:")

for token in token_stream.tokens:
    if token.type != Token.EOF:

        if token.type < len(lexer.literalNames) and lexer.literalNames[token.type] is not None:
            token_name = lexer.literalNames[token.type]
        elif token.type < len(lexer.symbolicNames):
            token_name = lexer.symbolicNames[token.type]
        else:
            token_name = str(token.type)

        print(f"Texto: {token.text}  Tipo: {token_name}")

parser = ProgramaParser(token_stream)

tree = parser.prog()

print("\nÁRBOL SINTÁCTICO:")
print(tree.toStringTree(recog=parser))