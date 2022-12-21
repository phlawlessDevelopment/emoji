# Generated from grammar/SongGrammar.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,3,40,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,0,1,0,1,1,1,1,3,1,20,8,1,4,1,22,8,1,11,1,12,1,23,
        1,1,3,1,27,8,1,1,2,1,2,3,2,31,8,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,
        4,0,0,5,0,2,4,6,8,0,0,39,0,11,1,0,0,0,2,21,1,0,0,0,4,30,1,0,0,0,
        6,32,1,0,0,0,8,35,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,13,1,0,
        0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,15,1,0,0,0,15,16,5,0,0,1,16,1,
        1,0,0,0,17,19,3,4,2,0,18,20,5,1,0,0,19,18,1,0,0,0,19,20,1,0,0,0,
        20,22,1,0,0,0,21,17,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,
        0,0,0,24,26,1,0,0,0,25,27,5,2,0,0,26,25,1,0,0,0,26,27,1,0,0,0,27,
        3,1,0,0,0,28,31,3,6,3,0,29,31,3,8,4,0,30,28,1,0,0,0,30,29,1,0,0,
        0,31,5,1,0,0,0,32,33,5,3,0,0,33,34,5,3,0,0,34,7,1,0,0,0,35,36,5,
        3,0,0,36,37,5,3,0,0,37,38,5,3,0,0,38,9,1,0,0,0,5,13,19,23,26,30
    ]

class SongGrammarParser ( Parser ):

    grammarFileName = "SongGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "' '", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "EMOJI" ]

    RULE_song = 0
    RULE_phrase = 1
    RULE_chunk = 2
    RULE_pair = 3
    RULE_triplet = 4

    ruleNames =  [ "song", "phrase", "chunk", "pair", "triplet" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    EMOJI=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SongContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SongGrammarParser.EOF, 0)

        def phrase(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SongGrammarParser.PhraseContext)
            else:
                return self.getTypedRuleContext(SongGrammarParser.PhraseContext,i)


        def getRuleIndex(self):
            return SongGrammarParser.RULE_song

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSong" ):
                listener.enterSong(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSong" ):
                listener.exitSong(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSong" ):
                return visitor.visitSong(self)
            else:
                return visitor.visitChildren(self)




    def song(self):

        localctx = SongGrammarParser.SongContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_song)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.phrase()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
                    break

            self.state = 15
            self.match(SongGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PhraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def chunk(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SongGrammarParser.ChunkContext)
            else:
                return self.getTypedRuleContext(SongGrammarParser.ChunkContext,i)


        def getRuleIndex(self):
            return SongGrammarParser.RULE_phrase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPhrase" ):
                listener.enterPhrase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPhrase" ):
                listener.exitPhrase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPhrase" ):
                return visitor.visitPhrase(self)
            else:
                return visitor.visitChildren(self)




    def phrase(self):

        localctx = SongGrammarParser.PhraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_phrase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 17
                    self.chunk()
                    self.state = 19
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==1:
                        self.state = 18
                        self.match(SongGrammarParser.T__0)



                else:
                    raise NoViableAltException(self)
                self.state = 23 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 25
                self.match(SongGrammarParser.T__1)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChunkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair(self):
            return self.getTypedRuleContext(SongGrammarParser.PairContext,0)


        def triplet(self):
            return self.getTypedRuleContext(SongGrammarParser.TripletContext,0)


        def getRuleIndex(self):
            return SongGrammarParser.RULE_chunk

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChunk" ):
                listener.enterChunk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChunk" ):
                listener.exitChunk(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChunk" ):
                return visitor.visitChunk(self)
            else:
                return visitor.visitChildren(self)




    def chunk(self):

        localctx = SongGrammarParser.ChunkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_chunk)
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.pair()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.triplet()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EMOJI(self, i:int=None):
            if i is None:
                return self.getTokens(SongGrammarParser.EMOJI)
            else:
                return self.getToken(SongGrammarParser.EMOJI, i)

        def getRuleIndex(self):
            return SongGrammarParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair" ):
                return visitor.visitPair(self)
            else:
                return visitor.visitChildren(self)




    def pair(self):

        localctx = SongGrammarParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(SongGrammarParser.EMOJI)
            self.state = 33
            self.match(SongGrammarParser.EMOJI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TripletContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EMOJI(self, i:int=None):
            if i is None:
                return self.getTokens(SongGrammarParser.EMOJI)
            else:
                return self.getToken(SongGrammarParser.EMOJI, i)

        def getRuleIndex(self):
            return SongGrammarParser.RULE_triplet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTriplet" ):
                listener.enterTriplet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTriplet" ):
                listener.exitTriplet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTriplet" ):
                return visitor.visitTriplet(self)
            else:
                return visitor.visitChildren(self)




    def triplet(self):

        localctx = SongGrammarParser.TripletContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_triplet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(SongGrammarParser.EMOJI)
            self.state = 36
            self.match(SongGrammarParser.EMOJI)
            self.state = 37
            self.match(SongGrammarParser.EMOJI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





