# Generated from PrintStat.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PrintStatParser import PrintStatParser
else:
    from PrintStatParser import PrintStatParser

# This class defines a complete listener for a parse tree produced by PrintStatParser.
class PrintStatListener(ParseTreeListener):

    # Enter a parse tree produced by PrintStatParser#stat.
    def enterStat(self, ctx:PrintStatParser.StatContext):
        pass

    # Exit a parse tree produced by PrintStatParser#stat.
    def exitStat(self, ctx:PrintStatParser.StatContext):
        pass


    # Enter a parse tree produced by PrintStatParser#expr.
    def enterExpr(self, ctx:PrintStatParser.ExprContext):
        pass

    # Exit a parse tree produced by PrintStatParser#expr.
    def exitExpr(self, ctx:PrintStatParser.ExprContext):
        pass



del PrintStatParser