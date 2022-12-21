# Generated from grammar/SongGrammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SongGrammarParser import SongGrammarParser
else:
    from SongGrammarParser import SongGrammarParser

# This class defines a complete generic visitor for a parse tree produced by SongGrammarParser.

class SongGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SongGrammarParser#song.
    def visitSong(self, ctx:SongGrammarParser.SongContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SongGrammarParser#phrase.
    def visitPhrase(self, ctx:SongGrammarParser.PhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SongGrammarParser#chunk.
    def visitChunk(self, ctx:SongGrammarParser.ChunkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SongGrammarParser#pair.
    def visitPair(self, ctx:SongGrammarParser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SongGrammarParser#triplet.
    def visitTriplet(self, ctx:SongGrammarParser.TripletContext):
        return self.visitChildren(ctx)



del SongGrammarParser