# Generated from grammar/SongGrammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SongGrammarParser import SongGrammarParser
else:
    from SongGrammarParser import SongGrammarParser

# This class defines a complete listener for a parse tree produced by SongGrammarParser.
class SongGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by SongGrammarParser#song.
    def enterSong(self, ctx:SongGrammarParser.SongContext):
        pass

    # Exit a parse tree produced by SongGrammarParser#song.
    def exitSong(self, ctx:SongGrammarParser.SongContext):
        pass


    # Enter a parse tree produced by SongGrammarParser#phrase.
    def enterPhrase(self, ctx:SongGrammarParser.PhraseContext):
        pass

    # Exit a parse tree produced by SongGrammarParser#phrase.
    def exitPhrase(self, ctx:SongGrammarParser.PhraseContext):
        pass


    # Enter a parse tree produced by SongGrammarParser#chunk.
    def enterChunk(self, ctx:SongGrammarParser.ChunkContext):
        pass

    # Exit a parse tree produced by SongGrammarParser#chunk.
    def exitChunk(self, ctx:SongGrammarParser.ChunkContext):
        pass


    # Enter a parse tree produced by SongGrammarParser#pair.
    def enterPair(self, ctx:SongGrammarParser.PairContext):
        pass

    # Exit a parse tree produced by SongGrammarParser#pair.
    def exitPair(self, ctx:SongGrammarParser.PairContext):
        pass


    # Enter a parse tree produced by SongGrammarParser#triplet.
    def enterTriplet(self, ctx:SongGrammarParser.TripletContext):
        pass

    # Exit a parse tree produced by SongGrammarParser#triplet.
    def exitTriplet(self, ctx:SongGrammarParser.TripletContext):
        pass



del SongGrammarParser