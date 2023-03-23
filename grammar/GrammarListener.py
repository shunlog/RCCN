# Generated from Grammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#document.
    def enterDocument(self, ctx:GrammarParser.DocumentContext):
        pass

    # Exit a parse tree produced by GrammarParser#document.
    def exitDocument(self, ctx:GrammarParser.DocumentContext):
        pass


    # Enter a parse tree produced by GrammarParser#typeDefinition.
    def enterTypeDefinition(self, ctx:GrammarParser.TypeDefinitionContext):
        pass

    # Exit a parse tree produced by GrammarParser#typeDefinition.
    def exitTypeDefinition(self, ctx:GrammarParser.TypeDefinitionContext):
        pass


    # Enter a parse tree produced by GrammarParser#objectTypeDefinition.
    def enterObjectTypeDefinition(self, ctx:GrammarParser.ObjectTypeDefinitionContext):
        pass

    # Exit a parse tree produced by GrammarParser#objectTypeDefinition.
    def exitObjectTypeDefinition(self, ctx:GrammarParser.ObjectTypeDefinitionContext):
        pass


    # Enter a parse tree produced by GrammarParser#fieldsDefinition.
    def enterFieldsDefinition(self, ctx:GrammarParser.FieldsDefinitionContext):
        pass

    # Exit a parse tree produced by GrammarParser#fieldsDefinition.
    def exitFieldsDefinition(self, ctx:GrammarParser.FieldsDefinitionContext):
        pass


    # Enter a parse tree produced by GrammarParser#fieldDefinition.
    def enterFieldDefinition(self, ctx:GrammarParser.FieldDefinitionContext):
        pass

    # Exit a parse tree produced by GrammarParser#fieldDefinition.
    def exitFieldDefinition(self, ctx:GrammarParser.FieldDefinitionContext):
        pass


    # Enter a parse tree produced by GrammarParser#params.
    def enterParams(self, ctx:GrammarParser.ParamsContext):
        pass

    # Exit a parse tree produced by GrammarParser#params.
    def exitParams(self, ctx:GrammarParser.ParamsContext):
        pass


    # Enter a parse tree produced by GrammarParser#param.
    def enterParam(self, ctx:GrammarParser.ParamContext):
        pass

    # Exit a parse tree produced by GrammarParser#param.
    def exitParam(self, ctx:GrammarParser.ParamContext):
        pass


    # Enter a parse tree produced by GrammarParser#queryDefinition.
    def enterQueryDefinition(self, ctx:GrammarParser.QueryDefinitionContext):
        pass

    # Exit a parse tree produced by GrammarParser#queryDefinition.
    def exitQueryDefinition(self, ctx:GrammarParser.QueryDefinitionContext):
        pass


    # Enter a parse tree produced by GrammarParser#selectionSet.
    def enterSelectionSet(self, ctx:GrammarParser.SelectionSetContext):
        pass

    # Exit a parse tree produced by GrammarParser#selectionSet.
    def exitSelectionSet(self, ctx:GrammarParser.SelectionSetContext):
        pass


    # Enter a parse tree produced by GrammarParser#fields.
    def enterFields(self, ctx:GrammarParser.FieldsContext):
        pass

    # Exit a parse tree produced by GrammarParser#fields.
    def exitFields(self, ctx:GrammarParser.FieldsContext):
        pass


    # Enter a parse tree produced by GrammarParser#field.
    def enterField(self, ctx:GrammarParser.FieldContext):
        pass

    # Exit a parse tree produced by GrammarParser#field.
    def exitField(self, ctx:GrammarParser.FieldContext):
        pass



del GrammarParser