# Generated from Sample1.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\5")
        buf.write("\27\b\1\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\3\6\3\r\n\3")
        buf.write("\r\3\16\3\16\3\4\6\4\22\n\4\r\4\16\4\23\3\4\3\4\2\2\5")
        buf.write("\3\3\5\4\7\5\3\2\4\3\2\62;\5\2\13\f\17\17\"\"\2\30\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\3\t\3\2\2\2\5\f\3\2\2")
        buf.write("\2\7\21\3\2\2\2\t\n\7/\2\2\n\4\3\2\2\2\13\r\t\2\2\2\f")
        buf.write("\13\3\2\2\2\r\16\3\2\2\2\16\f\3\2\2\2\16\17\3\2\2\2\17")
        buf.write("\6\3\2\2\2\20\22\t\3\2\2\21\20\3\2\2\2\22\23\3\2\2\2\23")
        buf.write("\21\3\2\2\2\23\24\3\2\2\2\24\25\3\2\2\2\25\26\b\4\2\2")
        buf.write("\26\b\3\2\2\2\5\2\16\23\3\b\2\2")
        return buf.getvalue()


class Sample1Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    Integer = 2
    WS = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'-'" ]

    symbolicNames = [ "<INVALID>",
            "Integer", "WS" ]

    ruleNames = [ "T__0", "Integer", "WS" ]

    grammarFileName = "Sample1.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


