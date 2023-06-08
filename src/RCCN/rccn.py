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

SelectionSet = tuple['Field']
TypeNameOrScalar = Union[str, ScalarType]
TypeDefinition = tuple[TypeNameOrScalar, TypeModifier]
TypeDefinitions = dict[str, TypeDefinition]


@dataclass
class Field():
    name: str
    params: dict[str, tuple[TypeNameOrScalar, str]]
    selection: SelectionSet


@dataclass
class AST():
    type_defs: TypeDefinitions
    selection: SelectionSet


class RCCNListener(GrammarListener):
    scalar_defs = {"Int": ScalarType.INT,
                   "String": ScalarType.STRING,
                   "Boolean": ScalarType.BOOLEAN}

    def __init__(self):
        self.type_defs = {}
        self.selection = ()
        self.parents_stack = []

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
        name = ctx.Name().getText()
        field = Field(name, {}, ())
        if not self.parents_stack:  # if root query selection
            self.selection += field,
        else:
            self.parents_stack[-1].selection += field,
        self.parents_stack.append(field)

        # params = {}
        # if ctx.params():
        #     for paramCtx in ctx.params().param():
        #         pname = paramCtx.Name().getText()
        #         val = paramCtx.value().getText()
        #         # TODO check param val properly
        #         if val[0] == '"':
        #             val = val[1:-1]
        #         elif val == 'true' or val == 'false':
        #             val = True if val == 'true' else False
        #         else:
        #             val = int(val)
        #             params[pname] = val

    def exitField(self, ctx):
        self.parents_stack.pop()


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

    return AST(listener.type_defs, listener.selection)


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

