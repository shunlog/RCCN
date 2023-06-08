#!/usr/bin/env python3

import pytest
from antlr4 import InputStream, FileStream
from icecream import ic

from RCCN import rccn

@pytest.mark.parametrize('input_text, expected_AST',
                         [
                             # a single scalar field
                             (
                                 'type Query {'
                                 'id: Int'
                                 '}',
                                 rccn.AST(
                                     {'Query': {'id': (rccn.ScalarType.INT,
                                                       rccn.TypeModifier.SCALAR)}},
                                     None)
                             ),

                             # two fields, list, non-scalar
                             (
                                 'type Character {'
                                 'name: String,'
                                 'appearsIn: [Episode]'
                                 '}',
                                 rccn.AST(
                                     {'Character': {'name': (rccn.ScalarType.STRING,
                                                             rccn.TypeModifier.SCALAR),
                                                    'appearsIn': ('Episode',
                                                                  rccn.TypeModifier.LIST)}},
                                     None)
                             ),

                             # two types
                             (
                                 'type Character {'
                                 'name: String,'
                                 'appearsIn: [Episode]'
                                 '}'
                                 'type Episode {'
                                 'id: Int,'
                                 'characters: [Character]'
                                 '}',
                                 rccn.AST(
                                     {'Character': {'name': (rccn.ScalarType.STRING,
                                                             rccn.TypeModifier.SCALAR),
                                                    'appearsIn': ('Episode',
                                                                  rccn.TypeModifier.LIST)},
                                      'Episode': {'id': (rccn.ScalarType.INT,
                                                         rccn.TypeModifier.SCALAR),
                                                  'characters': ('Character',
                                                                 rccn.TypeModifier.LIST)}},
                                     None)
                             ),

                         ])
def test_type_defs(input_text, expected_AST):
    input_stream = InputStream(input_text)
    AST = rccn.parse(input_stream)
    assert AST == expected_AST
