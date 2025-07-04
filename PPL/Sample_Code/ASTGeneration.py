from CompiledFiles.SampleVisitor import SampleVisitor
from CompiledFiles.SampleParser import SampleParser
from ASTUtils import *
from functools import reduce

class ASTGeneration(SampleVisitor):
    def visitProgram(self, ctx:SampleParser.ProgramContext):
        return Prog([ctx.comparison().accept(self)])

    def visitExpression(self, ctx:SampleParser.ExpressionContext):
        if ctx.expression():
            sign = ""
            if ctx.Add():
                sign = "+"
            elif ctx.Sub():
                sign = "-"
                            
            return BinOp(sign, ctx.expression().accept(self), ctx.term().accept(self))
        else:
            return ctx.term().accept(self)

    def visitTerm(self, ctx:SampleParser.TermContext):
        if ctx.term():
            sign = ""
            if ctx.Mul():
                sign = "*"
            elif ctx.Div():
                sign = "/"
            elif ctx.Mod():
                sign = "%"
            elif ctx.Exp():
                sign = "^"
            
            return BinOp(sign, ctx.term().accept(self), ctx.factor().accept(self))
        else:
            return ctx.factor().accept(self)
    
    def visitComparison(self, ctx:SampleParser.ComparisonContext):
        if len(ctx.expression()) == 2:
            sign = ""
            if ctx.Less():
                sign = "<"
            elif ctx.Greater():
                sign = ">"
            elif ctx.LessEqual():
                sign = "<="
            elif ctx.GreaterEqual():
                sign = ">="
            elif ctx.Equal():
                sign = "=="
            
            return BinOp(sign, ctx.expression(0).accept(self), ctx.expression(1).accept(self))
        else:
            return ctx.expression(0).accept(self)
        
    def visitFactor(self, ctx:SampleParser.FactorContext):
        if ctx.Integer():
            return self.visitInteger(ctx.Integer())

    def visitInteger(self, node:SampleParser.Integer):
        return Int(int(node.getText()))
    

