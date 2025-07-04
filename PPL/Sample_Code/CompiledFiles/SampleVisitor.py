# Generated from Sample.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SampleParser import SampleParser
else:
    from SampleParser import SampleParser

# This class defines a complete generic visitor for a parse tree produced by SampleParser.

class SampleVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SampleParser#program.
    def visitProgram(self, ctx:SampleParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampleParser#expression.
    def visitExpression(self, ctx:SampleParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampleParser#comparison.
    def visitComparison(self, ctx:SampleParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampleParser#term.
    def visitTerm(self, ctx:SampleParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampleParser#factor.
    def visitFactor(self, ctx:SampleParser.FactorContext):
        return self.visitChildren(ctx)



del SampleParser