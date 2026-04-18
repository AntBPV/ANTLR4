import sys
import os

from antlr4 import FileStream, CommonTokenStream

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

sys.path.append(os.path.join(BASE_DIR, "generated"))
sys.path.append(os.path.join(BASE_DIR, "interpreter"))

from WhileLangLexer import WhileLangLexer
from WhileLangParser import WhileLangParser
from visitor_impl import VisitorImpl


def run():
    current_dir = os.path.dirname(__file__)
    input_path = os.path.join(current_dir, "input.txt")

    input_stream = FileStream(input_path, encoding="utf-8")

    lexer = WhileLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = WhileLangParser(stream)

    tree = parser.program()

    visitor = VisitorImpl()

    try:
        visitor.visit(tree)
        print("Memoria final:", visitor.memory)
    except Exception as e:
        print("❌", e)


if __name__ == "__main__":
    run()