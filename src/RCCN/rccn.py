#!/usr/bin/env python3
import sys
from enum import Enum, auto, StrEnum
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

class ScalarType(StrEnum):
    INT = "Int"
    STRING = "String"
    BOOLEAN = "Boolean"

SelectionSet = tuple['Field']
TypeNameOrScalar = Union[str, ScalarType]
TypeDefinition = tuple[TypeNameOrScalar, TypeModifier]
TypeDefinitions = dict[str, TypeDefinition]
Scalar = Union[int, str, bool, float]
FieldValue = Union[dict, list, Scalar]
FieldArgs = dict[str, Scalar]

@dataclass
class Field():
    name: str
    args: FieldArgs
    selection: SelectionSet


@dataclass
class AST():
    type_defs: TypeDefinitions
    selection: SelectionSet


class RCCNListener(GrammarListener):
    def __init__(self):
        self.type_defs = {}
        self.selection = ()
        self.parents_stack = []

    def enterObjectTypeDefinition(self, ctx):
        fields : TypeDefinitions = {}
        for fieldCtx in ctx.fieldDefinitions().fieldDefinition():
            name = fieldCtx.Name().getText()
            field_text = fieldCtx.fieldType().getText()
            field_name = fieldCtx.fieldType().Name().getText()

            if field_text == field_name:
                modi = TypeModifier.SCALAR
            elif field_text == '[' + field_name + ']':
                modi = TypeModifier.LIST

            if field_name is ScalarType:
                field_name = ScalarType(field_name)
            fields[name] = (field_name, modi)

        name = ctx.Name().getText()
        self.type_defs[name] = fields

    def enterField(self, ctx):
        name = ctx.Name().getText()

        args = {}
        if ctx.params():
            for paramCtx in ctx.params().param():
                param_name = paramCtx.Name().getText()
                val_str = paramCtx.value().getText()

                # interpret string as scalar type
                if paramCtx.value().Int():
                    val = int(val_str)
                elif paramCtx.value().Float():
                    val = float(val_str)
                elif paramCtx.value().String():
                    val = str(val_str[1:-1])
                elif paramCtx.value().boolean():
                    val = bool(val_str)

                args[param_name] = val

        field = Field(name, args, ())

        # we keep a stack of parents,
        # the top of the stack being the parent of current field
        if not self.parents_stack:  # if root query selection
            self.selection += field,
        else:
            self.parents_stack[-1].selection += field,
        self.parents_stack.append(field)

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

    tree = parser.document() # start rule
    listener = RCCNListener()
    walker = antlr4.ParseTreeWalker()
    walker.walk(listener, tree)

    return AST(listener.type_defs, listener.selection)


def execute(AST: AST, resolver) -> dict[str, FieldValue]:
    def execute_field(parent_type: TypeDefinition, field: Field, parent_obj, resolver):
        obj = resolver(parent_type[0], field.name, parent_obj, field.args)

        if field.selection:
            field_type = AST.type_defs[parent_type[0]][field.name]
            if field_type[1] == TypeModifier.LIST:
                return [execute_selection(field_type, o, field.selection) for o in obj]
            else:
                return execute_selection(field_type, obj, field.selection)
        else:
            return obj

    def execute_selection(parent_type, parent_obj, selection):
        res = {}
        for field in selection:
            res[field.name] = execute_field(parent_type, field, parent_obj, resolver)
        return res

    return execute_selection(('Query', TypeModifier.SCALAR), None, AST.selection)
