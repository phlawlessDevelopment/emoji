# Generated from grammar/SongGrammar.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,3,13,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,1,1,1,1,2,1,2,0,
        0,3,1,1,3,2,5,3,1,0,1,153,0,35,35,42,42,48,57,169,169,174,174,8252,
        8252,8265,8265,8482,8482,8505,8505,8596,8601,8617,8618,8986,8987,
        9000,9000,9167,9167,9193,9203,9208,9210,9410,9410,9642,9643,9654,
        9654,9664,9664,9723,9726,9728,9732,9742,9742,9745,9745,9748,9749,
        9752,9752,9757,9757,9760,9760,9762,9763,9766,9766,9770,9770,9774,
        9775,9784,9786,9792,9792,9794,9794,9800,9811,9823,9824,9827,9827,
        9829,9830,9832,9832,9851,9851,9854,9855,9874,9879,9881,9881,9883,
        9884,9888,9889,9895,9895,9898,9899,9904,9905,9917,9918,9924,9925,
        9928,9928,9934,9935,9937,9937,9939,9940,9961,9962,9968,9973,9975,
        9978,9981,9981,9986,9986,9989,9989,9992,9997,9999,9999,10002,10002,
        10004,10004,10006,10006,10013,10013,10017,10017,10024,10024,10035,
        10036,10052,10052,10055,10055,10060,10060,10062,10062,10067,10069,
        10071,10071,10083,10084,10133,10135,10145,10145,10160,10160,10175,
        10175,10548,10549,11013,11015,11035,11036,11088,11088,11093,11093,
        12336,12336,12349,12349,12951,12951,12953,12953,126980,126980,127183,
        127183,127344,127345,127358,127359,127374,127374,127377,127386,127462,
        127487,127489,127490,127514,127514,127535,127535,127538,127546,127568,
        127569,127744,127777,127780,127891,127894,127895,127897,127899,127902,
        127984,127987,127989,127991,128253,128255,128317,128329,128334,128336,
        128359,128367,128368,128371,128378,128391,128391,128394,128397,128400,
        128400,128405,128406,128420,128421,128424,128424,128433,128434,128444,
        128444,128450,128452,128465,128467,128476,128478,128481,128481,128483,
        128483,128488,128488,128495,128495,128499,128499,128506,128591,128640,
        128709,128715,128722,128725,128727,128733,128741,128745,128745,128747,
        128748,128752,128752,128755,128764,128992,129003,129008,129008,129292,
        129338,129340,129349,129351,129535,129648,129652,129656,129660,129664,
        129670,129680,129708,129712,129722,129728,129733,129744,129753,129760,
        129767,129776,129782,12,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,1,7,
        1,0,0,0,3,9,1,0,0,0,5,11,1,0,0,0,7,8,5,32,0,0,8,2,1,0,0,0,9,10,5,
        10,0,0,10,4,1,0,0,0,11,12,7,0,0,0,12,6,1,0,0,0,1,0,0
    ]

class SongGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    EMOJI = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "' '", "'\\n'" ]

    symbolicNames = [ "<INVALID>",
            "EMOJI" ]

    ruleNames = [ "T__0", "T__1", "EMOJI" ]

    grammarFileName = "SongGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


