from os import path
from antlr4 import InputStream, TokenStream, CommonTokenStream
from blender_emoji import load_from_json
from dist.grammar.SongGrammarLexer import SongGrammarLexer
from dist.grammar.SongGrammarParser import SongGrammarParser
from dist.grammar.SongGrammarVisitor import SongGrammarVisitor

json_data = load_from_json("emoji_inverted.json")


class Visitor(SongGrammarVisitor):

    def visitChunk(self, ctx):
        # check if chunk is a pair
        pair = ctx.pair()
        if pair is not None:
            print("Pair")
            # do something with pair
            # for emoji in pair.EMOJI():
                # print(emoji.getText())
            return pair

        # otherwise it's a triplet
        triplet = ctx.triplet()
        print("Triplet")
        # do something with triplet
        # for emoji in triplet.EMOJI():
            # print(emoji.getText())
        return triplet

    def visitPhrase(self, ctx):
        print("Phrase")
        return [self.visitChunk(c) for c in ctx.chunk()]

    def visitSong(self, ctx):
        return [self.visitPhrase(p) for p in ctx.phrase()]


with open(path.join('grammar', 'sample.txt')) as f:

    input_stream = InputStream(f.read())
    lexer = SongGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SongGrammarParser(stream)
    context = SongGrammarParser.song(parser)

    visitor = Visitor()
    visitor.visit(context)
