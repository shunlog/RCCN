#!/usr/bin/env python3

import sys
from enum import Enum, auto, Flag
from typing import Union
from antlr4 import *
from build.GrammarLexer import GrammarLexer
from build.GrammarParser import GrammarParser
from build.GrammarListener import GrammarListener
from icecream import ic
import swapi


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

TypeOrScalar = Union['TypeDefinition', ScalarType]

class TypeDefinition():
    def __init__(self, name: str, fields: dict[str, tuple[TypeOrScalar, TypeModifiers]]):
        self.name = name
        self.fields = fields

    def __repr__(self):
        return str([self.name, self.fields])


class Field():
    def __init__(self, name: str, parent: 'Field', typ: TypeOrScalar,
                 modi: TypeModifiers, params: dict[str, tuple[TypeOrScalar, str]]):
        self.name = name
        self.parent = parent
        self.typ = typ
        self.modi = modi
        self.params = params

        self.selection = []

    def __repr__(self,):
        return str([self.name,
                    self.params,
                    [f.name for f in self.selection],
                    self.parent.name if self.parent else None,
                    self.typ.name if self.typ else None,
                    self.modi])


class RCCNListener(GrammarListener):
    fields = {}
    field_definitions = {"Int": ScalarType.INT,
                         "String": ScalarType.STRING,
                         "Boolean": ScalarType.BOOLEAN}
    rootField = None


    def enterObjectTypeDefinition(self, ctx):
        type_fields = {}
        for fieldCtx in ctx.fieldDefinitions().fieldDefinition():
            name = fieldCtx.Name().getText()
            tt = fieldCtx.fieldType().getText()
            # TODO check type modifier properly
            modi = TypeModifiers.LIST if tt[0] == '[' else TypeModifiers.SCALAR
            typ = fieldCtx.fieldType().Name().getText()
            type_fields[name] = (typ, modi)

        # TODO check param types
        name = ctx.Name().getText()

        fd = TypeDefinition(name, type_fields)
        token = ctx.start
        self.field_definitions[name] = fd

    def enterField(self, ctx):
        # link parent field
        name = ctx.Name().getText()

        if type(ctx.parentCtx) != GrammarParser.DocumentContext:
            parent_token = ctx.parentCtx.parentCtx.start
            parent = self.fields.get(parent_token)
        else:
            parent = None

        typ_name = 'Query' if not parent else parent.typ.fields[name][0]
        typ = self.field_definitions[typ_name]

        modi = TypeModifiers.SCALAR if not parent else parent.typ.fields[name][1]

        params = {}
        if ctx.params():
            for paramCtx in ctx.params().param():
                pname = paramCtx.Name().getText()
                val = paramCtx.value().getText()
                # TODO check param val properly
                if val[0] == '"':
                    val = val[1:-1]
                elif val == 'true' or val == 'false':
                    val = True if val == 'true' else False
                else:
                    val = int(val)
                params[pname] = val

        field = Field(name, parent, typ, modi, params)
        token = ctx.start
        self.fields[token] = field

        if type(ctx.parentCtx) == GrammarParser.DocumentContext:
            self.rootField = field

    def exitField(self, ctx):
        # link child fields
        field = self.fields[ctx.start]

        if ctx.selectionSet():
            selection = [self.fields[f.start] for f in ctx.selectionSet().field()]
            field.selection = selection


def parse(fn):
    input_stream = FileStream(fn)
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.document()

    listener = RCCNListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # ic(listener.fields)
    return listener.rootField


# objects = {(field): obj}
objects = {}

def execute(field, resolve):
    if field.parent:
        parent_obj = objects.get(field.parent)
        obj = resolve(field.parent.typ.name, field.name, parent_obj, field.params)
        objects[field] = obj

    if not field.selection:
        return obj

    if field.parent and type(obj) == list:
        vals = zip(*(execute(f, resolve) for f in field.selection))
        resp = [dict(zip((f.name for f in field.selection), vp)) for vp in vals]
    else:
        resp = dict([(f.name, execute(f, resolve)) for f in field.selection])

    return resp


def main(argv):
    root = parse(argv[1])
    resp = execute(root, swapi.resolve)

    import json
    print(json.dumps(resp, indent=4))


if __name__ == '__main__':
    main(sys.argv)
