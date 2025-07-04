# Generated from Sample1.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\5")
        buf.write("\34\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\7\3\23\n\3\f\3\16\3\26\13\3\3\4\3\4\3\5")
        buf.write("\3\5\3\5\2\3\4\6\2\4\6\b\2\2\2\30\2\n\3\2\2\2\4\f\3\2")
        buf.write("\2\2\6\27\3\2\2\2\b\31\3\2\2\2\n\13\5\4\3\2\13\3\3\2\2")
        buf.write("\2\f\r\b\3\1\2\r\16\5\b\5\2\16\24\3\2\2\2\17\20\f\4\2")
        buf.write("\2\20\21\7\3\2\2\21\23\5\b\5\2\22\17\3\2\2\2\23\26\3\2")
        buf.write("\2\2\24\22\3\2\2\2\24\25\3\2\2\2\25\5\3\2\2\2\26\24\3")
        buf.write("\2\2\2\27\30\7\3\2\2\30\7\3\2\2\2\31\32\7\4\2\2\32\t\3")
        buf.write("\2\2\2\3\24")
        return buf.getvalue()


class Sample1Parser ( Parser ):

    grammarFileName = "Sample1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "Integer", "WS" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_operation = 2
    RULE_term = 3

    ruleNames =  [ "program", "expression", "operation", "term" ]

    EOF = Token.EOF
    T__0=1
    Integer=2
    WS=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Sample1Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Sample1Parser.RULE_program




    def program(self):

        localctx = Sample1Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(Sample1Parser.TermContext,0)


        def expression(self):
            return self.getTypedRuleContext(Sample1Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Sample1Parser.RULE_expression



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Sample1Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 18
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Sample1Parser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 13
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 14
                    self.match(Sample1Parser.T__0)
                    self.state = 15
                    self.term() 
                self.state = 20
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Sample1Parser.RULE_operation




    def operation(self):

        localctx = Sample1Parser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_operation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(Sample1Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self):
            return self.getToken(Sample1Parser.Integer, 0)

        def getRuleIndex(self):
            return Sample1Parser.RULE_term




    def term(self):

        localctx = Sample1Parser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(Sample1Parser.Integer)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




