# Generated from Sample.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,13,64,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,
        1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,
        1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,11,4,11,54,8,11,11,11,12,11,
        55,1,12,4,12,59,8,12,11,12,12,12,60,1,12,1,12,0,0,13,1,1,3,2,5,3,
        7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,1,0,2,1,0,48,
        57,3,0,9,10,13,13,32,32,65,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,
        7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,
        1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,1,27,
        1,0,0,0,3,29,1,0,0,0,5,31,1,0,0,0,7,33,1,0,0,0,9,35,1,0,0,0,11,37,
        1,0,0,0,13,39,1,0,0,0,15,41,1,0,0,0,17,43,1,0,0,0,19,46,1,0,0,0,
        21,49,1,0,0,0,23,53,1,0,0,0,25,58,1,0,0,0,27,28,5,43,0,0,28,2,1,
        0,0,0,29,30,5,45,0,0,30,4,1,0,0,0,31,32,5,42,0,0,32,6,1,0,0,0,33,
        34,5,47,0,0,34,8,1,0,0,0,35,36,5,37,0,0,36,10,1,0,0,0,37,38,5,94,
        0,0,38,12,1,0,0,0,39,40,5,60,0,0,40,14,1,0,0,0,41,42,5,62,0,0,42,
        16,1,0,0,0,43,44,5,60,0,0,44,45,5,61,0,0,45,18,1,0,0,0,46,47,5,62,
        0,0,47,48,5,61,0,0,48,20,1,0,0,0,49,50,5,61,0,0,50,51,5,61,0,0,51,
        22,1,0,0,0,52,54,7,0,0,0,53,52,1,0,0,0,54,55,1,0,0,0,55,53,1,0,0,
        0,55,56,1,0,0,0,56,24,1,0,0,0,57,59,7,1,0,0,58,57,1,0,0,0,59,60,
        1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,62,1,0,0,0,62,63,6,12,0,0,
        63,26,1,0,0,0,3,0,55,60,1,6,0,0
    ]

class SampleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Add = 1
    Sub = 2
    Mul = 3
    Div = 4
    Mod = 5
    Exp = 6
    Less = 7
    Greater = 8
    LessEqual = 9
    GreaterEqual = 10
    Equal = 11
    Integer = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", "'<'", "'>'", "'<='", 
            "'>='", "'=='" ]

    symbolicNames = [ "<INVALID>",
            "Add", "Sub", "Mul", "Div", "Mod", "Exp", "Less", "Greater", 
            "LessEqual", "GreaterEqual", "Equal", "Integer", "WS" ]

    ruleNames = [ "Add", "Sub", "Mul", "Div", "Mod", "Exp", "Less", "Greater", 
                  "LessEqual", "GreaterEqual", "Equal", "Integer", "WS" ]

    grammarFileName = "Sample.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


