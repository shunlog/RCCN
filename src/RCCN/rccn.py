#!/usr/bin/env python3
import sys
from enum import Enum, auto, Enum
from typing import Union
from dataclasses import dataclass
import antlr4
from icecream import ic

from .build.GrammarLexer import GrammarLexer
from .build.GrammarParser import GrammarParser
from .build.GrammarListener import GrammarListener


class TypeModifier(Enum):
    SCALAR = 0
    LIST = 1

class ScalarType(Enum):
    INT = 1
    STRING = 2
    BOOLEAN = 3

TypeNameOrScalar = Union[str, ScalarType]
TypeDefinition = tuple[TypeNameOrScalar, TypeModifier]
TypeDefinitions = dict[str, TypeDefinition]


@dataclass
class Field():
    name: str
    params: dict[str, tuple[TypeNameOrScalar, str]]
    selection: tuple['Field']


@dataclass
class AST():
    type_defs: TypeDefinitions
    root_query: Field


class RCCNListener(GrammarListener):
    scalar_defs = {"Int": ScalarType.INT,
                   "String": ScalarType.STRING,
                   "Boolean": ScalarType.BOOLEAN}

    def __init__(self):
        self.fields = {}
        self.type_defs = {}
        self.root_field = None


    def enterObjectTypeDefinition(self, ctx):
        fields : TypeDefinitions = {}
        for fieldCtx in ctx.fieldDefinitions().fieldDefinition():
            name = fieldCtx.Name().getText()
            tt = fieldCtx.fieldType().getText()
            field_type = fieldCtx.fieldType().Name().getText()

            # TODO check type modifier properly
            modi = TypeModifier.LIST if tt[0] == '[' else TypeModifier.SCALAR
            if field_type in self.scalar_defs:
                field_type = self.scalar_defs[field_type]
            fields[name] = (field_type, modi)

        # TODO check param types
        name = ctx.Name().getText()
        self.type_defs[name] = fields

    def enterField(self, ctx):
        # link parent field
        name = ctx.Name().getText()

        if type(ctx.parentCtx) != GrammarParser.DocumentContext:
            parent_token = ctx.parentCtx.parentCtx.start
            parent = self.fields.get(parent_token)
        else:
            parent = None
            ic(parent)

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

        field = Field(name, params, tuple())
        token = ctx.start
        self.fields[token] = field

        if type(ctx.parentCtx) == GrammarParser.DocumentContext:
            self.root_field = field
            self.parent_field = field

    def exitField(self, ctx):
        # link child fields
        field = self.fields[ctx.start]

        if ctx.selectionSet():
            selection = tuple(self.fields[f.start] for f in ctx.selectionSet().field())
            field.selection = selection


class VerboseListener(antlr4.error.ErrorListener.ErrorListener) :
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        stack = recognizer.getRuleInvocationStack()
        stack.reverse()
        print("rule stack: ", str(stack))
        print("line", line, ":", column, "at", offendingSymbol, ":", msg)


def parse(input_stream: Union[antlr4.InputStream, antlr4.FileStream]) -> AST:
    '''Takes an ANTLR Stream of some kind and returns an AST.'''
    lexer = GrammarLexer(input_stream)
    tok_stream = antlr4.CommonTokenStream(lexer)

    parser = GrammarParser(tok_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(VerboseListener())

    tree = parser.document()

    listener = RCCNListener()
    walker = antlr4.ParseTreeWalker()
    walker.walk(listener, tree)

    ic(listener.fields)
    return AST(listener.type_defs, listener.root_field)


# objects = {(field): obj}
objects = {}

def execute(field, resolve):
    if field.parent:
        parent_obj = objects.get(field.parent)
        obj = resolve(field.parent.field_type.name, field.name, parent_obj, field.params)
        objects[field] = obj

    if not field.selection:
        return obj

    if field.parent and type(obj) == list:
        vals = zip(*(execute(f, resolve) for f in field.selection))
        resp = [dict(zip((f.name for f in field.selection), vp)) for vp in vals]
    else:
        resp = dict([(f.name, execute(f, resolve)) for f in field.selection])

    return resp

