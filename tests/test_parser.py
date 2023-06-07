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
    expected_AST = rccn.TypeDefinition('Character',
                                       {'name': (rccn.ScalarType.STRING,
                                                 rccn.TypeModifier.SCALAR),
                                        'appearsIn': ('Episode', rccn.TypeModifier.LIST)})

    input_stream = InputStream(inp)
    type_defs, root_node = rccn.parse(input_stream)
    assert type_defs['Character'] == expected_AST
