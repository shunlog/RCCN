#!/usr/bin/env python3

import sys
from antlr4 import *
from build.GrammarLexer import GrammarLexer
from build.GrammarParser import GrammarParser
from build.GrammarListener import GrammarListener

from icecream import ic

class TypeDefinition():
    # fields: dict[str, str]

    def __init__(self, fieldsCtx):
        ls = fieldsCtx.fieldDefinition()
        fields = set((f.Name().getText(),
                      f.fieldType().getText()) for f in ls)

        self.fields = fields.copy()

    def __repr__(self):
        return str(self.fields)


class Field():
    def __init__(self, name, parent, typ):
        self.name = name
        self.parent = parent
        self.typ = typ

    def __repr__(self,):
        return "Field: " + ', '.join([str(_) for _ in [ self.name, self.parent, self.typ]])


class RCCNListener(GrammarListener):
    def enterObjectTypeDefinition(self, ctx):
        fd = TypeDefinition(ctx.fieldDefinitions())

        token = ctx.start
        field_definitions[token] = fd

    def enterField(self, ctx):
        name = ctx.Name()
        typ = None
        parent = None
        try:
            parent = ctx.parentCtx.parentCtx.Name()
        except:
            pass
        field = Field(name, parent, typ)

        token = ctx.start
        fields[token] = field

fields = {}
field_definitions = {}

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.document()

    listener = RCCNListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    ic(fields)
    ic(field_definitions)

if __name__ == '__main__':
    main(sys.argv)
