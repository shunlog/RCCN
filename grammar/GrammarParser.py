# Generated from Grammar.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,150,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,3,0,25,8,0,1,0,5,0,28,
        8,0,10,0,12,0,31,9,0,5,0,33,8,0,10,0,12,0,36,9,0,1,0,1,0,1,1,1,1,
        5,1,42,8,1,10,1,12,1,45,9,1,1,2,1,2,1,2,1,2,5,2,51,8,2,10,2,12,2,
        54,9,2,1,2,1,2,1,2,1,2,1,3,5,3,61,8,3,10,3,12,3,64,9,3,1,4,1,4,3,
        4,68,8,4,1,4,1,4,1,4,5,4,73,8,4,10,4,12,4,76,9,4,1,5,1,5,5,5,80,
        8,5,10,5,12,5,83,9,5,1,5,1,5,1,5,5,5,88,8,5,10,5,12,5,91,9,5,5,5,
        93,8,5,10,5,12,5,96,9,5,1,5,1,5,5,5,100,8,5,10,5,12,5,103,9,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,5,7,115,8,7,10,7,12,7,118,
        9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,5,9,127,8,9,10,9,12,9,130,9,9,1,
        10,1,10,5,10,134,8,10,10,10,12,10,137,9,10,1,10,1,10,1,10,5,10,142,
        8,10,10,10,12,10,145,9,10,1,10,3,10,148,8,10,1,10,0,0,11,0,2,4,6,
        8,10,12,14,16,18,20,0,0,155,0,34,1,0,0,0,2,39,1,0,0,0,4,46,1,0,0,
        0,6,62,1,0,0,0,8,65,1,0,0,0,10,77,1,0,0,0,12,106,1,0,0,0,14,110,
        1,0,0,0,16,121,1,0,0,0,18,128,1,0,0,0,20,147,1,0,0,0,22,25,3,2,1,
        0,23,25,3,14,7,0,24,22,1,0,0,0,24,23,1,0,0,0,25,29,1,0,0,0,26,28,
        5,7,0,0,27,26,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,
        30,33,1,0,0,0,31,29,1,0,0,0,32,24,1,0,0,0,33,36,1,0,0,0,34,32,1,
        0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,34,1,0,0,0,37,38,5,0,0,1,38,
        1,1,0,0,0,39,43,3,4,2,0,40,42,5,7,0,0,41,40,1,0,0,0,42,45,1,0,0,
        0,43,41,1,0,0,0,43,44,1,0,0,0,44,3,1,0,0,0,45,43,1,0,0,0,46,47,5,
        8,0,0,47,48,5,10,0,0,48,52,5,6,0,0,49,51,5,7,0,0,50,49,1,0,0,0,51,
        54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,55,1,0,0,0,54,52,1,0,0,
        0,55,56,5,11,0,0,56,57,3,6,3,0,57,58,5,12,0,0,58,5,1,0,0,0,59,61,
        3,8,4,0,60,59,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,
        63,7,1,0,0,0,64,62,1,0,0,0,65,67,5,10,0,0,66,68,3,10,5,0,67,66,1,
        0,0,0,67,68,1,0,0,0,68,69,1,0,0,0,69,70,5,6,0,0,70,74,5,10,0,0,71,
        73,5,7,0,0,72,71,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,
        0,75,9,1,0,0,0,76,74,1,0,0,0,77,81,5,1,0,0,78,80,5,7,0,0,79,78,1,
        0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,94,1,0,0,0,83,
        81,1,0,0,0,84,85,3,12,6,0,85,89,5,2,0,0,86,88,5,7,0,0,87,86,1,0,
        0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,93,1,0,0,0,91,89,
        1,0,0,0,92,84,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,
        95,97,1,0,0,0,96,94,1,0,0,0,97,101,3,12,6,0,98,100,5,7,0,0,99,98,
        1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,104,1,
        0,0,0,103,101,1,0,0,0,104,105,5,3,0,0,105,11,1,0,0,0,106,107,5,10,
        0,0,107,108,5,6,0,0,108,109,5,10,0,0,109,13,1,0,0,0,110,111,5,9,
        0,0,111,112,5,10,0,0,112,116,5,6,0,0,113,115,5,7,0,0,114,113,1,0,
        0,0,115,118,1,0,0,0,116,114,1,0,0,0,116,117,1,0,0,0,117,119,1,0,
        0,0,118,116,1,0,0,0,119,120,3,16,8,0,120,15,1,0,0,0,121,122,5,11,
        0,0,122,123,3,18,9,0,123,124,5,12,0,0,124,17,1,0,0,0,125,127,3,20,
        10,0,126,125,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,1,0,
        0,0,129,19,1,0,0,0,130,128,1,0,0,0,131,135,5,10,0,0,132,134,5,7,
        0,0,133,132,1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,136,1,0,
        0,0,136,148,1,0,0,0,137,135,1,0,0,0,138,139,5,10,0,0,139,143,5,6,
        0,0,140,142,5,7,0,0,141,140,1,0,0,0,142,145,1,0,0,0,143,141,1,0,
        0,0,143,144,1,0,0,0,144,146,1,0,0,0,145,143,1,0,0,0,146,148,3,16,
        8,0,147,131,1,0,0,0,147,138,1,0,0,0,148,21,1,0,0,0,17,24,29,34,43,
        52,62,67,74,81,89,94,101,116,128,135,143,147
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "<INVALID>", "<INVALID>", 
                     "':'", "<INVALID>", "'type'", "'query'", "<INVALID>", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT", "WS", "COLON", "NL", "TYPE", "QUERY", "Name", 
                      "INDENT", "DEDENT" ]

    RULE_document = 0
    RULE_typeDefinition = 1
    RULE_objectTypeDefinition = 2
    RULE_fieldsDefinition = 3
    RULE_fieldDefinition = 4
    RULE_params = 5
    RULE_param = 6
    RULE_queryDefinition = 7
    RULE_selectionSet = 8
    RULE_fields = 9
    RULE_field = 10

    ruleNames =  [ "document", "typeDefinition", "objectTypeDefinition", 
                   "fieldsDefinition", "fieldDefinition", "params", "param", 
                   "queryDefinition", "selectionSet", "fields", "field" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    INT=4
    WS=5
    COLON=6
    NL=7
    TYPE=8
    QUERY=9
    Name=10
    INDENT=11
    DEDENT=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DocumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GrammarParser.EOF, 0)

        def typeDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.TypeDefinitionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.TypeDefinitionContext,i)


        def queryDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.QueryDefinitionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.QueryDefinitionContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.NL)
            else:
                return self.getToken(GrammarParser.NL, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_document

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDocument" ):
                listener.enterDocument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDocument" ):
                listener.exitDocument(self)




    def document(self):

        localctx = GrammarParser.DocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_document)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8 or _la==9:
                self.state = 24
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8]:
                    self.state = 22
                    self.typeDefinition()
                    pass
                elif token in [9]:
                    self.state = 23
                    self.queryDefinition()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 26
                    self.match(GrammarParser.NL)
                    self.state = 31
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
            self.match(GrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def objectTypeDefinition(self):
            return self.getTypedRuleContext(GrammarParser.ObjectTypeDefinitionContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.NL)
            else:
                return self.getToken(GrammarParser.NL, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_typeDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeDefinition" ):
                listener.enterTypeDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeDefinition" ):
                listener.exitTypeDefinition(self)




    def typeDefinition(self):

        localctx = GrammarParser.TypeDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_typeDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.objectTypeDefinition()
            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 40
                    self.match(GrammarParser.NL) 
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectTypeDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(GrammarParser.TYPE, 0)

        def Name(self):
            return self.getToken(GrammarParser.Name, 0)

        def COLON(self):
            return self.getToken(GrammarParser.COLON, 0)

        def INDENT(self):
            return self.getToken(GrammarParser.INDENT, 0)

        def fieldsDefinition(self):
            return self.getTypedRuleContext(GrammarParser.FieldsDefinitionContext,0)


        def DEDENT(self):
            return self.getToken(GrammarParser.DEDENT, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.NL)
            else:
                return self.getToken(GrammarParser.NL, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_objectTypeDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectTypeDefinition" ):
                listener.enterObjectTypeDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectTypeDefinition" ):
                listener.exitObjectTypeDefinition(self)




    def objectTypeDefinition(self):

        localctx = GrammarParser.ObjectTypeDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_objectTypeDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(GrammarParser.TYPE)
            self.state = 47
            self.match(GrammarParser.Name)
            self.state = 48
            self.match(GrammarParser.COLON)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 49
                self.match(GrammarParser.NL)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self.match(GrammarParser.INDENT)
            self.state = 56
            self.fieldsDefinition()
            self.state = 57
            self.match(GrammarParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldsDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.FieldDefinitionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.FieldDefinitionContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_fieldsDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldsDefinition" ):
                listener.enterFieldsDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldsDefinition" ):
                listener.exitFieldsDefinition(self)




    def fieldsDefinition(self):

        localctx = GrammarParser.FieldsDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_fieldsDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 59
                self.fieldDefinition()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Name(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.Name)
            else:
                return self.getToken(GrammarParser.Name, i)

        def COLON(self):
            return self.getToken(GrammarParser.COLON, 0)

        def params(self):
            return self.getTypedRuleContext(GrammarParser.ParamsContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.NL)
            else:
                return self.getToken(GrammarParser.NL, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_fieldDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldDefinition" ):
                listener.enterFieldDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldDefinition" ):
                listener.exitFieldDefinition(self)




    def fieldDefinition(self):

        localctx = GrammarParser.FieldDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_fieldDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(GrammarParser.Name)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 66
                self.params()


            self.state = 69
            self.match(GrammarParser.COLON)
            self.state = 70
            self.match(GrammarParser.Name)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 71
                self.match(GrammarParser.NL)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ParamContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ParamContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.NL)
            else:
                return self.getToken(GrammarParser.NL, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = GrammarParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(GrammarParser.T__0)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 78
                self.match(GrammarParser.NL)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 84
                    self.param()
                    self.state = 85
                    self.match(GrammarParser.T__1)
                    self.state = 89
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==7:
                        self.state = 86
                        self.match(GrammarParser.NL)
                        self.state = 91
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
             
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 97
            self.param()
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 98
                self.match(GrammarParser.NL)
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
            self.match(GrammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Name(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.Name)
            else:
                return self.getToken(GrammarParser.Name, i)

        def COLON(self):
            return self.getToken(GrammarParser.COLON, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = GrammarParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(GrammarParser.Name)
            self.state = 107
            self.match(GrammarParser.COLON)
            self.state = 108
            self.match(GrammarParser.Name)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUERY(self):
            return self.getToken(GrammarParser.QUERY, 0)

        def Name(self):
            return self.getToken(GrammarParser.Name, 0)

        def COLON(self):
            return self.getToken(GrammarParser.COLON, 0)

        def selectionSet(self):
            return self.getTypedRuleContext(GrammarParser.SelectionSetContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.NL)
            else:
                return self.getToken(GrammarParser.NL, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_queryDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryDefinition" ):
                listener.enterQueryDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryDefinition" ):
                listener.exitQueryDefinition(self)




    def queryDefinition(self):

        localctx = GrammarParser.QueryDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_queryDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(GrammarParser.QUERY)
            self.state = 111
            self.match(GrammarParser.Name)
            self.state = 112
            self.match(GrammarParser.COLON)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 113
                self.match(GrammarParser.NL)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 119
            self.selectionSet()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectionSetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(GrammarParser.INDENT, 0)

        def fields(self):
            return self.getTypedRuleContext(GrammarParser.FieldsContext,0)


        def DEDENT(self):
            return self.getToken(GrammarParser.DEDENT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_selectionSet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectionSet" ):
                listener.enterSelectionSet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectionSet" ):
                listener.exitSelectionSet(self)




    def selectionSet(self):

        localctx = GrammarParser.SelectionSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_selectionSet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(GrammarParser.INDENT)
            self.state = 122
            self.fields()
            self.state = 123
            self.match(GrammarParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.FieldContext)
            else:
                return self.getTypedRuleContext(GrammarParser.FieldContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_fields

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFields" ):
                listener.enterFields(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFields" ):
                listener.exitFields(self)




    def fields(self):

        localctx = GrammarParser.FieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_fields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 125
                self.field()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Name(self):
            return self.getToken(GrammarParser.Name, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.NL)
            else:
                return self.getToken(GrammarParser.NL, i)

        def COLON(self):
            return self.getToken(GrammarParser.COLON, 0)

        def selectionSet(self):
            return self.getTypedRuleContext(GrammarParser.SelectionSetContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField" ):
                listener.enterField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField" ):
                listener.exitField(self)




    def field(self):

        localctx = GrammarParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_field)
        self._la = 0 # Token type
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(GrammarParser.Name)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 132
                    self.match(GrammarParser.NL)
                    self.state = 137
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(GrammarParser.Name)
                self.state = 139
                self.match(GrammarParser.COLON)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 140
                    self.match(GrammarParser.NL)
                    self.state = 145
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 146
                self.selectionSet()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





