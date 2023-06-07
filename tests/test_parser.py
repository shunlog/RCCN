#!/usr/bin/env python3

import pytest
from antlr4 import InputStream, FileStream
from icecream import ic

from RCCN import rccn

def test_parser():
    inp = '''
type Character {
  name: String,
  appearsIn: [Episode]
}
    '''
    expected_AST = rccn.RCCN_AST({'Character':
                                  rccn.TypeDefinition(
                                      'Character',
                                      {'name': (rccn.ScalarType.STRING,
                                                rccn.TypeModifier.SCALAR),
                                       'appearsIn': ('Episode',
                                                     rccn.TypeModifier.LIST)})},
                                 None)

    input_stream = InputStream(inp)
    AST = rccn.parse(input_stream)
    assert AST == expected_AST
