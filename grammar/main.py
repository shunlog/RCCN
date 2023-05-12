#!/usr/bin/env python3

import sys
from enum import Enum, auto, Flag
from typing import Union
from antlr4 import *
from build.GrammarLexer import GrammarLexer
from build.GrammarParser import GrammarParser
from build.GrammarListener import GrammarListener
from icecream import ic


class TypeModifiers(Flag):
    SCALAR = auto()
    LIST = auto()
    SCALAR_NON_NULL = auto()
    LIST_NON_NULL = auto()
    LIST_ITEMS_NON_NULL = auto()


class ScalarType(Enum):
    INT = 1
    STRING = 2
    BOOLEAN = 3

class TypeDefinition():
    def __init__(self, name: str, fields: dict[str, tuple[Union['TypeDefinition', ScalarType], TypeModifiers]]):
        # fields: dict[name: (type, modifiers)]
        self.name = name
        self.fields = fields

    def __repr__(self):
        return str([self.name, self.fields])


class Field():
    def __init__(self, name: str, parent: 'Field', typ: Union[TypeDefinition, ScalarType],
                 modi: TypeModifiers, params: dict[str, tuple[Union[TypeDefinition, ScalarType], str]]):
        # params: dict[name: (type, value)]
        self.name = name
        self.parent = parent
        self.typ = typ
        self.modi = modi
        self.params = params

    def __repr__(self,):
        return str([self.name,
                    self.params,
                    self.parent.name if self.parent else None,
                    self.typ.name if self.typ else None,
                    self.modi])


class RCCNListener(GrammarListener):
    fields = {}
    field_definitions = {"Int": ScalarType.INT,
                         "String": ScalarType.STRING,
                         "Boolean": ScalarType.BOOLEAN}


    def enterObjectTypeDefinition(self, ctx):
        fields = {}
        for fieldCtx in ctx.fieldDefinitions().fieldDefinition():
            name = fieldCtx.Name().getText()
            tt = fieldCtx.fieldType().getText()
            # TODO check type modifier properly
            modi = TypeModifiers.LIST if tt[0] == '[' else TypeModifiers.SCALAR
            typ = fieldCtx.fieldType().Name().getText()
            fields[name] = (typ, modi)

        name = ctx.Name().getText()

        fd = TypeDefinition(name, fields)
        token = ctx.start
        self.field_definitions[name] = fd

    def enterField(self, ctx):
        name = ctx.Name().getText()

        if type(ctx.parentCtx) != GrammarParser.DocumentContext:
            parent_token = ctx.parentCtx.parentCtx.start
            parent = self.fields.get(parent_token)
        else:
            parent = None

        typ_name = 'Query' if not parent else parent.typ.fields[name][0]
        typ = self.field_definitions[typ_name]

        modi = TypeModifiers.SCALAR if not parent else parent.typ.fields[name][1]

        # TODO finish params
        params = {}

        field = Field(name, parent, typ, modi, params)
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

    ic(listener.field_definitions)
    ic(listener.fields)


if __name__ == '__main__':
    main(sys.argv)
