# Generated from Sample.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write(":\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\5\2!\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\5\3.\n\3\3\4\3\4\3\5\3\5\3\6\6\6\65\n\6")
        buf.write("\r\6\16\6\66\3\6\3\6\2\2\7\3\3\5\4\7\5\t\6\13\7\3\2\4")
        buf.write("\3\2c|\5\2\13\f\17\17\"\"\2@\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\3 \3\2\2\2\5-\3\2")
        buf.write("\2\2\7/\3\2\2\2\t\61\3\2\2\2\13\64\3\2\2\2\r\16\7E\2\2")
        buf.write("\16\17\7q\2\2\17\20\7w\2\2\20\21\7n\2\2\21!\7f\2\2\22")
        buf.write("\23\7U\2\2\23\24\7j\2\2\24\25\7q\2\2\25\26\7w\2\2\26\27")
        buf.write("\7n\2\2\27!\7f\2\2\30\31\7E\2\2\31\32\7c\2\2\32!\7p\2")
        buf.write("\2\33\34\7Y\2\2\34\35\7q\2\2\35\36\7w\2\2\36\37\7n\2\2")
        buf.write("\37!\7f\2\2 \r\3\2\2\2 \22\3\2\2\2 \30\3\2\2\2 \33\3\2")
        buf.write("\2\2!\4\3\2\2\2\"#\7j\2\2#.\7g\2\2$%\7u\2\2%&\7j\2\2&")
        buf.write(".\7g\2\2\'(\7v\2\2()\7j\2\2)*\7g\2\2*.\7{\2\2+,\7y\2\2")
        buf.write(",.\7g\2\2-\"\3\2\2\2-$\3\2\2\2-\'\3\2\2\2-+\3\2\2\2.\6")
        buf.write("\3\2\2\2/\60\t\2\2\2\60\b\3\2\2\2\61\62\7A\2\2\62\n\3")
        buf.write("\2\2\2\63\65\t\3\2\2\64\63\3\2\2\2\65\66\3\2\2\2\66\64")
        buf.write("\3\2\2\2\66\67\3\2\2\2\678\3\2\2\289\b\6\2\29\f\3\2\2")
        buf.write("\2\6\2 -\66\3\b\2\2")
        return buf.getvalue()


class SampleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    VERB = 1
    SUB = 2
    ID = 3
    E_Mask = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'?'" ]

    symbolicNames = [ "<INVALID>",
            "VERB", "SUB", "ID", "E_Mask", "WS" ]

    ruleNames = [ "VERB", "SUB", "ID", "E_Mask", "WS" ]

    grammarFileName = "Sample.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


