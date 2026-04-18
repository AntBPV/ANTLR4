import sys
import os

from antlr4 import FileStream, CommonTokenStream

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

# Agregar rutas al path
sys.path.append(os.path.join(BASE_DIR, "generated"))
sys.path.append(os.path.join(BASE_DIR, "interpreter"))

from WhileLangLexer import WhileLangLexer
from WhileLangParser import WhileLangParser
from visitor_impl import VisitorImpl


def run():
    input_stream = FileStream("input.txt", encoding="utf-8")

    lexer = WhileLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = WhileLangParser(stream)

    tree = parser.program()

    visitor = VisitorImpl()
    visitor.visit(tree)

    print("Memoria final:", visitor.memory)


if __name__ == "__main__":
    run()