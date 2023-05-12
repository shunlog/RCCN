#!/usr/bin/env python3

import sys
from enum import Enum
from typing import Union
from antlr4 import *
from build.GrammarLexer import GrammarLexer
from build.GrammarParser import GrammarParser
from build.GrammarListener import GrammarListener
from icecream import ic


class TypesEnum(Enum):
    SCALAR = 1
    SCALAR_NON_NULL = 2
    LIST = 3
    LIST_NON_NULL_LIST = 4
    LIST_NON_NULL_ITEMS = 5
    LIST_NON_NULL_BOTH = 6


class ScalarType(Enum):
    INT = 1
    STRING = 2
    BOOLEAN = 3

class TypeDefinitionField():
    def __init__(self, name: str, typ: TypesEnum):
        self.name = name
        self.typ = typ

    def __repr__(self,):
        return str([self.name, self.typ])


class TypeDefinition():
    def __init__(self, name: str, fields: set[TypeDefinitionField]):
        self.name = name
        self.fields = fields

    def __repr__(self):
        return str([self.name, self.fields])


class Field():
    def __init__(self, name: str, parent: 'Field', typ: Union[TypeDefinition, ScalarType]):
        self.name = name
        self.parent = parent
        self.typ = typ

    def __repr__(self,):
        return str([self.name, self.parent, self.typ])


class RCCNListener(GrammarListener):
    fields = {}
    field_definitions = {}

    def enterObjectTypeDefinition(self, ctx):

        fields = set()
        for fieldCtx in ctx.fieldDefinitions().fieldDefinition():
            name = fieldCtx.Name().getText()
            tt = fieldCtx.fieldType().getText()
            # TODO check field type properly
            typ = TypesEnum.LIST  if tt[0] == '[' else TypesEnum.SCALAR
            field = TypeDefinitionField(name, typ)
            fields.add(field)

        name = ctx.Name().getText()

        fd = TypeDefinition(name, fields)
        token = ctx.start
        self.field_definitions[token] = fd

    def enterField(self, ctx):
        name = ctx.Name().getText()
        typ = None
        parent = None

        if type(ctx.parentCtx) != GrammarParser.DocumentContext:
            parent_token = ctx.parentCtx.parentCtx.start
            parent = self.fields.get(parent_token)

        field = Field(name, parent, typ)
        token = ctx.start
        self.fields[token] = field

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.document()

    listener = RCCNListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    ic(listener.fields)
    ic(listener.field_definitions)

if __name__ == '__main__':
    main(sys.argv)
