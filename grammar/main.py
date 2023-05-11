#!/usr/bin/env python3

import sys
from antlr4 import *
from build.GrammarLexer import GrammarLexer
from build.GrammarParser import GrammarParser
from build.GrammarListener import GrammarListener

class KeyPrinter(GrammarListener):
    def enterField(self, ctx):
        print("Field", ctx.Name(),  ctx.parentCtx.parentCtx.parentCtx.Name())

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.document()

    printer = KeyPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main(sys.argv)
